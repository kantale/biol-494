## Serialization

Ας υποθέσουμε ότι έχουμε τη παρακάτω "πολύπλοκη" δομή:


```python
a={'a': [1,2,3,], 'ffrrf': {'b': [4,4,5,6]}}
```

Πως μπορούμε να αποθηκεύσουμε το a σε ένα αρχείο; Μπορούμε να τα αποθηκεύσουμε σε μορφή json:


```python
import json
a_json = json.dumps(a)
print (a_json)
```

    {"a": [1, 2, 3], "ffrrf": {"b": [4, 4, 5, 6]}}



```python
type(a_json)
```




    str



Οπότε μπορούμε να σώσουμε το a_json σε ένα αρχείο:


```python
with open('results.txt', 'w') as f:
    f.write(a_json + '\n')
```

Ή αλλιώς:


```python
with open('results.txt', 'w') as f:
    json.dump(a, f)
```


```python
!cat results.txt
```

    {"a": [1, 2, 3], "ffrrf": {"b": [4, 4, 5, 6]}}

Για όσους είναι στα windows, μπορείτε να γράψετε:


```python
!type results.txt
```

Αφού στείλουμε το αρχείο μπορεί ο παραλήπτης να το ανοίξει:


```python
with open('results.txt') as f:
    a = json.load(f)
print (a)
print (type(a))
```

    {'a': [1, 2, 3], 'ffrrf': {'b': [4, 4, 5, 6]}}
    <class 'dict'>


Αυτή η διαδικασία ονομάζεται [serialization](https://en.wikipedia.org/wiki/Serialization) και μας επιτρέπει να διαμοιραζόμαστε δεδομένα μαζί με τη δομή τους. 

Δεν μπορούν όλα να γίνουν json:


```python
try:
    json.dumps({1,2,3,4}) # Sets cannot be serialized
except Exception as e:
    print (e)
```

    Object of type set is not JSON serializable



```python
def f(x):
    return x+1

try:
    json.dumps(f) # Functions cannot be serialized 
except Exception as e:
    print (e)
```

    Object of type function is not JSON serializable


Το [φορμάτ json](https://en.wikipedia.org/wiki/JSON) είναι πολύ δημοφιλές στον διαμοιρασμό "δομημένων δεδομένων". Δηλαδή δεδομένα που αποτελούνται από λίστες και λεξικά ή/και συνδοιασμό αυτών. Επίσης είναι πολύ συνηθισμένο μία βάση δεδομένων να μοιράζεται τα δεδομένα της σε αυτό το φορμάτ. Για παράδειγμα σε αυτό το link:

http://mygene.info/v3/query?q=tumor&fields=symbol&size=1000&species=human'

Μπορείτε να ρωτήσετε μία βάση δεδομένων για να σας δώσει μία λίστα από 1000 γονίδια τα οποία έχουν συσχετιστεί με τον καρκίνο. Το αποτέλεσμα το επιστρέφει σε φορμάτ json. 

Εκτός από το json υπάρχουν και άλλα φορμάτ για την ανταλλαγή δομημένων δεδομένων. Μερικά παραδείγματα είναι το [XML](https://docs.python.org/3/library/xml.html) και το [YAML](https://github.com/yaml/pyyaml).

Είδαμε όμως ότι το json μπορεί να δεχτεί μόνο λίστες και dictionaries. Μία άλλη επιλογή είναι η βιβλιοθήλη [pickle](https://docs.python.org/3/library/pickle.html) η οποία μπορεί να κάνει serialize πολύ μεγαλύτερο πλήθος από δομές. Τα αρνητικά της είναι:

1. Είναι μόνο για python (ίσως αν ψάξετε να βρείτε και βιβλιοθήκες για άλλες γλώσσες)
2. Δεν είναι αναγνώσιμο απο ανθρώπους (σε αντίθεση με τη json).

Ας δούμε ένα παράδειγμα:


```python
import pickle


def a_function(x):
    return x+1

a_set = {1,2,3,4}

a_list = [1,'mitsos', {1:True}, a_function, a_set]

with open('my_data.pickle', 'wb') as f:
    pickle.dump(a_list, f)


```

Προσέξτε το 'wb' το οποίο σημαίνει εγγραφή σε δυαδικό (binary) φορμάτ. Σε αντίθεση με το σκέτο 'w' ή το 'wt' το οποίο σημείνει φορμάτ κειμένου (text).

Ας το κάνουμε τώρα un-pickle!


```python
with open('my_data.pickle', 'rb') as f:
    data = pickle.load(f)
```


```python
data[3](10) # Καλούμε τη συνάρτηση f !
```




    11



### Η βιβλιοθήκε itertools

Η [itertools](https://docs.python.org/3/library/itertools.html) περιέχει συναρτήσεις για να σας βοηθήσουν να κάνετε iterations και.. λούπες! Είναι μία από τις πιο χρησιμες βιβλιοθήκες κυρίως γιατί σας βοηθάει να απλοποιήσετε τον κώδικά σας. Πριν επιχευρήσετε να κάνετε κάποια πολύπλοκη επανάληψη (for μέσα σε for μέσα σε for...) ελέγξτε αν κάποια από τις συναρτήσεις της itertools μπορεί να σας βοηθήσει. 

#### Πρόβλημα 1 (καρτεσιανό γινόμενο)
Μπαίνετε σε ένα μαγαζί με ρούχα. Το μαγαζί έχει 10 διαφορετικά ζευγάρια παπούτσια στο νούμερό σας και η τιμή τους είναι:

```python
shoes = [22, 30, 83, 28, 72, 51, 61, 83, 25]
```

To μαγαζί έχει 3 διαφορετικά τζην στο νούμερό σας και η τιμή τους είναι:

```python
jeans = [30, 79, 34]
```

To μαγαζί έχει 8 διαφορετικά μπλουζάκια στο νούμερό σας. Η τιμή του είναι:

```python
shirts = [24, 25, 40, 40, 26, 28, 19]
```

Έσείς έχετε πάνω σας 100 ευρώ και πρέπει να πάρετε ένα από κάθε είδος. Πόσοι συνδυασμοί (παπούτσια, τζην και μπλουζάκι) ρούχων μπορείτε να αγοράσετε;



```python
shoes = [22, 30, 83, 28, 72, 51, 61, 83, 25]
jeans = [30, 79, 34]
shirts = [24, 25, 40, 40, 26, 28, 19]
```


```python
# Κλασσική λύση:
c = 0
for x in shoes:
    for y in jeans:
        for z in shirts:
            if x+y+z<=100:
                c += 1
print (c)
```

    53



```python
# Με itertools:
from itertools import product

c = 0
for x,y,z in product(shoes, jeans, shirts):
    if x+y+z<=100:
        c += 1
print (c)

```

    53


### Πρόβλημα 2 (συνδoιασμοί)

Μπαίνετε σε ένα μαγαζί το οποίο πουλάει μόνο μπλουζάκια. Το είδος και η τιμή για το κάθε μπλουζάκι είναι:

```python
shirts = [
    ('a', 22), 
    ('b', 30), 
    ('c', 83),
    ('d', 28),
    ('e', 72),
    ('f', 51),
    ('g', 61),
    ('h', 83),
    ('i', 25),
]
```

Εσείς μπορείτε να ξοδέψετε το πολύ 100ε και πρέπει να πάρετε ακριβώς 2. Ποια ζευγάρια μπορείτε να επιλέξετε; 



```python
shirts = [
    ('a', 22), 
    ('b', 30), 
    ('c', 83),
    ('d', 28),
    ('e', 72),
    ('f', 51),
    ('g', 61),
    ('h', 83),
    ('i', 25),
]

#O κλασσικός τρόπος:
c = 0
for i_1, (kind_1, price_1) in enumerate(shirts):
    for kind_2, price_2 in shirts[i_1+1:]:
        if price_1 + price_2 <= 100:
            c += 1
print (c)
    
```

    17



```python
# Με itertools
from itertools import combinations

c = 0
for (kind_1, price_1), (kind_2, price_2) in combinations(shirts, 2):
    if price_1 + price_2 <= 100:
        c += 1
print (c)

```

    17


### Πρόβλημα 3 (αντί while)

Ποιος είναι το άθροισμα όλων των πρώτων αριθμών που είναι μικρότεροι από 1000;


```python
from itertools import takewhile

# Αρχικά φτιάχνουμε ένα generator για πρώτους αριθμούς:
def gen_primes():
    yield 1
    n = 2
    while True:
        for i in range(2, n):
            if n%i==0:
                break
        else:
            yield n
        n += 1

# Φτιάχνουμε μία συνάρτηση που ελέγχει πότε θα σταματήσουμε:
def f(x):
    return x<1000

# Υπολόγισε το άθροισμα των πρώτων αριθμών, μέχρι να βρεθεί 
# κάποιος πρώτος που να μην ικανοποιεί τη f
sum(takewhile(f, gen_primes()))

```




    76128



## Regular Expressions

Τα [Regular Expressions](https://en.wikipedia.org/wiki/Regular_expression) (ή αλλιώς regexp για συντομία) είναι μια βασική ιδέα στην επιστήμη υπολογιστών (υπάρχουν απο το 1956..). Είναι στην ουσία μία νέα γλώσσα με την οποία μπορείς να δηλώσεις κάποια patterns μέσα σε ένα string. Ειδικοί αλγόριθμοι αναλαμβάνουν να εντοπίσουν αυτά τα patterns με πολύ μεγάλη ταχύτητα. Τα regexp υλοποιούνται στη python στη βιβλιοθήκη ```re```:


```python
import re # Regular Expression
```

Με τα regular expressions μπορούμε να κάνουμε πάρα πολύ γρήγορα πολύπλοκες λειτουργίες πάνω σε strings. Αυτέ οι λειτουργίες είναι:
* Έλεγχος αν ένα string ακολουθεί ένα συγκεκριμένο format / pattern (π.χ. αποτελέιται από 4 αριθμούς και 2 γράμματα
* Να πάρουμε ένα υπο-string. Για παράδειγμα από μια ημερομηνία γέννησης να εξάγουμε τη χρονιά
* Να πάρουμε όλα τα υπο-strings τα οποία ακολουθούν ένα πρότυπο. Για παράδειγμα από ένα τεράστιο αρχείο με κείμενο να εξάγουμε όλες τις ημερομηνίες που περιέχει.
* Να αντικαταστάσήσουμε ένα pattern από ένα string μέ κάποιο άλλο. Για παράδειγμα κάνε όλες τις ημερομηνίες οι οποίες είναι Μήνας/Μέρα/Χρονιά (αμερικανικό σύστημα) να είναι Μέρα/Μήνας/Χρονιά (ευρωπαϊκό σύστημα). 

Τα regular expressions (regex) είναι πρωτίστως strings. Κάθε regex δηλώνει και ένα pattern. Για παράδειγμα το regexp: '\d' δηλώνει "ένας χαρακτήρας που είναι αριθμός". Ας το δούμε στη πράξη:


```python
re.search(r'\d', '5')
```




    <re.Match object; span=(0, 1), match='5'>



Με αυτή την εντολή στην ουσία λέμε: "Ψάξε αν υπάρχει τουλάχιστον ένας αριθμός μέσα στο string". Παρατηρούμε ότι μας επέστρεψε "κάτι". Θα δούμε στη συνέχεια τι είναι αυτό. Για αρχή μπορούμε να ελέγξουμε τι επιστρέφει αν ΔΕΝ βρει το pattern:


```python
a = re.search(r'\d', 'a')
print (a)
```

    None


Αν δεν υπάρχει το pattern επιτρέφει None. Μπορούμε να επεκτείνουμε το pattern ζητώντας ένας αριθμό που να ακολουθείται με τον χαρακατήρα "a":


```python
a = re.search(r'\da', 'hello5ahello')
print (a)
```

    <re.Match object; span=(5, 7), match='5a'>



```python
a = re.search(r'\da', 'hello5hello')
print (a)
```

    None


Παρατηρούμε ότι:
* Στο 1ο το βρήκε. Με την εντολή search ζητάμε να βρει κάπου **οπουδήποτε** μέσα στο string.
* Στο δεύτερο δεν το βρήκε. Δεν υπάρχει πουθενά ένας αριθμός που να ακολουθείται από από το γράμμα "a".

Συνεχίζουμε ζητώντας ένας αριθμός ο οποίος να ακολουθείται είτε από το γράμμα "a" είτε με το γράμμα "b":


```python
a = re.search(r'\d[ab]', 'hello5ahello')
print (a)
```

    <re.Match object; span=(5, 7), match='5a'>



```python
a = re.search(r'\d[ab]', 'hello5bhello')
print (a)
```

    <re.Match object; span=(5, 7), match='5b'>



```python
a = re.search(r'\d[ab]', 'hello5chello')
print (a)
```

    None


Με τις αγκύλες λοιπόν δηλώνουμε ένα set από χαρακτήρες. Ζητάμε δηλαδή να βρεί έναν και μόνο ένα χαρακτήρα οποίος να ανήκει σε αυτό το set. 

Συνεχίζουμε ζητώντας έναν οποιοδήποτε αριθμό ακολουθούμενο από οποιοδήποτε χαρακτήρα από a μέχρι και το k: Μέσα σε αγγύλες μπορούμε να δηλώσουμε 1 ή παραπάνω έυρη χαρακτήρων:


```python
a = re.search(r'\d[a-k]', 'hello5dhello')
print (a)
```

    <re.Match object; span=(5, 7), match='5d'>



```python
a = re.search(r'\d[a-k]', 'hello5lhello')
print (a)
```

    None


Συνεχίζουμε ζητώντας ένας αριθμό ο οποίος ακολουθείται από οποιοδήποτε χαρακτήρα εκτός από αυτούς που ανήκουν στο εύρος a-k. Για να το κάνουμε αυτό βάζουμε το carret (```^```) μέσα στις αγκύλες:


```python
a = re.search(r'\d[^a-k]', 'hello5dhello')
print (a)
```

    None



```python
a = re.search(r'\d[^a-k]', 'hello5lhello')
print (a)
```

    <re.Match object; span=(5, 7), match='5l'>


Συνεχίζουμε ζητώντας έναν αριθμό που να αποτελείται από οποιοδήποτε χαρακτήρα! Η τελεία "." σημαίνει "οποιοσδήποτε χαρακτήρας":


```python
a = re.search(r'\d.', 'hello5bhello')
print (a)
```

    <re.Match object; span=(5, 7), match='5b'>



```python
a = re.search(r'\d.', 'hellohello5')
print (a)
```

    None


Συνεχίζουμε δηλώνοντας έναν αριθμό και ένα κενό ή tab ή new line. Ο ειδικός χαρακτήρας \s δηλώνει "[white space](https://en.wikipedia.org/wiki/White_space)":


```python
a = re.search(r'\d\s', 'hello5 hello')
print (a)
```

    <re.Match object; span=(5, 7), match='5 '>



```python
a = re.search(r'\d\s', 'hello5hello')
print (a)
```

    None


Συνεχίζουμε δηλώνοντας έναν αριθμό ακολουθούμενο από οποιοδήποτε γράμμα το οποίο ΔΕΝ είναι ειδικός χαρακτήρας. Το pattern \w δηλώνει οποιοδήποτε χαρακτήρα από τα: ```a-z``` ```A-Z``` ```0-9``` και ```_```:


```python
a = re.search(r'\d\w', 'hello5hello')
print (a)
```

    <re.Match object; span=(5, 7), match='5h'>



```python
a = re.search(r'\d\w', 'hello5$hello')
print (a)
```

    None


Δηλαδή αντί να γράφουμε ```[0-9]``` για να δηλώνουμε όλους τους αριθμούς και ```[a-zA-Z]``` για δηλώνουμε όλα τα γράμματα χρησιμοποιούμε τα εξής:

```\d``` είναι το ίδιο με: ```[0-9]```

```\w``` είναι το ίδιο με: ```[a-zA-Z0-9_]```

```\s``` είναι το ίδιο με: ```[ \t\n\r\f\v]``` 

#### Επαναλαμβανόμενα μοτίβα
Μπορούμε να ζητήσουμε σε ένα pattern να βρεί πολλαπλές επαναλήψεις από ένα σύνολο χαρακτήρων. Για παράδειγμα μπορούμε να ρωτήσουμε: να έχει 1 ή παραπάνω αριθμούς ακολουθούμενοι από το γράμμα "a". Αυτό το κάνουμε με τον ειδικό χαρακτήρα ```+```:


```python
a = re.search(r'\d+a', 'hello123431ahello') # Polloi ari8moi meta "a"
print (a)
```

    <re.Match object; span=(5, 12), match='123431a'>



```python
a = re.search(r'\d+a', 'hello1ahello') # enas ari8mos meta "a"
print (a)
```

    <re.Match object; span=(5, 7), match='1a'>



```python
a = re.search(r'\d+a', 'helloahello') # Kanenas ari8mos meta "a" (den kanei match)
print (a)
```

    None


Αν αντί για ```+``` βάλουμε ```*```. Τότε δηλώνουμε: "κανένα ή πολλά". Δηλαδή ενώ με το ```+``` πρέπει υποχρεωτικά να υπάρχει τουλάχιστον 1, με το ```*``` μπορεί να μην υπάρχει και κανένα: 


```python
a = re.search(r'\d*a', 'hello444a') # polloi ari8moi kai meta to a ! OK!
print (a)
```

    <re.Match object; span=(5, 9), match='444a'>



```python
a = re.search(r'\d*a', 'hello4a') # enas ari8mow kai meta to a ! OK!
print (a)
```

    <re.Match object; span=(5, 7), match='4a'>



```python
a = re.search(r'\d*a', 'helloa') # kanenas ari8mos kai meta to a ! PALI OK!
print (a)
```

    <re.Match object; span=(5, 6), match='a'>



```python
a = re.search(r'\d*a', 'hel555lo') # Yparxei ari8mos alla den yparxei to a. NOT OK!
print (a)
```

    None


Μπορούμε επίσης να δηλώσουμε "ένα ή κανένα". Για παράδειγμα θέλουμε είτε κανένα αριθμό και μετά το "a", είτε έναν αριθμό και μετά το "a". Αυτό το κάνουμε με τον χαρακτήρα ```?```:


```python
a = re.search(r'b\d?a', 'b5a') # yparxei to b meta enas ari8mos kai meta to a. OK
print (a)
```

    <re.Match object; span=(0, 3), match='b5a'>



```python
a = re.search(r'b\d?a', 'ba') # yparxei to b meta kanenas ari8mos kai meta to a. OK
print (a)
```

    <re.Match object; span=(0, 2), match='ba'>



```python
a = re.search(r'b\d?a', 'b65a') # yparxei to b meta polloi ari8moi kai meta to a. NOT OK
print (a)
```

    None


Τέλος μπορούμε να ζητήσουμε ένα σύνολο από χαρακτήρες να υπάρχει συγκεκριμμένο αριθμό από επαναλήψεις!


```python
a = re.search(r'ba{3}b', 'baaab') # b treis fores to a kai me ta b
print (a)
```

    <re.Match object; span=(0, 5), match='baaab'>



```python
a = re.search(r'ba{3}b', 'baab') # b treis fores to a kai me ta b
print (a)
```

    None



```python
a = re.search(r'ba{3}b', 'baaaab') # b treis fores to a kai me ta b
print (a)
```

    None


ή να δηλώσουμε ένα εύρος από επαναλήψεις:


```python
a = re.search(r'ba{2,4}b', 'bab') # Ζητάμε από 2 έως 4 "a"
print (a)
```

    None



```python
a = re.search(r'ba{2,4}b', 'baab') # Ζητάμε από 2 έως 4 "a"
print (a)
```

    <re.Match object; span=(0, 4), match='baab'>



```python
a = re.search(r'ba{2,4}b', 'baaab') # Ζητάμε από 2 έως 4 "a"
print (a)
```

    <re.Match object; span=(0, 5), match='baaab'>



```python
a = re.search(r'ba{2,4}b', 'baaaab') # Ζητάμε από 2 έως 4 "a"
print (a)
```

    <re.Match object; span=(0, 6), match='baaaab'>



```python
a = re.search(r'ba{2,4}b', 'baaaaab') # Ζητάμε από 2 έως 4 "a"
print (a)
```

    None



```python
a = re.search(r'ba{2,}b', 'baaaaab') # Ζητάμε 2 ή παραπάνω
print (a)
```

    <re.Match object; span=(0, 7), match='baaaaab'>



```python
a = re.search(r'ba{2,}b', 'bab') # Ζητάμε 2 ή παραπάνω
print (a)
```

    None



```python
a = re.search(r'ba{2,}b', 'baaaaaaab') # Ζητάμε 2 ή παραπάνω
print (a)
```

    <re.Match object; span=(0, 9), match='baaaaaaab'>



```python
a = re.search(r'ba{,2}b', 'baaab') # Ζητάμε 2 ή λιγότερα
print (a)
```

    None



```python
a = re.search(r'ba{,2}b', 'baab') # Ζητάμε 2 ή λιγότερα
print (a)
```

    <re.Match object; span=(0, 4), match='baab'>



```python
a = re.search(r'ba{,2}b', 'bab') # Ζητάμε 2 ή λιγότερα
print (a)
```

    <re.Match object; span=(0, 3), match='bab'>



```python
a = re.search(r'ba{,2}b', 'bb') # Ζητάμε 2 ή λιγότερα
print (a)
```

    <re.Match object; span=(0, 2), match='bb'>


Ας δούμε λίγο το παρακάτω:


```python
a = re.search(r'ba+b', 'hellobaaaaabhello')
print (a)
```

    <re.Match object; span=(5, 12), match='baaaaab'>


Με τη συνάρτηση .group μπορούμε να βρούμε ΤΙ έκανε match. Βάζοντας σαν παράμετρο τη τιμή 0 μας επιστρέφει όλο το string το οποίο έκανε match:


```python
a.group(0)
```




    'baaaaab'



Εδώ παρατηρούμε το εξής: το a+ "έπιασε" όλα τα "a" αυτό ονομάζεται greedy search. Η python γενικότερα θα προσπαθήσει να κάνει match όσο το δυνατόν περισσότερους χαρακτήρες γίνεται. Αυτό μπορεί να μας δημιουργήσει προβλήματα!. Για παράδειγμα. Έστω το string:


```python
s = 'gene:G1 function: F1, gene:G2 function:F2, gene:G3 function:F3'
```

Θέλουμε να πάρουμε το όνομα του πρώτου γονιδίου. Άρα να αρχίζει από ```gene:``` μετά ένα ακαθόριστο πλήθος από χαρακτήρες και μετά το string ```function```:


```python
a = re.search(r'gene:.+function', s)
print (a.group(0))
```

    gene:G1 function: F1, gene:G2 function:F2, gene:G3 function


Τι έγινε εδώ;; παρατηρούμε ότι αυτό που επέστρεψε όντως ακολουθεί το πρότυπο αφού ξεκινά από gene και τελειώνει σε function. Αυτό έγινε επειδή η python προσπάθησε να επιστρέψει το μεγαλύτερο δυνατό match. Δηλαδή και το string ```gene:G1 function``` ακολουθεί το πρότυπο που βάλαμε, αλλά δεν είναι το μεγαλύτερο δυνατό. Μπορούμε να αποτρέψουμε αυτή τη συμπεριφορά βάζοντας ένα ```?``` μετά το ```+```:


```python
a = re.search(r'gene:.+?function', s)
print (a.group(0))
```

    gene:G1 function


Ο χαρακτήρας ```?``` μετά από ```+,*,?,{}``` λέει στη python "φέρε το μικρότερο δυνατό". Δείτε αυτά τα παραδείγματα:


```python
a = re.search(r'b\d+\d', 'b12345')
print (a.group(0))
```

    b12345



```python
a = re.search(r'b\d+?\d', 'b12345')
print (a.group(0))
```

    b12



```python
a = re.search(r'b\d*\d', 'b12345')
print (a.group(0))
```

    b12345



```python
a = re.search(r'b\d*?\d', 'b12345')
print (a.group(0))
```

    b1



```python
a = re.search(r'b\d?\d', 'b12345')
print (a.group(0))
```

    b12



```python
a = re.search(r'b\d??\d', 'b12345')
print (a.group(0))
```

    b1



```python
a = re.search(r'b\d{2,4}', 'b12345') # epilegei to megalutero --> 4
print (a.group(0))
```

    b1234



```python
a = re.search(r'b\d{2,4}?', 'b12345') # epilegei to mikrotero --> 2
print (a.group(0))
```

    b12


#### Αρχή και τέλος

Μπορούμε να δηλώσουμε ότι ένα pattern πρέπει να υπάρχει στην αρχή του string, αν βάλουμε στην αρχή του pattern τον χαρακτήρα ```^```:



```python
a = re.search('^\d', '4hello') # Prepei o ari8mos na einai sthn arxh! OK!
print (a)
```

    <re.Match object; span=(0, 1), match='4'>



```python
a = re.search('^\d', 'h4ello') # Prepei o ari8mos na einai sthn arxh! NOT OK!
print (a)
```

    None


Ομοίως μπορούμε να δηλώσουμε ότι το pattern θα είναι στο τέλος με τον χαρακτήρα ```$```:


```python
a = re.search('\d$', 'hello4') # Prepei o ari8mos na einai sto telos! OK!
print (a)
```

    <re.Match object; span=(5, 6), match='4'>



```python
a = re.search('\d$', 'hell4o') # Prepei o ari8mos na einai sto telos! NOT OK!
print (a)
```

    None


#### Ο τελεστής  ή --> ```|``` 

Πολλές φορές θέλουμε ένα pattern να κάνει match ΚΑΤΙ ή ΚΑΤΙ ΑΛΛΟ. Αυτό γίνεται βάζοντας σε παρενθέσεις τα δύο patterns και χρησιμοποιώντας τον τελεστή ```|```:



```python
a = re.search(r'(ab)|(kl)', 'ab') # ab ή kl
print (a)
```

    <re.Match object; span=(0, 2), match='ab'>



```python
a = re.search(r'(ab)|(kl)', 'kl') # ab ή kl
print (a)
```

    <re.Match object; span=(0, 2), match='kl'>



```python
a = re.search(r'(ab)|(kl)', 'al') # ab ή kl
print (a)
```

    None


Μπορούμε να κάνουμε εμφωλευμένα ```|```:


```python
a = re.search(r'(a(12)|(34)b)|(1(ab)|(kl)2)', 'a12') 
print (a)
a = re.search(r'(a(12)|(34)b)|(1(ab)|(kl)2)', '34b') 
print (a)
a = re.search(r'(a(12)|(34)b)|(1(ab)|(kl)2)', '1ab') 
print (a)
a = re.search(r'(a(12)|(34)b)|(1(ab)|(kl)2)', 'kl2') 
print (a)

```

    <re.Match object; span=(0, 3), match='a12'>
    <re.Match object; span=(0, 3), match='34b'>
    <re.Match object; span=(0, 3), match='1ab'>
    <re.Match object; span=(0, 3), match='kl2'>


#### Παίρνοντας πεδία μέσα από patterns

Πολλές φορές θέλουμε να εξάγουμε υπο-πεδία από ένα string. Για να το κάνουμε αυτό βάζουμε παρενθέσεις στα κομμάτια του pattern που θέλουμε να εξάγουμε:




```python
import re
plate_number = ' This is my plate number: ABE 1234 hello'

a = re.search(r'(\w+) (\d+)', plate_number)
```

Στη συνέχεια μπορούμε να χρησιμοποιήσουμε τη group για να πάρουμε αυτά τα πεδία:

Όλο το string το οποίο έκανε match:


```python
a.group(0)
```




    'ABE 1234'



Το string που έκανε match στη 1η παρένθεση:


```python
a.group(1)
```




    'ABE'



το string που έκανε match στη 2η παρένθεση:


```python
a.group(2)
```




    '1234'



Ο τρόπος αυτός για να προσπελάσουμε τα πεδία που έχουμε κάνει match σε ένα group πολλές φορές δεν βολεύει γιατί απλά πρέπει να ξέρουμε τη σειρά με την οποία έχουμε βάλει τις παρενθέσεις. Ένας άλλος τρόπος είναι να δηλώσουμε ένα όνομα στο group το οποίο θέλουμε να κάνουμε match. Αυτά τα groups ονομάζονται named groups. Αυτό το κάνουμε με τη χρήση του `(?P<name_of_group><group_pattern>)`. Για παράδειγμα:


```python
import re
plate_number = ' This is my plate number: ABE 1234 hello'

a = re.search(r'(?P<letters>\w+) (?P<numbers>\d+)', plate_number)
```


```python
print (a.group('letters'))
```

    ABE



```python
print (a.group('numbers'))
```

    1234


Μπορούμε επίσης να χρησιμοποιήσουμε τη συνάρτηση `groupdict` για να πάρουμε όλα τα groups που έχουμε κάνει match σε ένα dictionary:


```python
print (a.groupdict())
```

    {'letters': 'ABE', 'numbers': '1234'}


Είναι ενδιαφέρον το γεγονός ότι αν ένα group δεν έχει γίνει match (επειδή π.χ. το έχουμε βάλει σαν προαιρετικό) τότε η τιμή του στο dictionary είναι `None`. Ας δούμε ένα παράδειγμα:


```python
m = re.search(r'(?P<prosimo>[+-])?(?P<number>\d+)', '123')
m.groupdict()
```




    {'prosimo': None, 'number': '123'}




```python
m = re.search(r'(?P<prosimo>[+-])?(?P<number>\d+)', '-123')
m.groupdict()
```




    {'prosimo': '-', 'number': '123'}



### Οι συναρτήσεις match, fullmatch,  findall  και  sub:

Η συνάρτηση search που έχουμε δει μέχρι στιγμής χρησιμοποιείται για να βρούμε ένα pattern μέσα σε ένα string. Μία άλλη χρήσιμη συνάρτηση είναι η ```fullmatch``` η οποία κάνει match **μόνο αν** όλο το string κάνει match το pattern:


```python
a = re.search('rs\d+', 'This is a mutation: rs123456')
print (a)
```

    <re.Match object; span=(20, 28), match='rs123456'>



```python
a = re.fullmatch('rs\d+', 'This is a mutation: rs123456')
print (a)
```

    None



```python
a = re.fullmatch('rs\d+', 'rs123456')
print (a)
```

    <re.Match object; span=(0, 8), match='rs123456'>


Η fullmatch κάνει το ίδιο με τη search αν εσωκλείσουμε το pattern μέσα σε ```^$```:


```python
a = re.search('rs\d+', 'This is a mutation: rs123456')
print (a)
```

    <re.Match object; span=(20, 28), match='rs123456'>



```python
a = re.search('^rs\d+$', 'This is a mutation: rs123456')
print (a)
```

    None



```python
a = re.search('^rs\d+$', 'rs123456')
print (a)
```

    <re.Match object; span=(0, 8), match='rs123456'>



```python
a = re.fullmatch('rs\d+', 'rs123456')
print (a)
```

    <re.Match object; span=(0, 8), match='rs123456'>


Η συνάρτηση match κοιτάει να δει αν το pattern είναι στην αρχή του string. Ισοδυναμεί με το να χρησιμοποιήσουμε τη search και να βάλουμε το ```^``` μπροστά από το pattern:


```python
a = re.match(r'\d+', '123hello')
print (a)
```

    <re.Match object; span=(0, 3), match='123'>



```python
a = re.match(r'\d+', 'hello123')
print (a)
```

    None



```python
a = re.search(r'^\d+', '123hello')
print (a)
```

    <re.Match object; span=(0, 3), match='123'>



```python
a = re.search(r'^\d+', 'hello123')
print (a)
```

    None


Τέλος η συνάρτηση sub, αλλάζει το κομμάτι που έχει γίνει match σε ένα string με ένα άλλο string. Μπορούμε λοιπόν να κάνουμε "capture" τα groups μέ παρενθέσεις μέσα στο pattern και μετά να αναφερθούμε σε αυτό με τον χαρακτήρα ```\``` και τον αριθμό της παρένθεσης:


```python
s = 'Name: James Bond'
re.sub(r'Name: (\w+) (\w+)', r'My name is \2, \1 \2', s)
```




    'My name is Bond, James Bond'



Τέλος με τη συνάρτηση findall μπορούμε να βρούμε όλα τα matches ενός pattern μέσα σε string:


```python
s = 'dg +5aaghqq4  ajdfhal+48f4++85tyru+4867dhgjghi4yifhl4i8+hdji74rl48ru'
re.findall(r'\+\d+', s) #  Όλοι οι αριθμοί που έχουν ένα "+" μπροστά τους
```




    ['+5', '+48', '+85', '+4867']



#### Μα τι είναι επιτέλους αυτό το r που βάζεις μπροστά από κάθε pattern;

Όπως έχουμε δει μπορούμε να βάλουμε "special" χαρακτήρες μέσα σε ένα string. Για παράδειγμα μπορούμε να βάλουμε το "Enter" (ή αλλιώς new line): 



```python
s = 'a\nb'
print (s)
```

    a
    b


Ομοίως αν θέλουμε ένα string να έχει τον χαρακτήρα ```\```, πρέπει να τον βάλουμε δύο φορές:


```python
s = 'a\\b'
print (s)
```

    a\b


Τι γίνεται όμως αν θέλουμε να δούμε αν ένα string περιέχει τον χαρακτήρα ```\``` ; Ο χαρακτήρας αυτός είναι ειδικός χαρακτήρας ΚΑΙ για τη python αλλά ΚΑΙ για τα regular expressions (Προσέξτε το ```\+``` που βάλαμε παραπάνω στην findall για να κάνουμε match τον χαρακτήρα ```+```). Για να δηλώσουμε λοιπόν τον χαρακτήρα ```\``` μέσα σε ένα pattern θα πρέπει να τον κάνουμε escape και να φτιάξουμε το pattern: ```\\```. Δηλαδή όπως ακριβώς κάναμε match το ```+``` με το pattern ```\+```, έτσι κάνουμε match το ```\``` με το ```\\```. Άρα θα πρέπει να "φτιάξουμε" ένα string το οποίο όταν το τυπώσουμε να τυπώσει: ```\\```. Αυτό το string είναι:




```python
s = '\\\\'
print (s)
```

    \\


Άρα για να κάνουμε match τον χαρακτήρα ```\``` πρέπει να γράψουμε το εξής:


```python
s = 'a\\b'
a = re.search('a\\\\b', s)
print (a)
```

    <re.Match object; span=(0, 3), match='a\\b'>


Αυτό μπορεί να είναι αρκετά.. μπερδεψηματικό και να είναι πηγή λάθους. Δυστυχώς αυτό το πρόβλημα είναι κοινό για όλες τις γλώσσες προγραμματισμού εδώ και πολλά χρόνια. Συλλογικά αυτό το πρόβλημα αναφέρεται σαν το [σύνδρομο της στραβής οδοντογλυφίδας](https://en.wikipedia.org/wiki/Leaning_toothpick_syndrome)(!!). Μία λύση που έχει η python είναι να μπορείς να δηλώσεις ένα string σαν raw (ωμό). Ένα raw string δηλώνεται βάζοντας το r μπροστά και σημαίνει ότι δεν περιέχει κανέναν άλλο χαρακτήρα πέρα από αυτούς που έχει!


```python
s = r'a\nb'
print (s)
```

    a\nb


Με αυτόν τον τρόπο μπορούμε να δηλώνουμε regular expressions χωρίς να ανησυχούμε μήπως οι ειδικοί χαρακτήρες της python συγχέονται με τους ειδικούς χαρακτήρες των regular expressions:


```python
s = 'a\\b'
a = re.search(r'a\\b', s)
print (a)
```

    <re.Match object; span=(0, 3), match='a\\b'>


Σε περίπτωση που όλα αυτά είναι δυσνόητα (πολύ λογικό) μπορείτε να θυμάστε το εξής: **Όταν χρησιμοποιούμε regular expressions, πάντα δηλώνουμε τα patterns σαν raw strings βάζοντας ένα r μπροστά.**

Επίσης το [επίσημο documentation της python](https://docs.python.org/3/library/re.html) εξηγεί πολύ όμορφά τα raw strings. 


#### Συνέχεια 

Έχουμε πει λιγότερα από τα μισά που περιέχει τόσο η θεωρία των regular expressions, όσο και η υποστήριξή τους από τη python. Μπορείτε να διαβάσετε περισσότερα για:

* [Look ahead and look begind regular expressions](https://www.rexegg.com/regex-lookarounds.html)
* [Named groups](https://docs.python.org/3/howto/regex.html#non-capturing-and-named-groups) (το καλύψαμε)
* [Non capturing parenthesis](https://docs.python.org/3/howto/regex.html#non-capturing-and-named-groups)
* [Compilation flags](https://docs.python.org/3/howto/regex.html#compilation-flags). Για παράδειγμα η τελεία θα πρέπει να "πιάνει" το enter;  Ή πως μπορώ να κάνω match αγνοώντας τη διαφορά μεταξύ κεφαλαίων και μικρών γραμμάτων;
* [Greedy vs. non-greedy](https://docs.python.org/3/howto/regex.html#greedy-versus-non-greedy) (τα εξηγήσαμε λίγο εδώ)
* [compile](https://stackoverflow.com/questions/452104/is-it-worth-using-pythons-re-compile). Μπορείτε να κάνετε compile ένα πολύπλοκο regexp για να το κάνετε match πολύ πιο γρήγορα
* [debug](https://stackoverflow.com/questions/606350/how-can-i-debug-a-regular-expression-in-python). Υπάρχουν και ειδικά site που σας βοηθάν να γράψετε και να διορθώσετε το regexp σας: [debuggex](https://www.debuggex.com/), [pythex](https://pythex.org/)
* [comments](https://softwareengineering.stackexchange.com/questions/178355/commenting-regular-expressions).  Μπορείτε να βάζετε comments  **μέσα** σε ένα regexp 

Μα καλά πόσο πολύπλοκο μπορεί να γίνει ένα regexp; Απάντηση: [Αρκετά πολύπλοκο](https://gist.githubusercontent.com/kantale/65e8652ab4f08307bb502609fcba29f4/raw/0da903d9932acb5b9c3567116979174a5da05c16/HGVS%2520regular%2520expression), αλλά αυτό δεν πρέπει να σας τρομάζει. Τις περισσότερες φορές (99.99%) ένα regexp με <20 χαρακτήρες θα είναι η λύση στο πρόβλημά σας! 

Επίσης εξαιρετικά καλή πηγή για να μάθετε σωστά regexp: https://github.com/ziishaned/learn-regex

#### Παράδειγμα:

Σαν παράδειγμα ας υποθέσουμε ότι έχουμε μία μετάλλαξη σε [HGVS format](https://varnomen.hgvs.org/bg-material/simple/)  


```python
s = 'NG_007400.1:g.8638G>T'
```

Ας φτιάξουμε μία συνάρτηση χωρίς regular expression για να κάνουμε validate τέτοιου είδους string:


```python
def validate(s):
    if s.count(':') != 1:
        return False
    
    s1,s2 = s.split(':')
    if s1.count('.') != 1:
        return False
    
    s11, s12 = s1.split('.')
    try:
        int(s12)
    except ValueError:
        return False
    
    if s2.count('.') != 1:
        return False
    
    s21, s22 = s2.split('.')
    if s21 not in ['c', 'g']:
        return False

    s221 = s22[:-3]
    s222 = s22[-3:]
    
    try:
        int(s221)
    except ValueError:
        return False
    
    if s222.count('>') != 1:
        return False
    
    s2221, s2222 = s222.split('>')
    
    bases = set('ACGT')
    
    if not s2221 in bases:
        return False
    
    if not s2222 in bases:
        return False
    
    return True
    

```


```python
validate('NG_007400.1:g.8638G>T')  
```




    True




```python
validate('NG_007400.1:g.8638H>T')  
```




    False



H ίδια συνάρτηση με regular expressions:


```python
def validate(s):
    m = re.fullmatch(r'\w+\.\d+:[cg]\.\d+[ACGT]>[ACGT]', s)
    return bool(m)
    
validate('NG_007400.1:g.8638G>T')
```




    True




```python
validate('NG_007400.1:g.8638H>T')
```




    False


