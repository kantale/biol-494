# ΒΙΟΛ-494

Σε αυτό το site θα βρείτε πληροφορίες και διαλέξεις για το μάθημα εαρινού εξαμήνου: **ΒΙΟΛ-494. Εισαγωγή στον Προγραμματισμό**, του Τμήματος Βιολογίας του Πανεπιστημίου Κρήτης.

### Διδάσκοντας
* [Αλέξανδρος Καντεράκης](https://www.ics.forth.gr/cbml/person/kanterakis/alexandros%C2%A0)
* email: [kantale@ics.forth.gr](mailto:kantale@ics.forth.gr)

### Ώρες Μαθήματος 
* Τετάρτη, 12:00-14:00 
* Αμφ. B

### Slack
Το κύριο μέσο επικοινωνίας με τον διδάσκοντα αλλά και μεταξύ των φοιτητών είναι το περιβάλλον slack. Για να συνδεθείτε στο slack θα πρέπει να πατήσετε ένα invitation link το οποία θα σας σταλεί. Στο πρώτο μάθημα θα ζητήσω τα ιδρυματικά σας μέιλ σε μία κόλλα. Σε αυτά τα μέιλ θα στείλω ένα invitation link με το οποίο θα μπορείτε να συνδεθείτε στο slack του μαθήματος. Μπορείτε επίσης να στείλετε ένα μείλ σε [εμένα](mailto:kantale@ics.forth.gr) από το ιδρυματικό σας μέιλ στο οποίο να φαίνεται το ΑΜ σας και σε αυτό θα στείλω το invitation link. Όταν συνδεθείτε με το slack μπορείτε να χρησιμοποιήσετε όποιο μέιλ θέλετε (ιδρυματικό ή μη). Θα πρέπει όμως στο slack να φαίνεται το όνομα ή/και το ΑΜ σας (στo profile). Μπορείτε επίσης (δεν είναι υποχρεωτικό!) να κατεβάσετε και την εφαρμογή του slack στο κινητό σας. 

### Περιγραφή
Το μάθημα αποτελεί μια εισαγωγή στις αρχές του προγραμματισμού Η/Υ με έμφαση στην εκμάθηση σε βασικό επίπεδο της γλώσσας προγραμματισμού Python. H διδασκόμενη ύλη ξεκινά με μια θεωρητική εισαγωγή στις έννοιες των αλγορίθμων και θεωρητικών τεχνικών πριν περάσει σε επιμέρους στοιχεία της γλώσσας προγραμματισμού python. 
Η διδασκαλία γίνεται με τρόπο τέτοιο ώστε οι διδασκόμενες γνώσεις να εφαρμόζονται σε υπαρκτά προβλήματα ανάλυσης βιολογικών/γονιδιωματικών αλληλουχιών.
Με την επιτυχή ολοκλήρωση του μαθήματος ο φοιτητής / τρια θα είναι σε θέση να:
* Σχεδιάσει και να υλοποιήσει απλούς αλγόριθμους ανάλυσης γονιδιωματικών αλληλουχιών αλλά και άλλων βιολογικών δεδομένων.    
* Να χρησιμοποιήσει έτοιμα προγράμματα και βιβλιοθήκες ανάλυσης βιολογικών δεδομένων (biopython, pandas).
* Nα προσπελάσει βιολογικές βάσεις δεδομένων και να εφαρμόσει απλή στατιστική ανάλυση.
* Nα αναπαραστήσει γραφικά βιολογικά δεδομένα σε Matplotlib / bokeh / seaborn.

**Η παρακολούθηση δεν είναι υποχρεωτική**

### Προηγούμενες χρονιές
* 2022
   * [Σημειώσεις για το μάθημα](README_2022.md)
   * [Ασκήσεις](exercises_2022.md)
   * [projects](biol_494_2022_projects.ipynb)
* 2021 
   * [Σημειώσεις για το μάθημα](README_2021.md)
   * [Ασκήσεις](exercises_2021.md)
   * [projects](projects_2021/)

### Ποια python να βάλω (και πως);
Η ελάχιστη έκδοση της python που απαιτείται για τα μαθήματα είναι η 3.6 . Προφανώς προτείνεται να εγκαταστήσετε τη πιο πρόσφατη έκδοση. Ο προτεινόμενος τρόπος εγκατάστασης είναι μέσω του [conda](https://docs.conda.io/en/latest/). Υπάρχουν 2 τρόποι για να εγκαταστήσετε τη python μέσω του συστήματος διαχείρησης πακέτων, conda. Είτε μέσω της [Anaconda](https://www.anaconda.com/) είτε μέσω της [miniconda](https://docs.conda.io/en/latest/miniconda.html). Για μία σχετική συζήτησε για τα πλεονεκτήματα/μειονεκτήματα της κάθε επιλογής δείτε [εδώ](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html). Η Anaconda είναι ίσως η πιο "εύκολη" επιλογή η οποία απαιτεί λιγότερο εξειδικευμένες γνώσης και περιλαμβάνει ένα τεράστιο πλήθος από χρήσιμες βιβλιοθήκες. Το μειονέκτημά της είναι ότι έχει αρκετές υπολογιστικές απαιτήσεις. Η miniconda, όπως λέει και το όνομά της, περιέχει μόνο τα ελάχιστα προγράμματα που απαιτούνται για να εγκαταστήσετε conda αλλά και τη τελευταία python. Παρόλα αυτά η miniconda σου επιτρέπει (μέσω του conda) να στήσεις το προγραμματιστικό περιβάλλον του υπολογιστή σου με ό,τι πακέτα θέλεις. Πολλοί που εγκαθιστούν τη python σε υπερυπολογιστικά συστήματα προτιμούν τη miniconda. 

Αν έχετε μπερδευτεί διαβάστε [αυτό τον απόλυτο οδηγό των conda, anaconda, miniconda](https://whiteboxml.com/blog/the-definitive-guide-to-python-virtual-environments-with-conda) 

* Tutorials για την εγκατάσταση της anaconda:
   * [Python Tutorial: Anaconda - Installation and Using Conda](https://www.youtube.com/watch?v=YJC6ldI3hWk)
   * [How to Set Up Your Data Science Environment (Anaconda Beginner)](https://www.youtube.com/watch?v=C4OPn58BLaU)
* Tutorials για την εγκατάσταση της miniconda:
   * [Installation of miniconda](https://www.youtube.com/watch?v=XCvgyvBFjyM)
   * [A very nice tutorial and presentation of the differences between anaconda / miniconda](https://www.youtube.com/watch?v=clKgaEZJYww])

### Διαλέξεις / Σημείωσεις 
* Διάλεξη 1η . 8 Φεβρουαρίου 2023 . Basics . [jupyter notebook](notes/python_basics.ipynb), [markdown](notes/python_basics.md), [pdf](notes/python_basics.pdf)
   * [Πρόχειρες σημειώσεις της διάλεξης σε φορμάτ jupyter notebook](https://gist.github.com/kantale/3b30f822832303e8b146bdcdae722e0e)
* Διάλεξη 2η . 15 Φεβρουαρίου 2023 . [Εγκατάσταση jupyter, σημείωσεις στα Αγγλικά](install_python.md) 
   * [Πρόχειρες σημειώσεις της διάλεξης σε φορμάτ jupyter notebook](https://gist.github.com/kantale/fc7b58c53a306df95cb57a091eeebaf7)
* Διάλεξη 3η . 22 Φεβρουαρίου 2023 . functions , if . [jupyter notebook](notes/python_vars_if_functions.ipynb), [markdown](notes/python_vars_if_functions.md), [pdf](notes/python_vars_if_functions.pdf)
   * [Πρόχειρες σημειώσεις της διάλεξης σε φορμάτ jupyter notebook](https://gist.github.com/kantale/b883aaff3d66faf24b04b021e68392aa)
* Διάλεξη 4η . 1 Μαρτίου 2023 . lists . [jupyter notebook](notes/python_lists.ipynb), [markdown](notes/python_lists.md), [pdf](notes/python_lists.pdf)
   * [Πρόχειρες σημειώσεις της διάλεξης σε φορμάτ jupyter notebook](https://gist.github.com/kantale/4483f5b1f39e424f739687f90ab2d4bf)
* Διάλεξη 5η . 15 Μαρτίου 2023 . for + list comprehension . [jupyter notebook](notes/python_list_comprehensions.ipynb), [markdown](notes/python_list_comprehensions.md), [pdf](notes/python_list_comprehensions.pdf)
   * [Πρόχειρες σημειώσεις της διάλεξης σε φορμάτ jupyter notebook](https://gist.github.com/kantale/2075c94409f23324a984fdad82cf9938)
* Διάλεξη 6η . 22 Μαρτίου 2023 . while + dictionary + tuples + sets . [jupyter notebook](notes/python_while_dictionary_tuples_sets.ipynb), [markdown](notes/python_while_dictionary_tuples_sets.md), [pdf](notes/python_while_dictionary_tuples_sets.pdf)
   * [Πρόχειρες σημειώσεις της διάλεξης σε φορμάτ jupyter notebook](https://gist.github.com/kantale/8e7353e9610ff328c09c771b6f5448df)
* Διάλεξη 7η . 29 Μαρτίου 2023 . Files + lambda + variable scoping + ternary operator + pass . [jupyter notebook](notes/python_files_tern_lambda_sf_is.ipynb), [markdown](notes/python_files_tern_lambda_sf_is.md), [pdf](notes/python_files_tern_lambda_sf_is.pdf)
   * [Πρόχειρες σημειώσεις της διάλεξης σε φορμάτ jupyter notebook](https://gist.github.com/kantale/5f66193286572d946561d92977c4c81b)
* Διάλεξη 8η . 5 Απριλίου 2023 .
   * [Πρόχειρες σημειώσεις της διάλεξης σε φορμάτ jupyter notebook](https://gist.github.com/kantale/558fc14a2f917439c4688764fb3c3931)
* Διάλεξη 9η . 26 Απριλίου 2023 . Generators + Import + Command Line + Exceptions + random + collections . [jupyter notebook](notes/python_gen_imp_cons_exc.ipynb), [markdown](notes/python_gen_imp_cons_exc.md), [pdf](notes/python_gen_imp_cons_exc.pdf)
   * [Πρόχειρες σημειώσεις της διάλεξης σε φορμάτ jupyter notebook](https://gist.github.com/kantale/b70cdcdfb8f3aeb2bfb06e90b7b0bf2c)
* Διάλεξη 10η. 3η Μαΐου 2023.  Serialization + Itertools + Regular Expressions. [jupyter notebook](notes/python_ser_iter_re.ipynb), [markdown](notes/python_ser_iter_re.md), [pdf](notes/python_ser_iter_re.pdf)
   * [Πρόχειρες σημειώσεις της διάλεξης σε φορμάτ jupyter notebook](https://gist.github.com/kantale/18eb3ce7ae124d202fdd241e11f332e3)

### Μελλοντικές διαλέξεις
* Διάλεξη 11η . 
   * pandas . [jupyter notebook](notes/python_pandas.ipynb), [markdown](notes/python_pandas.zip), [pdf](notes/python_pandas.pdf), [html](notes/python_pandas.html)
   * numpy . [jupyter notebook](notes/python_numpy.ipynb), [markdown](notes/python_numpy.zip), [pdf](notes/python_numpy.pdf), [html](notes/python_numpy.html) 
* Διάλεξη 12η  . matplotlib - plotting . [jupyter notebook](notes/python_matplotlib.ipynb), [markdown](notes/python_matplotlib.zip), [pdf](notes/python_matplotlib.pdf), [html](notes/python_matplotlib.html)
* Διάλεξη 13η . classes . [jupyter notebook](notes/python_classes.ipynb), [markdown](notes/python_classes.md), [pdf](notes/python_classes.pdf), [html](notes/python_classes.html)



### Βαθμολόγηση
Ο τελικός βαθμός του μαθήματος θα είναι το 33.3% των βαθμών από τις ασκήσεις, το 33.3% των βαθμών από το project και το υπόλοιπο 33.4% από το τελικό διαγώνισμα στο τέλος του τριμήνου. 

#### Ασκήσεις
[Το αρχείο με τις ασκήσεις βρίσκεται εδώ](exercises_2023.md)

Στο τέλος κάθε διάλεξης θα ανεβαίνουν 7-10 ασκήσεις σχετικά με την ύλη που παρουσιάστηκε στη διάλεξη. 

Συνολικά θα ανέβουν 100 ασκήσεις. Οι ασκήσεις είναι υποχρεωτικές και μετράνε στο 33.3% του βαθμού. Όλες οι ασκήσεις είναι βαθμολογικά ισοδύναμες. Οι ημερομηνίες παράδοσης των ασκήσεων είναι:

* Οι ασκήσεις 1-20 έχουν διορία μέχρι 15 Μαρτίου 2023. 
* Οι ασκήσεις 21-40 έχουν διορία μέχρι 5 Απριλίου 2023.
* Οι ασκήσεις 41-60 έχουν διορία μέχρι 23 Απριλίου 2023.  
* Οι ασκήσεις 61-80 έχουν διoρία μέχρι 17 Μαΐου 2023.
* Οι ασκήσεις 81-100 έχουν διορία μέχρι ΤΒΑ.


Η ώρα που λήγει η διορία είναι η 23:59 της αντίστοιχης μέρας στο Time Zone [Anywhere on Earth](https://time.is/Anywhere_on_Earth).

**Πως παραδίνουμε τις ασκήσεις**: Πριν το τέλος της διορίας παράδοσης στέλνουμε ένα μέιλ στο [kantale@ics.forth.gr](mailto:kantale@ics.forth.gr) με τις λύσεις των ασκήσεων μας. **Στέλνουμε από το ιδρυματικό μας (@edu.biology.uoc.gr) μέιλ**, εκτός αν δεν έχετε (έχετε πάρει το μάθημα από άλλα ιδρύματα μετά από συνενόηση με μένα). Αν δεν έχετε ιδρυματικό μέιλ, καλό θα είναι να το αναφέρετε στο μέιλ σας. Κάτι σαν "Δεν έχω ιδρυματικό μέιλ και ΑΜ". Στο subject του μέιλ γράφουμε το ΑΜ, το όνομά μας και τον αριθμό των ασκήσεων που έχουμε λύσει. Για παράδειγμα: ```ΑΜ 1234, Κατερίνα Στανίση, Ασκήσεις 41-60```. Στο μέιλ βάζουμε τις λύσεις των ασκήσεων. Κάθε λύση πρέπει να έχει ένα σχόλιο σε python με τον αριθμό της άσκησης που λύνουμε σε αυτή τη μορφή: ```# Askhsh <Noumero>```. Για παράδειγμα:

```python

# Askhsh 54
print ("Hello!")

# Askhsh 55
print ("This is the solution for ex. 55")

```

Αν και αυτός είναι ο ενδεδειγμένος τρόπος, μπορείτε αν θέλετε να στείλετε και attachments με .py αρχεία ή .ipynb αρχεία. 
* Αν στείλετε .py αρχεία **πρέπει** να υπάρχει σε σχόλιο ο αριθμός της κάθε άσκησης (όπως και πριν)
* Αν στείλετε .ipynb αρχεία πρέπει να υπάρχει σε σχόλιο ο αριθμός της κάθε άσκησης **μέσα στο κελί που έχει τη λύση** και όχι σε κελί με markdown. 

Για να αποθηκεύσετε μία σειρά ασκήσεων σε .ipynb ή σε .py φορμάτ, πηγαίντε στο Jupyter , File --> Download as -> Python (ή Notebook) και στείλτε μου το σαν συνημμένο:
![img](https://i.imgur.com/jm2tmHm.png) 

Αυτά γίνονται γιατί υπάρχει [σκριπτάκι](grade.py) που αναλύει αυτόματα τις ασκήσεις σας. Ο βαθμός σας θα σας αποσταλεί με μέιλ περίπου 2 εβδομάδες μετά που στείλετε τις ασκήσεις. 

**ΠΡΟΣΟΧΗ! Δεν στέλνουμε:**
* Αρχεία σε pdf, Microdoft word, LibreOffice, Google Docs (είναι για κείμενα, όχι για κώδικα)
* Συμπιεσμένα αρχεία
* Screenshots

#### Πως βαθμολογούνται οι ασκήσεις
Για κάθε άσκηση παίρνετε βαθμό: από 0 μέχρι 10. Όλες οι ερωτήσεις/ασκήσεις θεωρούνται ισοδύναμες. 

0. Δεν παραδώσατε κάτι..
1. Η άσκηση βγάζει λάθος αποτέλεσμα και κάποια ψήγματα υλοποίησης έχουν γίνει.
2. Η άσκηση βγάζει λάθος αποτέλεσμα αλλά έχει υλοποιηθεί ένα μικρό κομμάτι της λύσης.
3. Η άσκηση βγάζει λάθος αποτέλεσμα αλλά έχει υλοποιηθεί ένα σημαντικό κομμάτι της λύσης.
4. Η άσκηση βγάζει λάθος αποτελέσματα λόγω πολύ σημαντικών λαθών στη λογική.
5. Η άσκηση βγάζει λάθος αποτέλεσμα λογω λαθών στη λογική
6. Η άσκηση βγάζει λάθος αποτέλεσμα λόγω μικρών λαθών στη λογική. 
7. H άσκηση βγάζει σωστό αποτέλεσμα, αλλά όχι για όλα τα πιθανά σενάρια/inputs. 
8. Η άσκηση βγάζει σωστό αποτέλεσμα, αλλά η λογική σας έχει κάποιο λάθος (συμβαίνει πολλές φορές..). 
9. Η άσκηση βγάζει σωστό αποτέλεσμα, αλλά υπάρχει μία προφανής πιο γρήγορη/σύντομη λύση.
10. Η άσκηση είναι αλάνθαστη. Μπράβο!


### Projects
[Οι εκφωνήσεις των projects βρίσκονται εδώ](projects_2023.ipynb) 

* Τα projects θα παραδοθούν με τον ίδιο τρόπο όπως οι ασκήσεις,
* Τα projects μετράνε για το 33.3% του τελικού βαθμού.
* Η ημερομηνία παράδοσης των projects είναι μέχρι τη μέρα που θα δοθεί η τελική εξέταση του μαθήματος 23:59, Anywhere on Earth.


#### Τελικό διαγώνισμα.
Το τελικό διαγώνισμα μετράει στο 33.4% του βαθμού. Θα δοθούν οδηγίες αργότερα για τον τρόπο εξέταση και τη γενικότερη δομή των θεμάτων.

* [Θέματα εξέτασης Ιουνίου 2022](final_2022_may.ipynb)

### Εξεταστική Σεπτεμβρίου 
Η διαδιακασία εξέτασης στην εξεταστική του Σεπτεμβρίου θα είναι η ίδια με αυτή του Ιουνίου. Δηλαδή στην αίθουσα υπολογιστών. **Οι ασκήσεις και τα projects μετράνε και για τον Σεπτέμβρη. Δηλαδή ο βαθμός του Σεπτέμβρη θα μετρήσει για το 34% του τελικού**. 

### Επιπλέον υλικό:
* Official Documentation / General links
   * [Python documentation](https://docs.python.org/3/)
   * [The official Python Tutorial](https://docs.python.org/3/tutorial/index.html)
   * [Wikipedia](https://en.wikipedia.org/wiki/Python_%28programming_language%29)
* Courses / Books / Textbooks 
   * [CS61A: Online Textbook ](https://inst.eecs.berkeley.edu//~cs61a/sp12/book/). Ευχαριστώ τον Ιωάννη-Ραφαήλ Τζονευράκη για το link. 
   * [Python Computing for Data Science](https://github.com/profjsb/python-seminar)
   * [EbookFoundation free-programming-books on python](https://github.com/EbookFoundation/free-programming-books/blob/master/free-programming-books.md#python)
   * [Learn Python with Jupyter by Serena Bonaretti](https://learnpythonwithjupyter.com/assets/book/learn_python_with_jupyter.pdf)
* Running python
   * [Google Colab](https://colab.research.google.com/notebooks/intro.ipynb)
* Cheatsheets 
   * [pythoncheatsheet](https://www.pythoncheatsheet.org/) . Πολύ καλό και "συμπαγές" σημείο αναφοράς. Χρήσιμο όταν έχεις ξεχάσει πως γίνεται κάτι.
   * [Scientific Python Cheatsheet](https://ipgp.github.io/scientific_python_cheat_sheet/) 
   * [Matplotlib Cheatsheet](https://twitter.com/magnumdessert/status/1280543694760710144)
* For Beginners
   * [A beginner's python tutorial](https://en.wikibooks.org/wiki/A_Beginner%27s_Python_Tutorial)
   * [A Python course that takes beginners seriously](https://github.com/JdeH/LightOn)
   * [Beginner's Python Cheat Sheets](https://ehmatthes.github.io/pcc_2e/cheat_sheets/cheat_sheets/)
   * [Practical Python Programming from David Beazley](https://dabeaz-course.github.io/practical-python/)
   * [Automate the Boring Stuff with Python](https://automatetheboringstuff.com/) Practical programming for total beginners. Written by Al Sweigart. Free to read under a Creative Commons license.
* More advanced  
   * [Python: Notes for professionals book](https://books.goalkicker.com/PythonBook/)
   * [Non-beginner's python cheat sheet](https://gto76.github.io/python-cheatsheet/)
   * [Python Programming And Numerical Methods: A Guide For Engineers And Scientists](https://pythonnumericalmethods.berkeley.edu/notebooks/Index.html)
   * [Python & APIs: A Winning Combo for Reading Public Data](https://realpython.com/python-api/)
   * [Recursion in Python: An Introduction](https://realpython.com/python-recursion/)
   * [One a Day One Liners with Python](https://python.plainenglish.io/one-a-day-one-liners-with-python-week-3-d0a5c8229183)
   * [Python Classes: The Power of Object-Oriented Programming](https://realpython.com/python-classes/)
* Challenges: 
   * https://www.hackerrank.com/dashboard
   * https://stepik.org  
   * http://rosalind.info/problems/locations/ 
   * https://www.spoj.com/problems/classical/ 
   * https://github.com/microsoft/PythonProgrammingPuzzles 
   * https://projecteuler.net/ 
* NumPy
   * [NumPy Tutorial](https://realpython.com/numpy-tutorial/)
   * [NumPy: the absolute basics for beginners](https://numpy.org/devdocs/user/absolute_beginners.html)
   * [NumPy Illustrated: The Visual Guide to NumPy](https://medium.com/better-programming/numpy-illustrated-the-visual-guide-to-numpy-3b1d4976de1d), from Lev Maximov 
   * [Linear Algebra in Python: Matrix Inverses and Least Squares](https://realpython.com/python-linear-algebra/)
   * [Cheatsheet 1](https://s3.amazonaws.com/assets.datacamp.com/blog_assets/Numpy_Python_Cheat_Sheet.pdf)
   * [Cheatsheet 2](https://s3.amazonaws.com/dq-blog-files/numpy-cheat-sheet.pdf)
* Scipy
   * [Paper στο Nature για το scipy](https://www.nature.com/articles/s41592-019-0686-2) published: 3 February 2020
   * [scipy lectures](http://scipy-lectures.org/)
* Pandas:
   * [Cheatsheet](https://pandas.pydata.org/Pandas_Cheat_Sheet.pdf)
   * [Introduction to Pandas](https://realpython.com/pandas-dataframe/) . [plotting with pandas](https://realpython.com/pandas-plot-python/)
   * [100 pandas puzzles](https://github.com/ajcr/100-pandas-puzzles)
* Plotting
   * [Visualizing Data in Python Using plt.scatter()](https://realpython.com/visualizing-python-plt-scatter/)
* Regular Expressions
   * [Python Regex Cheatsheet](https://www.debuggex.com/cheatsheet/regex/python)
   * Debugging 
      * https://www.debuggex.com/
      * https://regexr.com/
* Jupyter
   * [Jupyter notebooks for teaching/learning Python 3](https://github.com/jerry-git/learn-python3)
   * Γιατί jupyter; https://www.nature.com/articles/d41586-018-07196-1 
   * [28 Jupyter Notebook tips, tricks and shortcuts - Dataquest](https://www.dataquest.io/blog/jupyter-notebook-tips-tricks-shortcuts/).  Ευχαριστώ τον Thimo Kristani για το link. 
* Tips & Tricks
   * 100 Helpful Python Tips You Can Learn Before Finishing Your Morning Coffee https://towardsdatascience.com/100-helpful-python-tips-you-can-learn-before-finishing-your-morning-coffee-eb9c39e68958 
* Forums & QAs 
   * https://www.reddit.com/r/bioinformatics/ 
   * https://bioinformatics.stackexchange.com/ 
   * https://www.biostars.org/ 



