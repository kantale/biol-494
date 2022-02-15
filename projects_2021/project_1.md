# Project 1

<!-- https://gist.github.com/kantale/24f4f02d5b87ce0146e0455791e71aeb  --> 

Σκοπός του project είναι να φτιάξετε σε python ένα πρόγραμμα με το οποίο θα μπορούν να υπολογιστούν βασικές παράμετροι της πληθυσμιακής γενετική. Αυτές οι παράμετροι είναι πολύ χρήσιμες σε [GWAS](https://en.wikipedia.org/wiki/Genome-wide_association_study) μελέτες. Τα GWAS (Genome Wide Association Studies) είναι μελέτες που προσπαθούν να βρουν μία στατιστική συσχέτιση μεταξύ ενός γονότυπου και ενώς φαινότυπου. Για τους σκοπούς αυτής της εργασίας έχουμε φτιάξει ένα τεχνιτό (artificial) genotype dataset. Αυτό το dataset βρίσκεται εδώ:

https://s3.eu-central-1.amazonaws.com/pythonprojectgwas/gwas.tar.gz

Αφού το κατεβάσετε μπορείτε να το κάνετε uncompress ως εξής:

```bash
tar zxvf gwas.tar.gz
```

ή 

```bash
gunzip gwas.tar.gz
tar xvf gwas.tar
```

Στη συνέχεια θα δείτε ότι υπάρχουν δύο αρχεία: το ```gwas.cases.gen``` και το ```gwas.controls.gen``` .
Τα αρχεία αυτά περιέχουν τα genotypes από 500 controls και 500 cases από μία υποθετική ασθένεια. **Προσοχή** περιέχεται μόνο το χρωμόσωμα 20. [Το φορμάτ των αρχείων](http://www.stats.ox.ac.uk/%7Emarchini/software/gwas/file_format.html#Genotype_File_Format), είναι σύμφωνα με το πρόγραμμα [HAPGEN2](https://mathgen.stats.ox.ac.uk/genetics_software/hapgen/hapgen2.html) το οποίο και χρησιμοποιήθηκε για να φτιαχτεί αυτό το artificial dataset. Λεπτομέρειες για το πως δημιουργήθηκε αυτό το dataset υπάρχουν στο τέλος. 

Κάθε γραμμή σε αυτά τα αρχεία περιέχει και ένα [SNP](https://en.wikipedia.org/wiki/Single-nucleotide_polymorphism) (όλες οι θέσεις είναι στο χρωμόσωμα 20). Η πρώτη στήλη περιέχει έναν μοναδικό κωδικό για κάθε SNP. Η δεύτερη στήλη περιέχει τον rs κωδικό του SNP σύμφωνα με το [dbsnp](https://www.ncbi.nlm.nih.gov/projects/SNP/) (για όσα δεν έχουν dbsnp κωδικό περιέχει απλά τη θέση). Εισάγοντας τον κωδικό αυτόν στο dbsnp μπορείτε να βρείτε περισσότερες πληροφορίες για το SNP. Η τρίτη στήλη περιέχει τη θέση του SNP σύμφωνα με το NCBI build 36. Οι επόμενες δύο στήλες (4η, 5η) περιέχουν τα 2 πιθανά αλληλόμορφα του SNP. Το πρώτο είναι το reference και το δεύτερο το alternative. 

Οι υπόλοιπες στήλες περιέχουν τον γονότυπο για κάθε ένα sample. Ο γονότυπος ενός sample αποτελείται από 3 στήλες από '0' και '1'. Κάθε τριάδα μπορεί να έχει μόνο ένα '1'. Αν το '1' είναι στη πρώτη θέση της τριάδας τότε το δείγμα αυτό είναι homozygous reference. Αν το '1' είναι στη δεύτερη θέση τότε είναι heterozygous και αν είναι στη 3η θέση είναι homozygous alternative. Ή αλλιώς αν υποθέσουμε ότι το SNP έχει reference A και alternative B, τότε:

* 1 0 0 ---> Α Α
* 0 1 0 ---> Α Β
* 0 0 1 ---> Β Β

Για παράδειγμα ας πάρουμε τη πρώτη γραμμή του ```gwas.cases.gen```:

```bash
head -n 1  gwas.cases.gen 
```

Για λόγους συντομίας δεν δείχνουμε όλες τις στήλες. Οι πρώτες 20 στήλες είναι οι παρακάτω:

```
snp_0 rs6078030 9098 C T 1 0 0 0 1 0 0 1 0 0 1 0 1 0 0
```

Άρα ο γονότυπος για τα πρώτα 5 δείγματα είναι (τα spaces είναι δικά μου):

```
1 0 0      0 1 0      0 1 0      0 1 0      1 0 0
 C C        C T        C T        C T        C C          
```

Δηλαδή το πρώτο case είναι CC, το δεύτερο case είναι C T, το πέμπτο case είναι C C κτλ.


Το πρόγραμμά σας σε python θα πρέπει να δέχεται τις εξής υποχρεωτικές παραμέτρους από το command line:
* -controls_file  : Το αρχείο με τα control genotypes (π.χ. gwas.controls.gen)
* -cases_file     : Το αρχείο με τα cases genotyes (π.χ. gwas.controls.gen)
* -output         : Ένα όνομα αρχείου. Το πρόγραμμα θα αποθηκεύει όλα τα αποτελέσματα σε διαφορετικές καταλήξεις αυτού του αρχείου 

Επίσης θα πρέπει να δέχεται τις παρακάτω μη-υποχρεωτικές παραμέτρους για τον χειρισμό SNP/Samples
* -keep_snps      : Ένα αρχείο με κωδικούς SNPs ανά γραμμή. Η ανάλυση θα γίνεται ΜΟΝΟ σε αυτά τα SNPs
* -remove_snps    : Ένα αρχείο με κωδικούς SNPs ανά γραμμή. Η ανάλυση θα γίνεται σε όλα τα SNPs εκτός αυτά.
* -keep_samples   : Ένα αρχείο με κωδικούς sample ανά γραμμή. Ένα sample έχει κωδικό: (case ή control)_αριθμός. Π.χ. το sample control_5 είναι το 5ο control. Το case_100 είναι το 100ό case. Η ανάλυση θα γίνεται ΜΟΝΟ σε αυτά τα samples.
* -remove_samples : Ένα αρχείο με κωδικούς sample ανά γραμμή (δες παραπάνω). Η ανάλυση θα γίνεται σε όλα τα samples εκτός από αυτά.

Αν έχει χρησιμοποιειθεί μία από τις παραπάνω 4 παραμέτρους τότε το πρόγραμμα θα πρέπει να δημιουργεί το αρχείο "output".cases.gen και "output".controls.gen το οποίο θα περιέχει μόνο τα SNPs/samples τα οποία δεν θα έχουν αφαιρεθεί. Το φορμάτ πρέπει να είναι αυτό που έχουμε περιγράψει. Το "output" είναι η τιμή της παραμέτρους -output.  

Για την ανάλυση των genotypes, το πρόγραμμα θα πρέπει να υποστηρίζει τις παρακάτω παραμέτρους:
* -allele_frequency : Τυπώνει στο αρχείο "output".frequency 6 στήλες:
  * Η 1η στήλη είναι ο κωδικός του SNP. 
  * Η 2η είναι η συχνότητα του reference στα controls 
  * Η 3η είναι η συχνότητα του alternative στα controls
  * H 4η είναι συχνότητα του reference στα cases
  * Η 5η είναι η συχνότητα του alternative στα cases
  * H 6η είναι η συχνότητα του reference στα cases και στα controls
  * H 7η είναι η συχνότητα του alternatice στα cases και στα controls

* -HWE : Τυπώνει στο αρχείο "output".hwe 2 στήλες:
  * Η 1η στήλη είναι ο κωδικός του SNP
  * H 2η στήλη θα περιέχει το [Hardy Weinberg Equilibrium](https://en.wikipedia.org/wiki/Hardy%E2%80%93Weinberg_principle) statistic για το ενωμένο cases+controls dataset. Μπορείτε να χρησιμοποιήσετε οποιαδίποτε μέθοδο για τον υπολογισμό του (π.χ.: https://en.wikipedia.org/wiki/Hardy%E2%80%93Weinberg_principle#Significance_tests_for_deviation)

* ~-LD SNP1 SNP2 : Τυπώνει στο αρχείο "output".ld το Linkage Disequilibrium (LD) R square και D' (D prime) μεταξύ των SNPs με κωδικό SNP1 και SNP2. Εξαιρετικά καλές και εύκολες οδηγίες για τον υπολογισμό του LD βρίσκονται εδώ: http://rannala.org/books/CUPChap3.pdf κεφάλαιο: 3.2.2 EM algorithm for estimating disequilibrium.~ **Αυτό το μέρος αποσύρεται**

Προσοχή! σε αυτό το λινκ http://rannala.org/books/CUPChap3.pdf υπάρχει ένα λάθος στη σελίδα 68 το λάθος είναι:

![slide3](https://cloud.githubusercontent.com/assets/1254711/23204323/c48aa784-f8ee-11e6-9194-fc97ae3e076d.jpg)

Credits στον Παύλο Παυλίδη που το εντόπισε!

* --HWE_filter NUMBER παράγει ένα αρχείο με το όνομα HWE_filter το οποίο περιέχει τους κωδικούς των SNPs που έχου HWE μεγαλύτερο από το NUMBER 
* --AF_filter NUMBER παράγει ένα αρχείο με το όνομα AF_filter το οποίο περιέχει τους κωδικούς των SNPs των οποίων το alternative allele έχει Allele Frequency μεγαλύτερο απο το NUMBER.
* --HWE_plot ONOMA_ARXEIOY.png παράγει ένα plot με τη κατανομή των τιμών του HWE statistic
* --AF_plot ONOMA_ARXEIOY.png παράγει ένα plot με τη κατανομή των τιμών του Allele Frequency
* ~--LD_run KWDIKOS_SNP threshold ΟΝΟΜΑ_ΑΡΧΕΙΟΥ.png με αυτή την εντολή υπολογίζει το LD μεταξύ του SNP KWDIKOS_SNP και όλων των SNPs downstream (δηλαδή σε μεγαλύτερες θέσεις) ή upstream (δηλαδή σε μικρότερες θέσεις). Μόλις βρει 1 SNP με LD μικρότερο από το threshold σταματάει. Φτιάχνει ένα plot όπου στον Χ είναι τα SNPs και στο Y είναι η τιμή του LD (R-square). Στο plot θα πρέπει να φαίνεται με κάποιο "σημάδι" η θέση του SNP KWDIKOS_SNP. Στο τέλος σώζει το plot στο αρχείο ΟΝΟΜΑ_ΑΡΧΕΙΟΥ.png.~ **Αυτό το μέρος αποσύρεται**



### Σημείωση: Υπολογισμός Hardy Weinberg Equilibrium"

H wikipedia δίνει ένα πολύ καλό παράδειγμα:
https://en.wikipedia.org/wiki/Hardy%E2%80%93Weinberg_principle#Significance_tests_for_deviation

Πρoσέξτε πως υπολογίζει τα expected values (1467.4, 141.2, 3.4) με βάση τα observed values (1469, 138, 5)

Αφού τα υπολογίσετε μετά μπορείτε να εφαρμόσετε το chi square test στη python:

```python
>>> from scipy import stats
>>> s = stats.chisquare([1469, 138, 5], [1467.4, 141.2, 3.4])
>>> print (s)
Power_divergenceResult(statistic=0.82720700518383861, pvalue=0.66126308839474002)
```

Προσέξτε ότι το statistic (0.8272..) είναι το ίδιο που δίνει και η wikipedia (0.83), απλά είναι στρογγυλοποιημένο.
Οπότε αυτό που πρέπει να πάρετε είναι το pvalue:

```python
>>> print (s.pvalue)
0.66126308839474002
```

