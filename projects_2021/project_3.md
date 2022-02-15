# Project 3
<!-- https://gist.github.com/kantale/81d7d728c22fb35d77112c3633e17389 -->


### Εισαγωγή
Θεωρούμε γνωστό ότι ο άνθρωπος είναι ένας διπλοειδής οργανισμός. Αυτό σημαίνει ότι κάθε χρωμόσωμα έχει δύο αντίγραφα.
Το ένα αντίγραφο το κληρονομούμε από τη μητέρα μας και το άλλο από τον πατέρα μας. Επίσης ο άνθρωπος έχει 2 φυλετικά χρωμοσώματα τα οποία για τους άντρες είναι διαφορετικά (XY) και για τις γυναίκες είναι ίδια (XX). Σε αυτή την εργασία δεν θα ασχοληθούμε με τα φυλετικά χρωμοσώματα. 

Οι διαφορετικές τιμές των νουκλεοτιδίων που υπάρχουν σε μία συγκεκριμένη θέση του γονιδιώματος ονομάζονται "αλληλόμορφα". Μέσω των πειραμάτων γονοτύπησης μπορούμε να "δούμε" ποια αλληλόμορφα έχει ένα άτομα σε διάφορες θέσεις του γονιδιώματος. Για παράδειγμα ο γονότυπος ενός ατόμου στη θέση 1.000.000 του χρωμοσώματος 1 μπορεί να είναι: ```A/C```. Στο παραπάνω παράδειγμα ο γονότυπος ```A/C``` σημαίνει ότι στο ένα σετ χρωμοσωμάτων στη θέση 1.000.000 του χρωμοσώματος 1 έχει ```Α``` ενώ στο άλλο σετ έχει ```C```. Στη συγκεκριμένη περίπτωση, όταν δηλαδή σε μία θέση στο γονιδίωμα υπάρχουν δύο αλληλόμορφα, λέμε ότι ο γονότυπος αυτός είναι *ετερόζυγος*. Ομοίως σε περίπτωση που σε μία θέση του γονιδιώματος υπάρχει ένα κοινό αλληλόμορφο, λέμε ότι στη θέση αυτή ο γονότυπος είναι *ομόζυγος*.

Όπως ξέρετε, κάθε άνθρωπος έχει μία μοναδική κατανομή γονότυπων (εκτός ίσως από τα μονοζυγωτικά δίδυμα). Επίσης, είναι πολύ ενδιαφέρον το γεγονός ότι πολύ σπάνια σε μία συγκεκριμένη περιοχή του γονιδιώματος να παρατηρούμε παραπάνω από 2 αλληλόμορφα μεταξύ των γονοτύπων διαφορετικών ανθρώπων. Αυτό σημαίνει ότι αν σε έναν άνθρωπο παρατηρήσουμε τον γονότυπο ```A/C```, τότε με μεγάλη σιγουριά μπορούμε να πούμε ότι ένας τυχαίος άλλος άνθρωπος θα έχει είτε τον ίδιο γονότυπο είτε θα είναι ομόζυγος στο Α (```Α/Α```) είτε ομόζυγος στο C (```C/C```). Αυτού του τύπου η γονιδιακή διαφορά ονομάζεται διαλληλική (bi-allelic). Φυσικά υπάρχουν και τρι-αλληλικές αλλά και τετρα-αλληλικές διαφορές, αλλά δεν θα μας απασχολήσουν σε αυτή την εργασία. 

Όσο πιο κοντά είναι οι κοινοί πρόγονοι μεταξύ δύο ανθρώπων τόσο πιο πολλές ομοιότητες έχουν στο γωνιδίωμά τους. Αυτό σημαίνει ότι η πιθανότητα μεταξύ δύο ανθρώπων να "έχουν" τον ίδιο γονότυπο σε μία συγκεκριμένη διαλληλική θέση, είναι μεγαλύτερη ανάλογα με το πόσο "συγγενείς" είναι. Αυτή ακριβώς είναι και η βασική αρχή της πληθυσμιακής γενετικής η οποία μελετάει τη σχέση των ανθρώπων/πληθυσμών με βάση τις γενετικές τους διαφορές.

Σήμερα, μέσω των πειραμάτων γονοτύπησης αλλα και αλληλούχησης (sequencing), έχουμε βρει περίπου 1.000.000.000 περιοχές στο γονιδίωμα στις οποίες έχουμε παρατηρήσει να έχουν διαφορετικό γονότυπο τουλάχιστον δύο άνθρωποι. Αυτό σημαίνει ότι κατά τη διάρκεια του χρόνου έχουν συμβεί μεταλλάξεις οι οποίες έχουν "μεταφερθεί" σε μικρά ή μεγαλύτερα τμήματα του πληθυσμού. Οι μεταλλάξεις αυτές που αφορούν μία μοναδική θέση ονομάζονται SNPs (Single Nucleotide Polymorphisms). Ένα διαλληλικό SNP ορίζεται με βάση τα παρακάτω:
* Τη θέση του στο χρωμόσωμα 
* Το πρώτο αλληλόμορφο που παρατηρούμε
* Το δεύτερο αλληλόμορφο που παρατηρούμε

Για παράδειγμα στο χρωμόσωμα 16 και στη θέση 53786615, έχουμε παρατηρήσει ότι [υπάρχει ένα SNP](https://www.ncbi.nlm.nih.gov/snp/rs9939609) το οποίο έχει τα αλληλόμορφα Τ και Α.

Για κάθε SNP ορίζουμε τη συχνότητά του σε έναν πληθυσμό. Αυτή η συχνότητα είναι ο λόγος του πλήθους των αλληλόμορφων που βρίσκουμε στον πληθυσμό για αυτό το SNP προς το πλήθος όλων των αλληλόμορφων. Για παράδειγμα ας υποθέσουμε ότι έχουμε ένα SNP με δύο αλληλόμορφα A και C, και έναν πληθυσμό από 3 ανθρώπους:


| Άνθρωπος | Γονότυπος   |
|----------|-------------|
|  1  |       Α/Α        |
|  2  |       Α/Α        |
|  3  |       C/A        |

Στο παραπάνω SNP, η συχνότητα του Α είναι 5/6 και η συχνότητα του C είναι 1/6. Το ποια από τις δύο συχνότητες θα χρησιμοποιήσουμε για να ορίσουμε τη συχνότητα αυτού του SNP είναι μία παραδοχή που μπορούμε να κάνουμε. Μερικές φορές χρησιμοποιούμε το μικρότερο από τα δύο (1/6). Αυτός ο ορισμός ονομάζεται Minor Allele Frequency (MAF). Διαφορετικά μπορούμε να ορίσουμε από πριν κάποιο αλληλόμορφο ως το "κοινό", με βάση κάποιο γονιδίωμα το οποίο ονομάζουμε γονιδίωμα αναφοράς (reference genome) και να ορίσουμε τη συχνότητα του SNP ως τη συχνότητα του κοινού αλληλόμορφου. 

### Ανάλυση της κατανομής των πληθυσμών με βάση τον γονότυπο
Μέσα σε έναν πληθυσμό λοιπόν, κάθε SNP έχει μία συχνότητα. Οι διαφορές των συχνοτήτων αυτών μεταξύ δύο διαφορετικών πληθυσμών (π.χ Ιταλοί με Σουηδοί) μπορεί να μας δώσει πληροφορία για το πόσο κοντά γενετικά είναι οι πληθυσμοί αυτοί. Ευτυχώς για εμάς, υπάρχουν έτοιμες μέθοδοι που κάνουν ακριβώς αυτό το πράγμα. Ας τις δούμε λίγο πιο αναλυτικά. Ας υποθέσουμε ότι έχουμε γονοτυπήσει ένα σύνολο από 100 ανθρώπους σε 1000 διαφορετικές θέσεις του γονιδιώματος. Υποθέτουμε ότι και οι 100 ανήκουν στον ίδιο πληθησμό αλλά δεν είμαστε σίγουροι για αυτό. Για να το επιβεβαιώσουμε δημιουργούμε έναν πίνακα που περιέχει τους γονότυπους όλων των ατόμων:

| Άνθρωπος | Γονότυπος 1  | Γονότυπος 2  | Γονότυπος 3  | Γονότυπος 4  | ..  |  Γονότυπος 1000  |
|----------|--------------|--------------|-------------|---------------|----|-------------------|
|  1  |       A/A        |     C/T        |     A/A     |    C/C       | ..  |     T/T          |
|  2  |       A/C        |     C/C        |     A/T     |    C/G       | ..  |     G/T          |
|  3  |       A/A        |     C/T        |     A/T     |    C/G       | ..  |     G/T          |
|  ..  |      C/C        |     C/C        |     A/T     |    G/G       | ..  |     G/G          |
|  100  |     A/A        |     T/T        |     A/T     |    G/G       | ..  |     T/T          |

Στη συνέχεια μπορούμε να μετατρέψουμε τον παραπάνω πίνακα ώστε να έχει αριθμητικές τιμές. Για κάθε γραμμή, διαλέγουμε ένα αλληλόμορφο ως το "κοινό". Ένας ομόζυγος γονότυπος που έχει 2 κοινά το κωδικοποιούμε με 0, ένας ετερόζυγος γονότυπος κωδικοποιείται με 1 και ένας ομόζυγος που έχει δύο μη-κοινά κωδικοποιείται με 2. Αν κάνουμε τα παραπάνω και ορίσουμε (αυθαίρετα) το πρώτο αλληλόμορφο του πρώτου ανθρώπου ώς το "κοινό" τότε ο παραπάνω πίνακας γίνεται:

| Άνθρωπος | Γονότυπος 1  | Γονότυπος 2  | Γονότυπος 3  | Γονότυπος 4  | ..  |  Γονότυπος 1000  |
|----------|--------------|--------------|-------------|---------------|----|-------------------|
|  1  |       0        |     1        |     0     |    0       | ..  |     0          |
|  2  |       1        |     0        |     1     |    1       | ..  |     1          |
|  3  |       0        |     1        |     1     |    1       | ..  |     1          |
|  ..  |      2        |     0        |     1     |    2       | ..  |     2          |
|  100  |     0        |     2        |     1     |    2       | ..  |     0          |

Αυτός ο πίνακας έχει 100 δείγματα με 1000 τιμές ο κάθε ένας. Είναι δηλαδή 100 αντικείμενα στον 1000-διάστατο χώρο. Πως μπορούμε να προβάλουμε τον πίνακα αυτό στον διδιάστατο χώρο έτσι ώστε να φαίνοναι οι αποστάσεις μεταξύ των ανθρώπων; Αυτό ακριβώς κάνει η μέθοδος [PCA (Principal Component Analysis)](https://en.wikipedia.org/wiki/Principal_component_analysis) και ευτυχώς για εσάς θα σας δοθεί έτοιμη μέθοδος στη python η οποία την υλοποιεί. Ας δούμε ένα παράδειγμα:

![img](https://i.imgur.com/DLDTKmw.png)

[πηγή](https://faculty.washington.edu/tathornt/SISG2015/lectures/assoc2015session05.pdf)

Σε αυτό το παράδειγμα βλέπουμε το αποτέλεσμα του PCA σε ένα σύνολο που περιείχε ανθρώπους από διάφορες περιοχές της Ευρώπης. Τα αποτελέσματα ήταν εντυπωσιακά δεδομένου ότι το γράφημα προσεγγίζει ικανοποιητικά τον χάρτη της Ευρώπης. Το PCA κάνει προβολή όλων των δεδομένων σε 2 ή παραπάνω διαστάσεις. Οι διαστάσεις αυτές επιλέγονται έτσι ώστε να υπάρχει όσο το δυνατόν μεγαλύτερο variance μεταξύ των δεδομένων. Περισσότερα για το PCA μπορείτε να βρείτε εδώ:
* [Meng's Notes: An intuitive explanation of PCA (Principal Component Analysis)](http://mengnote.blogspot.co.uk/2013/05/an-intuitive-explanation-of-pca.html)
* [rincipal Component Analysis 4 Dummies: Eigenvectors, Eigenvalues and Dimension Reduction](http://georgemdallas.wordpress.com/2013/10/30/principal-component-analysis-4-dummies-eigenvectors-eigenvalues-and-dimension-reduction/)

### Το πρόβλημα
Στο site του [GGV](http://popgen.uchicago.edu/ggv/) μπορείτε να δείτε τη συχνότητα ενός SNP σε διάφορες περιοχές της γης. Όπως παρατηρείτε, υπάρχουν SNPs των οποίων η συχνότητα έχει μεγάλες διαφορές μεταξύ πληθυσμών αλλά υπάρχουν και SNPs των οποίων η συχνότητα είναι κοινή. Οι αλγόριθμοι PCA κάνουν ό,τι μπορούν ώστε να εντοπίσουν και να προβάλουν τις διαφορές που υπάρχουν αλλά η ύπαρξη πολλών SNPs με κοινές συχνότητες μεταξύ των πληθυσμών μπορούν να κάνουν τη PCA ανάλυση εξαιρετικά δύσκολη. Σε αυτό το project θα πρέπει να κάνετε μία ανάλυση του παραπάνω προβλήματος. Συγκεκριμένα θα πρέπει να απαντήσετε στην ερώτηση:
* **Ποιο είναι το ελάχιστο ποσοστό των SNPs με διαφορετικές πληθυσμιακές συχνότητες που πρέπει να έχει ένα πείραμα γονοτύπησης ώστε να είναι ορατές οι διαφορετικές πληθυσμιακές ομάδες που υπάρχουν;**


### Δημιουργία τεχνητών γονοτυπικών δεδομένων
Το πρόγραμμά σας θα πρέπει να μπορεί να παράγει τυχαίους γονότυπους για ένα πλήθος από τεχνητά (μη-υπαρκτά) SNPs. Για να παραχθεί ένα τυχαίο SNP κάνουμε το εξής: 
* Επιλέγουμε ποια θα είναι η συχνότητά του, έστω p (θα δούμε μετά πως θα γίνει αυτό)
* Επιλέγουμε πόσα samples (άτομα) θα "γονοτυπίσουμε" (θα δούμε μετά και αυτό)
* Για κάθε sample διαλέγουμε τυχαία δύο αλληλόμορφα. Το κάθε αλληλόμορφο μπορεί να πάρει μία δυνατή τιμή: Α ή Β. Η πιθανότητα να πάρουμε το Α είναι p και η πιθανότητα να πάρουμε το Β είναι 1-p. Δηλαδή οι δυνατοί γονότυποι είναι: Α/Α, Α/Β, Β/Α και Β/Β. 

Για να παράγουμε αληθοφανείς γονότυπους πρέπει η κατανομή των συχνοτήτων των SNPs να είναι όσο το δυνατόν πιο κοντά στη πραγματικότητα. Για το λόγο αυτό θα χρησιμοποιήσετε τις συχνότητες των SNPs που υπάρχουν στο 1000 Genomes Project.

### Το 1000 Genomes Project
Το [1000 Genomes Project](https://en.wikipedia.org/wiki/1000_Genomes_Project) (1KGP για συντομία) είναι ίσως το δεύτερο πιο σημαντικό project στη γενετική μετά το [Human Genome Project](https://en.wikipedia.org/wiki/Human_Genome_Project) (HGP). Αν το HGP δημιούργησε το πρώτο πλήρες γονιδίωμα του ανθρώπου, το 1KGP ήταν το πρώτο που μελέτησε τη γενετική ετερογένεια ενός μεγάλου μέρους του ανθρώπινου πληθυσμού. Στη τελική του φάση, το 1KGP είχε αλληλουχίσει το γονιδίωμα από 2504 ανθρώπους οι οποίοι ανήκουν σε 26 διαφορετικούς πληθυσμούς. 

Ας παίξουμε λίγο με τα δεδομένα από το 1KGP!

Τα δεδομένα από τη τελευταία (τρίτη) φάση του 1KGP βρίσκονται σε αυτό το link: [ftp://ftp.1000genomes.ebi.ac.uk/vol1/ftp/release/20130502/](ftp://ftp.1000genomes.ebi.ac.uk/vol1/ftp/release/20130502/)

Αυτό το site (στη πραγματικότητα [ftp site](https://en.wikipedia.org/wiki/File_Transfer_Protocol) αλλά αυτό δεν έχει σημασία) περιέχει όλες τις μεταλλάξεις (variants) που εντοπίστηκαν. Όλα τα variants περιγράφονται σε [VCF](https://en.wikipedia.org/wiki/Variant_Call_Format) φορμάτ και είναι συμπιεσμένα με το πρόγραμμα [gzip](https://en.wikipedia.org/wiki/Gzip). Κάθε αρχείο έχει τη κατάλληξη .vcf.gz και υπάρχει ένα αρχείο για κάθε χρωμόσωμα. Ας "παίξουμε" με το μικρότερο χρωμόσωμα το οποίο είναι το 22. 

Αρχικά κατεβάζουμε το αρχείο. **ΠΡΟΣΟΧΗ** Το αρχείο αυτό, αν και συμπιεσμένο, είναι 205 ΜΒ:



```python
!wget -O 1kgp_chr1.vcf.gz ftp://ftp.1000genomes.ebi.ac.uk/vol1/ftp/release/20130502/ALL.chr22.phase3_shapeit2_mvncall_integrated_v5a.20130502.genotypes.vcf.gz
```

    --2017-12-16 18:32:50--  ftp://ftp.1000genomes.ebi.ac.uk/vol1/ftp/release/20130502/ALL.chr22.phase3_shapeit2_mvncall_integrated_v5a.20130502.genotypes.vcf.gz
               => ‘1kgp_chr1.vcf.gz’
    Resolving ftp.1000genomes.ebi.ac.uk... 193.62.192.8
    Connecting to ftp.1000genomes.ebi.ac.uk|193.62.192.8|:21... connected.
    Logging in as anonymous ... Logged in!
    ==> SYST ... done.    ==> PWD ... done.
    ==> TYPE I ... done.  ==> CWD (1) /vol1/ftp/release/20130502 ... done.
    ==> SIZE ALL.chr22.phase3_shapeit2_mvncall_integrated_v5a.20130502.genotypes.vcf.gz ... 214453750
    ==> PASV ... done.    ==> RETR ALL.chr22.phase3_shapeit2_mvncall_integrated_v5a.20130502.genotypes.vcf.gz ... done.
    Length: 214453750 (205M) (unauthoritative)
    
    ALL.chr22.phase3_sh 100%[===================>] 204.52M   995KB/s    in 3m 31s  
    
    2017-12-16 18:36:24 (991 KB/s) - ‘1kgp_chr1.vcf.gz’ saved [214453750]
    


Ας επιβεβαιώσουμε ότι το αρχείο έχει κατέβει:


```python
!ls -lh 1kgp_chr1.vcf.gz
```

    -rw-r--r--  1 alexandroskanterakis  staff   205M Dec 16 18:36 1kgp_chr1.vcf.gz


Αφού το αρχείο είναι συμπιεσμένο μπορούμε να το ανοίξουμε με τη βιβλιοθήκη [gzip](https://docs.python.org/3/library/gzip.html) της python: 


```python
import gzip
```

Ένα gzip αρχείο το ανοίγουμε όπως και τα υπόλοιπα, απλά χρησιμοποιούμε τη ```gzip.open```:


```python
filename = '1kgp_chr1.vcf.gz'
file = gzip.open(filename, 'rt')
```

Ας διαβάσουμε τη πρώτη γραμμή του αρχείου:


```python
line = file.readline()
print (line)
```

    ##fileformat=VCFv4.1
    


Η πρώτη γραμμή μας ενημερώνει την έκδοση του VCF φορμάτ που χρησιμοποιεί. Μπορούμε να το αγνοήσουμε αυτό. Επίσης οι πρώτες γραμμές του αρχείου περιέχουν διάφορες (μετα)πληροφορίες για το περιεχόμενο του αρχείου τις οποίες μπορούμε να αγνοήσουμε. Αυτές οι γραμμές αρχίζουμε με: ```##```. Οπότε ας αγνοήσουμε όλες τις γραμμές που ξεκινάν με ```##```:


```python
while line[:2] == '##':
    line = file.readline()
```

Η μεταβλητή ```line``` τώρα είναι μια γραμμή η οποιά ΔΕΝ ξεκινάει με: ```##```. Η ```line``` τώρα είναι:


```python
line
```




    '#CHROM\tPOS\tID\tREF\tALT\tQUAL\tFILTER\tINFO\tFORMAT\tHG00096\tHG00097\tHG00099...\n'



παρατηρούμε ότι περιέχει διάφορα πεδία χωρισμένα με tabs. Ας τη κάνουμε split:


```python
line_splitted = line.split()
line_splitted
```




    ['#CHROM',
     'POS',
     'ID',
     'REF',
     'ALT',
     'QUAL',
     'FILTER',
     'INFO',
     'FORMAT',
     'HG00096',
     'HG00097',
     ...]



Αυτή η γραμμή μας δίνει τους τίτλους των πεδίων (header) του αρχείου. Έτσι λοιπόν:
* Το 1ο πεδίο (#CHROM) είναι το χρωμόσωμα
* Το 2ο πεδίο (POS) είναι η θέση στο χρωμόσωμα
* Το 3ο πεδίο (ID) είναι ένα μοναδικό ID για αυτή τη θέση.
* Το 4ο πεδίο (REF) είναι το reference sequence αυτού του variant. Δηλαδή η ακολουθία που θεωρούμε ως αναφορά.
* Το 5ο πεδίο (ALT) είναι το alternative sequence αυτού του variant. Δηλαδή η ακολουθια που βρήκαμε αντί για το reference sequence
* Το 6ο πεδίο (QUAL) είναι ένα quality metric το οποίο μας λέει πόσο σίγουροι είμαστε ό,τι δεν έχει γίνει λάθος κατά τη γονοτύπηση αυτής της θέσης. Μπορούμε να αγνοήσουμε αυτό το πεδία.
* Το 7ο πεδίο (FILTER) μας λέει αν ο συγκεκριμένος γονότυπος πέρασε ή όχι το quality metric. Συνήθως η τιμή του είναι ```PASS```
* Το 8ο πεδίο (INFO) μας δίνει κάποιες επιπλέον πληροφορίες για αυτή τη θέση, τις οποίες θα τις δούμε μετά. 
* Το 9ο πεδίο (FORMAT) μπορούμε να το αγνοήσουμε (μας λέει πως περιγράφονται ο γονότυπος)
* Το 10ο πεδίο μέχρι και το τελευταίο περιέχει το κωδικό όνομα των samples. Δηλαδή κάθε sample (άνθρωπος) έχει ένα κωδικό όνομα σε όλο το 1KGP. 

Ας σώσουμε τη πρώτη γραμμή με το όνομα: ```header```


```python
header = line_splitted
```

Ας διαβάσουμε τώρα την επόμενη γραμμή


```python
line_splitted = file.readline().split()
line_splitted
```




    ['22',
     '16050075',
     'rs587697622',
     'A',
     'G',
     '100',
     'PASS',
     'AC=1;AF=0.000199681;AN=5008;NS=2504;DP=8012;EAS_AF=0;AMR_AF=0;AFR_AF=0;EUR_AF=0;SAS_AF=0.001;AA=.|||;VT=SNP',
     'GT',
     '0|0',
     '0|0',
     '0|0',
     ...]



**Κάθε μία από τις υπόλοιπες γραμμές του VCF αρχείου περιγράφει μία μοναδική μετάλλαξη**

Άρα, αυτή η γραμμή περιέχει τις πληροφορίες για τον πρώτο variant του αρχείου. Για να δούμε λοιπόν:
* Το 1ο πεδίο είναι '22' το οποίο είναι το χρωμόσωμα
* Το 2ο πεδίο είναι '16050075' το οποίο είναι η θέση του variant στο χρωμόσωμα 22.
* Το 3ο πεδίο είναι ο κωδικός (ID) του variant ο οποίο είναι rs587697622.
* Το 4ο πεδίο είναι το reference sequence το οποίο για αυτό το variant είναι: ```A```.
* Το 5ο πεδίο είναι το alternative sequence το οποίο για αυτό το variant είναι: ```G```.
* Το 6ο πεδίο είναι το quality του variant το οποίο είναι 100 (το οποίο σημαίνει κάτι σαν "100% σίγουροι")
* Το 7ο πεδίο μας λέει αν πέρασε το quality filter ή όχι. Το ```PASS``` που περιέχει μας λέει ότι το πέρασε.
* Το 8ο πεδίο περιέχει κάποιες επιπλέον πληροφορίες για αυτόν τον variant. Οι πληροφορίες αυτές κωδικοποιούνται ως εξής: ```ΤΙΤΛΟΣ_1=ΤΙΜΗ_1;ΤΙΤΛΟΣ_2=ΤΙΜΗ_2...ΤΙΤΛΟΣ_N=ΤΙΜΗ_Ν```

Ας φτιάξουμε ένα dictionary με αυτές τις τιμές για αυτόν τον variant:


```python
INFO_index = header.index('INFO')
info = line_splitted[INFO_index]
info_dict = dict([x.split('=') for x in info.split(';')])
info_dict
```




    {'AA': '.|||',
     'AC': '1',
     'AF': '0.000199681',
     'AFR_AF': '0',
     'AMR_AF': '0',
     'AN': '5008',
     'DP': '8012',
     'EAS_AF': '0',
     'EUR_AF': '0',
     'NS': '2504',
     'SAS_AF': '0.001',
     'VT': 'SNP'}



Ας αναλύσουμε αυτές τις πληροφορίες:
* Το ```AA``` μπορούμε να το αγνοήσουμε
* Το ```NS``` είναι το Number of Samples. Δηλαδή σε πόσους ανθρώπους μπόρεσαν να ανιχνεύσουν αν αυτό το variant υπάρχει ή όχι. Το συγκεκριμένο είναι 2504
* Το ```AN``` είναι το Allele Number,  Δηλαδή σε πόσα χρωμοσώματα μπόρεσαν να ανιχνεύσουν αν αυτό το variant υπάρχει ή όχι. Το συγκεκριμένο είναι 5008 (δηλαδή 2504 * 2).
* Το ```AC``` είναι το "Allele Count". Δηλαδή σε πόσα χρωμοσώματα βρέθηκε το alternative sequence. Εδώ είναι μόνο 1. 
* Το ```AF``` είναι το Allele Frequency του alternative sequence. Αυτό είναι ίσο με AC/AN. Δηλαδή το συγκεκριμένο είναι: 1/5008 = 0.000199681
* Το ```AFR_AF``` είναι το Allele Frequency του variant στα samples με καταγωγή από Αφρική.
* Το ```AMR_AF``` είναι το Allele Frequency του variant στα samples με καταγωγή από Αμερική.
* Το ```EAS_AF``` είναι το Allele Frequency του variant στα samples με καταγωγή από ανατολική Ασία (East Asia).
* Το ```SAS_AF``` είναι το Allele Frequency του variant στα samples με καταγωγή από νότια Ασία (Sout Asia).
* Το ```EUR_AF``` είναι το Allele Frequency του variant στα samples με καταγωγή από Ευρώπη.
* Το ```VT``` είναι το Variant Type. Δηλαδή ο τύπος του variant. **ΠΡΟΣΟΧΗ! Σε αυτό το project θα ασχοληθούμε μόνο με variants που ο τύπος τους είναι "SNP"**.
* Το ```DP``` (DePth) μπορούμε να το αγνοήσουμε.

Συνεχίζουμε με τη περιγραφή των πεδίων του πρώτου variant.
* Το 9ο πεδίο είναι 'GT' και μπορούμε να το αγνοήσουμε. 

Τα επόμενα πεδία από το 10ο μέχρι το τέλος, περιέχουν τους γονότυπους των samples:


```python
genotypes = line_splitted[9:]
```

Πόσα samples υπάρχουν;


```python
len(genotypes)
```




    2504



Ας διαβάσουμε τον γονότυπο του πρώτου sample:


```python
genotypes[0]
```




    '0|0'



Ας αναλύσουμε λίγο αυτό το '0|0'

Αυτοί οι δύο αριθμοί μας λένε ποιο αλληλόμορφο έχει το κάθε ένα από τα 2 σετ χρωμοσωμάτων στη θέση αυτού του variant:
* Αν ο αριθμός είναι 0, τότε το αλληλόμορφο είναι ίδιο με το reference sequence
* Αν ο αριθμός είναι 1, τότε το αλληλόμορφο είναι ίδιο με το alternative sequence

Δηλαδή δεδομένου ότι το reference sequence αυτού του variant είναι ```A``` και το alternative sequence είναι ```G```. τότε ο γονότυπος αυτού του sample είναι: ```A/A```.

Ο γονότυπος του 1438-ου sample είναι:


```python
genotypes[1437]
```




    '0|1'



Αυτό σημαίνει ότι ο γονότυπος του 1438-ού sample είναι: ```A/G```

Σημείση 1: Ο γονότυπος 1|0 και ο γονότυπος 0|1 θα θεωρείται ότι είναι ο ίδιος. (Στη πραγματικότητα επείδη οι γονότυποι του 1KGP είναι [phased](https://en.wikipedia.org/wiki/Haplotype_estimation) το πρώτο νούμερο είναι το αλληλόμορφο στο πρώτο σετ χρωμοσωμάτων και το δεύτερο αλληλόμορφο στο δεύτερο)

Σημείωση 2: Ο αριθμός αυτός μπορεί να είναι και μεγαλύτερος του 1. Για παράδειγμα, αν έχουμε κάποιο SNP το οποίο είναι tri-allelic, μπορεί ένα sample να έχει γονότυπο 0|1 (π.χ. Α/Τ) και ένα άλλο sample να έχει γονότυπο 0|2 (π.χ. Α/G). Αυτό σημαίνει ότι αυτό το variant έχει τρία διαφορετικά αλληλόμορφά. Αγνοήστες αυτά τα variants.

Το κάθε sample στο 1KGP, ανήκει σε 1 από 5 διαφορετικές περιοχές (European, African, American, East Asia, South Asian) και σε 1 από 26 διαφορετικούς πληθυσμούς. Για αρχή ας φτιάξουμε μία λίστα που θα έχει όλους τους κωδικούς των samples:


```python
sample_ids = header[9:]
sample_ids
```




    ['HG00096',
     'HG00097',
     'HG00099',
     ...]



Η πληροφορία για τις περιοχές και τους πληθυσμούς που ανήκει κάθε sample υπάρχει στο αρχείο που βρίσκεται σε αυτό το link: [ftp://ftp.1000genomes.ebi.ac.uk/vol1/ftp/release/20130502/integrated_call_samples_v3.20130502.ALL.panel](ftp://ftp.1000genomes.ebi.ac.uk/vol1/ftp/release/20130502/integrated_call_samples_v3.20130502.ALL.panel) . Ας το κατεβάσουμε:


```python
!wget -O sample_information.csv ftp://ftp.1000genomes.ebi.ac.uk/vol1/ftp/release/20130502/integrated_call_samples_v3.20130502.ALL.panel
```

    --2017-12-16 20:41:20--  ftp://ftp.1000genomes.ebi.ac.uk/vol1/ftp/release/20130502/integrated_call_samples_v3.20130502.ALL.panel
               => ‘sample_information.csv’
    Resolving ftp.1000genomes.ebi.ac.uk... 193.62.192.8
    Connecting to ftp.1000genomes.ebi.ac.uk|193.62.192.8|:21... connected.
    Logging in as anonymous ... Logged in!
    ==> SYST ... done.    ==> PWD ... done.
    ==> TYPE I ... done.  ==> CWD (1) /vol1/ftp/release/20130502 ... done.
    ==> SIZE integrated_call_samples_v3.20130502.ALL.panel ... 55156
    ==> PASV ... done.    ==> RETR integrated_call_samples_v3.20130502.ALL.panel ... done.
    Length: 55156 (54K) (unauthoritative)
    
    integrated_call_sam 100%[===================>]  53.86K   183KB/s    in 0.3s    
    
    2017-12-16 20:41:24 (183 KB/s) - ‘sample_information.csv’ saved [55156]
    


Για να δούμε τι πληροφορία έχει:


```python
sample_filename = 'sample_information.csv'
sample_file = open(sample_filename)
sample_data = sample_file.read()
sample_file.close()

sample_data
```




    'sample\tpop\tsuper_pop\tgender\t\t\nHG00096\tGBR\tEUR\tmale\nHG00097\tGBR\tEUR\tfemale\nHG00099\n'



Παρατηρούμε ότι είναι ένα tab delimited αρχείο:


```python
sample_data_splitted = [x.split() for x in sample_data.split('\n')]
sample_data_splitted
```




    [['sample', 'pop', 'super_pop', 'gender'],
     ['HG00096', 'GBR', 'EUR', 'male'],
     ['HG00097', 'GBR', 'EUR', 'female'],
     ['HG00099', 'GBR', 'EUR', 'female'],
     ...]



Η πρώτη γραμμή είναι το header του αρχείου. Οι υπόλοιπες γραμμές περιέχουν την εξής πληροφορία:

* Το 1ο πεδίο (sample) περιέχει τον κωδικό του sample όπως υπάρχει και στο VCF αρχείο
* Το 2ο πεδίο (pop) περιέχει τον πληθυσμό στον οποίο ανήκει (έναν από τους 26)
* Το 3ο πεδίο (super_pop) περιέχει τη περιοχή στην οποία ανήκει (μία από τις 5)
* Το 4ο πεδίο (gender) περιέχει το φύλο του sample. Δυνατές τιμές είναι 'male' και 'female'. Μπορούμε να την αγνοήσουμε αυτή τη πληροφορία. 

Για παράδειγμα ας πάρουμε όλους τα samples που είναι βρετανοί:


```python
sample_ids_british = [x[0] for x in sample_data_splitted[1:] if x and x[1] == 'GBR']
sample_ids_british
```




    ['HG00096',
     'HG00097',
     'HG00099',
     'HG01791',
     ...]



## Γενικά 
Το πρόγραμμά σας θα πρέπει να δέχεται διάφορες παραμέτρους από το command line. Η βασική παράμετρος είναι η ```--action <ACTION_NAME>```. Ανάλογα με τη τιμή της παραμέτρου αυτής, το πρόγραμμά σας θα πρέπει να κάνει διάφορες λειτουργίες. 

### Μέρος 1ο
Το πρόγραμμά σας θα πρέπει να δέχεται τις εξής παραμέτρους:
* ```--vcf <FILENAME>``` θα παίρνει ένα vcf ή ένα vcf.gz αρχείο (ό,τι θέλετε). 
* Με το ```--action VCF_INFO```. Το πρόγραμμά σας θα τυπώνει πόσα SNPs έχει το vcf και πόσα samples.

Π.χ:
```text
> python project.py --vcf 1kgp_chr1.vcf.gz --action VCF_INFO

File has 2502 samples
File has 1234567 SNPs
```

### Μέρος 2ο
Το πρόγραμμα σας θα πρέπει να δέχεται τις εξής παραμέτρους:
* ```--sample_filename <FILENAME>``` όπου θα παίρνει ΕΠΙΠΛΕΟΝ το όνομα του αρχείου που θα περιέχει τη πληθυσμιακη πληροφορία των samples
* ```--action SAMPLE_INFO``` θα τυπώνει πόσα samples περιέχει το sample_filename και πόσα samples έχει ο κάθε πληθυσμός. Μαζί με τον πληθυσμό θα τυπώνει και σε ποια περιοχή ανήκει αυτός ο πληθυσμός. 
* ```--action VALIDATE_SAMPLE_INFO``` θα επιβεβαιώνει ότι όλα τα samples που υπάρχουν στο vcf υπάρχουν και στο sample_filename και το αντίστροφο.

Π.χ:
```text
> python project.py --sample_filename sample_information.csv --action SAMPLE_INFO

File has 5 Areas.
Area 1 is EUR and contains 1234 samples splitted in the following populations:
GBR 100 samples
ITA 109 samples
Area 2 is AMR and contain 5678 samples splitted in the following populations:
...
```

Και:

```text
> python project.py --vcf 1kgp_chr1.vcf.gz --sample_filename sample_information.csv --action VALIDATE_SAMPLE_INFO

Everything is OK!

or..

These samples are present in VCF but not in SAMPLE:
XYZ
KLM
```

### Μέρος 3ο
* ```--population <POPULATION_NAME> <NUMBER_OF_SAMPLES> --SNPs <Number of SNPs> --output <FILENAME> --action SIMULATE``` 

Με αυτές τις παραμέτρους το πρόγραμμά σας θα πρέπει να δημιουργεί ένα αρχείο με το όνομα ```<FILENAME>```. Το αρχείο θα περιέχει ```<SNPs>``` *διαφορετικά* SNPs και ```<NUMBER_OF_SAMPLES>``` διαφορετικά samples. Οι γονότυποι αυτών των SNPs θα είναι τυχαίοι. Τα allele frequencies αυτών των SNPS θα πρέπει να ίδια με τυχαία (αλλά υπαρκτά) SNPs από το αρχείο που έχει δηλωθεί με τη ```--vcf``` παράμετρο. Το φορμάτ του αρχείο του αρχείου ```<FILENAME>``` μπορεί να είναι ό,τι θέλετε εσείς αλλά συνίσταται να είναι σε VCF.

Π.χ: Η παρακάτω εντολή θα πρέπει να παράγει ένα αρχείο με το όνομα ```random_genotypes.vcf``` το οποίο θα έχει 100 samples και 1000 SNPs. Το κάθε SNP θα έχει το ίδιο allele frequency με το allele frequency κάποιου υπαρκτού SNP στο ```1kgp_chr1.vcf.gz```  το οποίο θα έχετε επιλέξει τυχαία (το SNP). Για να υπολογίσετε το allele_frequency θα πάρετε ΜΟΝΟ τα samples που ανήκουν στον GBR πληθυσμό:

```text
> python project.py --vcf 1kgp_chr1.vcf.gz --sample_filename sample_information.csv --population GBR 100 --SNPs 1000 --output random_genotypes.vcf --action SIMULATE
```

### Μέρος 4ο
Στο 4ο μέρος θα πρέπει το πρόγραμμά σας να δέχεται πολλές διαφορετικές παράμετρους ```--population```. Με αυτόν τον τρόπο θα μπορεί να δημιουργεί αρχεία τα οποία θα έχουν samples από πολλούς διαφορετικούς πληθυσμούς. Για παράδειγμα η παρακάτω εντολή θα πρέπει να παράγει το αρχείο ```random_genotypes.vcf``` το οποίο θα έχει 100 samples με allele frequencies από τον GBR πληθυσμό και 200 samples από τον IBS πληθυσμό και θα παράγει στο σύνολο 1000 SNPs:

```text
> python project.py --vcf 1kgp_chr1.vcf.gz --sample_filename sample_information.csv --population GBR 100 --population IBS 200 --SNPs 1000 --output random_genotypes.vcf --action SIMULATE
```

**ΠΡΟΣΟΧΗ!** Τα allele frequencies θα πρέπει να προέρχονται από το ΙΔΙΟ τυχαία επιλεγμένο SNP και για τους δύο πληθυσμούς. Απλά θα υπολογίζετε ένα allele frequency για τους GBR και ένα για τους IBS. Στη συνέχεια χρησιμοποιείται αυτά τα 2 allele frequencies για να φτιάξετε τους 100 τυχαίους GBR και τους 200 τυχαίους IBS. Για παράδειγμα αν επιλέξουμε τυχαία ένα SNP από το 1KGP του οποίου το allele freuquency στα GBR samples είναι 0.25 και το allele frequency στα IBS samples είναι 0.29, τότε θα πρέπει να χρησιμοποιήσετε τις αντίστοιχες συχνότητες (0.25 και 0.29) όταν δημιουργείτε τα τυχαία δείγματά σας.

**ΠΡΟΣΟΧΗ!** Το πρόγραμμά σας δεν πρέπει να έχει όριο στο πλήθος από διαφορετικούς πληθυσμούς που δηλώνονται στο command line. Δηλαδή θα πρέπει να μπορεί ο χρήστης να δημιουργεί 100 τυχαίους ITA, 200 τυχαίους GBR και 150 τυχαίους PEL με ένα και μόνο command.

### Μέρος 5ο
Το πρόγραμμά σας θα πρέπει να δέχεται τη παράμετρο ```--independent <NUMBER_OF_INDEPENDENT_SNPs>``` το οποίο θα προσθέτει SNPs των οποίων τα allele frequencies θα υπολογίζεται με βάση ΟΛΟΥΣ τους πληθυσμούς που έχουν δηλωθεί μέσω των ```--population parameters```. Για παράδειγμα η παρακάτω εντολή:

```bash
> python project.py \
   --vcf 1kgp_chr1.vcf.gz --sample_filename sample_information.csv \
   --population GBR 100 \
   --population IBS 200 \
   --SNPs 1000 \
   --independent 700 \
   --output random_genotypes.vcf \
   --action SIMULATE
```

θα πρέπει να παράγει συνολικά 1.700 SNPs. Από αυτά, τα 1000 θα έχουν allele frequencies που θα υπολογίζονται με βάση το 4ο μέρος. Τα 700 θα έχουν το allele frequency των GBR και των IBS, αν θεωρήσουμε ότι αυτά τα δείγματα ανήκουν στον ίδιο πληθυσμό. 

Ένα επιπλέον παράδειγμα: Ας υποθέσουμε ότι έχουμε το παρακάτω SNP:

```text
IBS_1 IBS_2 IBS_3 GBR_1 GBR_2
 A/A   A/C   A/A   A/A   A/C 
```

Τα ```IBS_1, IBS_2, IBS_3``` είναι 3 samples από IBS.

Τα ```GBR_1, GBR_2``` είναι 2 samples από GBR.

Τότε το allele frequency των IBS είναι 1/6. Το allele frequency των GBR είναι 1/4. Το allele frequency όλων είναι 2/10. 

Οπότε με βάση αυτό το SNP, θα πρέπει να φτιάξετε 1000 SNPs των οποίων τα 100 samples να έχουν allele frequency 1/4 και 200 samples με allele frequency 1/6. Θα πρέπει επιπλέον να φτιάξετε 700 SNPs τα οποία θα έχουν allele frequency 2/10 και για τα 300 samples (100+200).


### Μέρος 6ο
Σε αυτό το μέρος θα παίρνει ένα αρχείο που εσείς θα έχετε παράξει (με τη παράμετρο ```--output <FILENAME>```) με βάση τις εντολές που περιγράφονται στα μέρη 3,4,5,6 και θα κάνει PCA. Πως κάνουμε όμως PCA στη python; Ας το εξερευνήσουμε! 

Για αρχή ας φτιάξουμε μερικές συναρτήσεις που δημιουργούν τυχαίους γονότυπους για δύο πληθυσμούς. Για κάθε SNP διαλέγουμε μία τυχαία τιμή από το 0 μέχρι το 0.5. Αυτό θα είναι το allele frequency του reference allele. Στη συνέχεια διαλέγουμε δύο τυχαίους αριθμός από το -0.2 μέχρι το 0.2 και φτιάχνουμε δύο perturbations (διακυμάνσεις) του allele frequency. Για παράδειγμα αν υποθέσουμε ότι το τυχαίο allele frequency είναι 0.3 και τα δύο τυχαία perturbations είναι 0.1 και -0.05 τότε τα allele frequencies για τους δύο πληθυσμούς θα είναι:

* Allele frequency για τον πληθυσμό 1: 0.3 + 0.1\*0.3 = 0.33
* Allele frequency για τον πληθυσμό 2: 0.3 - 0.05\*0.3 = 0.285

Στη συνέχεια φτιάχνουμε δύο τυχαίες λίστες με γονότυπους χρησιμοποιώντας τα παραπάνω allele frequencies. Η πρώτη λίστα είναι η εξομείωση του SNP στον πρώτο πληθυσμό και η δεύτερη η εξομείωση για τον δεύτερο.


```python
import random
def random_frequency():
    '''
    Generate a random number between 0.0 and 0.5
    '''
    return random.uniform(0.0, 0.5)

def random_perturbation(r, perturbation=0.2):
    '''
    Takes a random value and returns a random perturbation in the range of -perturbation to +perturbation 
    '''
    perturbation = random.uniform(-perturbation, perturbation)
    return r + (r*perturbation)
    
def generate_random_frequencies(n):
    '''
    Simulates n random allele frequencies from n different populations
    '''
    base_frequency = random_frequency()
    return [random_perturbation(base_frequency) for i in range(n)]

def generate_random_allele(p, reference='A', alternative='B'):
    '''
    Generates a random allele.
    It selects "alternative" with propability p and "reference" with probability 1-p 
    '''
    if random.random() <= p:
        return alternative
    return reference

def generate_random_genotype(frequency):
    '''
    Generates a random genotype
    '''
    return [generate_random_allele(frequency) for i in range(2)]

def generate_random_genotypes(frequency, n):
    '''
    Generates n random SNPs with specific frequency
    '''
    return [generate_random_genotype(frequency) for i in range(n)]
    
    
def generate_random_population(pop_1, pop_2, SNPs):
    '''
    Generates a dataset that contains:
    pop_1 samples belonging to #1 population
    pop_2 samples belonging to #2 population
    
    SNPs is the number of SNPs
    '''
    
    ret = [] # We will return this
    
    for snp_counter in range(SNPs):
        # Take 2 different allele grequencies
        fr_1, fr_2 = generate_random_frequencies(2)
        
        # Generate genotypes
        pop_1_genotypes = generate_random_genotypes(fr_1, pop_1)
        pop_2_genotypes = generate_random_genotypes(fr_2, pop_2)
        
        #Merge into a single list add it to the ret
        merged = pop_1_genotypes + pop_2_genotypes
        ret.append(merged)
        
    return ret


```

Στη συνέχεια φτιάχνουμε ένα τυχαίο dataset με δύο πληθυσμούς, 100 samples ο κάθε ένας και 1000 SNPs:


```python
genotypes = generate_random_population(100, 100, 1000)
```

Για να συνεχίσουμε θα πρέπει να φτιάξουμε μία συνάρτηση που μετατρέπει τους γονότυπους σε αριθμητικές τιμές:
* Ο γονότυπος Α/Α (ομόζυγο reference) γίνεται 0
* Ο γονότυπος Α/Β (ετερόζυγο) γίνεται 1
* Ο γονότυπος Β/Β (ομόζυγο alternative) γίνεται 2



```python
def convert_genotype_to_numeral(genotype):
    if genotype == ['A', 'A']:
        return 0
    if genotype == ['A', 'B']:
        return 1
    if genotype == ['B', 'A']:
        return 1
    if genotype == ['B', 'B']:
        return 2
    
    assert False # This should never happen
    
def convert_genotype_data_to_numeral(genotypes):
    ret = []
    for snp in genotypes:
        snp_numerical = [convert_genotype_to_numeral(g) for g in snp]
        ret.append(snp_numerical)
        
    return ret

```

Μετατρέπουμε τα genotypes σε numerical:


```python
genotypes_numerical = convert_genotype_data_to_numeral(genotypes)
```

Τώρα έχουμε μία λίστα από λίστες με αριθμητικές τιμές που περιέχει τους γονότυπους. Για να συνεχίσουμε θα πρέπει να χρησιμοποιήσουμε τη βιβλιοθήκη [numpy](http://www.numpy.org/). Το numpy είναι μια βιβλιοθήκη για αλγορίθμους γραμμικής άλγεβρας και [αριθμητικής ανάλυσης](https://en.wikipedia.org/wiki/Numerical_analysis). Είναι υλοποιημένη σε [γλώσσες χαμηλού επιπέδου](https://en.wikipedia.org/wiki/Low-level_programming_language) και δίνει στη python τη δυνατότητα να επεξεργαστεί με εξαιρετική ταχύτητα μεγάλα αριθμητικά δεδομένα.


```python
import numpy
```

Μετατρέπουμε το genotypes_numerical σε έναν πίνακα ώστε να μπορεί να τον διαχειριστές η numpy:


```python
genotypes_array = numpy.array(genotypes_numerical)
```

Στη συνέχεια πρέπει να εφαρμόσουμε PCA στον πίνακα genotypes_numerical. Το κάνουμε αυτό μέσω της βιβλιοθήκης [sklearn](http://scikit-learn.org/). Αρχικά εγκαθιστούμε τη βιβλιοθήκη: 


```python
!conda install -y scikit-learn
```

    Fetching package metadata .........
    Solving package specifications: .
    
    Package plan for installation in environment /Users/alexandroskanterakis/anaconda3/envs/arkalos:
    
    The following NEW packages will be INSTALLED:
    
        scikit-learn: 0.19.0-np113py36_0
        scipy:        0.19.1-np113py36_0
    
    scipy-0.19.1-n 100% |################################| Time: 0:04:11  64.85 kB/s
    scikit-learn-0 100% |################################| Time: 0:00:42 130.11 kB/s


Κάνουμε import τις συναρτήσεις που κάνουν PCA:


```python
from sklearn.decomposition import PCA
```

Δηλώνουμε ότι μέσω του PCA θα κάνουμε προβολή των δεδομένων μας στις δύο διαστάσεις: 


```python
pca = PCA(n_components=2)
```

Κάνουμε fit το pca. Προσοχή: Ο πίνακας genotypes_array έχει 1000 γραμμές (SNPs) και 200 στήλες (samples). Η συνάρτηση PCA θεωρεί ότι οι γραμμές είναι data και οι στήλες διαστάσεις. Οπότε πρέπει να κάνουμε [transpose](https://en.wikipedia.org/wiki/Transpose) τον πίνακα: 


```python
pca.fit(genotypes_array.T)
```




    PCA(copy=True, iterated_power='auto', n_components=2, random_state=None,
      svd_solver='auto', tol=0.0, whiten=False)



Κάνουμε προβολή στις 2 διαστάσεις που υπολόγισε το pca.fit:


```python
genotypes_PCA = pca.transform(genotypes_array.T)
```

Ελέγχουμε τις διαστάσεις του genotypes_PCA:


```python
genotypes_PCA.shape
```




    (200, 2)



Προσέχτε ότι από τις 1000 διαστάσεις, πήγαμε στις 2. Τώρα μπορούμε να "δούμε" τα δεδομένα μας στις δύο διαστάσεις:


```python
import matplotlib.pyplot as plt
```

Τα πρώτα 100 samples ανήκουν στον πρώτο πληθυσμό και θα είναι με κόκκινο χρώμα. Τα υπόλοιπα 100 samples ανήκουν στον δεύτερο πληθυσμό και θα τα δείξουμε με μπλε χρώμα:


```python
plt.plot(genotypes_PCA[:100,0], genotypes_PCA[:100,1], '.', color="red")
plt.plot(genotypes_PCA[100:,0], genotypes_PCA[100:,1], '.', color="blue")
plt.show()
```


    
![png](output_77_0.png)
    


Παρατηρούμε ότι το PCA μπόρεσε και διαχώρισε σε έναν βαθμό τους δύο πληθυσμούς. Οπότε σε αυτό το μέρος θα πρέπει το πρόγραμμά σας να δέχεται τους παρακάτω παραμέτρους:
* ```--input_filename <FILENAME>``` αυτό είναι το αρχείο με τους τυχαίους γονότυπους που έχετε φτιάξει στο μέρος 3,4 ή 5.
* ```--action PCA``` δηλώνουμε ότι θέλουμε να κάνουμε PCA. Δηλαδή το πρόγραμμά σας θα πρέπει να κάνει την ανάλυση που περιγράφηκε παραπάνω
* ```--PCA_filename <FILENAME>``` στο αρχείο αυτό θα σώζετε τα δι-διάστατα δεδομένα από το PCA.
* ```--PCA_plot <FILENAME>``` στο αρχείο αυτό θα πρέπει να σώζετε το plot από το PCA (σε ό,τι φορμάτ θέλετε)



### Σημειώσεις
1. Ο κώδικας που δίνεται εδώ είναι ενδεικτικός. Μπορείτε να τον χρησιμοποιήσετε, αλλάξετε κτλ.
2. Μπορείτε να χρησιμοποιήσετε όποια μέθοδο θέλετε για PCA.
3. Ποτέ δεν ξεχνάμε να κλείσουμε τα αρχεία που έχουμε ανοίξει!


```python
file.close()
```


