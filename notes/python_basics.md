
# Προγραμματισμός με τη γλώσσα python
### [Alexandros Kanterakis](mailto:kantale@ics.forth.gr) kantale@ics.forth.gr

### Αντί εισαγωγής
Όλες οι διαλέξεις θα διατίθονται σε μορφή [jupyter notebooks](http://jupyter.org/). Το Jupyter είναι ένα περιβάλλον που σου επιτρέπει να γράφεις python και να βλέπεις άμεσα τα αποτελέσματα των εντολών στον browser του υπολογιστή σου. Μπορείτε να σώσετε την ανάλυση σε ένα αρχείο, να το στείλετε mail κτλ. 

Ένα jupyter notebook αποτελείται από κελιά. Κάθε κελί μπορεί να περιέχει είτε κώδικα python (επιτρέπονται και άλλες γλώσσες) είτε [markdown](https://en.wikipedia.org/wiki/Markdown). Το markdown είναι μια συλλογή από συμβάσεις για να εισάγουμε μορφοποίηση σε ένα αρχείο κειμένου. Π.χ. αν στο markdown γράγουμε μία λέξη ανάμεσα σε 2 αστεράκια (π.χ.: ```**Αλέξανδρος**```) τότε αυτή θα εμφανιστεί ως bold (έντονη) δηλαδή έτσι: **Αλέξανδρος**. [Πλήρη λίστα με όλες τις markdown συμβάσεις](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet).

Επίσης μπορείτε να φορτώσετε κάποιο notebook που θα σας στείλουν στον browser σας. Ακόμα καλύτερα μπορείτε να αποθηκεύσετε ένα notebook στο Internet δωρεάν! Ως [gist](https://gist.github.com/). 

## Μία πρώτη γεύση

### print 


```python
print ('kati')
```

    kati


Μπορούμε να χρησιμοποιήσουμε μονά (') ή διπλά αυτάκια (") ή τριπλά αυτάκια (''') ή (""")


```python
print ("hello")
```

    hello



```python
print ("""hello""")
```

    hello



```python
print ('''hello''')
```

    hello


Μπορούμε να βάλουμε ένα "Enter" μέσα σε ένα string με "\n":


```python
print ("hello\nworld")
```

    hello
    world


Ομοίως μπορούμε να βάλουμε μονά ή διπλά αυτάκια σε ένα string. Ανάλογα με το τι χρησιμοποιούμε για να δηλώσουμε ένα string (μονά ή διπλά αυτάκια) θα πρέπει να χρησιμοποιήσουμε \' ή \":


```python
print ("his master's voice")
```

    his master's voice



```python
print ('his master\'s voice')
```

    his master's voice



```python
print (" I am \"fear\"  ")
```

     I am "fear"  



```python
print ('i am "fear"')
```

    i am "fear"


Αν χρησιμούμε τριπλά αυτάκια μπορούμε να έχουμε πολλές γραμμές σε ένα string (multiline strings):


```python
print ("""ἄνδρα μοι ἔννεπε, μοῦσα, πολύτροπον, ὃς μάλα πολλὰ
πλάγχθη, ἐπεὶ Τροίης ἱερὸν πτολίεθρον ἔπερσεν·
πολλῶν δ᾽ ἀνθρώπων ἴδεν ἄστεα καὶ νόον ἔγνω,
πολλὰ δ᾽ ὅ γ᾽ ἐν πόντῳ πάθεν ἄλγεα ὃν κατὰ θυμόν,
ἀρνύμενος ἥν τε ψυχὴν καὶ νόστον ἑταίρων.""")
```

    ἄνδρα μοι ἔννεπε, μοῦσα, πολύτροπον, ὃς μάλα πολλὰ
    πλάγχθη, ἐπεὶ Τροίης ἱερὸν πτολίεθρον ἔπερσεν·
    πολλῶν δ᾽ ἀνθρώπων ἴδεν ἄστεα καὶ νόον ἔγνω,
    πολλὰ δ᾽ ὅ γ᾽ ἐν πόντῳ πάθεν ἄλγεα ὃν κατὰ θυμόν,
    ἀρνύμενος ἥν τε ψυχὴν καὶ νόστον ἑταίρων.


(θα επανέλθουμε αργότερα)

### Σχόλια
Σε οποιαδήποτε γραμμή οτιδήποτε ακολουθεί τον χαρακτήρα ```#``` θεωρείται σχόλιο και αγνοείται:


```python
# Αυτό είναι ένα σχόλιο
print ('Αυτό δεν είναι σχόλιο') # Αυτό όμως είναι!
```

    Αυτό δεν είναι σχόλιο


### Μαθηματικές πράξεις:

Η python μπορεί να κάνεις πράξεις με ακέραιους με οποιοδήποτε πλήθος αριθμών:


```python
24328470239847502934672098347520349867 * 234573458729835619384756398456
```




    5706813409766902302233897564852365380972748955782671565995978605352



Έχουμε τις κλασσικές πράξεις: πρόσθεση, αφαίρεση, πολλαπλασιασμός διαίρεση:


```python
3+2
```




    5




```python
3-2
```




    1




```python
3*2
```




    6



Δεκαδική διαίρεση:


```python
3/2
```




    1.5



Ακέραια διαίρεση:


```python
3//2
```




    1



**Προσοχή!**


```python
1/0
```


    ---------------------------------------------------------------------------

    ZeroDivisionError                         Traceback (most recent call last)

    <ipython-input-18-9e1622b385b6> in <module>()
    ----> 1 1/0
    

    ZeroDivisionError: division by zero


Έχουμε επίσης κάποιες επιπλέον πράξεις:

Το υπόλοιπο της διαίρεσης:


```python
15 % 4 
```




    3



Δηλαδη 15 = 3\*4 + **3**

Το εκθετικό:


```python
4**2
```




    16



**Προσοχή**: Το εκθετικό ΔΕΝ είναι \^:


```python
4 ^ 2
```




    6



Το ^ είναι μια άλλη πράξη που ονομάζεται [XOR](https://en.wikipedia.org/wiki/Exclusive_or) και δεν θα μας απασχολήσει σε αυτό το μάθημα.

Στη python κάθε πράξη έχει μία προτεραιότητα. Για παράδειγμα οι πολλαπλασιασμοί και διαρέσεις εκτελούνται **πριν** τις προσθέσεις και αφαιρέσεις:


```python
10+6/2
```




    13.0



**Σημείωση:** Ποτέ δεν "εμπιστευόμαστε" τη προτεραιότητα πράξεων! Πολλές φορές δεν είναι και τόσο ξεκάθαρο. Χρησιμοποιούμε παρενθέσεις:


```python
10+(6/2)
```




    13.0




```python
(10+6)/2
```




    8.0



Αν μία πράξη σε οποιοδήποτε σημείο της έχει τη διαίρεση **ή** συμμετέχει κάποιος δεκαδικός αριθμός, το αποτέλεσμα είναι δεκαδικό, αλλιώς είναι ακέραιος:



```python
2/2
```




    1.0




```python
2*2
```




    4




```python
2 + 2.0
```




    4.0




```python
2+2
```




    4



Η python έχει μία:
* συνώνυμη λέξη για το 1: το ```True``` 
* συνώνυμη λέξη για το 0: το ```False```


```python
True + 1
```




    2




```python
False + 1
```




    1



Τα ```False``` και ```True``` θα τα δούμε λίγο αργότερα!

Παρόλο που οι ακέραιοι μπορούν να έχουν απεριοριστό πλήθος από ψηφία, οι δεκαδικοί αριθμοί έχουν συγκεκριμένη ακρίβεια:


```python
5.123456789012345678901234567
```




    5.123456789012345



Γιατί γίνεται αυτό; Έναν ακέραιο, όσο μεγάλος και να είναι, μπορούμε να τον αναπαραστήσουμε στη μνήμη χωρίς να χάνουμε ακρίβεια. Για κάποιους δεκαδικούς όμως είναι απλά αδύνατο να έχουμε άπειρη ακρίβεια. Για παράδειγμα:


```python
1/3
```




    0.3333333333333333



Το ```1/3``` έχει άπειρα δεκαδικά ψηφία! Πως θα το αποθηκεύσουμε αυτό στη μνήμη; Η λύση είναι να αποθηκεύουμε ένα συγκεκριμένο πλήθος από δεκαδικά ψηφία. Ευτυχώς υπάρχει ένα διεθνές πρότυπο [IEEE-754](https://en.wikipedia.org/wiki/IEEE_754) το οποίο καθορίζει με ποιο τρόπο αποθηκεύουμε τους δεκαδικούς αριθμούς. Παρόλα αυτά μπορείτε να [καθοδηγήσετε τη python](https://docs.python.org/3/library/decimal.html) να μη χρησιμοποιεί αυτό το πρότυπο και να χειρίζεστε δεκαδικούς με όση ακρίβεια θέλετε (θυσιάζοντας λίγο τη μνήμη και τη ταχύτητα των υπολογισμών). 

### Αλφαριθμητικά (ή αλλιώς: strings)


```python
"mitsos"
```




    'mitsos'



Μπορούμε να προσθέσουμε δύο strings:


```python
'a' + 'b'
```




    'ab'



Μπορούμε να πολλαπλασιάσουμε string με ακέραιο:


```python
'a' * 10
```




    'aaaaaaaaaa'



Υπάρχει και το άδειο string


```python
''
```




    ''



Η ```len``` επιστρέφει το μέγεθος ενός string


```python
len("abcdefg")
```




    7




```python
len('')
```




    0



H ```count``` μας επιστρέφει πόσες φορές υπάρχει ένα string μέσα σε ένα άλλο string.


```python
"zabarakatranemia".count('a')
```




    6




```python
"zabarakatranemia".count('ra')
```




    2




```python
"zabarakatranemia".count('c')
```




    0



H ```index``` μας επιστρέφει σε ποιο σημείο συναντάμε ΠΡΩΤΗ φορά κάποιο string μέσα σε ένα άλλο string.


```python
"zabarakatranemia".index('anemia')
```




    10




```python
"zabarakatranemia".index('ra') # Το "ra" υπάρχει δύο φορές αλλά επιστρέφει τη θέση της πρώτης.
```




    4



Αν δεν υπάρχει τότε πετάει λάθος!


```python
"zabarakatranemia".index('c')
```


    ---------------------------------------------------------------------------

    ValueError                                Traceback (most recent call last)

    <ipython-input-237-1515cc1d7dbe> in <module>()
    ----> 1 "zabarakatranemia".index('c')
    

    ValueError: substring not found


**Προσοχή!** Δύο strings το ένα δίπλα στο άλλο θεωρούνται ένα!


```python
"Hello" "world"
```




    'Helloworld'



Ένα string μπορεί να έχει χαρακτήρες σε οποιαδίποτε γλώσσα!


```python
a = "σε οποιαδίποτε γλώσσα ذا كيور (بالإنجليزية: The Cure) هي فرقة روك إنجليزية، تم تكوينها في كرولي، غرب ساسكس عام 1976. واجهت الفرقة عِدة تغيرات؛ مع "
print (a)
```

    σε οποιαδίποτε γλώσσα ذا كيور (بالإنجليزية: The Cure) هي فرقة روك إنجليزية، تم تكوينها في كرولي، غرب ساسكس عام 1976. واجهت الفرقة عِدة تغيرات؛ مع 


Ναι, τα [emoji](https://unicode.org/emoji/charts/full-emoji-list.html) συμπεριλαμβάνονται:


```python
print ("\U0001F621")
```

    😡


Μετά από τα παραπάνω που μας έβαλαν σιγά σιγά στη python, μπορούμε να μιλήσουμε λίγο πιο θεωρητικά:

# Τελεστές
Οι τελεστες είναι σύμβολα ή δεσμευμένες λέξεις με τους οποίους εφαρμόζουμε βασικές πράξεις σε διάφορες εκφράσεις. Για πειρσσότερα μπορείτε να διαβάσετε εδώ: https://en.wikipedia.org/wiki/Operator_(computer_programming)

Μερικοί από τους πιο βασικους τελεστές που υποστηρίζει η python είναι:
* +
* -
* /
* //
* *
* %
* \*\*
* <
* \>
* <=
* \>=
* !=
* ==
* and
* or
* not
* in
* is

### Ο τελεστής +
Οι πράξεις που επιστρέπονται με τον τελεστή '+' είναι:


```python
3+2
```




    5




```python
3+2.0
```




    5.0




```python
3+0.0
```




    3.0




```python
'ab' + 'cde' 
```




    'abcde'




```python
True + True + False
```




    2




```python
True + 2
```




    3




```python
True + 0.0
```




    1.0




```python
[1,2,3] + [4,5,6] # Λίστες θα το δούμε αργότερα
```




    [1, 2, 3, 4, 5, 6]



### Ο τελεστής -
Οι πράξεις που επιτρέπονται με τον τελεστή '-' είναι:


```python
3-2
```




    1




```python
3-7
```




    -4




```python
4-6.0
```




    -2.0




```python
True - True
```




    0




```python
True - 6.6
```




    -5.6



### O τελεστής *
Οι πράξεις που επιτρέπονται με τον τελεστή '\*' είναι:


```python
6*7
```




    42




```python
6.6*2
```




    13.2




```python
True * 2
```




    2




```python
True * False
```




    0




```python
True * 2.3
```




    2.3




```python
6 * 'hello'
```




    'hellohellohellohellohellohello'




```python
[1,2,3] * 5  # Λίστες, θα τα δούμε αργότερα..
```




    [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]



### Ο τελεστής '/'

Οι πράξεις που επιτρέπονται με τον τελεστή '/' είναι:


```python
4/5
```




    0.8



**ΠΡΟΣΟΧΗ!!**


```python
5/0
```


    ---------------------------------------------------------------------------

    ZeroDivisionError                         Traceback (most recent call last)

    <ipython-input-57-0106664d39e8> in <module>()
    ----> 1 5/0
    

    ZeroDivisionError: division by zero



```python
True/True
```




    1.0




```python
6/3
```




    2.0




```python
6.5/3
```




    2.1666666666666665



### O τελεστής '//'
Αυτός ο τελεστής μας δίνει το αποτέλεσμα της ακέραιας διαίρεσης


```python
5//2
```




    2




```python
11//3
```




    3




```python
6.5 // 2.1
```




    3.0




```python
True // 2
```




    0



### Ο τελεστής %
Αυτός ο τελεστής μας δίνει το υπόλοιπο της ακέραιας διαίρεσης


```python
5%2
```




    1




```python
5.2 % 2
```




    1.2000000000000002




```python
True % 2
```




    1



Ο τελεστής % χρησιμοποιείται (όχι και τόσο συχνά) για να βάλουμε strings μέσα σε strings


```python
'my name is %s nice to meet you' % "mitsos"
```




    'my name is mitsos nice to meet you'



Μπορείτε να βρείτε [εδώ](https://python-reference.readthedocs.io/en/latest/docs/str/formatting.html) για το πως μπορείτε να χρησιμοποιείσετε αυτόν τον τελεστή για strings με περισσότερα παραδείγματα

### Ο τελεστής **
Αυτός ο τελεστής μας επιστρέφει το εκθετικό $a^b$


```python
3**2
```




    9




```python
3.2**2.3
```




    14.515932837559118




```python
True ** 2
```




    1



## Λογικοί Τελεστές
Είδαμε πριν τις σταθερές ```True``` και ```False```. Ποιος είναι ο σκοπός τους; Μέχρι στιγμής είδαμε τελεστές οι οποίοι μπορούν να παράγουν αριθμούς. Για την παράδειγμα ο τελεστής ```+``` μπορεί να παράξει έναν οποιοδήποτε αριθμό. Υπάρχει όμως μία ομάδα τελεστών που μπορύν να παράξουν 2 μόνο διαφορετικές τιμές. Τις τιμές ```True``` και ```False```. Οι τελεστές αυτές είναι:
* Οι τελεστές σύγκρισης <, >, <=, >=
* Οι τελεστές ισότητας ==, !=
* Οι τελεστές and, or, not
* Οι τελεστές in, is (θα τους δούμε αργότερα)

Αυτοί οι τελεστές επιστρέφουν **πάντα** True ή False σε **ότι** και αν τους εφαρμόσουμε!

Ο α < β ελέγχει αν το α είναι μικρότερο από το β:


```python
2<3 
```




    True




```python
3<2
```




    False




```python
3<3
```




    False



Ο α <= β ελέγχει α είναι μικρότερο ή ίσο με το β:


```python
2<=3
```




    True




```python
3<=2
```




    False




```python
3<=3
```




    True



Ο α > β ελέγχει αν το α είναι μεγαλύτερο από το β:


```python
3 > 2
```




    True




```python
2 > 3
```




    False




```python
3 > 3
```




    False



Ο α >= β ελέγχει αν το α είναι μεγαλύτερο ή ίσο με β:


```python
3 >= 2
```




    True




```python
2 >= 3
```




    False




```python
3 >= 3
```




    True



Ο τελέστής α == β ελέγχει αν το α είναι ίσο με το β


```python
3==2
```




    False




```python
3==3
```




    True




```python
3==3.0
```




    True




```python
"3" == 3
```




    False




```python
16**0.5 == 4
```




    True




```python
'mitsos' == 'mits' + 'os'
```




    True




```python
3 == 6/2
```




    True




```python
True == True or False
```




    True




```python
3 == True + True + True + False
```




    True




```python
3 == 'mits' + 'os'
```




    False




```python
[1,2,3] == [1,2,3] # Λίστες, θα τα δούμε αργότερα
```




    True




```python
[1,2,3] == [2,1,3]
```




    False



Ο τελεστής α != β αν το α **δεν** είναι ίσο με το β


```python
3 != 2
```




    True




```python
2 != 2
```




    False




```python
2 != 2.0
```




    False




```python
1 != True
```




    False




```python
'hello' != ' hello '
```




    True




```python
'' != ''
```




    False




```python
'' != ' '
```




    True



Μπορούμε επίσης να χρησιμοποιήσουμε τους ίδιους τελεστές <, >, <=, >= παραπάνω από μία φορά:


```python
2<3<4
```




    True




```python
2<3<3
```




    False



Όταν εφαρμόζονται σε strings, τότε τα συγκρίνουμε αλφαριθμητικά (λεκτικά). Ποιο μικρό θεωρείται αυτό που σε μία ταξινόμηση, παίρνει τη μικρότερη θέση:


```python
'ab' < 'fg'
```




    True




```python
'ab' < 'b'
```




    True




```python
'ab' < 'ac'
```




    True




```python
'ab' < 'a'
```




    False



Το άδειο string έχει τη πιο μικρή δυνατή τιμή


```python
'' < '0'
```




    True




```python
"A" < "a"
```




    True




```python
"05456745674" < "5"
```




    True




```python
'8' < '09'
```




    False



Πολλές φορές θέλουμε να πάρουμε μία απόφαση ανάλογα με τα αν 2 ή παραπάνω λογικές τιμές είναι αληθής. Για παράδειγμα:

Θα βγω έξω αν κάνει καλό καιρό **και** δεν έχω δουλειά.

Θα βγω έξω αν κάνει καλό καιρό **ή** δεν έχω δουλεία. 

Έτσι έχουμε δύο επειπλέον λογικούς τελεστές: ```and``` , ```or``` . 

Ο α and β είναι ```True``` αν τα α και τα β είναι ```True```, αν ένα από τα α,β είναι ```False``` είναι ```False``` (ή και τα δύο), τότε το αποτέλεσμα είναι ```False```:


```python
True and True
```




    True




```python
True and False
```




    False




```python
False and True
```




    False




```python
False and False
```




    False




```python
(1==1) and (2==3-1)
```




    True




```python
(1==1) and (2==3)
```




    False




```python
(1>=1) and (2<=2)
```




    True



Ομοίως το αποτέλεσμα της πράξη α or β είναι ```True``` αν ένα από τα α,β (ή και τα δύο) είναι ```True```, διαφορετικά είναι ```False```:


```python
True or True
```




    True




```python
True or False
```




    True




```python
False or True
```




    True




```python
False or False
```




    False




```python
1==2 or 1<=1
```




    True




```python
1>2 or 2<1
```




    False




```python
0==1 or True
```




    True



Τέλος, υπάρχει ο τελεστής ```not```. Αυτός ο τελεστής έχειτην ιδαιτερότητα ότι εφαρμόζεται σε μία μόνο τιμή. Το ```not``` α, έχει σαν αποτέλεσμα ```False``` αν το α είναι ```True``` και ```True``` αν το α είναι ```False```:


```python
not True
```




    False




```python
not False
```




    True




```python
not 0
```




    True




```python
not 0.0000000001
```




    False




```python
not ''
```




    True




```python
not 1
```




    False




```python
not ' '
```




    False




```python
not 3==4
```




    True




```python
not 3==3
```




    False




```python
not "mitsos"=="Mitsos"
```




    True




```python
not "mitsos" == "mitsos"
```




    False



**Fun fact:** Ο υπολογιστής που έχετε και κάνει όλα τα απίστευτα πράγματα που κάνει στην ουσία μπορεί να κάνει μία και μόνο μία πράξη: ```not (a and b)```. Αυτή η πράξη ονομάζεται NAND. Για παράδειγμα όταν ο υπολογιστής κάνει μία μαθηματική πράξη (π.χ. ```14.2 * 51.1```), "σπάει" τη πράξη αυτή σε πράξεις NAND. Δηλαδή ο επεξεργαστής έχει δισεκατομύρια κυκλώματα που κάνουν αυτή και μόνο αυτή τη πράξη. Είναι όμως οργανωμένα έτσι ώστε όταν συνδυαστούν με τον σωστό τρόπο να κάνουν όλες τις αριθμητικές πράξεις! [Περισσότερα](https://en.wikipedia.org/wiki/NAND_logic). Ακόμα και όταν κάνει πιο πολύπλοκα πράγμα (streaming, παίζει ένα παιχνίδι, ελέγχει έναν πυρηνικό αντιδραστήρα, καθοδηγεί ένα διαστημόπλοιο) πάλι σπάει όλες τις πράξεις που χρειάζονται σε πράξεις NAND. 

### Επιστροφή στα strings!

Όλα κεφαλαία:


```python
"abcde".upper()
```




    'ABCDE'



Όλα μικρά:


```python
"ABCDE".lower()
```




    'abcde'



Αντικατάσταση κάποιου κομματιού του string με ένα άλλο:


```python
"hello world".replace('l', "QQQ")
```




    'heQQQQQQo worQQQd'



Μπορούμε να αφαιρέσουμε τα κενά από το τέλος και από την αρχή:


```python
"    hello    "
```




    '    hello    '




```python
"    hello    ".strip()
```




    'hello'




```python
"+++hello+++".strip('+')
```




    'hello'




```python
not "     "
```




    False




```python
not "     ".strip()
```




    True



Έλεγχος αν ένα string αρχίζει με ένα άλλο string:


```python
"heraklio".startswith('her')
```




    True



Έλεγχος αν ένα string τελειώνει με ένα άλλο string:


```python
"alex".endswith("lex")
```




    True



### Indexing
Στα strings (όπως και στις λίστες όπως θα δούμε παρακάτω), μπορούμε να παραπάνω ένα υποσύνολό τους χρησιμοποιώντας το ```[]```. Αυτή η δυνατότητα ονομάζεται indexing. 


```python
print ("hello")
```

    hello


**Προσοχή!** Η αρίθμηση ξεκινάει από το 0!


```python
"hello"[0]
```




    'h'




```python
"hello"[1]
```




    'e'



**Προσοχή!** H αρίθμηση δεν πρέπει να ξεπεράσει το μέγεθος του string!


```python
"hello"[100]
```


    ---------------------------------------------------------------------------

    IndexError                                Traceback (most recent call last)

    <ipython-input-197-e6ccf1afaf71> in <module>()
    ----> 1 "hello"[100]
    

    IndexError: string index out of range


To index (ή αλλιώς η "αρίθμηση") μπορεί να πάρει πάρει και αρνητικές τιμές! το ```-1``` είναι το τελευταίο στοιχείο. Το ```-2``` το προτελευταίο κτλ..


```python
"hello"[-1]
```




    'o'




```python
"hello"[-2]
```




    'l'




```python
"hello"[-100]
```


    ---------------------------------------------------------------------------

    IndexError                                Traceback (most recent call last)

    <ipython-input-201-552ff00ad524> in <module>()
    ----> 1 "hello"[-100]
    

    IndexError: string index out of range


### Indexing spaces
Μπορούμε να πάρουμε κάποια ένα υποσύνολο ενώς string με βάση τα διαστήματα που ορίζουμε στο ```[]```


```python
"hello"[1:3]
```




    'el'



Όταν γράφουμε ```[a:b]``` εννοούμε "ξεκίνα από το α-στό στοιχείο (η αρίθμηση ξεκινάει από 0!) και σταμάτο στο β-στό στοιχείο, ΧΩΡΙΣ ΟΜΩΣ ΝΑ ΠΑΡΕΙΣ ΑΥΤΟ!!"


```python
"hello"[1:4]
```




    'ell'



Αν θέλουμε να πάρουμε ένα υποσύνολο που ξεκινάει από την αρχή του string τότε μπορούμε να γράψου είτε ```[0:b]``` είτε ```[:b]```


```python
"hello"[0:2]
```




    'he'




```python
"hello"[:2]
```




    'he'



Αν θέλουμε ένα υποσύνολο που τελειώνει στο τέλος του string τότε μπορούμε να γράψουμε ```[a:]```


```python
"hello"[2:]
```




    'llo'



### Indexing spaces with steps
Μπορούμε να χρησημοποιήσουμε για indexing το ```[a:b:c]```. Αυτό σημαίνει: πήγαινε από το a-στο στο b-στο (χωρίς να πάρεις το b-στο!) με βήμα: c


```python
"abcdefgij"[1:7:2]
```




    'bdf'




```python
"abcdefgij"[1:7:3]
```




    'be'



Αν παραλείψουμε το πρώτο στοιχείο τότε από default βάζει το 0


```python
"abcdefgij"[:7:3]
```




    'adg'



Αν παραλείψουμε το δεύτερο τότε από default βάζει το τέλος του string


```python
"abcdefgij"[1::3]
```




    'bei'



Μπορούμε να παραλείψουμε και τα δύο οπότε θα πάρει από την αρχή μέχρι το τέλος του string


```python
"abcdefgij"[::3]
```




    'adg'



Αν παραλείψουμε το τρίτο τότε από default βάζει το 1


```python
"abcdefgij"[1:7:]
```




    'bcdefg'



To c δεν μπορεί να είναι 0!


```python
"abcdefgij"[1:7:0]
```


    ---------------------------------------------------------------------------

    ValueError                                Traceback (most recent call last)

    <ipython-input-219-96e6dd4da4bc> in <module>()
    ----> 1 "abcdefgij"[1:7:0]
    

    ValueError: slice step cannot be zero


### Αρνητικά indexing steps.
Το βήμα ```c``` μπορεί να είναι αρνητικό! 


```python
"abcdefgij"[7:1:-1]
```




    'igfedc'




```python
"abcdefgij"[7:1:-2]
```




    'ifd'




```python
"abcdefgij"[7::-2]
```




    'ifdb'




```python
"abcdefgij"[::-2]
```




    'jgeca'




```python
"abcdefgij"[::-1] # Reverse a string! 
```




    'jigfedcba'



Χρήσιμο όταν έχουμε cDNA !


```python
"ACGT"[::-1]
```




    'TGCA'



Φυσικά μπορεί να μπει και κάποια μεταβλητή σε αυτά.


```python
a=3
"abcde"[0:a]
```




    'abc'



### Special Characters
Έχουμε πει ότι με τα μονά ή διπλά "αυτάκια" μπορούμε να δηλώσουμε ένα string. Τι γίνεται όμως όταν θέλουμε να βάλουμε μέσα ένα string ένα μονό ή διπλό αυτάκι; Μπορούμε να χρησιμοποιήσουμε το ```\``` ή αλλιώς backslash:


```python
print("mitsos")
```

    mitsos



```python
print("My name is \"mitsos\"")
```

    My name is "mitsos"



```python
print('My name is "mitsos"')
```

    My name is "mitsos"



```python
print ('My name is \'Mitsos\'')
```

    My name is 'Mitsos'



```python
print ("My name is 'Mitsos'")
```

    My name is 'Mitsos'


Υπάρχουν επίσης και οι παρακάτω ειδικοί χαρακτήρες: 
* Νέα γραμμή: ```\n``` (n = New line)
* Tab: ```\t``` 


```python
print("Line 1\nLine 2")
```

    Line 1
    Line 2



```python
print ("Col 1\tCol2")
```

    Col 1	Col2


Σε περίπτωση που θέλουμε να γράψουμε ένα μεγάλος string που έχει μέσα πολλούς ειδικούς χαρακτήρε (αυτάκια, new lines, κτλ.. ) μπορούμε να χρησημοποιείσουμε τα τριπλά μονά ή διπλα αυτάκια:


```python
print( '''
"Be realistic - demand the impossible!"
    Soyez réalistes, demandez l'impossible! - Anonymous graffiti, Paris 1968
''')
```

    
    "Be realistic - demand the impossible!"
        Soyez réalistes, demandez l'impossible! - Anonymous graffiti, Paris 1968
    


### Συνδοιασμός μεταβλητών διαφορετικών τύπων

float και int μας κάνει float:


```python
3+0.0
```




    3.0




```python
0 + 0.0
```




    0.0



Η διαίρεση έχει πάντα αποτέλεσμα float:


```python
5/2
```




    2.5




```python
6/2
```




    3.0



float/int και string δεν επιτρέπεται


```python
4.5 + "μίτσος"
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-19-835a49c7937c> in <module>()
    ----> 1 4.5 + "μίτσος"
    

    TypeError: unsupported operand type(s) for +: 'float' and 'str'


όταν αναμειγνύουμε float/int με boolean τότε το True αντιστοιχεί με 1 και το False με 0:


```python
4 + True
```




    5




```python
4 * False
```




    0




```python
6 / True
```




    6.0



Μπορούμε να κάνουμε και το εξής:


```python
'Μήτσος' * True # είναι το ίδιο με 'Μήτσος' * 1
```




    'Μήτσος'




```python
'Μήτσος' * False #  είναι το ίδιο με 'Μήτσος' * 0
```




    ''



### Μπορούμε να προσθέσουμε True/False μεταβλητές μεταξύ τους! 
Και γενικότερα μπορούμε να κάνουμε οποιαδήποτε μαθηματική πράξη


```python
True + True
```




    2




```python
True + False + True
```




    2




```python
(True + False) / (True + True)
```




    0.5




```python
True * True * True * True * True * True
```




    1




```python
True * True * True * True * False * True
```




    0



### Οι τελεστές ```and``` και ```or``` με μεταβλητές που ΔΕΝ είναι boolean

Θυμάστε τους τελεστές ```and``` και ```or```. Π.χ:


```python
True and False
```




    False



Τι θα γίνει αν τους χρησιμοποιήσω με μεταβλητές (ή σταθερές) που ΔΕΝ είναι boolean;

Αν κάνω ```Α and B and C and ... and Z``` θα μου επιστρέψει τη πρώτη έκφραση που είναι False. Αν δεν υπάρχει καμία που να είναι False, θα μου επιστρέψει τη τελευταία:


```python
5 and '' and 'Μήτσος'
```




    ''




```python
5 and 'Μήτσος' and 0.0
```




    0.0




```python
5 and 'Μήτσος' and 3.2
```




    3.2



Γιατί όμως γίνεται αυτό; Γιατί όταν σε μία έκφραση A and B and C τo B είναι False, τότε δεν έχει νόημα να δούμε τι τιμή είναι το C. Είτε το C είναι True, είτε False, το αποτέλεσμα θα είναι False. Οπότε στην ουσία η python επιστρέφει τη τιμή της έκφρασης που αποτίμησε τελευταία.   

Αυτή η τεχνική ονομάζεται [short-circuit evaluation](https://en.wikipedia.org/wiki/Short-circuit_evaluation)

Ομοίως α κάνουμε: ```A or B or C or ... or Z```. Θα επθστρέχει τη πρώτη τιμή που είναι True. Αν δεν υπάρχει καμία που να είναι True, τότε θα επιστρέψει τη τελευταία:


```python
0 or 5.3 or 'Μήτσος'
```




    5.3




```python
0 or 5.3 or ''
```




    5.3




```python
0 or False or ''
```




    ''



### Έλεγχος του τύπου μιας τιμής

Η συνάρτηση ```type``` επιστρέφει ένα string το οποίο περιέχει τον τύπο μίας τιμής:



```python
type(2)
```




    int




```python
type(2.0)
```




    float




```python
type('')
```




    str




```python
type('mitsos')
```




    str




```python
type(True)
```




    bool




```python
type(1==2)
```




    bool




```python
type(1+2)
```




    int



### Μετατροπή τύπων

Υπάρχουν ειδικές συναρτήσεις για να μετατρέπουμε μεταβλητές από έναν τύπο στον άλλο:
* ```int``` μετατράπει σε ακέραιο
* ```float``` μετατρέπει σε δεκαδικό
* ```bool``` μετατρέπει σε δυαδικό
* ```str``` μετατρέπει σε αλφαριθμητικό

Μερικά παραδείγματα:


```python
int('42')
```




    42




```python
int('42.4')
```


    ---------------------------------------------------------------------------

    ValueError                                Traceback (most recent call last)

    <ipython-input-33-c0c93863b08a> in <module>()
    ----> 1 int('42.4')
    

    ValueError: invalid literal for int() with base 10: '42.4'



```python
int(42.4)
```




    42




```python
int(True)
```




    1




```python
int(False)
```




    0




```python
int(42)
```




    42




```python
int('mitsos')
```


    ---------------------------------------------------------------------------

    ValueError                                Traceback (most recent call last)

    <ipython-input-39-24e8b5b4a1dd> in <module>()
    ----> 1 int('mitsos')
    

    ValueError: invalid literal for int() with base 10: 'mitsos'



```python
int('                                 42')
```




    42




```python
int('42                                  ')
```




    42




```python
int('               42                    ')
```




    42




```python
float('3.4')
```




    3.4




```python
float('3')
```




    3.0




```python
float('')
```


    ---------------------------------------------------------------------------

    ValueError                                Traceback (most recent call last)

    <ipython-input-45-45d756431581> in <module>()
    ----> 1 float('')
    

    ValueError: could not convert string to float: 



```python
float('mitsos')
```


    ---------------------------------------------------------------------------

    ValueError                                Traceback (most recent call last)

    <ipython-input-46-a78f2c30f998> in <module>()
    ----> 1 float('mitsos')
    

    ValueError: could not convert string to float: 'mitsos'



```python
float('3.4             ')
```




    3.4




```python
float('   3.4           ')
```




    3.4




```python
float('               3.4')
```




    3.4




```python
float(3)
```




    3.0




```python
float(3.4)
```




    3.4




```python
float(True)
```




    1.0




```python
float(False)
```




    0.0




```python
bool(2)
```




    True




```python
bool(0)
```




    False




```python
bool(3.3)
```




    True




```python
bool(0.0)
```




    False




```python
bool(0.000000000001)
```




    True




```python
bool('mitsos')
```




    True




```python
bool('')
```




    False




```python
bool(' ')
```




    True




```python
bool(True)
```




    True




```python
bool(False)
```




    False



### Βοήθεια και οδηγίες

Όλα αυτά είναι πολλά! Πως θα τα θυμάμαι; 

Δεν χρειάζεστε να θυμάστε πολλά.. Έχετε πάντα το google.. αν ρωτήσετε "how to ... in python" συνήθως το πρώτο αποτέλεσμα θα έχει μία πολύ καλή απάντηση! Πρόσφατα [ο δημιουργός της python](https://en.wikipedia.org/wiki/Guido_van_Rossum) είπε ότι χρησιμοποιεί ο ίδιος το google για να βρίσκει πως θα κάνει μερικά πράγματα στη.. python. 

Παρόλα αυτά η 
python περιέχει κάποιες βασικές οδηγίες και βοήθεια:


```python
help(len)
```

    Help on built-in function len in module builtins:
    
    len(obj, /)
        Return the number of items in a container.
    



```python
help("".count)
```

    Help on built-in function count:
    
    count(...) method of builtins.str instance
        S.count(sub[, start[, end]]) -> int
        
        Return the number of non-overlapping occurrences of substring sub in
        string S[start:end].  Optional arguments start and end are
        interpreted as in slice notation.
    


Δοκιμάστε και:


```python
?len
```
