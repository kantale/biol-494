'''
Author:
Alexandros Kanterakis (kantale@ics.forth.gr)

This is a script to help grade exercises for this course
'''


import re
import os
import glob
import json
import email
import time
import argparse
import smtplib, ssl # For mail
import pandas as pd

from itertools import groupby
from collections import defaultdict
from os.path import expanduser

from get_ask import get_ask

def get_home_dir():
    '''
    '''
    return expanduser("~")

class Mail:

    PASSWORD_PATH = '.gmail/settings.json'

    def __init__(self,):
        self.connect_to_gmail()

    @staticmethod
    def get_password():
        password_filename = os.path.join(get_home_dir(), Mail.PASSWORD_PATH)
        with open(password_filename) as f:
            data = json.load(f)
        return data['password']

    def connect_to_gmail(self,):
        port = 587  # For starttls
        smtp_server = "smtp.gmail.com"
        sender_email = "alexandros.kanterakis@gmail.com"
        password = Mail.get_password() 

        context = ssl.create_default_context()
        self.server = smtplib.SMTP(smtp_server, port)

        self.server.ehlo()  # Can be omitted
        self.server.starttls(context=context)
        self.server.ehlo()  # Can be omitted
        self.server.login(sender_email, password)

        print ('CONNECTED TO GMAIL')



    def do_send_mail(self, to, subject, text, sleep=10, actually_send_mail=False):
        from email.header import Header
        from email.mime.text import MIMEText
        from email.mime.multipart import MIMEMultipart

        msg = MIMEText(text, 'plain', 'utf-8')
        sender_email = "alexandros.kanterakis@gmail.com"
        receiver_email = to


        email = MIMEMultipart('mixed')
        email['From'] = sender_email
        email['To'] = receiver_email
        email['Subject'] = Header(subject, 'utf-8')

        msg.set_payload(text.encode('utf-8'))
        email.attach(msg)

        message = email.as_string()

        if False:
            message = 'Subject: {}\n\n{}'.format(subject, text)

        if actually_send_mail:
            self.server.sendmail(sender_email, receiver_email, message)
        else:
            print (text)
        time.sleep(sleep)
        print ('Mail sent')

    def disconnect_from_gmail(self,):
        self.server.quit()
        print ('DISCONNECTED FROM GMAIL')



class Grades:

    # Filetypes
    IPYNB = 1
    MIME = 2
    PLAIN = 3

    declarations = [
        'askhsh','Askhsh','ASKHSH','Askisi','askisi',
        '΄askhsh','ΆΣΚΗΣΗ','ΑΣΚΗΣΗ','ασκηση','άσκηση',
        'Άσκηση','ασκιση', 'akshsh', 'Αskhsh', 'Askhsk', 
        'Απαντηση ασκησης', 'Απάντηση ασκησης', 'απαντηση ασκησης',
        'Task_', 'απαντηση ακσησης', 'απάντηση άσκησης',
        'this is the solution for ex.', r'-+ΑΣΚΗΣΗ',
        "'Ασκηση", "Αskisi", "Άσκση", "asksisi", 'Aslisi',
        'Ασκηση', "Task", "ask", "AKHSH", "aksisi", 'Akshsh',
        'askshsh', 'ασκ', '΄άσκηση', 'Asksh', 'Askhshh', 'asksi',
        'Ask', 'askkisi', 'aσκηση', 'ASkhsh', '΄Άσκηση', 'Akhsh',
        'Askhh', 'Askshsh', '΄΄Ασκηση'
    ]

    ex_regexp = re.compile(r'^\s*#+\s*({})\s*(?P<ask>\d+)'.format('|'.join(declarations)))

    SOLUTIONS_FILENAME_PATTERN = 'AM_{id_}_ASK_{ASK}'

    GREETING_1 = '''
Γεια σας,

Παρακάτω ακολουθεί η βαθμολογία σας στις ασκήσεις {START}-{END} στο μάθημα:'''

    GREETING_2 = '''
Γεια σας,

Παρακάτω ακολουθεί η βαθμολογία σας στη τελική εξέταση του μαθήματος:'''
    
    MAIL_PATTERN = '''
{GREETING}
ΒΙΟΛ-494 - Εισαγωγή στον προγραμματισμό

AM: {AM}


{EXERCISES}

================================
Συγκεντρωτικά:

{SUMMARY}

Για απορίες στείλτε DM στο slack. Μην ξεχάσετε να αναφέρετε το ΑΜ σας στις απορίες. 

Χαιρετώ,
Αλέξανδρος Καντεράκης

'''

    MAIL_EXERCISE_PATTERN = '''
================================
  Άσκηση: {EXERCISE}
================================
  Η λύση σας:
--------------------------------
{SOLUTION}
--------------------------------
Σχόλια:
{COMMENT}
--------------------------------
Βαθμός: {GRADE}/10
--------------------------------
'''

    MAIL_SUBJECT_1 = 'ΒΙΟΛ-494 - Βαθμοί ασκήσεων {START}-{END}'
    MAIL_SUBJECT_2 = 'ΒΙΟΛ-494 - Βαθμοί τελικού διαγωνίσματος'

    def __init__(self, directory, solutions_dir, action, 
            ex=None, 
            actually_send_mail=False,
            start = 1,
            end = 20,
            send_to_me=False,
            random_list=None,
        ):
        self.dir = directory
        self.solutions_dir = solutions_dir
        self.actually_send_mail = actually_send_mail
        self.start = start
        self.end = end
        self.exercises_range = list(range(self.start, self.end+1))
        self.send_to_me = send_to_me
        self.all_anonymous_grades = [] # For plotting and statistics
        self.random_list = random_list

        self.get_filenames(ex)
        self.get_all_exercises()

        if action == 'grade':
            self.grade()
        elif action == 'send_mail':
            self.collect_all_grades()

            self.mail = Mail()
            self.send_mail()
            self.mail.disconnect_from_gmail()
        else:
            raise Exception('Unknown action: {}'.format(action))

    def save_anonymoys_grades(self,):
        with open('grades.json', 'w') as f:
            json.dump(self.all_anonymous_grades, f)
        print ('Saved anonymous grades at: grades.json ')

    def get_solutions_filename(self, id_, exercise):

        filename = self.SOLUTIONS_FILENAME_PATTERN.format(id_=id_, ASK=exercise)

        return os.path.join(self.solutions_dir, filename)

    def get_grade_from_comment(self, comment=None, filename=None):

        if filename:
            with open(filename) as f:
                comment = f.read()

        grades = [int(x) for x in comment.split('\n') if re.match(r'^\d+$', x)]
        assert len(grades) == 1
        assert grades[0] in range(0,11)

        return grades[0]

    def remove_grade_from_comment(self, comment):

        return '\n'.join(x for x in comment.split('\n') if not re.match(r'^\d+$', x))



    def grade(self,):

        # How many answers are in total?
        total = len(self.all_exercises)
        print ('Total Answers:', total)

        for i, (exercise, id_, answer) in enumerate(self.all_exercises):

            filename = self.get_solutions_filename(id_, exercise)

            print ('Progress: {}/{} {:0.2f}%'.format(i+1, total, 100*(i+1)/total))
            print ('Exercise:', exercise)
            print ('      AM:', id_, '             Origin:', os.path.join(self.dir, id_))
            print ('Filename:', filename)
            print ('==================')

            #if id_ == '3052':
            #    print (answer)

            if os.path.exists(filename):
                print ('   Already graded..')
                continue

            print (answer)
            print ('==================')
            comment = ''
            while True:
                line = input() # NEVER USE INPUT!! 
                if line.strip() in ['q', 'Q', ';']:
                    break

                comment += line + '\n'

            # Is there a grade in there?
            grade = self.get_grade_from_comment(comment)

            # Good.. no exception happened. Save the comment
            with open(filename, 'w') as f:
                f.write(comment)

    def get_id_from_filename(self, filename):

        # Some files are like 1234.1 1234.2 ...
        dot_splitted = filename.split('.')
        if re.match(r'^\d+$', dot_splitted[-1]): # last part is a number
            filename = '.'.join(dot_splitted[:-1])

        return os.path.split(filename)[1]


    def get_all_exercises(self,):

        # Read all files
        data = []
        for filename in self.filenames:
            #print (filename)
            id_ = self.get_id_from_filename(filename)
            content = self.get_exercises(filename)

            try:
                for ask, solution in self.iterate_exercises(content):
                    data.append((id_, ask, solution))
            except Exception as e:
                print ('Problem in file:', filename)
                raise e

        # Group together multiple solutions to the same exercise from the same student
        self.all_exercises = defaultdict(dict)

        for group, it in groupby(sorted(data), lambda x : x[:2]):
            self.all_exercises[group[0]][group[1]] = '\n'.join(x[2] for x in it)

        # Print some stats..
        print ('Total students:', len(self.all_exercises))
        print ('Average exercises per student:', sum(len(v) for k,v in self.all_exercises.items())/len(self.all_exercises))

        # Some basic quality control..
        for k,v in self.all_exercises.items():
            for k2,v2 in v.items():
                assert k
                if not k2:
                    raise Exception('AM: {} Empty ASK:{} '.format(k, str(k2)))

        # Group and sort according to ask / AM
        self.all_exercises = sorted((int(k2), k, v2) for k,v in self.all_exercises.items() for k2,v2 in v.items())

    def collect_all_grades(self,):
        all_answers = {}

        #print (json.dumps(self.all_exercises, indent=4))
        #print ('=====')

        for ask, AM, answer in self.all_exercises:
            if not AM in all_answers:
                all_answers[AM] = {}

            assert not ask in all_answers[AM]

            filename = self.get_solutions_filename(AM, ask)
            with open(filename) as f:
                comment = f.read()

            grade = self.get_grade_from_comment(comment)
            comment = self.remove_grade_from_comment(comment)
            
            all_answers[AM][ask] = {
                'answer': answer,
                'grade': grade,
                'comment': comment,
            }
        self.all_answers = all_answers
        #print (json.dumps(self.all_answers, indent=4))

        self.all_anonymous_grades = [
            [
                v.get(i, {'grade':0})['grade'] for i in self.exercises_range
            ] 
            for k,v in all_answers.items()
        ]

        with open('grades.json', 'w') as f:
            json.dump(self.all_anonymous_grades, f)
        print ('Created anonymous grades.json')

    @staticmethod
    def create_mail_address(AM):
        if '@' in AM:
            return AM

        return 'bio' + AM + '@edu.biology.uoc.gr'

    def send_mail(self,):

        total = len(self.all_answers)
        for i, AM in enumerate(self.all_answers):

            if self.send_to_me:
                mail_address = 'alexandros.kanterakis@gmail.com'
            else:
                mail_address = Grades.create_mail_address(AM)
            
            print ('{}/{} -- {}'.format((i+1), total, mail_address)) # Don't comment this!

            mail = self.create_mail(AM)
            #print(mail) # Comment this! 

            if True:
                self.mail.do_send_mail(
                    to=mail_address, 
                    #subject=self.MAIL_SUBJECT_1.format(START=self.start, END=self.end), 
                    subject=self.MAIL_SUBJECT_2, 
                    text=mail,
                    actually_send_mail=self.actually_send_mail,
                )
            #a=1/0

    def create_exercise_mail(self,exercise, solution, comment, grade):

        return self.MAIL_EXERCISE_PATTERN.format(
            EXERCISE=exercise,
            SOLUTION=solution,
            COMMENT=comment,
            GRADE=grade,
        )

    def create_mail(self, AM):

        exercises_mail = ''

        pandas_df = []

        if not self.random_list is None:
            required_list = get_ask(AM)
        else:
            required_list = None

        #for ASK, details in self.all_answers[AM].items():
        for ASK in self.exercises_range:

            if required_list and not ASK in required_list:
                continue

            if ASK in self.all_answers[AM]:
                details = self.all_answers[AM][ASK]

                answer = details['answer']
                comment = details['comment']
                grade = details['grade']
            else:
                answer = '\n'
                comment = 'Δεν έστειλες τίποτα για αυτή την άσκηση!'
                grade = 0

            grade_dics = {'Άσκηση': ASK, 'Βαθμός': grade}
            exercises_mail += self.create_exercise_mail(ASK, answer, comment, grade)
            pandas_df.append(grade_dics)

        pandas_df = pd.DataFrame(pandas_df)
        summary = pandas_df.to_string(index=False)
        average = pandas_df['Βαθμός'].mean()
        summary += '\n\nΜέσος Όρος: {}'.format(average)

        #greeting = self.GREETING_1.format(START=self.start, END=self.end)
        greeting = self.GREETING_2

        ret = self.MAIL_PATTERN.format(
            GREETING=greeting,
            AM=AM,
            EXERCISES=exercises_mail,
            SUMMARY=summary,
        )

        return ret

    def get_type(self, filename):
        '''
        Return the type of file
        '''
        
        with open(filename) as f:
            content = f.read()

        # try to parse it as json
        try:
            data = json.loads(content)
        except json.decoder.JSONDecodeError:
            # This is not a JSON file..
            pass 
        else:
            # this is json.. assume ipynb..
            return self.IPYNB

        # Check if MIME. Any better way?
        if 'X-Google-Smtp-Source' in content:
            return self.MIME

        # Assuming file with content
        return self.PLAIN


    def iterate_exercises(self, text):

        content = ''
        exercise = None
        for line in text.split('\n'):
            #print (line)
            m = re.match(self.ex_regexp, line)

            # Set this true to check declarations!
            if False:
                if re.match(r'^\s*#', line):
                    print (line, '-->', {True: 'MATCHED', False: 'NO MATCH!'}[bool(m)])
            if m:
                if exercise:
                    yield (exercise, content)
                    content = ''
                exercise = m.groupdict()['ask']

            content += '\n' + line

        if exercise is None:
            print ('Could not find any exercise in file!')
            print (text)
            assert False

        yield (exercise, content)

    def get_exercises(self, filename):
        t = self.get_type(filename)
        
        if t == self.IPYNB:
            content = self.get_exercises_ipynb(filename)
        elif t == self.MIME:
            content = self.get_exercises_MIME(filename)
        elif t == self.PLAIN:
            content  = self.get_exercises_plain(filename)
        else:
            raise Exception('Unknown type={}'.format(t))

        return content


    def get_exercises_plain(self, filename):
        with open(filename) as f:
            content = f.read()

        return content

    def get_exercises_ipynb(self, filename):
        with open(filename) as f:
            content = json.load(f)

        code_cells = [
            ''.join(x['source']) for x in content['cells'] 
                if x['cell_type'] == 'code'
        ]
        return '\n\n'.join(code_cells)

    def get_exercises_MIME(self, filename):
        with open(filename) as f:
            content = f.read()

        m = email.message_from_string(content)
        payload = m.get_payload()
        #assert len(payload) == 21 # FIXME

        content = ""
        #for x in payload[1:]:
        for x in payload[:]:
            if hasattr(x, "get_payload"):
                content += '\n' + x.get_payload(decode=True).decode("utf-8")

        return content 

        
    def get_filenames(self, ex=None):
        if not ex:
            ex='*'
        else:
            ex = ex + '*'

        self.filenames = glob.glob(os.path.join(self.dir, ex))
        print ('Read: {} files'.format(len(self.filenames)))

if __name__ == '__main__':
    '''
    python grade.py --dir /Users/admin/biol-494/exercises/ --sol /Users/admin/biol-494/solutions --action grade
    python grade.py --dir /Users/admin/biol-494/exercises/ --sol /Users/admin/biol-494/solutions --action send_mail
    python grade.py --dir /Users/admin/biol-494/exercises/ --sol /Users/admin/biol-494/solutions --action send_mail --actually_send_mail
    python grade.py --dir /Users/admin/biol-494/exercises/ --ex 3158 --action grade 
    python grade.py --dir /Users/admin/biol-494/exercises/ --sol /Users/admin/biol-494/solutions --ex 2743 --action grade 
    python grade.py --dir /Users/admin/biol-494/exercises/ --sol /Users/admin/biol-494/solutions --ex 2743 --action send_mail --actually_send_mail

    # 2nd Round grade:
    python grade.py --dir /Users/admin/biol-494/exercises2/ --sol /Users/admin/biol-494/solutions2 --action grade --start 21 --end 40 

    # 2nd Round Send mail:
    python grade.py --dir /Users/admin/biol-494/exercises2/ --sol /Users/admin/biol-494/solutions2 --ex 2743 --action send_mail --start 21 --end 40  
    python grade.py --dir /Users/admin/biol-494/exercises2/ --sol /Users/admin/biol-494/solutions2 --ex 2743 --action send_mail --start 21 --end 40 --actually_send_mail  
    python grade.py --dir /Users/admin/biol-494/exercises2/ --sol /Users/admin/biol-494/solutions2 --ex 3052 --action send_mail --start 21 --end 40 --actually_send_mail --send_to_me
    python grade.py --dir /Users/admin/biol-494/exercises2/ --sol /Users/admin/biol-494/solutions2 --action send_mail --start 21 --end 40 --actually_send_mail  
    python grade.py --dir /Users/admin/biol-494/exercises2/ --sol /Users/admin/biol-494/solutions2 --ex 3052 --action send_mail --start 21 --end 40 --actually_send_mail


    python grade.py --dir /Users/admin/biol-494/exercises2/ --sol /Users/admin/biol-494/solutions2 --action send_mail --start 21 --end 40 --actually_send_mail 

    python grade.py --dir /Users/admin/biol-494/exercises/ --sol /Users/admin/biol-494/solutions --ex 2743 --action grade 

    python grade.py --dir /Users/admin/biol-494/exercises2/ --sol /Users/admin/biol-494/solutions2 --action grade

    # 3rd Round
    python grade.py --dir /Users/admin/biol-494/exercises3/ --sol /Users/admin/biol-494/solutions3 --action grade --start 41 --end 60 
    python grade.py --dir /Users/admin/biol-494/exercises3/ --sol /Users/admin/biol-494/solutions3 --ex 3053 --action send_mail --start 41 --end 60 --send_to_me --actually_send_mail   
    python grade.py --dir /Users/admin/biol-494/exercises3/ --sol /Users/admin/biol-494/solutions3  --action send_mail --start 41 --end 60 --actually_send_mail

    # 4th Round 
    python grade.py --dir /Users/admin/biol-494/exercises4/ --sol /Users/admin/biol-494/solutions4 --action grade --start 61 --end 80 
    python grade.py --dir /Users/admin/biol-494/exercises4/ --sol /Users/admin/biol-494/solutions4 --action send_mail --ex 3168 --send_to_me --actually_send_mail --start 61 --end 80 
    python grade.py --dir /Users/admin/biol-494/exercises4/ --sol /Users/admin/biol-494/solutions4 --action send_mail --ex 2729 --actually_send_mail --start 61 --end 80 
    python grade.py --dir /Users/admin/biol-494/exercises4/ --sol /Users/admin/biol-494/solutions4 --action send_mail --ex 2913 --actually_send_mail --start 61 --end 80 
    python grade.py --dir /Users/admin/biol-494/exercises4/ --sol /Users/admin/biol-494/solutions4 --action send_mail --ex 3125 --actually_send_mail --start 61 --end 80
    python grade.py --dir /Users/admin/biol-494/exercises4/ --sol /Users/admin/biol-494/solutions4 --action send_mail --ex 2898 --actually_send_mail --start 61 --end 80

    # 5th Round
    python grade.py --dir /Users/admin/biol-494/exercises5/ --sol /Users/admin/biol-494/solutions5 --action grade --start 81 --end 90  
    python grade.py --dir /Users/admin/biol-494/exercises5/ --sol /Users/admin/biol-494/solutions5 --ex 2970  --action send_mail --send_to_me --actually_send_mail --start 81 --end 90
    python grade.py --dir /Users/admin/biol-494/exercises5/ --sol /Users/admin/biol-494/solutions5 --action send_mail --actually_send_mail --start 81 --end 90  
    python grade.py --dir /Users/admin/biol-494/exercises5/ --sol /Users/admin/biol-494/solutions5 --ex 2967  --action send_mail --actually_send_mail --start 81 --end 90  
    python grade.py --dir /Users/admin/biol-494/exercises5/ --sol /Users/admin/biol-494/solutions5 --ex 3037  --action send_mail --actually_send_mail --start 81 --end 90  

    # final
    python grade.py --dir /Users/admin/biol-494/final/ --sol /Users/admin/biol-494/solutions_final --action grade --start 1 --end 100  
    python grade.py --dir /Users/admin/biol-494/final/ --sol /Users/admin/biol-494/solutions_final --action grade --start 1 --end 100 --ex 2979
    python grade.py --dir /Users/admin/biol-494/final/ --sol /Users/admin/biol-494/solutions_final --ex 2979  --action send_mail --random_list 10 --actually_send_mail --send_to_me --start 1 --end 100 
    python grade.py --dir /Users/admin/biol-494/final/ --sol /Users/admin/biol-494/solutions_final --ex 2979  --action send_mail --random_list 10 --actually_send_mail --start 1 --end 100 
    python grade.py --dir /Users/admin/biol-494/final/ --sol /Users/admin/biol-494/solutions_final --ex 3117  --action send_mail --random_list 10 --actually_send_mail --start 1 --end 100 --send_to_me
    python grade.py --dir /Users/admin/biol-494/final/ --sol /Users/admin/biol-494/solutions_final   --action send_mail --random_list 10 --actually_send_mail --start 1 --end 100 
    '''

    parser = argparse.ArgumentParser()
    parser.add_argument("--dir", help="Directory with exercises")
    parser.add_argument("--sol", help="Directory with solutions")
    parser.add_argument("--ex", help="Examine only given ΑΜ")
    parser.add_argument("--action", help="What to do: grade")
    parser.add_argument("--actually_send_mail", action="store_true")
    parser.add_argument("--send_to_me", action="store_true")
    parser.add_argument("--start", type=int, help="Start from")
    parser.add_argument("--end", type=int, help="Start end")
    parser.add_argument("--random_list", type=int, help='Number of random exercises')
    args = parser.parse_args()

    g = Grades(directory=args.dir, ex=args.ex, solutions_dir=args.sol, 
        action=args.action,
        actually_send_mail=args.actually_send_mail,
        send_to_me=args.send_to_me,
        start = args.start,
        end = args.end,
        random_list = args.random_list,
        )
    
