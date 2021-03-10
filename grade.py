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
import argparse

from itertools import groupby
from collections import defaultdict

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
        "'Ασκηση", "Αskisi", "Άσκση",
    ]

    ex_regexp = re.compile(r'^\s*#+\s*({})\s*(?P<ask>\d+)'.format('|'.join(declarations)))

    SOLUTIONS_FILENAME_PATTERN = 'AM_{id_}_ASK_{ASK}'

    def __init__(self, directory, solutions_dir, action, ex=None):
        self.dir = directory
        self.solutions_dir = solutions_dir
        self.get_filenames(ex)
        self.get_all_exercises()
        if action == 'grade':
            self.grade()

    def get_solutions_filename(self, id_, exercise):

        filename = self.SOLUTIONS_FILENAME_PATTERN.format(id_=id_, ASK=exercise)

        return os.path.join(self.solutions_dir, filename)

    def get_grade_from_comment(self, comment):
        grades = [int(x) for x in comment.split('\n') if re.match(r'^\d+$', x)]
        assert len(grades) == 1
        assert grades[0] in range(0,11)

        return grades[0]


    def grade(self,):

        # How many answers are in total?
        total = len(self.all_exercises)
        print ('Total Answers:', total)

        for i, (exercise, id_, answer) in enumerate(self.all_exercises):

            filename = self.get_solutions_filename(id_, exercise)

            print ('Progress: {}/{} {:0.2f}%'.format(i+1, total, 100*(i+1)/total))
            print ('Exercise:', exercise)
            print ('      AM:', id_)
            print ('Filename:', filename)
            print ('==================')

            if os.path.exists(filename):
                print ('   Already graded..')
                continue

            print (answer)
            print ('==================')
            comment = ''
            while True:
                line = input() # NEVER USE INPUT!! 
                if line.strip() in ['q', ';']:
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
            id_ = self.get_id_from_filename(filename)
            content = self.get_exercises(filename)

            for ask, solution in self.iterate_exercises(content):
                data.append((id_, ask, solution))

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
                assert k2

        # Group and sort according to ask / AM
        self.all_exercises = sorted((int(k2), k, v2) for k,v in self.all_exercises.items() for k2,v2 in v.items())
        

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

        code_cells = ['\n'.join(x['source']) for x in content['cells'] if x['cell_type'] == 'code']
        return '\n\n'.join(code_cells)

    def get_exercises_MIME(self, filename):
        with open(filename) as f:
            content = f.read()

        m = email.message_from_string(content)
        payload = m.get_payload()
        assert len(payload) == 21 # FIXME

        content = ""
        for x in payload[1:]:
            content += '\n' + x.get_payload(decode=True).decode("utf-8")

        return content 

        
    def get_filenames(self, ex=None):
        if not ex:
            ex='*'

        self.filenames = glob.glob(os.path.join(self.dir, ex))
        print ('Read: {} files'.format(len(self.filenames)))

if __name__ == '__main__':
    '''
    python grade.py --dir /Users/admin/biol-494/exercises/ --sol /Users/admin/biol-494/solutions --action grade
    python grade.py --dir /Users/admin/biol-494/exercises/ --ex 3158 
    '''

    parser = argparse.ArgumentParser()
    parser.add_argument("--dir", help="Directory with exercises")
    parser.add_argument("--sol", help="Directory with solutions")
    parser.add_argument("--ex", help="Examine only given exercise")
    parser.add_argument("--action", help="What to do: grade")
    args = parser.parse_args()

    g = Grades(directory=args.dir, ex=args.ex, solutions_dir=args.sol, action=args.action)
    
