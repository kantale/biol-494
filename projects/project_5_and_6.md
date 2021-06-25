

# Project 5 & Project 6

Η εισαγωγή για αυτά τα δύο projects είναι κοινή.

<!-- https://gist.github.com/kantale/993abe0fedb45703b0528abd7f048b42 -->
### Εισαγωγή
Σήμερα υπάρχουν πάρα πολλές βάσεις δεδομένων που περιέχουν πολύτιμη πληροφορία για οποιαδήποτε έννοια της γενετικής.
Κλασικά παραδείγματα είναι πληροφορίες για την ακολουθία ενός γονιδίου, τη θέση του στο γονιδιώματα, πόσα exons/introns έχει, κτλ.
Η αναζήτηση σε μία τέτοια βάση δεδομένων γίνεται συνήθως με δύο τρόπους. 
Ο πρώτος είναι να πάμε σε κάποιο site (π.χ. http://www.ensembl.org) και μέσα από τη περιήγησή μας αλλά και τα πεδία που θα δώσουμε σε διάφορες φόρμες να βρούμε τη πληροφορία που θέλουμε.
Ο δεύτερος τρόπος είναι να κάνουμε το ίδιο τρόπο προγραμματιστικά. 
Δηλαδή να φτιάξουμε ένα πρόγραμμα/script το οποίο θα "ρωτάει" μία βάση δεδομένων και θα τυπώνει το αποτέλεσμα.

Είναι προφανές ότι κάθε μέθοδος έχει τα θετικά και τα αρνητικά της. 
Το να αλληλεπιδρούμε με ένα site είναι αργό (και βαρετό) για επαναλαμβανόμενες ερωτήσεις ενώ ο προγραμματιστικός τρόπος απαιτεί τη γνώση κάποιας γλώσσας προγραμματισμού αλλά και τον τρόπο με τον οποία θα πρέπει να "μιλήσει" το πρόγραμμα με τη βάση.
Ένας τρόπος να το διαπιστώσουμε αυτό είναι να ρωτήσουμε κάποιον έμπειρο βιολόγο κάτι απλό, π.χ: πόσα exons έχει το γονίδιο APOE;
Μπορούμε στη συνέχεια να κάνουμε την ίδια ερώτηση σε έναν βιοπληροφορικό και να δούμε τον τρόπο που θα απαντήσουν στην ερώτηση. 
Με όποιον τρόπο επιλέξουν να απαντήσουν, θα διαπιστώσουμε (ίσως με έκπληξη) ότι μία τέτοια απλή ερώτηση απαιτεί αρκετή ώρα "ψαξίματος".
Δεν θα ήταν ωραίο, λοιπόν, να υπήρχε κάποιο site το οποίο να μπορούσες να του θέσεις σε φυσική γλώσσα, απλές ερωτήσεις της γενετικής και αυτό να σου απαντούσε;

Αυτό λοιπόν είναι και το αντικείμενο του project!
Θα πρέπει να φτιάξετε ένα πρόγραμμα το οποίο θα παίρνει ως είσοδο απλές ερωτήσεις γενετικής, να ψάχνει τις κατάλληλες βάσεις δεδομένων και να τυπώνει την απάντηση. Οι ερωτήσεις θα πρέπει να είναι στα Αγγλικά. 

### Οντότητες
Το πρόγραμμά σας καταρχήν θα πρέπει να μπορεί να αναγνωρίζει τις παρακάτων οντότητες από το κείμενο της ερώτησης:

* Γονίδιο
    * Ένα από τα ονόματα που αναγνωρίζει επίσημα το HGNC. Μπορείτε να πάρετε τη λίστα όπως είχε περιγραφεί στην [άσκηση 18, της 3ης σειράς](https://gist.github.com/kantale/ae81d885cc84ee03edb7d39513b7deaf). Το link είναι: ftp://ftp.ebi.ac.uk/pub/databases/genenames/new/tsv/locus_groups/protein-coding_gene.txt 

* Μετάγραφο (transcript)
    * [RefSeq μετάγραφα](https://www.ncbi.nlm.nih.gov/refseq/). π.χ: ```NM_001350497.1``` ή ```NM_001350497``` . Λίστα με όλα τα μετάγραφα σε RefSeq, υπάρχει [εδώ](https://www.ncbi.nlm.nih.gov/projects/genome/guide/human/index.shtml) (RefSeq Reference Genome Annotation). Δεν είναι απαραίτητο να κατεβάσετε αυτό το αρχείο.
    * [ENSEMBL μετάγραφα](https://www.ensembl.org/info/genome/genebuild/genome_annotation.html). Για παράδειγμα: ```ENST00000003084```.

* Μετάλλαξη: (σε αυτό το project θα ασχοληθούμε μόνο με [Single Nucleotide Polymorphisms](https://en.wikipedia.org/wiki/Single-nucleotide_polymorphism))
    * ```rs12345678``` . [dbSNP](https://www.ncbi.nlm.nih.gov/projects/SNP/) variants
    * ```chr1:1234567A>G``` . Δηλαδή στο χρωμόσωμα 1, στη θέση 1234567 το Α γίνεται G.
    * ```1:1234567A>G```
    * <Γονίδιο>:c.100A>G . Δηλαδή στη 100η coding θέση του γονιδίου το Α, γίνεται G. 
    * <Μετάγραφο>:c.100A>G . Στη 100η coding θέση του μετάγραφου το Α, γίνεται G.

* Θέση στο γονιδίωμα: (θα το αναφέρουμε απλά ως "Θέση")
    * ```1:1234567``` (Χρωμόσωμα 1, θέση 1234567)
    * ```chr1:1234567```
    * ```chromosome 1, position 1234567```
    * ```chromosome 1 and position 1234567```
    * <Μετάλλαξη> , η θέση της μετάλλαξης στο γονιδίωμα


### requests
H βιβλιοθήkη [requests](http://docs.python-requests.org/en/master/) είναι ίσως η πιο δημοφιλής βιβλιοθήκη της python η οποία δεν είναι μέρος της "επίσημης" έκδοσης της python. Παρέχει πολύ απλούς μηχανισμούς για να έχετε πρόσβαση σε online πηγές δεδομένων. Για να την εγκαταστήσετε κάντε στο shell:
```bash
pip install requests 
```

Στη συνέχεια μπορείτε να τη κάνετε import στη python:
```python
import requests
```

Μέσω της ```requests``` μπορείτε να χρησιμοποιείτε τους μηχανισμούς [GET και POST που υποστηρίζει το HTTP πρωτόκολο](https://www.w3schools.com/tags/ref_httpmethods.asp) για να ζητάτε και να παίρνετε δεδομένα από άλλα sites. Μπορείτε να δείτε και τις [περσινές σημειώσεις](https://gist.github.com/kantale/66e077dd377b2459fe58f854467c40cd) για το πως μπορείτε να το κάνετε αυτό. 

### Βασικές πηγές πληροφορίας
Πριν ξεκινήσετε θα πρέπει να μελετήσετε τις παρακάτω πολύ βασικές πηγές βιολογικής πληροφορίας.

#### [mygene.info](http://docs.mygene.info/en/latest/doc/data.html)
Το mygene.info είναι μία από τις πιο δημοφιλής, γρήγορη και σύγχρονη πηγή (μετα)μεταπληροφορία για γονίδια. Περιέχει πληροφορία για τη θέση, λειτουργία, μονοπάτια κτλ για όλα τα γονίδια από πολλούς οργανισμούς. 

Υπάρχει [αναλυτική περιγραφή στο documentation του mygene.info για το πως μπορούμε να κάνουμε GET requests για να πάρουμε διάφορες πληροφορίες για γονίδια](http://docs.mygene.info/en/latest/doc/query_service.html). 

Για παράδειγμα έστω ότι θέλουμε να βρούμε ποια είναι η θέση του γονιδίου TPMT. Μέσω της ```requests```:

```python
import requests

parameters = {
  'fields': 'genomic_pos',
  'species': 'human',
  'q' : 'symbol:tpmt',
}
url = 'http://mygene.info/v3/query'

response = requests.get(url, params=parameters)

```

Στη συνέχεια μπορούμε να δούμε αν όλα πήγαν καλά:

```python
response.ok # Αυτό πρέπει να είναι True
```

Αφού επιβεβαιώσουμε ότι το ```response.ok``` είναι ```True```, μπορούμε να πάρουμε το αποτέλεσμα σε μορφή json:

```python
data = response.json()
print (data)
```
```text
{'max_score': 88.12873,
 'took': 4,
 'total': 1,
 'hits': [{'_id': '7172',
   '_score': 88.12873,
   'genomic_pos': {'chr': '6',
    'end': 18155074,
    'ensemblgene': 'ENSG00000137364',
    'start': 18128311,
    'strand': -1}}]}
```

Βλέπουμε ότι υπάρχει ένα ```start``` και ένα ```end```. Μπορούμε να τα προσπελάσουμε:

```python
chromosome = data['hits'][0]['genomic_pos']['chr']
start = data['hits'][0]['genomic_pos']['start']
end = data['hits'][0]['genomic_pos']['end']
print (chromosome, start, pos)
# Τυπώνει: ('6', 18128311, 18155074)
```  

#### [myvariant.info](http://docs.myvariant.info/en/latest/)
Παρόμοια με το mygene.info υπάρχει και το [myvariant.info το οποίο παρέχει ένα API για πληροφορίες για μεταλλάξεις](http://docs.myvariant.info/en/latest/). 
Η πρόσβαση γίνεται μέσω GET requests. 
Για παράδειγμα ποια είναι η θέση της μετάλλαξης rs58991260;

```python
url = 'http://myvariant.info/v1/query'
parameters = {
    'q': 'rs58991260',
    'fields': 'dbsnp',
}

data = requests.get(url, params=parameters)
```
```python
data.ok # True
```
```python
chromsome = d['hits'][0]['dbsnp']['chrom']
start = d['hits'][0]['dbsnp']['hg19']['start']
end = d['hits'][0]['dbsnp']['hg19']['end']
print (chromosome, start, end)
## Τυπώνει: 6 218631822 218631822 
# To start με το end είναι το ίδιο αφού πρόκειται για SNP
```

Αν θέλετε μπορείτε να διαβάσετε και τη δημοσίευση:

> [Xin, Jiwen, et al. "High-performance web services for querying gene and variant annotation." Genome biology 17.1 (2016): 91.](https://genomebiology.biomedcentral.com/articles/10.1186/s13059-016-0953-9)


#### GENCODE
Η [GENCODE](https://www.gencodegenes.org/) είναι μία προσπάθεια ώστε να καταγραφούν όλα τα "λειτουργικά" κομμάτια του ανθρώπινου γονιδιώματος.
[Χρησιμοποιώντας διάφορες μεθοδολογίες](https://en.wikipedia.org/wiki/GENCODE#Methodology) (αυτόματες και με ανθρώπινο curation), καταγράφει σε ποιες περιοχές υπάρχουν γονίδια και πως τα γoνίδια αυτά χωρίζονται σε υπο-περιοχές (introns, exons, CDS, stop codons, start codon, 5' UTR και 3'UTR).


Σε αυτό το ftp site: ```ftp://ftp.ebi.ac.uk/pub/databases/gencode/Gencode_human/release_29/``` υπάρχουν όλα τα αρχεία με τη τελευταία έκδοση της GENCODE.
Ειδικά σε αυτό το αρχείο: ```ftp://ftp.ebi.ac.uk/pub/databases/gencode/Gencode_human/release_29/_README.TXT``` περιγράφεται τι περιέχει το κάθε αρχείο. Εκεί διαβάζουμε:

```
1. gencode.vX.annotation.{gtf,gff3}.gz:
  Main file, gene annotation on reference chromosomes in GTF and GFF3 file formats.
  These are the main GENCODE gene annotation files. They contain annotation (genes, 
  transcripts, exons, start_codon, stop_codon, UTRs, CDS) on the reference chromosomes,
  which are chr1-22, X, Y, M in human and chr1-19, X, Y, M in mouse.
```

Οπότε για αυτό το project θα χρησιμοποιήσουμε το ```gencode.v29.annotation.gff3.gz``` το οποίο μπορούμε να κατεβάσουμε απο εδώ: ftp://ftp.ebi.ac.uk/pub/databases/gencode/Gencode_human/release_29/gencode.v29.annotation.gff3.gz
Επίσης μπορείτε να μελετήσετε το [format gff3](http://gmod.org/wiki/GFF3) το οποίο χρησιμοποιεί η GENCODE.
Η ίδια πληροφορία υπάρχει και σε ένα άλλο format το οποίο λέγεται GTF, αλλά το GFF3 θεωρείται λίγο πιο εξελιγμένο. Μπορείτε να [διαβάσετε περισσότερα εδώ](https://www.biostars.org/p/99462/).

Ας κατεβάσουμε λοιπόν το αρχείο από το command line:
```bash
wget ftp://ftp.ebi.ac.uk/pub/databases/gencode/Gencode_human/release_29/gencode.v29.annotation.gff3.gz 
```

Μέσα σε αυτό το αρχείο βρίσκουμε αυτές τις γραμμές:
(Εχω κρατήσει μόνο ένα συγκεκριμμένο μήκος για κάθε γραμμή)
```
chr1    ENSEMBL transcript      2586750 2591467 .       +       .       ID=ENST00000444521.6;Parent=ENSG00000157870.15;
chr1    ENSEMBL exon    2586750 2586948 .       +       .       ID=exon:ENST00000444521.6:1;Parent=ENST00000444521.6;
chr1    ENSEMBL CDS     2586796 2586948 .       +       0       ID=CDS:ENST00000444521.6;Parent=ENST00000444521.6;
chr1    ENSEMBL start_codon     2586796 2586798 .       +       0       ID=start_codon:ENST00000444521.6;Parent=ENST00000444521.6;
chr1    ENSEMBL exon    2587091 2587295 .       +       .       ID=exon:ENST00000444521.6:2;Parent=ENST00000444521.6;
chr1    ENSEMBL CDS     2587091 2587295 .       +       0       ID=CDS:ENST00000444521.6;Parent=ENST00000444521.6;
chr1    ENSEMBL exon    2587741 2587792 .       +       .       ID=exon:ENST00000444521.6:3;Parent=ENST00000444521.6;
chr1    ENSEMBL CDS     2587741 2587792 .       +       2       ID=CDS:ENST00000444521.6;Parent=ENST00000444521.6;
chr1    ENSEMBL exon    2588336 2588453 .       +       .       ID=exon:ENST00000444521.6:4;Parent=ENST00000444521.6;
chr1    ENSEMBL CDS     2588336 2588453 .       +       1       ID=CDS:ENST00000444521.6;Parent=ENST00000444521.6;
chr1    ENSEMBL exon    2588550 2588625 .       +       .       ID=exon:ENST00000444521.6:5;Parent=ENST00000444521.6;
chr1    ENSEMBL CDS     2588550 2588625 .       +       0       ID=CDS:ENST00000444521.6;Parent=ENST00000444521.6;
chr1    ENSEMBL exon    2588922 2589040 .       +       .       ID=exon:ENST00000444521.6:6;Parent=ENST00000444521.6;
chr1    ENSEMBL CDS     2588922 2589040 .       +       2       ID=CDS:ENST00000444521.6;Parent=ENST00000444521.6;
chr1    ENSEMBL exon    2589410 2591467 .       +       .       ID=exon:ENST00000444521.6:7;Parent=ENST00000444521.6;
chr1    ENSEMBL CDS     2589410 2589427 .       +       0       ID=CDS:ENST00000444521.6;Parent=ENST00000444521.6;
chr1    ENSEMBL stop_codon      2589425 2589427 .       +       0       ID=stop_codon:ENST00000444521.6;Parent=ENST00000444521.6;
chr1    ENSEMBL five_prime_UTR  2586750 2586795 .       +       .       ID=UTR5:ENST00000444521.6;Parent=ENST00000444521.6;
chr1    ENSEMBL three_prime_UTR 2589428 2591467 .       +       .       ID=UTR3:ENST00000444521.6;Parent=ENST00000444521.6;
chr1    ENSEMBL transcript      2586750 2591467 .       +       .       ID=ENST00000378425.9;Parent=ENSG00000157870.15;
```

Τι σημαίνουν όλα αυτά; Αυτά είναι τα δομικά στοιχεία μίας μεταγραφής (ENST00000444521.6) ενός γονιδίου (PRXL2B). 
Ένα γονίδιο μπορεί να μεταγραφεί με πολλούς τρόπους, ή αλλιώς σε πολλά μετάγραφα (transcripts). 
Στο παράδειγμά μας βλέπουμε τα δομικά στοιχεία του μετάγραφου ENST00000444521.6 .
Ένα μετάγραφο περιέχει exons και introns.
Το πρώτο exon αποτελείται από τη περιοχή 5'UTR και τη περιοχή CDS (CoDing Sequence).
H περιοχή CDS του πρώτου exon αρχίζει από το start codon.
Στα exons που δεν είναι πρώτα ή τελευταία η περιοχή CDS ταυτίζεται με τη περιοχή του exon.
Το τελευταίο exon αποτελείται από το CDS και 3'UTR. 
To CDS του τελευταίου exon τελειώνει με το stop codon.

Παρακάτω υπάρχει ένα διάγραμμα με τη παραπάνω πληροφορία ([powerpoint version](https://www.dropbox.com/s/vo36k1syab5fp35/6b1cafa6581b4ae1b90d69b93858c49e.pptx?dl=0)). 
![img](https://i.imgur.com/84rY2x0.png)


Άρα από το αρχείο ```gencode.v29.annotation.gff3.gz``` μπορούμε να ξέρουμε τι ακριβώς μπορεί να βρούμε σε οποιαδήποτε περιοχή του γoνιδιώματος. 


Αν παρατηρήσουμε το αρχείο θα δούμε ένα βασικό πρόβλημα: Για κάθε γονίδιο υπάρχουν πολλά transcripts. 
Αυτό είναι γνωστό από τη βιολογία, ότι ένα γονίδιο μπορεί να έχει πολλά μετάγραφα λόγω ενός φαινομένου που ονομάζεται [alternative splicing](https://en.wikipedia.org/wiki/Alternative_splicing).
Πως μπορώ να ξέρω εγώ ποιο είναι το πιο "βασικό";
Δηλαδή για πιο transcript θα απαντάει το πρόγραμμά μου;
Για να το λύσουμε αυτό υπάρχουν δύο τρόποι. 

Ο πρώτος είναι να συμβουλευτούμε τη βάση δεδομένων [appris](http://appris.bioinfo.cnio.es), η οποία έχει τη πληροφορία "πόσο βασικό" είναι ένα transcript για όλα τα γονίδια. 
Η appris έχει φτιάξει ένα [σύστημα ιεραρχικοποιήσης των transcripts](http://appris.bioinfo.cnio.es/#/downloads).
Ιεραρχικοποιεί τα transcripts με 8 tags: PRINCIPAL:1, PRINCIPAL:2, PRINCIPAL:3, PRINCIPAL:4, PRINCIPAL:5, ALTERNATIVE:1, ALTERNATIVE:2 και MINOR.
Τα transcripts τα οποία είναι πιο "πάνω" στην ιεραρχία είναι και τα πιο βασικά. 
Μπορείτε να κατεβάσετε και όλη τη βάση appris από [αυτό το link](http://appris.bioinfo.cnio.es/#/downloads).

Ο δεύτερος τρόπος είναι να χρησιμοποιήσετε το πεδίo ```tag```, στο αρχείο από το GENCODE. 
Εκεί θα δείτε να υπάρχει σε κάποια transcripts, η πληροφορία ```tag=basic,appris_principal_2,CCD``` το οποίο αντιστιχεί και στη τιμή που έχει δόσει η appris. 
Αν ένα entry δεν έχει αυτή τη πληροφορία μπορείτε να το αγνοείται.

Μπορείτε να υλοποιήσετε οποιαδήποτε από τις δύο μεθόδους για να βρίσκετε το primary transcript ενός γονιδίου. 

#### Ensembl Sequence Region
H Ensembl δίνει το παρακάτω API: https://rest.ensembl.org/documentation/info/sequence_region με το οποίο μπορείτε να ζητήσετε το γονιδίωμα αναφοράς για οποιαδήποτε περιοχή.
Στο site αυτό δίνονται παραδείγματα καθώς και python 3 κώδικας. 

#### Ensembl Variant Effect Predictor (VEP)
Επίσης η Ensembl δίνει το παρακάτω API: https://rest.ensembl.org/documentation/info/vep_hgvs_get . To API αυτό δίνει πληροφορίες για μεταλλάξεις. Όπως βλέπετε και από το documentation υποστηρίζει μεταλλάξεις όπως: ```<Γονίδιο>:c.100A>T``` και ```<Ensembl Transcript>:c.100A>G```.

Αν έχετε βρει κάποιο άλλο API ή dataset το οποίο κάνει αυτές τις λειτουργίες εννοείται ότι μπορείτε να το χρησιμοποιήσετε. 

### Tasks
Τώρα που ξέρουμε πως να πάρουμε πληροφορία από το mygene.info, myvariant.info, το GENCODE, Ensembl Sequence Region και VEP, μπορούμε επιτέλους να απαντάμε στις πιο συχνές ερωτήσεις που έχουν οι βιολόγοι και βιοπληροφορικοί σχετικά με το ανθρώπινο γονιδίωμα. 
Σε αυτό το project λοιπόν, θα πρέπει να υλοποιήσετε ένα πρόγραμμα σε python το οποίο θα παίρνει σαν input μία ερώτηση στην Αγγλική γλώσσα και θα τυπώνει την απάντηση.
Το πρόγραμμά σας θα πρέπει να τρέχει από command line και θα πρέπει να δέχεται μία παράμετρο: ```-q <question>``` ή ```--question <question>```. 
Για παράδειγμα:
```bash
python project.py -q "What is the location of the gene TPMT?"
```
Στο οποίο θα τυπώνει κάτι σαν:
```text
chr 6
18128311-18155074
6p22.3
```

Στη python μπορείτε να πάρετε ορίσματα από τη γραμμή εντολών χρησιμοποιώντας τη βιβλιοθήκη [argparse](https://docs.python.org/3/library/argparse.html).
Για παράδειγμα για να διαβάσετε το όρισμα που δίνεται είτε με ```-q``` είτε με ```--question```, ένας τρόπος είναι:

```python
import argparse

if __name__ == '__main__':
   parser = argparse.ArgumentParser(description='The best python project ever')
   
   parser.add_argument('-q', '--question', help='Your question in english')

   args = parser.parse_args()
   question = args.question

   print ('The question asked is:', question)
```

Σε [αυτό το post](https://stackoverflow.com/questions/419163/what-does-if-name-main-do) υπάρχει μία πολύ καλή εξήγηση του τι κάνει το ```if __name__ == '__main__':```.

###  Project 5. Εμφάνιση exon/intron map 
Ο σκοπός αυτού του project είναι να φτιάξετε ένα γράφημα με τα intron/exon maps όπως κωδικοποιείται στο GENCODE.

Το πρόγραμμά σας θα παίρνει μία από τις παρακάτω παραμέτρους
* --gene όνομα_γονιδίου
* --transcript όνομα_ματάγραφου 
* --mutation όνομα_μετάλλαξης

Αν δοθεί η παράμετρος ```--gene``` τότε θα φτιάχνει το intron / exon map του κύριου μετάγραφου (primary transcript) του γονιδίου της παραμέτρου. Αν δοθεί η παράμετρος ```--transcript``` τότε θα φτιάχνει το intro/exon map αυτού του μετάγραφου. Αν δοθεί η παράμετρος ```--mutation``` τότε θα φτιάχνει το intro/exon map του κύριου μετάγραφου του γονιδίου που βρίσκεται η μετάλλαξη (αν η μετάλλαξη δεν είναι σε γονίδιο, πετάει ένα μήνυμα λάθους). 

Το πρόγραμμά σας λοιπόν θα πρέπει να βγάζει ένα γράφημα με το intron/exon map κάποιου μετάγραφου. 
Τι είναι αυτό όμως;

Ένα παράδειγμα αμφιβόλου αισθητικής, που έφτιαξα, είναι εδώ:

![img](https://i.imgur.com/5Tze5nC.png)

Μπορείτε να βρείτε πολλά παρόμοια στα Internets αν γκουγκλάρετε "exon/intron map" και ψάξετε για images. Υπάρχει και [σχετική συζήτηση στο biostars](https://www.biostars.org/p/17841/)
Προσέξτε ότι αν δηλωθεί η παράμετρος ```--mutation``` τότε η θέση της μετάλλαξης θα πρέπει να φαίνεται στο γράφημα. 


#### intron/exon map with string representation.
Αντί για το γράφημα με το intron/exon map που σας ζητήθηκε, αν θέλετε μπορείτε να το υλοποιήσετε έτσι ώστε το πρόγραμμά σας να βγάζει το ίδιο γράφημα αλλά σε text!
Μπορείτε να "πάρετε" χαρακτήρες για τους πίνακες από της [σελίδα της wikipedia για box drawing](https://en.wikipedia.org/wiki/Box-drawing_character#Unicode):
Δηλαδή μία αναπαράσταση σε κείμενο του γραφήματος που έδωσα στο παράδειγμα είναι:
```text
      Gene: PRXL2B
      Transcript: ENST00000444521.6

      ╔═════════════════════════════╗      ╱╲      ╔══════════════════════════════╗      ╱╲      ╔══════════════╗      ╱╲      ╔════════════════════════════╗
      ║            Exon 1           ║     ╱  ╲     ║            Exon 2            ║     ╱  ╲     ║    Exon 3    ║     ╱  ╲     ║            Exon 4          ║
      ╟──────────────┬──────────────╢    ╱    ╲    ╟──────────────┬───────────────╢    ╱    ╲    ╟──────────────╢    ╱    ╲    ╟──────────────┬─────────────╢
      ║    5'UTR     │    CDS       ║   ╱      ╲   ║              █               ║   ╱      ╲   ║              ║   ╱      ╲   ║     CDS      │    3'UTR    ║
      ╟──────────────┼──────────────╢  ╱        ╲  ║              █               ║  ╱        ╲  ║              ║  ╱        ╲  ╟──────────────┼─────────────╢
      ║              │              ║ ╱          ╲ ║              █               ║ ╱          ╲ ║              ║ ╱          ╲ ║              │             ║
      ║              │              ║╱            ╲║              █               ║╱            ╲║              ║╱            ╲║              │             ║
 123,456,789    123,456,890    123,458,895    123,459,345    123,459,445     123,459,545    123,460,765    123,460,865    123,461,865    123,462,543   123,462,865
                                                               **A>G**

```

Σημείωση: στο τερματικό μου [εμφανίζει κάτι σαν χριστουγεννιάτικα δέντρα](https://i.imgur.com/U2uC8t8.png), στις συνδέσεις των exons (γραμματοσειρά: Andale Mono).

**Σημείωση:** Για να τεστάρετε την υλοποίησή σας μπορείτε να πάρετε και μεταλλάξεις από το HBA1, ένα μικρό και "εύκολο" γονίδιο. Μπορείτε να βρείτε όλες τις μεταλλάξεις αυτού του γονιδίου εδώ: https://gnomad.broadinstitute.org/gene/ENSG00000206172?dataset=gnomad_r2_1 

### Project 6. Απάντηση ερωτημάτων του χρήστη.
Σε αυτό το project το πρόγραμμά σας θα πρέπει να απαντάει στις ερωτήσεις. 
Παραθέτω τα ελάχιστα ερωτήματα που πρέπει να υποστηρίζει το πρόγραμμά σας (και στα οποία θα βαθμολογηθείτε). 
Προφανώς και μπορείτε να τα επεκτείνετε όπως θέλετε εσείς. 
Για κάθε ερώτημα παραθέτω μερικές οδηγίες ή links για το πως μπορεί το πρόγραμμα σας να τις απαντήσει και κάποιες ενδεικτικές απαντήσεις. 
Εσείς μπορείτε να ακολουθήσετε διαφορετικές προσεγγίσεις για να τις απαντήσετε και μπορούν οι απαντήσεις σας να έχουν διαφορετική μορφή (αρκεί φυσικά να υπάρχει η ζητούμενη πληροφορία). 


1. "Which gene is upstream to gene <Γονίδιο> ?". Χρησιμοποιήστε το GENCODE. 
```
NHLRC1
```

Επίσης: "Which gene is downstream?", "Which gene is closest?"

2. "How many transcripts does the gene <Γονίδιο> have?" Χρησιμοποιήστε το GENCODE ή το mygene.info [link](http://mygene.info/v3/query?q=symbol:tpmt&fields=exons&species=human) (ή και τα δύο..)
```
[Τυπώστε μία λίστα με όλα τα διαφορετικά μετάγραφα και αναφέρεται πιο είναι το primary]
```

Επίσης: "Which transcripts exist for gene <Γονίδιο> ?"

3. "What is in <Θέση> ?" (Χρησιμοποιήστε το GENCODE)  

Παράδειγμα απάντησης:
```
This the 100th nucleotide of the 2nd exon of gene PRXL2B for transcript ENST00000444521.6. The length of this exon is XXX . downstream element is an intron in XXX bases. upstream element is an intron in XXX bases.
[Συμπληρώστε κατάλληλες τιμές για τα XXX]
Προσθέστε την ακολουθία του γονιδιώματος αναφοράς για -50 και +50 θέσεις από τη <Θέση> 
```

Για να βρείτε την ακολουθία μίας περιοχής του γονιδιώματος, μπορείτε να χρησιμοποιήσετε το ```sequence_region``` service της Ensembl: https://rest.ensembl.org/documentation/info/sequence_region

Αν δεν υπάρχει γονίδιο σε αυτή τη θέση μπορείτε να τυπώσετε:
```
This is an intergenic region.
Upstream closest gene is TP73 upstream in XXX bases.
Downstream closest gene is YYY downstream in ZZZ bases
```

Αν είναι μετάλλαξη αναφέρεται και το reference, alternative, sequence change και protein change [link](http://myvariant.info/v1/query?q=rs1815739)

Π.χ: "What is the location of the mutations <Μετάλλαξη> ?" ή ""What is the location of <Μετάλλαξη> ?"
```
chromosome: 11
position: 66328095
reference: C
alternative: T
Type: SNP
Gene: ACTN3
Transcript NM_001104.3, sequence change: c.1729C>T, protein change: p.Ter577Ter
Transcript NM_003793.3, sequence change: c.*3309G>A, protein change: ---
```

Η πληροφορία για τα transcripts, sequence change και protein change, υπάρχει στη myvariant.info. Παράδειγμα screenshot output από το myvariant.info: https://imgur.com/GOUFskO 

To myvariant.info μπορεί να επιστρέψει και πληροροφορίες για μια μετάλλαξη έχοντας μόνο της θέση της. Π.χ: http://myvariant.info/v1/query?q=chr3:8762685-8762685 

Επίσης: "What is the reference and alternative of <Μετάλλαξη> ?", "What type of mutation is <Μετάλλαξη> ?"


4. "What is the name of the gene <Γονίδιο> ?" (Χρησιμοποιήστε το mygene.info) [link](http://mygene.info/v3/query?q=symbol:tpmt&fields=name&species=human) [link2](http://mygene.info/v3/query?q=symbol:TPMT&fields=other_names&species=human)

Παράδειγμα για TPMT:
```
thiopurine methyltransferase

Other names:
S-adenosyl-L-methionine:thiopurine S-methyltransferase
thiopurine S-methyltransferase
```

5. "Where is the location of <Γονίδιο, μετάγραφο ή μετάλλαξη> ?" [link 1](http://mygene.info/v3/query?q=symbol:TPMT&fields=map_location&species=human) [link 2](http://mygene.info/v3/query?q=symbol:tpmt&fields=genomic_pos&species=human) [link 3](http://mygene.info/v3/query?q=symbol:tpmt&fields=genomic_pos.chr&species=human)

Π.χ για γονίδιο:
```
chr 6
18128311-18155074
6p22.3
```

Επίσης: "What is the chromosome of <...> ?", "What is the size of <...> ?", "Where is the start of <...> ?", "Where is the end of <...> ?"


6. "Which are the refseq transcripts of the gene <Γονίδιο> ?". Μπορείτε να χρησιμoποιήσετε το ftp://ftp.ebi.ac.uk/pub/databases/gencode/Gencode_human/release_29/gencode.v29.metadata.RefSeq.gz όπου υπάρχει αντιστοιχία μεταξύ ENSEMBL και RefSeq transcripts. Εναλλακτικά μπορείτε να χρησιμοποιήστε το mygene.info [link](http://mygene.info/v3/query?q=symbol:TPMT&fields=refseq&species=human)

Για παράδειγμα:
```
Which are the refseq transcripts of the gene TPMT?
```

```
[NM_000367, NM_001346817, NM_001346818]
[Also report which is the primary transcript. For example: NM_000367 is the primary]
```

7. "How many exons does <Γονίδιο ή Μετάγραφο> have ?". Μπορείτε να χρησιμοποιήσετε το GENCODE ή το mygene.info [link](http://mygene.info/v3/query?q=symbol:TPMT&fields=exons&species=human). Αν είναι γονίδιο πάρτε το primary transcript.

```
[List the start/end positions for all exons]
Chromosome 9
[18128313, 18130780],
[18132132, 18132177],
[18133803, 18133889],
[18138962, 18139037],
[18139664, 18139717],
[18143595, 18143728],
[18147822, 18147915],
[18148987, 18149171],
[18155032, 18155169]
```

Επίσης: "What are the locations of the exons of the gene <Γονίδιο> ?"


8. "Where is the location of the CDS of the <Γονίδιο ή Μετάγραφο> ?". Επίσης GENCODE ή mygene.info ([ίδιο link με πριν](http://mygene.info/v3/query?q=symbol:TPMT&fields=exons&species=human)). Αν είναι <Γονίδιο> πάρτε το primary transcript
```
Chromosome 9
[18149127, 18130667]
```

Επίσης: "Where is the location of the start codon?", "Where is the location of end codon?", "Where is the location of 3' UTR?", "Where is the location of the 5' UTR?"

9. "What is the primary transcript of the gene <Γονίδιο> ?" 
```
Refseq: NM_000367
Ensembl: ENST00000419916
```

10. "In which gene does <Μετάγραφο, Μετάλλαξη ή θέση> belong"? 

<!--
11. "What is the fasta sequence of the transcript NM_001346817 ?"
```python
entrez_request()
```


Επίσης: "What is the fasta sequency of the gene TPMT" (φέρνει το FASTA από το primary transcript)
-->



