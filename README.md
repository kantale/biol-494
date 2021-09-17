# ΒΙΟΛ-494

Σε αυτό το site θα βρείτε πληροφορίες και διαλέξεις για το μάθημα εαρινού εξαμήνου: **ΒΙΟΛ-494. Εισαγωγή στον Προγραμματισμό**, του Τμήματος Βιολογίας του Πανεπιστημίου Κρήτης.

### Διδάσκοντας
* [Αλέξανδρος Καντεράκης](https://www.ics.forth.gr/cbml/person/kanterakis/alexandros%C2%A0)
* email: [kantale@ics.forth.gr](mailto:kantale@ics.forth.gr)

### Ώρες Μαθήματος 
* Τετάρτη, 17:00-19:00
* Αμφ. Α

### Slack
Το κύριο μέσο επικοινωνίας με τον διδάσκοντα αλλά και μεταξύ των φοιτητών είναι το περιβάλλον slack: biol-494.slack.com . Σας έχει σταλεί ένα link με το οποίο μπορείτε να μπείτε (invite). Μπορείτε να γραφτείτε με όποιο μέιλ θέλετε (ιδρυματικό ή μη). Μπορείτε επίσης (δεν είναι υποχρεωτικό!) να κατεβάσετε και την εφαρμογή του slack στο κινητό σας. 

### Περιγραφή
Το μάθημα αποτελεί μια εισαγωγή στις αρχές του προγραμματισμού Η/Υ με έμφαση στην εκμάθηση σε βασικό επίπεδο της γλώσσας προγραμματισμού Python. H διδασκόμενη ύλη ξεκινά με μια θεωρητική εισαγωγή στις έννοιες των αλγορίθμων και θεωρητικών τεχνικών όπως τα διαγράμματα ροής και ο σχεδιασμός προγραμμάτων με ψευδοκώδικα πριν περάσει σε επιμέρους στοιχεία της γλώσσας προγραμματισμού python. 
Η διδασκαλία γίνεται με τρόπο τέτοιο ώστε οι διδασκόμενες γνώσεις να εφαρμόζονται σε υπαρκτά προβλήματα ανάλυσης βιολογικών/γονιδιωματικών αλληλουχιών.
Με την επιτυχή ολοκλήρωση του μαθήματος ο φοιτητής / τρια θα είναι σε θέση να:
* Σχεδιάσει και να υλοποιήσει απλούς αλγόριθμους ανάλυσης γονιδιωματικών αλληλουχιών αλλά και άλλων βιολογικών δεδομένων.    
* Να χρησιμοποιήσει έτοιμα προγράμματα και βιβλιοθήκες ανάλυσης βιολογικών δεδομένων (biopython, pandas).
* Nα προσπελάσει βιολογικές βάσεις δεδομένων και να εφαρμόσει απλή στατιστική ανάλυση.
* Nα αναπαραστήσει γραφικά βιολογικά δεδομένα σε Matplotlib / bokeh / seaborn

### Ποια python να βάλω (και πως);
Η ελάχιστη έκδοση της python που απαιτείται για τα μαθήματα είναι η 3.6 . Προφανώς προτείνεται να εγκαταστήσετε τη πιο πρόσφατη έκδοση. Ο προτεινόμενος τρόπος εγκατάστασης είναι μέσω του [conda](https://docs.conda.io/en/latest/). Υπάρχουν 2 τρόποι για να εγκαταστήσετε τη python μέσω του συστήματος διαχείρησης πακέτων, conda. Είτε μέσω της [Anaconda](https://www.anaconda.com/) είτε μέσω της [miniconda](https://docs.conda.io/en/latest/miniconda.html). Για μία σχετική συζήτησε για τα πλεονεκτήματα/μειονεκτήματα της κάθε επιλογής δείτε [εδώ](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html). Η Anaconda είναι ίσως η πιο "εύκολη" επιλογή η οποία απαιτεί λιγότερο εξειδικευμένες γνώσης και περιλαμβάνει ένα τεράστιο πλήθος από χρήσιμες βιβλιοθήκες. Το μειονέκτημά της είναι ότι έχει αρκετές υπολογιστικές απαιτήσεις. Η miniconda, όπως λέει και το όνομά της, περιέχει μόνο τα ελάχιστα προγράμματα που απαιτούνται για να εγκαταστήσετε conda αλλά και τη τελευταία python. Παρόλα αυτά η miniconda σου επιτρέπει (μέσω του conda) να στήσεις το προγραμματιστικό περιβάλλον του υπολογιστή σου με ό,τι πακέτα θέλεις. Πολλοί που εγκαθιστούν τη python σε υπερυπολογιστικά συστήματα προτιμούν τη miniconda. 

Αν έχετε μπερδευτεί διαβάστε [αυτό τον απόλυτο οδηγό των conda, anaconda, miniconda](https://whiteboxml.com/blog/the-definitive-guide-to-python-virtual-environments-with-conda) 

* Tutorials για την εγκατάσταση της anaconda:
   * [Python Tutorial: Anaconda - Installation and Using Conda](https://www.youtube.com/watch?v=YJC6ldI3hWk)
   * [How to Set Up Your Data Science Environment (Anaconda Beginner)](https://www.youtube.com/watch?v=C4OPn58BLaU)
* Tutorials για την εγκατάσταση της miniconda:
   * [Installation of miniconda](https://www.youtube.com/watch?v=XCvgyvBFjyM)
   * [A very nice tutorial and presentation of the differences between anaconda / miniconda](https://www.youtube.com/watch?v=clKgaEZJYww])

### Διαλέξεις
* Διάλεξη 1η - 3 Φεβρουαρίου 2021 . [Εγκατάσταση jupyter, σημείωσεις στα Αγγλικά](install_python.md) 
* Διάλεξη 2η - 10 Φεβρουαρίου 2021 . Basics . [jupyter notebook](notes/python_basics.ipynb), [markdown](notes/python_basics.md), [pdf](notes/python_basics.pdf)
   * Οι **πρόχειρες** σημειώσεις της διάλεξης είναι διαθέσιμες ως [jupyter notebook](2021/draft_lesson_1.ipynb), [markdown](2021/draft_lesson_1.md), [html](2021/draft_lesson_1.html), [pdf](2021/draft_lesson_1.pdf)
* Διάλεξη 3η - 17 Φεβρουαρίου 2021 . functions , if . [jupyter notebook](notes/python_vars_if_functions.ipynb), [markdown](notes/python_vars_if_functions.md), [pdf](notes/python_vars_if_functions.pdf)
   * Οι **πρόχειρες** σημειώσεις της διάλεξης είναι διαθέσιμες ως [jupyter notebook](2021/draft_lesson_2.ipynb), [markdown](2021/draft_lesson_2.md), [html](2021/draft_lesson_2.html), [pdf](2021/draft_lesson_2.pdf)
* Διάλεξη 4η - 24 Φεβρουαρίου 2021 . lists . [jupyter notebook](notes/python_lists.ipynb), [markdown](notes/python_lists.md), [pdf](notes/python_lists.pdf)
   * Οι **πρόχειρες** σημειώσεις της διάλεξης είναι διαθέσιμες ως [jupyter notebook](2021/draft_lesson_3.ipynb), [markdown](2021/draft_lesson_3.md), [html](2021/draft_lesson_3.html), [pdf](2021/draft_lesson_3.pdf)
* Διάλεξη 5η - 3 Μαρτίου 2021 . for + list comprehension . [jupyter notebook](notes/python_list_comprehensions.ipynb), [markdown](notes/python_list_comprehensions.md), [pdf](notes/python_list_comprehensions.pdf)
   * Οι **πρόχειρες** σημειώσεις της διάλεξης είναι διαθέσιμες ως [jupyter notebook](2021/draft_lesson_4.ipynb), [markdown](2021/draft_lesson_4.md), [html](2021/draft_lesson_4.html), [pdf](2021/draft_lesson_4.pdf)
* Διάλεξη 6η - 10 Μαρτίου 2021 . while + dictionary + tuples + sets . [jupyter notebook](notes/python_while_dictionary_tuples_sets.ipynb), [markdown](notes/python_while_dictionary_tuples_sets.md), [pdf](notes/python_while_dictionary_tuples_sets.pdf)
   * Οι **πρόχειρες** σημειώσεις της διάλεξης είναι διαθέσιμες ως [jupyter notebook](2021/draft_lesson_5.ipynb), [markdown](2021/draft_lesson_5.md), [html](2021/draft_lesson_5.html), [pdf](2021/draft_lesson_5.pdf)
* Διάλεξη 7η - 17 Μαρτίου 2021 . Files + lambda + variable scoping + ternary operator + pass . [jupyter notebook](notes/python_files_tern_lambda_sf_is.ipynb), [markdown](notes/python_files_tern_lambda_sf_is.md), [pdf](notes/python_files_tern_lambda_sf_is.pdf)
   * Οι **πρόχειρες** σημειώσεις της διάλεξης είναι διαθέσιμες ως [jupyter notebook](2021/draft_lesson_6.ipynb), [markdown](2021/draft_lesson_6.md), [html](2021/draft_lesson_6.html), [pdf](2021/draft_lesson_6.pdf)
* Διάλεξη 8η - 24 Μαρτίου 2021 . Generators + Import + Command Line + Exceptions + random + collections . [jupyter notebook](notes/python_gen_imp_cons_exc.ipynb), [markdown](notes/python_gen_imp_cons_exc.md), [pdf](notes/python_gen_imp_cons_exc.pdf)
   * Οι **πρόχειρες** σημειώσεις της διάλεξης είναι διαθέσιμες ως [jupyter notebook](2021/draft_lesson_7.ipynb), [markdown](2021/draft_lesson_7.md), [html](2021/draft_lesson_7.html), [pdf](2021/draft_lesson_7.pdf)
* Διάλεξη 9η - 31 Μαρτίου 2021 . Serialization + Itertools + Regular Expressions. [jupyter notebook](notes/python_ser_iter_re.ipynb), [markdown](notes/python_ser_iter_re.md), [pdf](notes/python_ser_iter_re.pdf)
   * Οι **πρόχειρες** σημειώσεις της διάλεξης είναι διαθέσιμες ως [jupyter notebook](2021/draft_lesson_8.ipynb), [markdown](2021/draft_lesson_8.md), [html](2021/draft_lesson_8.html), [pdf](2021/draft_lesson_8.pdf)
* Διάλεξη 10η - 7 Απριλίου 2021 . pandas . [jupyter notebook](notes/python_pandas.ipynb), [markdown](notes/python_pandas.zip), [pdf](notes/python_pandas.pdf), [html](notes/python_pandas.html)
   * Οι **πρόχειρες** σημειώσεις της διάλεξης είναι διαθέσιμες ως [jupyter notebook](2021/draft_lesson_9.ipynb), [markdown](2021/draft_lesson_9.zip), [html](2021/draft_lesson_9.html), [pdf](2021/draft_lesson_9.pdf)
* Διάλεξη 11η - 14 Απριλίου 2021 . numpy . [jupyter notebook](notes/python_numpy.ipynb), [markdown](notes/python_numpy.zip), [pdf](notes/python_numpy.pdf), [html](notes/python_numpy.html)
   * Οι **πρόχειρες** σημειώσεις της διάλεξης είναι διαθέσιμες ως [jupyter notebook](2021/draft_lesson_10.ipynb), [markdown](2021/draft_lesson_10.zip), [html](2021/draft_lesson_10.html), [pdf](2021/draft_lesson_10.pdf)
* Διάλεξη 12η - 21 Απριλίου 2021 . matplotlib - plotting . [jupyter notebook](notes/python_matplotlib.ipynb), [markdown](notes/python_matplotlib.zip), [pdf](notes/python_matplotlib.pdf), [html](notes/python_matplotlib.html)
   * Οι **πρόχειρες** σημειώσεις της διάλεξης είναι διαθέσιμες ως [jupyter notebook](2021/draft_lesson_11.ipynb), [markdown](2021/draft_lesson_11.zip), [html](2021/draft_lesson_11.html), [pdf](2021/draft_lesson_11.pdf)
* Διάλεξη 13η - 12 Μαΐου 2021 . classes . [jupyter notebook](notes/python_classes.ipynb), [markdown](notes/python_classes.md), [pdf](notes/python_classes.pdf), [html](notes/python_classes.html)
   * Οι **πρόχειρες** σημειώσεις της διάλεξης είναι διαθέσιμες ως [jupyter notebook](2021/draft_lesson_12.ipynb), [markdown](2021/draft_lesson_12.md), [html](2021/draft_lesson_12.html), [pdf](2021/draft_lesson_12.pdf)



### Βαθμολόγηση
Ο τελικός βαθμός του μαθήματος θα είναι το 33.3% των βαθμών από τις ασκήσεις, το 33.3% των βαθμών από το project και το υπόλοιπο 33.4% από το τελικό διαγώνισμα στο τέλος του τριμηνου. 

#### Ασκήσεις
Στο τέλος κάθε διάλεξης θα ανεβαίνουν εδώ 10 ασκήσεις σχετικά με την ύλη που παρουσιάστηκε στη διάλεξη. 

**[Οι ασκήσεις βρίσκονται εδώ](exercises.md)**

Συνολικά θα ανέβουν 100 ασκήσεις. Οι ασκήσεις είναι υποχρεωτικές και μετράνε στο 33.3% του βαθμού. Όλες οι ασκήσεις είναι βαθμολογικά ισοδύναμες. Οι ημερομηνίες παράδοσης των ασκήσεων είναι:
* Ασκήσεις  1-20 : 3 Μαρτίου 2021 
* Ασκήσεις 21-40 : 19 Μαρτίου 2021
* Ασκήσεις 41-60 : 4 Απριλίου 2021 
* Ασκήσεις 61-80 : 18 Απριλίου 2021 
* Ασκήσεις 81-90: 2 Μαΐου 2021 
* Ασκήσεις 91-100: ~31 Μαΐου 2021~ 30 Ιουνίου 2021  

Η ώρα που λήγει η διορία είναι η 23:59 της αντίστοιχης μέρας στο Time Zone [Anywhere on Earth](https://time.is/Anywhere_on_Earth).

Πως παραδίνουμε τις ασκήσεις: Πριν το τέλος της διορίας παράδοσης στέλνουμε ένα μέιλ στο [kantale@ics.forth.gr](mailto:kantale@ics.forth.gr) με τις λύσεις των ασκήσεων μας. **Στέλνουμε από το ιδρυματικό μας (@edu.biology.uoc.gr) μέιλ**, εκτός αν δεν έχετε (έχετε πάρει το μάθημα από άλλα ιδρύματα μετά από συνενόηση με μένα). Αν δεν έχετε ιδρυματικό μέιλ, καλό θα είναι να το αναφέρετε στο μέιλ σας. Κάτι σαν "Δεν έχω ιδρυματικό μέιλ και ΑΜ". Στο subject του μέιλ γράφουμε το ΑΜ, το όνομά μας και τον αριθμό των ασκήσεων που έχουμε λύσει. Για παράδειγμα: ```ΑΜ 1234, Κατερίνα Στανίση, Ασκήσεις 41-60```. Στο μέιλ βάζουμε τις λύσεις των ασκήσεων. Κάθε λύση πρέπει να έχει ένα σχόλιο σε python με τον αριθμό της άσκησης που λύνουμε σε αυτή τη μορφή: ```# Askhsh <Noumero>```. Για παράδειγμα:

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
* Αρχεία σε pdf, doc (είναι για κείμενα, όχι για κώδικα)
* Συμπιεσμένα αρχεία
* Screenshots

#### Πως βαθμολογούνται οι ασκήσεις
Για κάθε άσκηση παίρνετε βαθμό: από 1 μέχρι 10. Όλες οι ερωτήσεις/ασκήσεις θεωρούνται ισοδύναμες. 

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
Πάλι σε αυτό το site μέχρι το τέλος του Απριλίου θα ανέβουν 10 projects. To projects θα περιέχουν υπαρκτά προβλήματα στη περιοχή της βιολογίας στα οποία καλείστε να απαντήσετε (ή να.. προσεγγίσετε) με python. Τα projects μπορείτε να τα πάρετε είτε σε ομάδες των 2 ατόμων είτε ατομικά. **Δεν θα βαθμολογηθούν ηπιότερα οι υλοποιήσεις των projects που έχουν γίνει ατομικά**. Δηλαδή όποιος πάρει ένα project ατομικά θα περιμένω να έχει δουλέψει για 2 άτομα! **Σε καμία περίπτωση δεν θα δοθεί ένα project σε ομάδα των τριών (ή περισσότερων) ατόμων**. Για τη διευκόλυνσή σας το κάθε project θα έχει χωριστεί σε 2 μέρη. Συνίσταται κάθε άτομο να κάνει από ένα μέρος (αν και δεν είναι υποχρεωτικό αυτό). 

Η παράδοση του κάθε project θα πρέπει να περιέχει:
* Τον κώδικα του project. Προτιμάται αρχείο/α σε .py τα οποία να μπορώ να τρέξω από τη command line.
* Mία αναφορά με 1000 - 1500 λέξεις με:
   * Μία εισαγωγική παράγραφο με τη βιολογική πλευρά και σημασία του προβλήματος/ερωτήματος.
   * Τη γενικότερη φιλοσοφία της λύσης / προσέγγισής σας. Πως δομήσατε τον κώδικα;
   * Τα αποτελέσματά σας.
   * Μία συζήτηση η οποία να περιέχει: Τι σας δυσκόλεψε; Πως κρίνετε τα αποτελέσματα; Τι θα μπορούσατε να κάνετε καλύτερα; Η βιβλιογραφία πως έχει αντιμετωπίσει αυτό το θέμα; Ποιες άλλες επεκτάσεις υπάρχουν για αυτό το πρόβλημα;
   * Η αναφορά θα πρέπει επίσης να έχει 1-2 προτάσεις που να αναφέρουν ποιο μέρος του project ανέλαβε το κάθε μέλος. 

Η υλοποίηση θα εξεταστεί με βάση:
* Καθαρός / ευανάγνωστος κώδικας (10%). Θα δοθούν σχετικές οδηγίες αργότερα. 
* Λύνει το πρόβλημα, ή δίνει μια καλή προσέγγιση (80%)
* Ποιότητα γραφικών παραστάσεων (5%)
* Αναφορά (5%)

Τα projects θα δοθούν με τη λογική "first come first serve" έτσι ώστε να μην πάρουν όλες οι ομάδες τα ίδια projects! Δηλαδή:
* ΠΡΩΤΑ θα στείλετε ένα μέιλ με τη σύσταση της ομάδας σας (ή ότι θέλετε να πάρετε ένα project ατομικά)
* ΜΕΤΑ θα δημοσιεύσω τα projects μαζί με τον μέγιστο αριθμό από ομάδες που μπορούν να τα πάρουν.
* ΜΕΤΑ θα στείλετε ένα μέιλ που να δηλώνετε ποιο project επιθυμείτε. Σε περίπτωση που το project που επιθυμείτε έχει.. καλυφθεί θα πρέπει να δηλώσετε κάποιο άλλο. 

Ημερομηνία παράδοσης των projects είναι ~31 Μαΐου 2021~ 30 Ιουνίου. Δηλαδή θα έχετε 2 μήνες (Μάιο-Ιούνιο) για να το υλοποιήσετε.

**Update**
Η εκφώνηση των projects έχει υλοποιηθεί και βρίσκεται στον κατάλογο [projects](projects/). Έκανα ότι μπορούσα ώστε όλα τα projects να έχουν την ίδια δυσκολία. Παρόλα αυτά δεν μπορώ να αποκλείσω το γεγονός ότι κάποια projects ίσως να είναι πιο δύσκολα. Για αυτό αν και στην αρχή σκόπευα να υπάρχει ο περιορισμός ότι ένα projects δεν μπορούν να το πάρουν περισσότερες από #ομάδες/10 ομάδες, αυτό δεν ισχύει. Ο περιορισμός λοιπόν είναι ο μαγικός αριθμός **10**. Δηλαδή δεν μπορούν να πάρουν τον ίδιο project παραπάνω από 10 ομάδες. Αυτό σημαίνει ότι ίσως κάποια projects να μην τα πάρει καμία ομάδα, το οποίο είναι απολύτως αποδεκτό. Το πλήθος από ομάδες είναι 25. 

#### Τελικό διαγώνισμα.
Το τελικό διαγώνισμα μετράει στο 33.4% του βαθμού. Υπάρχει μία πολύ μικρή περίπτωση να επιτραπεί η δια ζώσης εξέταση για αυτό έχω φτιάξει το εξής.. διάγραμμα ροής για τη τελική εξέταση:
* Αν επιτραπεί η δια ζώσης εξέταση (πολύ μικρή πιθανότητα..). Θα έχετε δύο επιλογές (ο καθένας δηλαδή μπορεί να διαλέξει). 
   * Ή να έρθετε με τα laptop σας και να λύσετε δύσκολα θέματα με ανοικτές σημειώσεις + Internet. Αν έρθετε με τα laptop σας φροντίστε η μπαταρία να μπορεί να διαρκέσει 3 ώρες! Δεν θα δεχτώ δικαιολογία του στυλ: "μου τελείωσε η μπαταρία".
   * Ή να λύσετε πιο εύκολα θέματα με κλειστές σημειώσεις σε μία κόλλα χαρτί. 
* Αν δεν επιτραπεί η δια ζώσης εξέταση (πιο πιθανό), τότε η εξέταση θα γίνει από το.. σπίτι σας με τον εξής τρόπο: Μία μέρα πριν την εξέταση θα σας δοθεί μία συνάρτηση σε python στην οποία βάζετε τον αριθμό μητρώου σας και επιστρέφει 10 τυχαίους αριθμούς χωρίς επανάληψη από το 1 μέχρι το 100. Την ώρα της εξέτασης θα σας δοθούν.. 100 θέματα! Εσείς Θα πρέπει να λύσετε τα 10 τα οποία έβγαλε η συνάρτηση μέσα σε 3 ώρες. **Δεν** θα πρέπει να έχετε ανοικτές κάμερες ή κάτι τέτοιο, επιτρέπεται το Internet, ανοικτές σημειώσεις κτλ.. Φυσικά δεν επιτρέπεται η.. αντιγραφή. 


**Update**
Τη Κυριακή 23 Μαΐου θα σας δοθεί μία συνάρτηση σε python. Η συνάρτηση θα παίρνει το ΑΜ σας (ή το μέιλ σας για όσους δεν έχετε ΑΜ) και θα επιστρέφει μία λίστα με 10 αριθμούς από το 1 μέχρι το 100. Μπορείτε να εισάγετε το ΑΜ σας είτε σαν string είτε σαν ακέραιο. H συνάρτηση θα σας σταλεί με μέιλ αλλά και από το slack. Η τελική εξέταση θα γίνει τη Δευτέρα στις 24 Μαΐου 2021. Στις 11:55 π.μ. στις 24 Μαΐου, θα σας στείλω ένα link το οποίο θα περιέχει 100 θέματα. Το link θα το στείλω με μέιλ αλλά και από το slack. Από τη στιγμή που το λάβετε μπορείτε να ξεκινήσετε να λύνετε τα 10 θέματα με τους αριθμούς που επέστρεψε η συνάρτηση που λάβατε τη Κυριακή. Έχετε περιθώριο μέχρι τις 15:05 να στείλετε ένα μέιλ στο kantale@ics.forth.gr με τις λύσεις σας. Ο τρόπος με τον οποίο θα στείλετε τις λύσεις είναι ακριβώς ίδιος με τις ασκήσεις. **Δεν ξεχνάμε να γράψουμε ένα σχόλιο με τον αριθμό της κάθε άσκησης που λύνουμε πριν από κάθε λύση**, για παράδειγμα: ```# άσκηση 68```. Πολλές ασκήσεις ΔΕΝ έχουν διορθωθεί και έχουν μηδενιστεί και είναι αυτό αιτία. Σε κάθε μέιλ που λαμβάνω θα απαντάω με ένα "οκ" όσο πιο γρήγορα μπορώ. 

Κατά τη διάρκεια της εξέτασης μπορείτε να ρωτάτε σχετικά με τα θέματα στο slack. **Απαγορεύεται να στέλνετε DMs κατά τη διάρκεια της εξέτασης. Αν στείλετε δεν θα απαντήσω.** Για να μη γίνει.. συνωστισμός στο slack έχουν δημιουργηθεί 10 κανάλια #1-10, #11-20, ..., #91-100. Θα στείλετε την απορία στο αντίστοιχο κανάλι του αριθμού της άσκησης/θέματος. Για παράδειγμα μία απορία για την άσκηση/θέμα #58 θα πάει στο κανάλι #51-60. 

### Εξεταστική Σεπτεμβρίου 
Η εξεταστική Σεπτεμβρίου θα γίνει τη Παρασκευή 24 Σεπτεμβρίου, 17:00 - 20:00. Η διαδικασία είναι ακριβώς ίδια με την εξεταστική του Μαΐου (δες παραπάνω). Υπάρχει όμως μία μεγάλη διαφορά. Μπορείτε να επιλέξετε μεταξύ των παρακάτω:

1. Λύνετε 10 τυχαία θέματα σε 3 ώρες και ο βαθμός σας μετράει για το 33.4% του τελικού βαθμού. 
2. Λύνετε 20 τυχαία θέματα σε 4 ώρες και ο βαθμός σας μετράει για το 100% του τελικού βαθμού. 

Στη συνάρτηση που θα σας δοθεί θα πρέπει να δώσετε 2 ορίσματα: το ΑΜ σας (ή το μέιλ σας για όσους δεν έχετε ΑΜ), και τον αριθμό τον θεμάτων που θέλετε (10 ή 20). Η συνάρτηση θα επιστρέψει 10 ή 20 τυχαίους αριθμούς τα οποία θα είναι και τα θέματα που θα πρέπει να λύσετε. 

* Αν επιλέξετε 10 θέματα θα πρέπει να στείλετε μέιλ με τις απαντήσεις σας μέχρι τις 20:05. 
* Αν επιλέξετε 20 θέματα θα πρέπει να στείλετε μέιλ με τις απαντήσεις σας μέχρι τις 21:05.
* Σύμφωνα με τον οδηγό σπουδών, αν συμμετέχετε στην εξεταστική του Σεπτεμβρίου, τότε ο βαθμός που θα διαμορφωθεί, θα είναι και ο τελικός. Αυτό σημαίνει ότι αν ο βαθμός που θα διαμορφωθεί (τελικός) από την εξεταστική του Σεπτεμβρίου είναι χειρότερος από τον βαθμό που διαμορφώθηκε μετά την εξεταστική του Μαΐου, τότε θα πάρετε τον βαθμό του Σεπτεμβρίου.





### Επιπλέον υλικό:
* Official Documentation / General links
   * [Python documentation](https://docs.python.org/3/)
   * [The official Python Tutorial](https://docs.python.org/3/tutorial/index.html)
   * [Wikipedia](https://en.wikipedia.org/wiki/Python_%28programming_language%29)
* Courses / Books / Textbooks 
   * [CS61A: Online Textbook ](https://inst.eecs.berkeley.edu//~cs61a/sp12/book/). Ευχαριστώ τον Ιωάννη-Ραφαήλ Τζονευράκη για το link. 
   * [Python Computing for Data Science](https://github.com/profjsb/python-seminar)
   * [EbookFoundation free-programming-books on python](https://github.com/EbookFoundation/free-programming-books/blob/master/free-programming-books.md#python)
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



