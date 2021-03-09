
## 1
Ένα έτος είναι δίσεκτο (δλδ έχει 366 μέρες αντί για 365) αν διαρείται τέλεια με το 4. Π.χ. το έτος 2020 ήταν δίσεκτο. Από αυτόν τον κανόνα εξαιρούνται τα έτη που διαιρούνται με το 100. Δηλαδή το έτος 1900 παρόλο που διαιρείται με το 4 ΔΕΝ είναι δίσεκτο! Από τον τελευταίο κανόνα εξαιρούνται τα έτη που διαιρούνται με 400! Δλδ το έτος 2000 παρόλο που διαρείται με το 100 ΗΤΑΝ δίσεκτο (I know..).Γράψτε μία συνάρτηση σε python η οποία θα παίρνει μία παράμετρο με το όνομα year η οποία θα αναπαριστάει ένα έτος. Η συνάρτηση θα επιστρέφει True/False ανάλογα με τo αν το year είναι δίσεκτο ή όχι.

Bonus: MHN χρησιμοποιήσετε if

Σημείωση: Προσπαθήστε να αντισταθείτε στη παρόρμησή σας να google-άρετε για τη λύση.. 

```python
def f(year):
	return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
```

```python
def f(year):
   if year % 4 == 0:
      # Διαρείται με το 4! αλλά ακόμα δεν ξέρω αν είναι δίσεκτο ή όχι!
      # Ας κάνω και άλλους ελέγχους!
      if year % 100 == 0:
         # Διαρείται με το 100 !
         # Ακόμα δεν ξέρω αν είναι δίσεκτο ή όχι! 
         # Πρέπει να κάνω και άλλους ελέγχους..
         if year % 400 == 0:
            # Διαιρείται με το 400, άρα δίσεκτο!
            return True
         else:
            # Χμμ.. διαρείται με το 100 αλλά ΔΕΝ διαρείται με το 400
            # Άρα ΔΕΝ είναι δίσεκτο!
            return False
      else:
         # Δεν διαρείται με το 100, αλλά δαιρείται με το 4. Είναι δίσεκτο!
         return True
   else:
      # Δεν διαιρείται με το 4, άρα δεν είναι δίσεκτο
      return False
```

```python
def f(year):
   if year % 400 == 0:
      return True   if year % 100 == 0:
      return False   if year % 4 == 0:
      return True   return False
```

## 2 
Ο υπολογισμός της Κυριακής του Πάσχα είναι ένας από τους αρχαιότερους αλγόριθμους που υπάρχουν. Η ιστορία του ξεκινάει από τον 5ο αιώνα π.Χ. όταν ο [Μέτων ο Αθηναίος](https://en.wikipedia.org/wiki/Meton_of_Athens) ανακάλυψε ότι οι μέρες που έχουμε πανσέλληνο μέσα σε έναν χρόνο εμφανίζουν μία περιοδικότητα. Long story short μερικούς αιώνες αργότερα το Πάσχα κανονίστηκε να εορτάζεται την [πρώτη Κυριακή μετά τη πρώτη πανσέλληνο της εαρινής ισημερίας](https://en.wikipedia.org/wiki/Ecclesiastical_full_moon). Προφανώς οι παπάδες τσακώθηκαν αργότερα για το [τι ακριβώς εννοείς "Κυριακή" δλδ με βάση πιο ημερολόγιο, και με πιο τρόπο θα διαφοροποιηθούν από το Ιουδαϊκό Πάσχα ώστε να μην φαίνεται ότι κάναν τη γιορτή κόπι-πάστα](https://en.wikipedia.org/wiki/Easter_controversy). Από μαθηματικής άποψης, ο υπολογισμός αυτής της ημερομηνίας εμφανίστηκε να έχει πολλές δυσκολίες. Κυρίως γιατί πρέπει να συγχρονιστούν τέσσερα συστήματα: κύκλος του Μέτονα, κύκλος της σελήνης, εαρινή ισημερία και το εκάστωτε ημερολόγιο που χρησιμοποιείται. Για αυτό τα πολυυυυ παλιά χρόνια το Πάσχα υπολογιζόταν με βάσει διάφορους αστρονομικούς πίνακες. Το πρόβλημα ήταν τόσο πολύπλοκο που ο Gauss (ίσως ο μεγαλύτερος μαθηματικός ever) δημοσίευσε 3 διαφορετικές εκδόσεις του αλγόριθμου που αποδείκτηκαν και οι τρεις λάθος! Ο καλύτερος αλγόριθμος που έχουμε αυτή τη στιγμή δημοσιεύτηκε μόλις το 1991(!) και.. δουλεύει σωστά για όλες τις ημερομηνίες από το 1900 μέχρι το 2099 (αν και με μια μικρή διόρθωση μπορεί να "παίξει" και για οποιαδήποτε ημερομηνία). Ο αλγόριθμος αυτός ονομάζεται Meeus's Julian algorithm. Μπορείτε να διαβάσετε περισσότερα για όλη αυτή τη τρέλα σε αυτό [το φανταστικό άρθρο της wikipedia](https://en.wikipedia.org/wiki/Computus). Στο [τέλος αυτού του άρθρου υπάρχει και ο αλγόριθμος του Meeus's Julian algorithm με παραδείγματα για διάφορες ημερομηνίες](https://en.wikipedia.org/wiki/Computus#Meeus's_Julian_algorithm). Ο αλγόριθμος είναι ο εξής:Έστω Υ ο χρόνος. Κάνουμε τους εξής υπολογισμούς:

```
a = Y mod 4     
b = Y mod 7     
c = Y mod 19    
d = (19c + 15) mod 30   
e = (2a + 4b − d + 34) mod 7    
month = (d + e + 114) div 31    
day = ((d + e + 114) mod 31) + 1    
```

Αν το month είναι 4 τότε ο μήνας είναι ο Απρίλιος, αν το month είναι 5 τότε είναι Μάιος. Επίσης το mod είναι ο τελεστής που βγάζει το υπόλοιπο, το αντίστοιχο % στη python. To div είναι ο τελεστής που βγάζει την ακέραια διαίρεση, το αντίστοιχο // στη python.
Ο αλγόριθμος αυτός βγάζει την ημερομηνία για το Ιουλιανό ημερολόγιο (παλιοημερολογήτικο!). Για να βγάλει τη σωστή ημερομηνία στο Γρηγοριανό, θα πρέπει να το "πάτε μπροστά" 13 μέρες.
Φτιάξτε λοιπόν μία συνάρτηση σε python η οποία θα παίρνει σαν παράμετρο έναν ακέραιο αριθμό ο οποίος θα αναπαριστάει ένα έτος και θα επιστρέφει την ημερομηνία της Κυριακής του Πάσχα για αυτό το έτος. Η ημερομηνία πρέπει να είναι γραμμένη στα ελληνικά γιατί μέρος αυτής της άσκησης είναι να βρείτε πως βάζουμε διαλυτικά με τόνο στη λέξη Μαΐου.Πως να τεστάρετε τον αλγόριθμό σας:

* f(2020) # Επιστρέφει: "19 Απριλίου"
* f(2021) # Επιστρέφει: "2 Μαΐου"
* f(2022) # Επιστρέφει: "24 Απριλίου"

```python


def f(Y):

    # Ο αλγόριθμός Meeus's Julian algorithm 

    a = Y % 4
    b = Y % 7
    c = Y % 19
    d = (19*c + 15) % 30
    e = (2*a + 4*b - d + 34) % 7
    month = (d + e + 114) // 31
    day = ((d + e + 114) % 31) + 1 

    # Πάμε 13 μέρες μπροστά
    day += 13

    # Υπολογίζουμε το μήνα σε string
    if day > 30:
        month = 'Μαΐου'
        day -= 30
    else:
        month = 'Απριλίου'

    return str(day) + " " + month

​

print (f(2020))
print (f(2021))
print (f(2022))
```

## 3

Ν παιδάκια θέλουν να παίξουν κρυφτό και πρέπει να βρούν ποιος θα τα "φυλάει". Σχηματίζουν έναν κύκλο όπου το παιδάκι με αριθμό 1 έχει στα δεξιά του το παιδάκι με αριθμό 2. Το παιδάκι με αριθμό 2 έχει στα δεξιά του το παιδάκι με αριθμό 3 κτλ.. το παιδάκι με αριθμό Ν έχει στα δεξιά του το παιδάκι με αριθμό 1. Έστω ότι το παιδάκι με αριθμό k (το k είναι ένας αριθμός από το 1 μέχρι και το Ν), αρχίζει να λέει ένα ποιηματάκι (α-μπε-μπα-μπλομ-κτλ..) για να δει ποιος θα τα φυλάει. Το ποιηματάκι έχει s συλλαβές και το παιδάκι που λέει το ποιηματάκι αρχίζει να δείχνει ένα-ένα τα παιδάκια ξεκινώντας από τα δεξιά του και συνεχίζοντας δεξιόστροφα. Όταν φτάσει στη τελευταία συλλαβή του ποιήματος, ποιος είναι ο αριθμός του παιδιού που θα δείχνει; Φτιάξτε μία συνάρτηση με το όνομα f, η οποία θα παίρνει 3 παραμέτρους και οι 3 ακέραιοι: το Ν, το k και το s. H συνάρτηση θα πρέπει να επιστρέφει έναν αριθμό από το 1 μέχρι το Ν που θα είναι ο αριθμός του παιδιού που θα τα φυλάει.
Πως θα τεστάρετε τη συνάρτησή σας:
* f(4,1,2) # επιστρέφει 3 (4 παιδάκια, το ποιηματάκι το λέει το 1ο παιδί, και έχει 2 συλλαβές)
* f(4,2,3) # επιστρέφει 1 (4 παιδάκια, το ποιηματάκι το λέει το 2ο παιδί, και έχει 3 συλλαβές)
* f(321,101,4549) # επιστρέφει 156 

Χρησιμοποιώντας τη συνάρτηση f φτιάξτε τη συνάρτηση hours η οποία θα παίρνει δύο ορίσματα: το a και το b. H συνάρτηση θα επιστρέφει έναν αριθμό o οποίος θα είναι η ώρα που είναι αν έχουν περάσει b ώρες από την ώρα a (χρησιμοποιήστε 12ωρο ή 24ωρο ρολόι, ότι θέλετε). Για παράδειγμα hours(5, 210) επιτρέφει τι ώρα θα είναι μετά από 210 ώρες αν η ώρα τώρα είναι 5.Χρησιμοποιώντας τη συνάρτηση f φτιάξτε τη συνάρτηση day η οποία θα παίρνει δύο ορίσματα: το a και το b. Η συνάρτηση θα επιστρέφει τη μέρα της μέρας (1=Δευτέρα, 2=Τρίτη, ...7=Κυριακή) που θα είναι μετά από b μέρες όταν η μέρα είναι a. Για παράδειγμα: day(2,300) επιστρέφει τι μέρα (από 1 μέχρι και 7) θα είναι μετά από 300 μέρες αν σήμερα είναι Τρίτη

```python


def f(N,k,s):
    return 1+((k+s-1)%N) 

​

def hours(a,b):
    return f(12, a, b)

​

def days(a,b):
    return f(7, a, b)

```

## 4
Σε ένα φορολογικό σύστημα ισχύει το εξής:

* Τα πρώτα 10.000 ευρώ δεν φορολογούνται
* Τα υπόλοιπα και μέχρι και τα 20.000 ευρώ φορολογούνται με φόρο 15%
* Τα υπόλοιπα και μέχρι και τα 40.000 ευρώ φορολογούνται με φόρο 20%
* Τα υπόλοιπα και μέχρι και τα 60.000 ευρώ φορολογούνται με φόρο 30%
* Τα υπόλοιπα (>60.000 ευρώ) φορολογούνται με φόρο 40%

Γράψτε μία συνάρτηση με το όνομα f, η οποία θα παίρνει σαν παράμετρο τη μεταβλητή income η οποία θα αναπαριστάει το εισόδημα ενός φορολογούμενου. Η συνάρτηση θα επιτρέφει τη φορολογία που αναλογεί στον φορολογούμενο. Παραδείγματα:

* f(5000)  # Epistrefei: 0
* f(15000) # Epistrefei: 750.0
* f(30000) # Epistrefei: 3500.0
* f(50000) # Epistrefei: 8500.0
* f(70000) # Epistrefei: 15500.0

```python


def g(income, start, end):

    

    new_income = income - start
    if new_income < 0:
        return 0

    if end == None:
        return new_income 

    new_end = end - start
    if new_end < new_income:
        return new_end

    return new_income

    

def f(income):

    ret = 0
    ret += g(income, 10_000, 20_000) * 0.15
    ret += g(income, 20_000, 40_000) * 0.2
    ret += g(income, 40_000, 60_000) * 0.3
    ret += g(income, 60_000, None) * 0.4

    return ret

```


## 5 
Φτιάξτε μία συνάρτηση σε python με το όνομα f. Η συνάρτηση παίρνει σαν παράμετρο ένα string. Το string περιέχει δύο θετικούς ακέραιους αριθμούς και ανάμεσα τους τη πράξη + ή τη πράξη -. Για παράδειγμα το string μπορεί να είναι ```"34+5"```,  ```"10-9"``` . Μεταξύ των αριθμών και της πράξης μπορεί να υπάρχει ένας αυθαίρετος αριθμός από κενά (spaces). Η συνάρτηση θα πρέπει να επιστρέφει το αποτέλεσμα της πράξης. Πως να τη τεστάρετε:

```
f(" 34  +5   ") # Επιστρέφει: 39
f("10    -     9") # Επιστρέφει: 1
```

```python


def f(x):
    if '+' in x:
        op = '+'
    elif '-' in x:
        op = '-'
    else:

        print ('THIS SHOULD NOT HAPPEN!')

    index = x.index(op)
    first = int(x[:index])
    second = int(x[index+1:])

    if op == '+':
        return first + second

    return first - second

```

## 6
Φτιάξτε μία συνάρτηση η οποία δεν θα παίρνει κανένα όρισμα. Η συνάρτηση θα επιτρέφει μία λίστα με όλους τους αριθμούς που είναι τέλεια τετράγωνα από το 100 μέχρι και το 10.000.Ένας αριθμός α είναι τέλειο τετράγωνο αν υπάρχει ένας ακέραιος αριθμός β, τέτοιος ώστε: β^2=α. Παράδειγμα αριθμών που είναι τέλεια τετράγωνα είναι: 100 (=10^2), 144(=12^2), 256(16^2).Απαγορεύεται η χρήση for, import, και οτιδήποτε δεν έχουμε πει! Hint:

```
list(range(1,10)) # --> [1,2,3,4,5,6,7,8,9]
```

```python
def f():
    def g(x):
        return x**2
    return list(map(g, range(10,101)))

print(f())
```

## 7
Φτιάξτε μία συνάρτηση η οποία θα παίρνει μία παράμετρο. Η παράμετρος θα είναι ένα string. Η συνάρτηση θα επιτρέφει το άθροισμα όλων των αριθμών που έχει η παράμετρος. Για παράδειγμα:

```
f('m1ts9s') # Επιστρέφει: 10 (1+9)
f('hel10 wor19') # Επιστρέφει: 11 (1+0+1+9)  
```

```python
def f(x):
   def g(x):
      if x in '0123456789':
         return int(x)
      return 0   return sum(map(g,x))
```

```python
def f(x):
   def g(x):
      return x in '0123456789'   return sum(map(int,filter(g,x)))
```

## 8
Φτιάξτε μία συνάρτηση η οποία θα παίρνει σαν παράμετρο 2 λίστες. Η πρώτη θα είναι λίστα από strings και η 2η λίστα από αριθμός. Η πρώτη λίστα θα περιέχει τα ονόματα των μαθητών μιας τάξης και η 2η τους βαθμούς τους, έτσι ώστε η ι-ιοστή θέση της κάθε λίστας να αναφέρεται στον ίδιο μαθητή. Οι λίστες δεν είναι ταξινομημένες ως προς κάτι. Η συνάρτηση θα επιστρέφει το όνομα του μαθητή που έχει τον μεγαλύτερο βαθμό.

Bonus: Κάντε το ίδιο απλά η συνάρτηση θα επιστρέφει τον βαθμό του μαθητή που είναι ο πρώτος αλφαβητικά. 


```python
def f(a,b):
    return b[a.index(max(a))] ##Epistrefei onoma

def g(a,b):
    return b[a.index(min(a))]##Epistrefei bathmo
```

## 9
Εδώ υπάρχουν δύο λίστες που περιέχουν τους πόντους στους τελικούς της Eurovision του 2018 και του 2019: 

```python
eur_2019 = [
	 ['Netherlands ', 498],
	 ['Italy ', 472],
	 ['Russia ', 370],
	 ['Switzerland ', 364],
	 ['Sweden ', 334],
	 ['Norway ', 331],
	 ['North Macedonia ', 305],
	 ['Azerbaijan ', 302],
	 ['Australia ', 284],
	 ['Iceland ', 232],
	 ['Czech Republic ', 157],
	 ['Denmark ', 120],
	 ['Cyprus ', 109],
	 ['Malta ', 107],
	 ['Slovenia ', 105],
	 ['France ', 105],
	 ['Albania ', 90],
	 ['Serbia ', 89],
	 ['San Marino ', 77],
	 ['Estonia ', 76],
	 ['Greece ', 74],
	 ['Spain ', 54],
	 ['Israel ', 35],
	 ['Belarus ', 31],
	 ['Germany ', 24],
	 ['United Kingdom ', 11],
]

​

eur_2018 = [
	 ['Israel ', 529],
	 ['Cyprus ', 436],
	 ['Austria ', 342],
	 ['Germany ', 340],
	 ['Italy ', 308],
	 ['Czech Republic ', 281],
	 ['Sweden ', 274],
	 ['Estonia ', 245],
	 ['Denmark ', 226],
	 ['Moldova ', 209],
	 ['Albania ', 184],
	 ['Lithuania ', 181],
	 ['France ', 173],
	 ['Bulgaria ', 166],
	 ['Norway ', 144],
	 ['Ireland ', 136],
	 ['Ukraine ', 130],
	 ['Netherlands ', 121],
	 ['Serbia ', 113],
	 ['Australia ', 99],
	 ['Hungary ', 93],
	 ['Slovenia ', 64],
	 ['Spain ', 61],
	 ['United Kingdom ', 48],
	 ['Finland ', 46],
	 ['Portugal ', 39],
 ]

```

* Βρείτε τις χώρες που συμμετείχαν και στους 2 τελικούς
* Από αυτές τις χώρες, ποια έχει το μεγαλύτερα άθροισμα πόντων; 

```python


def f(x):
    return x[0]

countries_2018 = list(map(f, eur_2018))
countries_2019 = list(map(f, eur_2019))

def g(x):
    return x in countries_2019


common = list(filter(g, countries_2018))
print (common)

​
def h(x):
    index_2018 = countries_2018.index(x)
    index_2019 = countries_2019.index(x)
    total = eur_2018[index_2018][1] + eur_2019[index_2019][1]

    return total

print (max(common, key=h))


```

## 10
Φτιάξτε μία συνάρτηση η οποία θα παίρνει μία παράμετρο. Η παράμετρος θα είναι μία λίστα με ακέραιους. Η συνάρτηση θα επιστρέφει True αν το πλήθος από ζυγούς αριθμούς που έχει η λίστα είναι μονός αριθμός, και False αν το πλήθος από ζυγούς είναι ζυγός αριθμός.

```python
def f(l):
    def is_even(k):
        return k % 2 == 0
    return not is_even(sum(map(is_even, l)))
```

## 11
Δίνονται οι παρακάτω λίστες:

```python
a = [0.05, 0.59, 0.89, 0.15, 0.93, 0.37, 0.07, 0.58, 0.17, 0.15, 0.66, 0.9, 0.17, 0.57, 0.73, 0.76, 0.97, 0.38, 0.06, 0.38]
b = [0.26, 0.98, 0.79, 0.35, 0.44, 0.5, 0.76, 0.42, 0.13, 0.63, 0.1, 0.47, 0.77, 0.17, 0.64, 0.77, 0.24, 0.47, 0.98, 0.6]
```

Επίσης δίνεται η συνάρτηση: ```f(a,b) = a*b - a + b - 1```

Έστω το στοιχείο x το οποίο υπάρχει στη θέση i στην a

Έστω το στοιχείο y το οποίο υπάρχει στη θέση j στην b.

Για όλα τα δυνατά ζευγάρια x,y τέτοια ώστε i==j ποιο είναι αυτό για το οποίο η f(x,y) έχει τη μικρότερη απόσταση από το 0;

```python
a = [0.05, 0.59, 0.89, 0.15, 0.93, 0.37, 0.07, 0.58, 0.17, 0.15, 0.66, 0.9, 0.17, 0.57, 0.73, 0.76, 0.97, 0.38, 0.06, 0.38]
b = [0.26, 0.98, 0.79, 0.35, 0.44, 0.5, 0.76, 0.42, 0.13, 0.63, 0.1, 0.47, 0.77, 0.17, 0.64, 0.77, 0.24, 0.47, 0.98, 0.6]

def f(x,y):
    return x*y - x + y - 1

def g(x,y):
    return [abs(f(x,y)), x,y]min(map(g,a,b))[1:]
```

## 12 
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

print(len([1 for s in shoes for j in jeans for sh in shirts if s+j+sh<=100]))
```

```python
print(sum(s+j+sh<=100 for s in shoes for j in jeans for sh in shirts))
```
