# Project 2
<!-- https://gist.github.com/kantale/24f4f02d5b87ce0146e0455791e71aeb  --> 

Σκοπός του project είναι να φτιάξετε σε python ένα πρόγραμμα με το οποίο θα μπορεί να γίνουν [GWAS](https://en.wikipedia.org/wiki/Genome-wide_association_study) μελέτες. Τα GWAS (Genome Wide Association Studies) είναι μελέτες που προσπαθούν να βρουν μία στατιστική συσχέτιση μεταξύ ενός γονότυπου και ενώς φαινότυπου. Για τους σκοπούς αυτής της εργασίας έχουμε φτιάξει ένα τεχνιτό (artificial) genotype dataset. Αυτό το dataset βρίσκεται εδώ:

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
* -keep_samples   : Ένα αρχείο με κωδικούς sample ανά γραμμή. Ένα sample έχει κωδικό: (case ή control)\_αριθμός. Π.χ. το sample control_5 είναι το 5ο control. Το case_100 είναι το 100ό case. Η ανάλυση θα γίνεται ΜΟΝΟ σε αυτά τα samples.
* -remove_samples : Ένα αρχείο με κωδικούς sample ανά γραμμή (δες παραπάνω). Η ανάλυση θα γίνεται σε όλα τα samples εκτός από αυτά.

Αν έχει χρησιμοποιειθεί μία από τις παραπάνω 4 παραμέτρους τότε το πρόγραμμα θα πρέπει να δημιουργεί το αρχείο "output".cases.gen και "output".controls.gen το οποίο θα περιέχει μόνο τα SNPs/samples τα οποία δεν θα έχουν αφαιρεθεί. Το φορμάτ πρέπει να είναι αυτό που έχουμε περιγράψει. Το "output" είναι η τιμή της παραμέτρους -output.  

Για την ανάλυση των genotypes, το πρόγραμμα θα πρέπει να υποστηρίζει τις παρακάτω παραμέτρους:

* -association_test : Τυπώνει στο αρχείο "output".association τα αποτελέσματα από το association test μεταξύ genotype και phenotype για όλα τα SNPs. Για το association test χρησιμοποιείστε το απλό Genotypic Association test το οποίο περιγράφεται με μεγαλή σαφήνεια στο paper: [Basic statistical analysis in genetic case-control studies](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3154648/). (Αν θέλετε υλοποιήσετε περισσότερα tests π.χ. Cochran-Armitage trend). Το αρχείο πρέπει έχει μία γραμμή για κάθε SNP. Κάθε γραμμή θα περιέχει τον κωδικό του SNP, τη θέση του (locus), το p-value από το association test και το Odds Ratio. 

* -manhattan ONOMA_ARXEIOY.png : Φτιάχνει ένα [Manhattan plot](https://en.wikipedia.org/wiki/Manhattan_plot) από το p-values του association test και το σώζει στο αρχείο ONOMA_ARXEIOY.png. 

* -qqplot ONOMA_ARXEIOY.png : Φτιάχνει ένα [qq-plot](https://en.wikipedia.org/wiki/Q%E2%80%93Q_plot) από τα p-values του association test και το σώζει στο αρχείο με το όνομα ONOMA_ARXEIOY.png. 


### Σημείωση 1: Πως επαληθεύουμε (δεν είναι υποχρεωτικό).
* Υπάρχουν πολλά εργαλεία που έχουν σχεδιαστεί για GWA Studies και κάνουν κάποια από τα tasks που περιγράφονται εδώ. Δύο από τα πιο γνωστά είναι το [plink](http://pngu.mgh.harvard.edu/~purcell/plink/index.shtml) και το [SNPTEST](https://mathgen.stats.ox.ac.uk/genetics_software/snptest/snptest.html#introduction). Μπορείτε φυσικά αν θέλετε να τα χρησιμοποιήσετε για επιβεβαίωση αλλά θα πρέπει επιπλέον να υλοποιήσετε μεθόδους για τη μετατροπή των δεδομένων στο format των εργαλείων αυτών. 

### Σημείωση 2: Πως δημιουργήθηκε το artificial dataset (για όσους αναρωτιούνται)
Κατεβάζουμε το [hapgen2](https://mathgen.stats.ox.ac.uk/genetics_software/hapgen/hapgen2.html):

```bash
wget https://mathgen.stats.ox.ac.uk/genetics_software/hapgen/download/builds/x86_64/v2.2.0/hapgen2_x86_64.tar.gz
mkdir -p hapgen2
tar zxvf hapgen2_x86_64.tar.gz -C hapgen2 
```

Κατεβάζουμε το 1000 Genomes Project (August 2009 CEU haplotypes) - NCBI Build 36 (dbSNP b126) reference dataset:

```bash
wget https://mathgen.stats.ox.ac.uk/wtccc-software/CEU.0908.impute.files.tgz
tar zxvf CEU.0908.impute.files.tgz
```

Τρέχουμε το hapgen2:

```bash
hapgen2/hapgen2 \
    -m CEU.0908.impute.files/genetic_map_chr20_combined_b36.txt \
    -l CEU.0908.impute.files/CEU.0908.chr20.legend \
    -h CEU.0908.impute.files/CEU.0908.chr20.hap \
    -o ./gwas \
    -dl <location, risk allele and relative risks for each artificial disease risk variant, NOT SHOWN!!!>
    -n 500 500
```


### Παράδειγμα Manhattan plot με ένα χρωμόσωμα

Υπάρχει εδώ: http://2.bp.blogspot.com/-w1h3x3rpOLY/TbXVEHCr1cI/AAAAAAAALqI/wiQqpr1HJ6c/s400/2011-04-19+GGD+manhattan4.png 
(Αγνοήστε τα χρώματα αν θέλετε)

