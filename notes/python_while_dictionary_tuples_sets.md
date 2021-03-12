### Η εντολή ```while```
Η εντολή ```while``` χρησιμοποιείται για επανάληψη. Με την εντολή ```while <ΛΟΓΙΚΗ ΣΥΝΘΗΚΗ>:``` δηλώνουμε ότι όλες οι εντολές "κάτω" από τη while θα τρέχουν μέχρι η ```<ΛΟΓΙΚΗ ΣΥΝΘΗΚΗ>``` να γίνει ```False```. 


```python
# Τύπωσε όλους τους αριθμούς από το 0 μέχρι και το 9
a=0
while a<10:
    print (a)
    a += 1
```

    0
    1
    2
    3
    4
    5
    6
    7
    8
    9


Τύπωσε όλους τους **μονούς** αριθμούς από το 1 μέχρι το 50


```python
a=1

while a<50:
    if a%2 == 1:
        print (a)
    a+=1
```

    1
    3
    5
    7
    9
    11
    13
    15
    17
    19
    21
    23
    25
    27
    29
    31
    33
    35
    37
    39
    41
    43
    45
    47
    49


Τύπωσε τη "προπαίδεια" του 8


```python
a = 1
while a<=10:
    print (a*8)
    a+=1

```

    8
    16
    24
    32
    40
    48
    56
    64
    72
    80


Λίγο καλύτερα:


```python
a = 1
while a<=10:
    print (a, 'fores to 8 mas kanei', a*8)
    a+=1
```

    1 fores to 8 mas kanei 8
    2 fores to 8 mas kanei 16
    3 fores to 8 mas kanei 24
    4 fores to 8 mas kanei 32
    5 fores to 8 mas kanei 40
    6 fores to 8 mas kanei 48
    7 fores to 8 mas kanei 56
    8 fores to 8 mas kanei 64
    9 fores to 8 mas kanei 72
    10 fores to 8 mas kanei 80


Τύπωσε τη προπαίδεια όλων των αριθμών από το 1 μέχρι το 10


```python
a = 1
while a<=10:
    b=1
    while b<=10:
        print (a, 'fores to ', b, ' mas kanei', a*b)
        b+=1
    a+=1
```

    1 fores to  1  mas kanei 1
    1 fores to  2  mas kanei 2
    1 fores to  3  mas kanei 3
    1 fores to  4  mas kanei 4
    1 fores to  5  mas kanei 5
    1 fores to  6  mas kanei 6
    1 fores to  7  mas kanei 7
    1 fores to  8  mas kanei 8
    1 fores to  9  mas kanei 9
    1 fores to  10  mas kanei 10
    2 fores to  1  mas kanei 2
    2 fores to  2  mas kanei 4
    2 fores to  3  mas kanei 6
    2 fores to  4  mas kanei 8
    2 fores to  5  mas kanei 10
    2 fores to  6  mas kanei 12
    2 fores to  7  mas kanei 14
    2 fores to  8  mas kanei 16
    2 fores to  9  mas kanei 18
    2 fores to  10  mas kanei 20
    3 fores to  1  mas kanei 3
    3 fores to  2  mas kanei 6
    3 fores to  3  mas kanei 9
    3 fores to  4  mas kanei 12
    3 fores to  5  mas kanei 15
    3 fores to  6  mas kanei 18
    3 fores to  7  mas kanei 21
    3 fores to  8  mas kanei 24
    3 fores to  9  mas kanei 27
    3 fores to  10  mas kanei 30
    4 fores to  1  mas kanei 4
    4 fores to  2  mas kanei 8
    4 fores to  3  mas kanei 12
    4 fores to  4  mas kanei 16
    4 fores to  5  mas kanei 20
    4 fores to  6  mas kanei 24
    4 fores to  7  mas kanei 28
    4 fores to  8  mas kanei 32
    4 fores to  9  mas kanei 36
    4 fores to  10  mas kanei 40
    5 fores to  1  mas kanei 5
    5 fores to  2  mas kanei 10
    5 fores to  3  mas kanei 15
    5 fores to  4  mas kanei 20
    5 fores to  5  mas kanei 25
    5 fores to  6  mas kanei 30
    5 fores to  7  mas kanei 35
    5 fores to  8  mas kanei 40
    5 fores to  9  mas kanei 45
    5 fores to  10  mas kanei 50
    6 fores to  1  mas kanei 6
    6 fores to  2  mas kanei 12
    6 fores to  3  mas kanei 18
    6 fores to  4  mas kanei 24
    6 fores to  5  mas kanei 30
    6 fores to  6  mas kanei 36
    6 fores to  7  mas kanei 42
    6 fores to  8  mas kanei 48
    6 fores to  9  mas kanei 54
    6 fores to  10  mas kanei 60
    7 fores to  1  mas kanei 7
    7 fores to  2  mas kanei 14
    7 fores to  3  mas kanei 21
    7 fores to  4  mas kanei 28
    7 fores to  5  mas kanei 35
    7 fores to  6  mas kanei 42
    7 fores to  7  mas kanei 49
    7 fores to  8  mas kanei 56
    7 fores to  9  mas kanei 63
    7 fores to  10  mas kanei 70
    8 fores to  1  mas kanei 8
    8 fores to  2  mas kanei 16
    8 fores to  3  mas kanei 24
    8 fores to  4  mas kanei 32
    8 fores to  5  mas kanei 40
    8 fores to  6  mas kanei 48
    8 fores to  7  mas kanei 56
    8 fores to  8  mas kanei 64
    8 fores to  9  mas kanei 72
    8 fores to  10  mas kanei 80
    9 fores to  1  mas kanei 9
    9 fores to  2  mas kanei 18
    9 fores to  3  mas kanei 27
    9 fores to  4  mas kanei 36
    9 fores to  5  mas kanei 45
    9 fores to  6  mas kanei 54
    9 fores to  7  mas kanei 63
    9 fores to  8  mas kanei 72
    9 fores to  9  mas kanei 81
    9 fores to  10  mas kanei 90
    10 fores to  1  mas kanei 10
    10 fores to  2  mas kanei 20
    10 fores to  3  mas kanei 30
    10 fores to  4  mas kanei 40
    10 fores to  5  mas kanei 50
    10 fores to  6  mas kanei 60
    10 fores to  7  mas kanei 70
    10 fores to  8  mas kanei 80
    10 fores to  9  mas kanei 90
    10 fores to  10  mas kanei 100


Βρες πόσα ψηφία έχει ένας αριθμός:


```python
a=51234123
# Πρώτος τρόπος (fast and better)
len(str(a))
```




    8




```python
# Δεύτερος τρόπος
# Παρατηρούμε ότι όταν δαιρούμε (ακέραια διαίρεση) έναν αριθμό με το 10, τότε του αφαιρούμε ένα ψηφίο από το τέλος:
# 51234123 // 10 --> 5123412

a=51234123
c=0
upoloipo = a
while upoloipo != 0:
    upoloipo = upoloipo // 10
    c += 1
print (c)
```

    8


Πόσες φορές υπάρχει το γράμμα a σε ένα string;


```python
# Πρώτος τροπος (better / faster)
a = 'zabarakatranemia'
a.count('a')
```




    6




```python
# Δεύτερος τρόπος
index = 0
c = 0
while index < len(a):
    if a[index] == 'a':
        c += 1
    index += 1
print (c)
```

    6


Αντιστροφή ενός string.


```python
# Πρώτος τρόπος (better / faster)
a = 'zabarakatranemia'
a[::-1]
```




    'aimenartakarabaz'




```python
# Δεύτερος τρόπος
index = len(a)-1
anapodo = ''
while index >= 0:
    anapodo = anapodo + a[index]
    index -= 1
print (anapodo)
```

    aimenartakarabaz


To άθροισμα όλων των αριθμών από το 1 μέχρι 20 



```python
s = 0
c = 0
while c < 20:
    c += 1
    s += c
print (s)
```

    210



```python
s = 0
c = 1
while c <= 20:
    s += c
    c += 1
print (s)
```

    210



```python
sum(range(1,21))
```




    210



Όπως και με τη for μπορούμε να κάνουμε break και continue. Με τη break βγαίνουμε τελείως από τη while και με τη continue μεταβαίνουμε στην αρχή της while όπου γίνεται η εκτίμηση της λογικής συνθήκης. 


```python
a=0
while a<10:
    a += 1
    if a== 5:
        continue
        
    print (a)
```

    1
    2
    3
    4
    6
    7
    8
    9
    10


Προσέξτε ότι το 5 δεν υπάρχει.


```python
a=0
while a<10:
    a += 1
    if a== 5:
        break
        
    print (a)
```

    1
    2
    3
    4


Και εδώ όταν το a γίνει 5 τότε βγαίνει τελείως από τη while. 

Κάτι που χρησιμοποιείται σπάνια αλλά είναι ιδιαίτερα χρήσιμο είναι η else μετά τη while. Σε αυτή την else μπαίνει μόνο αν αν έχει συμβεί break μέσα στη while.


```python
a=0
while a<10:
    a += 1
    if a== 5:
        break
        
    print (a)
else:
    print ('No break happened')
```

    1
    2
    3
    4



```python
a=0
while a<10:
    a += 1
    #if a== 5:
    #    break
        
    print (a)
else:
    print ('No break happened')
```

    1
    2
    3
    4
    5
    6
    7
    8
    9
    10
    No break happened


Τη while τη χρησιμοποιούμε πολλές φορές όταν θέλουμε να κάνουμε μία επανάληψη αλλά δεν ξέρουμε πόσες φορές πρέπει να γίνει αυτή η επανάληψη. Για παράδειγμα: αφήνουμε να πέσει μία μπάλα από το 1 μέτρο. Κάθε φορά που αναπηδάει φτάνει στο 90% του ύψους της. Μετά από 5 αναπηδήσεις σε τι ύψος θα έχει φτάσει. Εδώ ξέρουμε πόσες επαναλήψεις θα κάνουμε οπότε θα χρησιμοποιήσουμε for:


```python
height=1
for i in range(5):
    height -= 0.1*height
print (height)
```

    0.5904900000000001


Ας δούμε τώρα ένα άλλο πρόβλημα: Πόσες αναπηδήσεις πρέπει να γίνουν ώστε το ύψος της μπάλας να γίνει μικρότερο από 0.5 μέτρα; Τώρα δεν ξέρουμε το πλήθος από επαναλήψεις (για την ακρίβεια αυτό είναι και το ζητούμενο), άρα "βολεύει" h while:


```python
height = 1
bounces = 0
while height > 0.5:
    bounces += 1
    height -= 0.1*height
print (bounces)
```

    7


Ένα άλλο παράδειγμα: Η παρακάτω συνάρτηση ελέγχει αν ένας αριθμός είναι πρώτος ή όχι:


```python
def is_prime(n):
    for x in range(2, int(n**0.5)+1):
        if n%x==0:
            return False
    
    return True
```

Αν αρχίζουμε και αθροίζουμε όλους τους πρώτους ξεκινώντας από το 1 σε ποιον πρώτο αριθμό αυτό το άθροισμα θα ξεπεράσει το 1.000.000 ;


```python
s = 0
c = 1
while s < 1_000_000:
    if is_prime(c):
        s += c
    c += 1
print (c-1)
```

    3943



```python

```

### Tuples
Τα tuples είναι δομές δεδομένων που μοιάζουν με τη λίστα. Η διαφορά τους είναι ότι στα tuples δεν μπορούμε να αλλάξουμε μία τιμή. Αντί για αγκύλες (```[1,2,3]```) στα tuples χρησημοποιούμε παρενθέσεις (```(1,2,3)```).


```python
a = (1,2,3)
type(a)
```




    tuple




```python
a[2] = 7 #Πετάει μήνυμα λάθους. Δεν μπορούμε να το αλλάξουμε 
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-85-42aa7089a9ac> in <module>
    ----> 1 a[2] = 7 #Πετάει μήνυμα λάθους. Δεν μπορούμε να το αλλάξουμε
    

    TypeError: 'tuple' object does not support item assignment



```python
b = [1,2,3]
b[2] = 7 # Αυτό είναι οκ, δεν πετάει μήνυμα λάθους
```

Παρόλο που στα tuples δεν μπορώ να προσθέσω ή να αφαιρέσω ένα στοιχείο μπορώ να βάλω στοιχεία στις λίστες ή στα dictionaries που περιέχουν:


```python
a = (1,[4,5],10)
a[1].append(6)
print (a)
```

    (1, [4, 5, 6], 10)


Επίσης μπορούμε να χρησιμοποιήσουμε τα tuples όπως ακριβώς τις λίστες για να κάνουμε επανάληψη, min, max, sort, ...


```python
for x in (1,2,3):
    print (x)
```

    1
    2
    3



```python
sum((5,6,7))
```




    18



### Συναρτήσεις που επιστρέφουν παραπάνω από 1 τιμή
Στη python μία συνάρτηση μπορεί να επιστρέψει παραπάνω από μία τιμή:


```python
def f():
    return 1,2
```


```python
a,b = f()
print (a)
print (b)
```

    1
    2


Αν αποθηκεύσουμε σε μία μόνο μεταβλητή το αποτέλεσμα μίας συνάρτησης η οποία επιστρέφει παραπάνω από μία τιμές τότε αυτό που επιστρέφει είναι ένα tuple.


```python
a = f()
```


```python
print (a)
```

    (1, 2)



```python
type(a)
```




    tuple




```python

```


```python

```

### Dictionaries
Μέχρι στιγμής έχουμε μάθει τους παρακάτω τύπους μεταβλητών:


```python
a=0 # ακέραιοι
a=True # λογικοί
a="324234" # αλφαρηθμιτικά
a=5.6 # δεκαδικοί
a=[2,4,4] # λίστες
a=None # None
```

Τα dictionaries είναι ένα νέος τύπος μεταβλητής. Τα dictionaries έχουν δεδομένα με τη μορφή κλειδί --> τιμή. Κάθε κλειδί (key) είναι μοναδικό. Για παράδειγμα:


```python
a = {"mitsos": 50, "anna": 40}
```


```python
print(a)
```

    {'mitsos': 50, 'anna': 40}



```python
a['mitsos']
```




    50




```python
a['anna']
```




    40



Η ```keys``` επιστρέφει μία λίστα με όλα τα κλειδιά του dictionary


```python
a.keys()
```




    dict_keys(['mitsos', 'anna'])



Η ```values``` επιστρέφει μία λίστα με όλες τις τιμές του dictionary


```python
a.values()
```




    dict_values([50, 40])



Μπορούμε να προσθέσουμε ένα νέο ζευγάρι κλειδί,τιμή με τον εξής τρόπο:


```python
a["kitsos"] = 100
```


```python
print (a)
```

    {'mitsos': 50, 'anna': 40, 'kitsos': 100}


Επίσης μπορούμε να αφαιρέσουμε ένα ζευγάρι κλειδί,τιμή με την εντολή del:


```python
del a['kitsos']
print (a)
```

    {'mitsos': 50, 'anna': 40}


Το κλειδί μπορεί να είναι αριθμός, string και boolean και tuple. Ενώ το value μπορεί να είναι οτιδίποτε.


```python
a[123] = 0.1
a[3.14] = "hello"
a[False] = [1,2,3]
a[(4,7)] = 4
```


```python
print (a)
```

    {'mitsos': 50, 'anna': 40, 'kitsos': 100, 123: 0.1, 3.14: 'hello', False: [1, 2, 3], (4, 7): 4}



```python
# Προσοχή! False == 0 !
a[0]
```




    [1, 2, 3]



Το κλειδί ΔΕΝ μπορεί να είναι λίστα:


```python
a[[1,2,3]] = 0
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-141-6cebb9942dfe> in <module>
    ----> 1 a[[1,2,3]] = 0
    

    TypeError: unhashable type: 'list'


Το κλειδί ΔΕΝ μπορεί να είναι ούτε dictionary:


```python
a[{}] = 0
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-142-b372ccb1b9be> in <module>
    ----> 1 a[{}] = 0
    

    TypeError: unhashable type: 'dict'


Στη python μπορούμε να έχουμε dictionaries μέσα σε lists και lists μέσα σε dictionaries χωρίς κανένα περιορισμό


```python
d = {"a": {2:"a"}, 3: ["hello", False, []], 3.1: True}
print (d)
```

    {'a': {2: 'a'}, 3: ['hello', False, []], 3.1: True}


Μπορούμε να συνθέσουμε listes και dictionaries από άλλες listes και dictionaries:


```python
[d, d, d["a"]]
```




    [{'a': {2: 'a'}, 3: ['hello', False, []], 3.1: True},
     {'a': {2: 'a'}, 3: ['hello', False, []], 3.1: True},
     {2: 'a'}]




```python
{"a": d, "b": d[3]}
```




    {'a': {'a': {2: 'a'}, 3: ['hello', False, []], 3.1: True},
     'b': ['hello', False, []]}



Υπάρχει και το άδειο dictionary


```python
a = {}
```

Η ```len``` επιστρέφει το πλήθος των εγγραφών που έχει ένα dictionary:


```python
person = {"name": "alex", "age": 50, "occupation": "master"}
```


```python
len(person)
```




    3




```python
len({})
```




    0



Μπορούμε να ελέγξουμε αν ένα κλειδί υπάρχει σε ένα dictionary


```python
"name" in person
```




    True




```python
"alex" in person
```




    False



Μπορούμε να ελέγξουμε αν μία τιμή υπάρχει σε dictionary:


```python
"alex" in person.values()
```




    True



Μπορούμε να κάνουμε επανάληψη σε όλα τα στοιχεία ενός dictionary:


```python
for i in person:
    print (i)
```

    name
    age
    occupation



```python
for i in person:
    print ("key: {}  Value: {}".format(i, person[i]))
```

    key: name  Value: alex
    key: age  Value: 50
    key: occupation  Value: master


Μπορούμε να μετατρέψουμε μία λίστα (ή tuple) σε dictionary με τη συνάρτηση dict. Πρέπει όμως η λίστα να αποτελέιται από υπολίστες, όπου η κάθε υπολίστα έχει 2 στοιχεία. Σε αυτές τις υπολίστες το πρώτο στοιχείο θα γίνει το κλειδί και το δεύτερο η τιμή:


```python
a = [("mitsos", 1), ('maria', 2), ('elenh', 4) ]
dict(a)
```




    {'mitsos': 1, 'maria': 2, 'elenh': 4}



Μπορεί να γίνει και το αντίθετο με τη items() 


```python
a = {'mitsos': 1, 'maria': 2, 'elenh': 4}
print(list(a.items()))
```

    [('mitsos', 1), ('maria', 2), ('elenh', 4)]


### Προσπέλαση στοιχείων σε dictionary
Μπορούμε να χρησιμοποιήσουμε πάνω από μια φορά το ```[][]``` ώστε να προσπελάσουμε κάποιο στοιχείο:


```python
person = {"name": "alex", "age": 50, "occupation": "master", "exper": ["python", "karate"]}
```


```python
print (person)
```

    {'name': 'alex', 'age': 50, 'occupation': 'master', 'exper': ['python', 'karate']}



```python
print (person['exper'][0])
```

    python



```python
print (person['exper'][1])
```

    karate



```python
print (person['exper'])
```

    ['python', 'karate']



```python
a = ["a", "b", {"name": "mitsos", "surnmae": "sdfsdfsdf"}]
```


```python
a[0]
```




    'a'




```python
a[1]
```




    'b'




```python
a[2]
```




    {'name': 'mitsos', 'surnmae': 'sdfsdfsdf'}




```python
a[2]['name']
```




    'mitsos'



Η συνάρτηση ```a.get(b,c)``` ελέγχει αν το b υπάρχει στο dictionary a. Αν υπάρχει επιστρέφει τη τιμή: ```a[b]```. Αν δεν υπάρχει επιστρέφει το c:


```python
a = {"a": 1, "b": 2, "c": 3}
```


```python
a.get("mitsos", 50)
```




    50




```python
a.get("a", 50)
```




    1



### Iteration σε ένα dictionary
Έστω ένα list και ένα dictionary:


```python
a = [1,2,3]
b = {"a":1, "b":2, "c":3}
```

Μπορούμε να κάνουμε iterate (επανάληψη) σε ένα list ως εξής:


```python
for x in a:
    print (x)
```

    1
    2
    3


Το ίδιο μπορούμε να κάνουμε και σε ένα dictionary:


```python
for x in b:
    print (x, b[x])
```

    a 1
    b 2
    c 3


Μπορούμε όμως να πάρουμε τα ζευγάρια κλειδιά-τιμές του dictionary ως μία λίστα χρησιμοποιώντας την ```items()```


```python
list(b.items())
```




    [('a', 1), ('b', 2), ('c', 3)]



Άρα όπως έχουμε δει και από πριν μπορούμε να κάνουμε iterate και να αναθέσουμε σε δύο μεταβλητές το κλειδί-τιμή κάθε μέλους του dictionary:


```python
for x,y in b.items():
    print (x,y)
```

    a 1
    b 2
    c 3


### Παραδείγματα με dictionary

Μετράμε πόσες φορές υπάρχει το κάθε στοιχείο μίας λίστας:


```python
a = [3,2,3,2,4,5,4,3,6,5,7,9,1,2,8,9,9]
d = {}

for x in a:
    if not x in d:
        d[x] = 0
    d[x] += 1

print (d)
```

    {3: 3, 2: 3, 4: 2, 5: 2, 6: 1, 7: 1, 9: 3, 1: 1, 8: 1}


Βρες το value που έχει το μεγαλύτερο κey:


```python
a = {1:3, 5:2, 3:1} # Το μεγαλύτερο key είναι το 5 και το value του 5 είναι 2

max_key = max(a.keys())
print(a[max_key])
```

    2


Βρες το key που έχει το μεγαλύτερο value


```python
a = {1:3, 5:2, 3:1} # Το μεγαλύτερο value είναι το 3 που έχει το κey 1
max( (v,k)  for k,v in a.items())[1]
```




    1



Πως βγήκε αυτό; Ας το "σπάσουμε" σε βήματα:


```python
b = list(a.items()) # Μετατρέπουμε σε λίστα
print (b)

c = [(v,k) for k,v in b] # Αντιμεταθέτουμε τα ζευγαράκια κλεδί/τιμή
print(c)

d = max(c) # Παίρνουμε το tuple το οποίο έχει το μεγαλύτερο value
print(d)

e = d[1] # Παίρνουμε το δευτερο στοιχείο το οποίο είναι το κλειδί.
print (e)
```

    [(1, 3), (5, 2), (3, 1)]
    [(3, 1), (2, 5), (1, 3)]
    (3, 1)
    1


### Dictionary Comprehension
Σε προηγούμενη διάλεξη είχαμε πει τα list comprehensions


```python
# List comprehension
[x for x in [1,2,3,4] if x>2]
```




    [3, 4]



Είχαμε πει ότι το παραπάνω είναι ισοδύναμο με:


```python
a = []
for x in [1,2,3,4]:
    if x>2:
        a.append(x)
print (a)
```

    [3, 4]


Το ίδιο μπορύμε να κάνουμε και με τα dictionaries:


```python
{ x:x*10 for x in range(1,10)}
```




    {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60, 7: 70, 8: 80, 9: 90}



Αυτό είναι ισοδύναμο με:


```python
a={}
for x in range(1,10):
    a[x] = x*10
print (a)
```

    {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60, 7: 70, 8: 80, 9: 90}


Ένα άλλο παράδειγμα:


```python
{ x:'hello {}'.format(x*10) for x in range(1,10)}
```




    {1: 'hello 10',
     2: 'hello 20',
     3: 'hello 30',
     4: 'hello 40',
     5: 'hello 50',
     6: 'hello 60',
     7: 'hello 70',
     8: 'hello 80',
     9: 'hello 90'}



### Σύνολα 
H ```set``` είναι μία δομή δεδομένων που μοντελοποιεί ένα σύνολο. Κάθε στοιχείο σε ένα set μπορεί να υπάρχει **μόνο μία φορά**:


```python
set([1,2,3])
```




    {1, 2, 3}




```python
set([1,2,3,2])
```




    {1, 2, 3}




```python
a = set(['a','b', 'a'])
a
```




    {'a', 'b'}




```python
'b' in a
```




    True




```python
set("Hello World!")
```




    {' ', '!', 'H', 'W', 'd', 'e', 'l', 'o', 'r'}



Η πράξη ```&``` μεταξύ δύο set μας επιστρέφει την τομή των συνόλων:


```python
a = set([1,2,3,4])
b = set([3,4,5,6])
a & b
```




    {3, 4}



Το ίδιο μπορεί να γίνει και με τη συνάρτηση intersection:


```python
a.intersection(b)
```




    {3, 4}



Η πράξη ```|``` μεταξύ δύο set μας επιστρέφει την ένωση των συνόλων:


```python
a | b
```




    {1, 2, 3, 4, 5, 6}



Το ίδιο μπορεί να γίνει με τη συνάρτηση union:


```python
a.union(b)
```




    {1, 2, 3, 4, 5, 6}



Η πράξη ```-``` μεταξύ δύο σετ ```α``` και ```β``` μας επιστρέφει τα στοιχεία της ```α``` που δεν υπάρχουν στην ```β```:


```python
a - b
```




    {1, 2}




```python
b - a
```




    {5, 6}




```python
(a - b) & (b-a)
```




    set()



Μπορούμε να προσθέσουμε ένα στοιχείο σε ένα set με τη συνάρτηση add:


```python
a = {1,2,3}
a.add(10)
print (a)
```

    {10, 1, 2, 3}


Ένας άλλλος τρόπος να προσθέσουμε ένα στοιχείο είναι να χρησιμοποιήσουμε τον τελεστή | :


```python
a = {1,2,3}
a = a | {10}
print (a)
```

    {10, 1, 2, 3}


Δεν μπορούμε να προσθέσουμε μία λίστα σε ένα set. Αυτό γίνεται γιατί μπορούμε να προσθέσουμε μόνο στοιχεία που ΔΕΝ αλλάζουν:


```python
a.add([7,8,9])
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-79-1706898a2cfb> in <module>
    ----> 1 a.add([7,8,9])
    

    TypeError: unhashable type: 'list'


Τα sets είναι ένας επιπλέον τύπος δεδομένων:


```python
type(set([1,2,3]))
```




    set




```python
a = set([1,2,3])
type(a) is set
```




    True



### set comprehension
Όπως ακριβώς με τις λίστες και τα dictionaries, μπορούμε να έχουμε comprehensions και με τα sets:


```python
{x%4 for x in range(10)}
```




    {0, 1, 2, 3}




```python

```
