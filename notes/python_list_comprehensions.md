### Οι μέθοδοι ```split``` και ```join```
Αν θέλουμε να "σπάσουμε" ένα string σε μία λίστα από πολλά string τότε μπορούμε να χρησιμοποιήσουμε τη ```split```


```python
"a+b+c".split('+')
```




    ['a', 'b', 'c']




```python
"hello world".split(' ')
```




    ['hello', 'world']




```python
"I like to move it move it".split('move')
```




    ['I like to ', ' it ', ' it']




```python
a = '''
ἄνδρα μοι ἔννεπε, μοῦσα, πολύτροπον, ὃς μάλα πολλὰ
πλάγχθη, ἐπεὶ Τροίης ἱερὸν πτολίεθρον ἔπερσεν·
πολλῶν δ᾽ ἀνθρώπων ἴδεν ἄστεα καὶ νόον ἔγνω,
πολλὰ δ᾽ ὅ γ᾽ ἐν πόντῳ πάθεν ἄλγεα ὃν κατὰ θυμόν,
ἀρνύμενος ἥν τε ψυχὴν καὶ νόστον ἑταίρων.
ἀλλ᾽ οὐδ᾽ ὣς ἑτάρους ἐρρύσατο, ἱέμενός περ·
αὐτῶν γὰρ σφετέρῃσιν ἀτασθαλίῃσιν ὄλοντο,
νήπιοι, οἳ κατὰ βοῦς Ὑπερίονος Ἠελίοιο
ἤσθιον· αὐτὰρ ὁ τοῖσιν ἀφείλετο νόστιμον ἦμαρ.
'''
a.split('\n')
```




    ['',
     'ἄνδρα μοι ἔννεπε, μοῦσα, πολύτροπον, ὃς μάλα πολλὰ',
     'πλάγχθη, ἐπεὶ Τροίης ἱερὸν πτολίεθρον ἔπερσεν·',
     'πολλῶν δ᾽ ἀνθρώπων ἴδεν ἄστεα καὶ νόον ἔγνω,',
     'πολλὰ δ᾽ ὅ γ᾽ ἐν πόντῳ πάθεν ἄλγεα ὃν κατὰ θυμόν,',
     'ἀρνύμενος ἥν τε ψυχὴν καὶ νόστον ἑταίρων.',
     'ἀλλ᾽ οὐδ᾽ ὣς ἑτάρους ἐρρύσατο, ἱέμενός περ·',
     'αὐτῶν γὰρ σφετέρῃσιν ἀτασθαλίῃσιν ὄλοντο,',
     'νήπιοι, οἳ κατὰ βοῦς Ὑπερίονος Ἠελίοιο',
     'ἤσθιον· αὐτὰρ ὁ τοῖσιν ἀφείλετο νόστιμον ἦμαρ.',
     '']



Αν η ```split``` δεν έχει κάποιο όρισμα, τότε αφαιρεί όλα τα κενά (και τα tabs και τα enters) μεταξύ των λέξεων σε ένα string:


```python
"hello                 world".split()
```




    ['hello', 'world']



Η μέθοδος ```join``` κάνει το αντίθετο. Παίρνει μία λίστα από strings και τα εννώνει σε ένα string:


```python
'+'.join(['a','b','c'])
```




    'a+b+c'




```python
' '.join(['hello', 'world'])
```




    'hello world'




```python
print ('\n'.join(['line 1', 'line 2']))
```

    line 1
    line 2


### Οι συναρτήσεις all και any

Η ```all``` επιστρέφει ```True``` αν **όλα** τα στοιχεία μιας λίστας είναι ```True```


```python
all([True, True, True])
```




    True




```python
all([True, False, True])
```




    False




```python
all([3,4,5,4,5])
```




    True




```python
all([3,4,5,'',4,5])
```




    False



H ```any``` μας επιστρέφει ```True``` αν έστω και ένα στοιχείο της λίστας είναι ```True```:


```python
any([False, False, False])
```




    False




```python
any([False, False, False, "mitsos"])
```




    True



**Προσοχή** H άδεια λίστα έχει ```all``` ```True``` και ```any``` ```False```: 


```python
all([])
```




    True




```python
any([])
```




    False




```python

```

### H συνάρτηση range

Η συνάρτηση ```range``` δημιουργεί κάτι* που αναπαραστάει μία αριθμητική ακολουθία.

\* Αυτό το "κάτι" ονομάζεται generator και θα το μάθουμε στην επόμενη διάλεξη


```python
range(1,10) 
```




    range(1, 10)



Το σημαντικό είναι ότι αν του εφαρομόσουμε τη ```list``` τότε μας επιστρέφει μία λίστα:


```python
list(range(10)) # Από το 0 έως το 10 (χωρίς το 10)
```




    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]




```python
list(range(5,10)) # Από το 5 έως το 10 (χωρίς το 10)
```




    [5, 6, 7, 8, 9]




```python
list(range(1,11,2)) # Από το 1 έως το 11 (χωρίς το 11) με βήμα 2
```




    [1, 3, 5, 7, 9]



H αριθμητική πρόοδος μπορεί να είναι και "ανάποδη" 


```python
list(range(11,1,-2))
```




    [11, 9, 7, 5, 3]




```python
list(range(10,1,-1))
```




    [10, 9, 8, 7, 6, 5, 4, 3, 2]



H ```list(range(...))``` επιστρέφει μία λίστα που μπορούμε να κάνουμε πράξεις κανονικά όπως έχουμε μάθει:


```python
a = list(range(100, 120, 5)) + ["mitsos"]
print (a)
```

    [100, 105, 110, 115, 'mitsos']


Γιατί στη python όποτε βλέπουμε το ```"ΧΥΖ"[a:b]```, ```[1,2,3][a:b]```, ```range(a,b)``` αυτό σημαίνει από το ```a``` μέχρι το ```b``` **ΧΩΡΙΣ ΤΟ ```b```**; Αυτή η ιστορία ξεκινάει από [πολύυυυυ παλιά](https://en.wikipedia.org/wiki/Zero-based_numbering). Το βασικό είναι ότι όταν λέμε σε έναν υπολογιστή "θέλω Ν" στοιχεία, τότε με βάση μιας παλιάς σύμβασης, το πρώτο στοιχείο έχει δείκτη (index) 0, το δεύτερο 1, κτλ. Οπότε όταν λέμε ```range(10)``` ο υπολογιστής φτιάχνει τη λίστα από το 0 μέχρι και το 9. Όταν λέμε range(5,7) τότε στην ουσία ζητάμε από τον υπολογιστή μία λίστα με 2 στοιχεία (7-5). Το πρώτο σύμφωνα με την ίδια σύμβαση θα είναι "από εκεί που ξεκινάει η αρίθμηση" δηλαδή το 5. Αφού η λίστα πρέπει να έχει 2 στοιχεία τότε το δεύτερο θα είναι το επόμενο δηλαδή το 6. Αυτή η αρίθμηση μας "βολεύει" και για [κάποιους μαθηματικούς υπολογισμούς](https://www.johndcook.com/blog/2008/06/26/why-computer-scientists-count-from-zero/). Κάποια επιπλέον παραδείγματα:


```python
list(range(3,10,2))
```




    [3, 5, 7, 9]




```python
list(range(3,11,2))
```




    [3, 5, 7, 9]




```python
list(range(3,12,2))
```




    [3, 5, 7, 9, 11]




```python
list(range(10)) # list(range(0,10))
```




    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]




```python
list(range(5,7)) # list(range(a,b)) # b-a
```




    [5, 6]



### Η μέθοδος ```zip```
Με τη ```zip``` μπορούμε να 'ενώσουμε΄ δύο λίστες σε μία λίστα από υπολίστες:


```python
list(zip([1,2,3], ['a', 'b', 'c']))
```




    [(1, 'a'), (2, 'b'), (3, 'c')]



### Η μέθοδος ```enumerate```

H μέθοδος ```enumerate``` παίρνει μία λίστα και δημιουργεί μία άλλη λίστα η οποία περιέχει και τις θέσεις (indexes) και τα στοιχεία της πρώτης λίστας:


```python
a = ["python", "mitsos", "Crete"]
print (list(enumerate(a)))
```

    [(0, 'python'), (1, 'mitsos'), (2, 'Crete')]


Μπορείτε να κάνετε ότι και η ```enumerate``` αν συνδοιάσετε τη ```range``` με τη ```zip```:


```python
a = ["python", "mitsos", "Crete"]
print (list(zip(range(len(a)),a)))
```

    [(0, 'python'), (1, 'mitsos'), (2, 'Crete')]



```python

```

### Η εντολή ```for```
Με τον εντολή ```for``` μπορούμε να επαναλάβουμε εντολές για κάθε στοιχεία μιας λίστας


```python
for x in [1,4,6]: 
    print (x)
```

    1
    4
    6



```python
for x in [1,4,6]: 
    print ("The number is:", x)
```

    The number is: 1
    The number is: 4
    The number is: 6



```python
for x in range(1,10): 
    print ("The number is:", x)
```

    The number is: 1
    The number is: 2
    The number is: 3
    The number is: 4
    The number is: 5
    The number is: 6
    The number is: 7
    The number is: 8
    The number is: 9



```python
for i in range(1,10,3): 
    print ("Hello:", i)
```

    Hello: 1
    Hello: 4
    Hello: 7


Αν οι εντολές που θέλουμε να επαναλάβουμε είναι πάνω από 1 τότε είναι **ΥΠΟΧΡΕΩΤΙΚΟ** να τις βάλουμε στην επόμενη γραμμή και πιο μέσα. Αυτό ονομάζεται υποχρεωτικό [indentation](https://en.wikipedia.org/wiki/Indentation_style) ή αλλιώς [κανόνας off-side](https://en.wikipedia.org/wiki/Off-side_rule)! 


```python
for i in range(1,10,3):
    print ("command A:", i)
    print ("command B:", i)
```

    command A: 1
    command B: 1
    command A: 4
    command B: 4
    command A: 7
    command B: 7


Αν υπάρχει ```for``` μέσα στη ```for``` τότε πρέπει οι επόμενες γραμμές να μπούν ακόμα πιο μέσα:


```python
for i in range(1,5):
    for j in range(1,5):
        print (i,j)
```

    1 1
    1 2
    1 3
    1 4
    2 1
    2 2
    2 3
    2 4
    3 1
    3 2
    3 3
    3 4
    4 1
    4 2
    4 3
    4 4


Παράδειγμα: Ο πίνακας πολλαπλασιασμού:


```python
for i in range(1,11):
    for j in range(1,11):
        print ("{} X {} = {}".format(i,j,i*j))
    print ("=" * 10)
```

    1 X 1 = 1
    1 X 2 = 2
    1 X 3 = 3
    1 X 4 = 4
    1 X 5 = 5
    1 X 6 = 6
    1 X 7 = 7
    1 X 8 = 8
    1 X 9 = 9
    1 X 10 = 10
    ==========
    2 X 1 = 2
    2 X 2 = 4
    2 X 3 = 6
    2 X 4 = 8
    2 X 5 = 10
    2 X 6 = 12
    2 X 7 = 14
    2 X 8 = 16
    2 X 9 = 18
    2 X 10 = 20
    ==========
    3 X 1 = 3
    3 X 2 = 6
    3 X 3 = 9
    3 X 4 = 12
    3 X 5 = 15
    3 X 6 = 18
    3 X 7 = 21
    3 X 8 = 24
    3 X 9 = 27
    3 X 10 = 30
    ==========
    4 X 1 = 4
    4 X 2 = 8
    4 X 3 = 12
    4 X 4 = 16
    4 X 5 = 20
    4 X 6 = 24
    4 X 7 = 28
    4 X 8 = 32
    4 X 9 = 36
    4 X 10 = 40
    ==========
    5 X 1 = 5
    5 X 2 = 10
    5 X 3 = 15
    5 X 4 = 20
    5 X 5 = 25
    5 X 6 = 30
    5 X 7 = 35
    5 X 8 = 40
    5 X 9 = 45
    5 X 10 = 50
    ==========
    6 X 1 = 6
    6 X 2 = 12
    6 X 3 = 18
    6 X 4 = 24
    6 X 5 = 30
    6 X 6 = 36
    6 X 7 = 42
    6 X 8 = 48
    6 X 9 = 54
    6 X 10 = 60
    ==========
    7 X 1 = 7
    7 X 2 = 14
    7 X 3 = 21
    7 X 4 = 28
    7 X 5 = 35
    7 X 6 = 42
    7 X 7 = 49
    7 X 8 = 56
    7 X 9 = 63
    7 X 10 = 70
    ==========
    8 X 1 = 8
    8 X 2 = 16
    8 X 3 = 24
    8 X 4 = 32
    8 X 5 = 40
    8 X 6 = 48
    8 X 7 = 56
    8 X 8 = 64
    8 X 9 = 72
    8 X 10 = 80
    ==========
    9 X 1 = 9
    9 X 2 = 18
    9 X 3 = 27
    9 X 4 = 36
    9 X 5 = 45
    9 X 6 = 54
    9 X 7 = 63
    9 X 8 = 72
    9 X 9 = 81
    9 X 10 = 90
    ==========
    10 X 1 = 10
    10 X 2 = 20
    10 X 3 = 30
    10 X 4 = 40
    10 X 5 = 50
    10 X 6 = 60
    10 X 7 = 70
    10 X 8 = 80
    10 X 9 = 90
    10 X 10 = 100
    ==========


Επίσης μπορούμε να κάνουμε επανάληψη χρησιμοποιώντας string αντί για λίστα:


```python
for letter in "python":
    print (letter)
```

    p
    y
    t
    h
    o
    n


Αν μία λίστα έχει υπο-λίστες με παραπάνω από 1 στοιχεία τότε μπορούμε να χρησιμοποιήσουμε παραπάνω απο 1 μεταβλητές στη ```for```:


```python
a = [[2, "Crete"], [3, "Cyprus"], [4, "Majiorca"]]
for x, y in a:
    print ("Number: {} Island: {}".format(x,y))
```

    Number: 2 Island: Crete
    Number: 3 Island: Cyprus
    Number: 4 Island: Majiorca


Φυσικά το ίδιο μπορεί να γίνει αν έχει υπο-λίστες με 3 στοιχεία κτλ..


```python
a = [[1,2,3], ["a", "b", "c"]]
for x,y,z in a:
    print ("{} {} {}".format(x,y,z))
```

    1 2 3
    a b c


H ```if``` μπορεί να είναι μέσα σε μία ```for```:


```python
for i in range(1,10):
    if i>5:
        print (i)
```

    6
    7
    8
    9



```python
for i in range(1,10):
    if i>=5:
        print (i)
```

### break και continue

Με την εντολή ```break``` "σταματάμε" την επανάληψη της for. Όταν ο υπολογιστής "δει" τη ```break``` τότε βγαίνει τελείως από τη ```for```: 


```python
for i in range(1,10):
    print (i)
    if i>5:
        break # Get out from for !!!
```

    1
    2
    3
    4
    5
    6


Με την εντολή ```continue``` σταματάμε για αυτό και μόνο το κομμάτι της επανάληψης. Ο υπολογιστής "συνεχίζει" (continue..) με την επόμενη επανάληψη:


```python
for i in range(1,10):
    if i == 5: # ΔΕΝ ΤΥΠΩΝΕΙ ΤΟ 5
        continue
    print (i) # TO PRINT **DEN** EINAI MESA STHN IF! (einai mesa sth for)
```

    1
    2
    3
    4
    6
    7
    8
    9


**Προσοχή!** ότι υπάρχει κάτω (και στο ίδιο indentation) από τη ```continue``` και τη ```break``` αγνοείται!


```python
for i in range(1,10):
    if i == 5:
        continue
        print (i) #  TO PRINT EINAI MESA STHN IF!
```


```python

```


```python

```

# List Comprehensions
Τα List Comprehensions είναι ένας μηχανισμός για να δημιουργήσουμε μία λίστα από κάποια άλλη λίστα. Η [επίσημη περιγραφή βρίσκεται εδώ](https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions). Η γενικότερη μορφή είναι:
```python
a = [ΕΚΦΡΑΣΗ for ΜΕΤΑΒΛΗΤΗ in LIST]
```

Το οποίο είναι ισοδύναμο με:
```python
a = []
for ΜΕΤΑΒΛΗΤΗ in LIST:
    a.append(ΕΚΦΡΑΣΗ)
```

Παράδειγμα:


```python
a = [1,2,3]
```


```python
b = [x+1 for x in a]
print (b)
```

    [2, 3, 4]


Το παραπάνω είναι ισοδύναμο με:


```python
a = [1,2,3]
b = []
for x in a:
    b.append(x+1)
print (b)
```

    [2, 3, 4]


Κάποια άλλα παραδείγματα:


```python
a = ["a", "b", "c"]
["hello: " + x for x in a]
```




    ['hello: a', 'hello: b', 'hello: c']




```python
a = ["a", "b", "c"]
b  = [x * 3 for x in a]
print (b)
```

    ['aaa', 'bbb', 'ccc']



```python
a = [1,2,3,4,5,6]
[x/2 for x in a]
```




    [0.5, 1.0, 1.5, 2.0, 2.5, 3.0]



Επίσης μπορούμε να χρησημοποιήσουμε την ```if``` στα list comprehensions. Η γενικότερη μορφή είναι:

```python
a = [ΕΚΦΡΑΣΗ for ΜΕΤΑΒΛΗΤΗ in LIST if ΛΟΓΙΚΗ_ΕΚΦΡΑΣΗ]
```

Το οποίο είναι ισοδύναμε με:
```python
a = []
for ΜΕΤΑΒΛΗΤΗ in LIST:
    if ΛΟΓΙΚΗ_ΕΚΦΡΑΣΗ:
        a.append(ΕΚΦΡΑΣΗ)
```

Παραδείγματα:


```python
a = [1,2,3,4,5,6]
[x/2 for x in a if x>4]
```




    [2.5, 3.0]



Αυτό είναι ισοδύναμο με:


```python
a = [1,2,3,4,5,6]
b = []
for x in a:
    if x>4:
        b.append(x/2)
print (b)
```

    [2.5, 3.0]


Άλλο ένα παράδειγμα. Έστω η λίστα:


```python
a = [1,2,3,4,5,4,3,5,6,7,8,7,6,5,5,4]
```

Ποιές είναι όλες οι θέσεις που έχουν τι τιμή 4;

Πρώτος τρόπος:


```python
[i for i, x in enumerate(a) if x==4]
```




    [3, 5, 15]



Δεύτερος τρόπος:


```python
a = [1,2,3,4,5,4,3,5,6,7,8,7,6,5,5,4]
[x for x in range(len(a)) if a[x] == 4]
```




    [3, 5, 15]




```python
list(range(len(a)))
```




    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]



Επίσης ένα list comprehension μπορεί να έχει παραπάνω από 1 ```for```:


```python
a = [1,2,3]
b = ["a", "b", "c"]
["{}{}".format(x,y) for x in a for y in b]
```




    ['1a', '1b', '1c', '2a', '2b', '2c', '3a', '3b', '3c']



Αυτό είναι ισοδύναμο με:


```python
c = []
for x in a:
    for y in b:
        c.append("{}{}".format(x,y))
print (c)
```

    ['1a', '1b', '1c', '2a', '2b', '2c', '3a', '3b', '3c']


Χρησιμοποιώντας list comprehension μπορούμε να παράξουμε ένα string που περιέχει όλη τη προπαίδεια:


```python
print ('\n'.join(["{} X {} = {}".format(x,y,x*y) for x in range(1,11) for y in range(1,11)]))
```

    1 X 1 = 1
    1 X 2 = 2
    1 X 3 = 3
    1 X 4 = 4
    1 X 5 = 5
    1 X 6 = 6
    1 X 7 = 7
    1 X 8 = 8
    1 X 9 = 9
    1 X 10 = 10
    2 X 1 = 2
    2 X 2 = 4
    2 X 3 = 6
    2 X 4 = 8
    2 X 5 = 10
    2 X 6 = 12
    2 X 7 = 14
    2 X 8 = 16
    2 X 9 = 18
    2 X 10 = 20
    3 X 1 = 3
    3 X 2 = 6
    3 X 3 = 9
    3 X 4 = 12
    3 X 5 = 15
    3 X 6 = 18
    3 X 7 = 21
    3 X 8 = 24
    3 X 9 = 27
    3 X 10 = 30
    4 X 1 = 4
    4 X 2 = 8
    4 X 3 = 12
    4 X 4 = 16
    4 X 5 = 20
    4 X 6 = 24
    4 X 7 = 28
    4 X 8 = 32
    4 X 9 = 36
    4 X 10 = 40
    5 X 1 = 5
    5 X 2 = 10
    5 X 3 = 15
    5 X 4 = 20
    5 X 5 = 25
    5 X 6 = 30
    5 X 7 = 35
    5 X 8 = 40
    5 X 9 = 45
    5 X 10 = 50
    6 X 1 = 6
    6 X 2 = 12
    6 X 3 = 18
    6 X 4 = 24
    6 X 5 = 30
    6 X 6 = 36
    6 X 7 = 42
    6 X 8 = 48
    6 X 9 = 54
    6 X 10 = 60
    7 X 1 = 7
    7 X 2 = 14
    7 X 3 = 21
    7 X 4 = 28
    7 X 5 = 35
    7 X 6 = 42
    7 X 7 = 49
    7 X 8 = 56
    7 X 9 = 63
    7 X 10 = 70
    8 X 1 = 8
    8 X 2 = 16
    8 X 3 = 24
    8 X 4 = 32
    8 X 5 = 40
    8 X 6 = 48
    8 X 7 = 56
    8 X 8 = 64
    8 X 9 = 72
    8 X 10 = 80
    9 X 1 = 9
    9 X 2 = 18
    9 X 3 = 27
    9 X 4 = 36
    9 X 5 = 45
    9 X 6 = 54
    9 X 7 = 63
    9 X 8 = 72
    9 X 9 = 81
    9 X 10 = 90
    10 X 1 = 10
    10 X 2 = 20
    10 X 3 = 30
    10 X 4 = 40
    10 X 5 = 50
    10 X 6 = 60
    10 X 7 = 70
    10 X 8 = 80
    10 X 9 = 90
    10 X 10 = 100


# Μερικά παραδείγματα χρήσης των παραπάνω

## 1. Από μία λίστα πάρε μόνο αυτά που έχουν μία ιδιότητα
π.χ. Από μία λίστα πάρε μόνο τους μονούς αριθμούς 


```python
a = [1,2,3,4,5,6,7,8,9,10]
def f(x):
    return x%2==1

```


```python
# 1ος τρόπος
b = list(filter(f,a))
print (b)
```

    [1, 3, 5, 7, 9]



```python
# 2ος τρόπος
b = []
for x in a:
    if f(x):
        b.append(x)
print (b)
```

    [1, 3, 5, 7, 9]



```python
# 3ος τρόπος
b = []
for x in a:
    if not f(x):
        continue
        
    b.append(x)
print (b)
```

    [1, 3, 5, 7, 9]



```python
# 4ος τρόπος
b = [x for x in a if f(x)]
print (b)
```

    [1, 3, 5, 7, 9]


## 2. Από μία λίστα μέτρα αυτά που έχουν μία ιδιότητα
Πόσοι είναι οι μονοί αριθμοί;


```python
# 1ος τρόπος
c = len(list(filter(f,a)))
print(c)
```

    5



```python
# 2ος τρόπος
c = sum(map(f,a))
print (c)
```

    5



```python
# 3ος τρόπος
c = 0
for x in a:
    if f(x):
        c += 1
print (c)
```

    5



```python
# 4ος τρόπος
c = 0
for x in a:
    if not f(x):
        continue
    c += 1
print (c)
```

    5



```python
# 5ος τρόπος
c = len([None for x in a if f(x)])
print (c)
```

    5



```python
# 6ος τρόπος
c = sum(f(x) for x in a)
print (c)
```

    5


## 3. Εφάρμοσε μία συνάρτηση σε όλα τα στοιχεία μίας λίστας
π.χ δεκαπλασίασε όλα τα στοιχεια


```python
a = [1,2,3,4,5,6,7,8,9,10]
def f(x):
    return x*10
```


```python
# 1ος τρόπος
b = list(map(f,a))
print (b)
```

    [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]



```python
# 2ος τρόπος
b = []
for x in a:
    b.append(f(x))
print (b)
```

    [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]



```python
# 3ος τρόπος
b = [f(x) for x in a]
print (b)
```

    [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]


## 4. Ένας συνδυασμός όλων των παραπάνω
Βρες το άθροισμα του γινόμενου επί 10 των μονών αριθμών μίας λίστας.


```python
a = [1,2,3,4,5,6,7,8,9,10]
def f(x):
    return x%2==1
def g(x):
    return x*10
```


```python
# 1ος τρόπος
c = sum(map(g, filter(f, a)))
print (c)
```

    250



```python
# 2ος τρόπος
c = 0
for x in a:
    if f(x):
        c += g(x)
print (c)
```

    250



```python
# 3ος τρόπος
c = 0
for x in a:
    if not f(x):
        continue
    c += g(x)
print (c)
```

    250



```python
# 4ος τρόπος
c = sum(g(x) for x in a if f(x))
print (c)
```

    250


## 5. Συνδοιάζοντας πάνω από μία λίστες

Έχουμε δύο λίστες με το ίδιο μέγεθος α,β. Σε κάθε θέση των ληστών έχουμε από μία μετρήση. Η κάθε μέτρηση έχει 2 "τιμές". Για παράδειγμα:

Οι πόλεις:


```python
cities = ['Heraklion', 'Athens', 'Thessaloniki']
```

και οι **αντίστοιχοι** πληθυσμοί τους: 


```python
pop = [200_000, 4_000_000, 500_000]
```

Βρες τις πόλεις που έχουν πληθυσμό κάτω από 1.000.000:


```python
# 1ος τρόπος
solution = []
for city, p in zip(cities, pop):
    if p < 1_000_000:
        solution.append(city)
print (solution)
```

    ['Heraklion', 'Thessaloniki']



```python
# 2ος τρόπος
solution = []
for i, p in enumerate(pop):
    if p < 1_000_000:
        solution.append(cities[i])
print (solution)
```

    ['Heraklion', 'Thessaloniki']



```python
# 3ος τρόπος
solution = [city for city, p in zip(cities, pop) if p<1_000_000]
print (solution)
```

    ['Heraklion', 'Thessaloniki']



```python
# 4ος τρόπος
solution = [cities[i] for i,p in enumerate(pop) if p<1_000_000]
print (solution)
```

    ['Heraklion', 'Thessaloniki']



```python
# 5ος τρόπος (πολύ άσχημος!)
def f(x):
    return x[1]<1_000_000

def g(x):
    return x[0]

def h(x):
    return cities[x]

solution = list(map(h, map(g, filter(f, enumerate(pop)))))
print (solution)
```

    ['Heraklion', 'Thessaloniki']


## 6. Κάνε μία λίστα με λίστες, μία επίπεδη (flat) λίστα
Έστω η λίστα:


```python
a = [ [1,2], ["a", "b"], [True, False] ]
```

Φτιάξε μία λίστα που θα έχει όλα τα στοιχεία της a σε ένα επίπεδο (χωρίς υπολίστες)


```python
# 1ος τρόπος
b = []
for x in a:
    b.extend(x)
print (b)
```

    [1, 2, 'a', 'b', True, False]



```python
# 2ος τρόπος
b = []
for x in a:
    for y in x:
        b.append(y)
print (b)
```

    [1, 2, 'a', 'b', True, False]



```python
# 2ος τρόπος (hot!)
b = [y for x in a for y in x]
print (b)
```

    [1, 2, 'a', 'b', True, False]


## 7. Ξεζιπάρισμα!
Έστω η λίστα:


```python
a = [ [1, "a"], [2, "b"], [3, "c"]]
```

Φτιάξτε δύο λίστες k,l οι ποίες θα έχουν τα πρώτα και δεύτερα στοιχεία των υποληστών της a αντίστοιχα!


```python
# 1ος τρόπος
k = []
l = []
for x in a:
    k.append(x[0])
    l.append(x[1])
print (k)
print (l)
```

    [1, 2, 3]
    ['a', 'b', 'c']



```python
# 2ος τρόπος:
k = []
l = []
for x,y in a:
    k.append(x)
    l.append(y)
print (k)
print (l)
```

    [1, 2, 3]
    ['a', 'b', 'c']



```python
# 3ος τρόπος
k = [x[0] for x in a]
l = [x[1] for x in a]
print (k)
print (l)
```

    [1, 2, 3]
    ['a', 'b', 'c']


## 8. Έλεγχος αν υπάρχει ένα στοιχείο σε μία λίστα. 
υπάρχει το 3 στη λίστα ```a = [1,2,3,4,5,6,7,8,9,10]``` ;



```python
a = [1,2,3,4,5,6,7,8,9,10]

```


```python
# 1ος τρόπος
b = 3 in a
print (b)
```

    True



```python
# 2ος τρόπος
b = False
for x in a:
    if x==3:
        b = True
        break
print (b)
```

    True



```python
# 3ος τρόπος
b = True
for x in a:
    if x==3:
        break
else:
    b = False
print (b)
```

    True



```python

```
