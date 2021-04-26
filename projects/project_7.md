
# Project 7
<!-- https://github.com/kantale/python_lessons/blob/master/2019_2020/assignment_5.ipynb -->

## Μέρος 1
Χρησιμοποιώντας το [Rest API της ENSEMBL](https://rest.ensembl.org/), φτιάξτε μία συνάρτηση η οποία θα παίρνει ένα χρωμόσωμα μία αρχή και ένα τέλος και θα επιστρέφει την ακολουθία του ανθρώπινου γονιδιώματος για αυτή τη περιοχή. 

Hint: https://rest.ensembl.org/documentation/info/sequence_region

## Μέρος 2
Χρησιμοποιώντας το REST API του [myvariant.info](http://docs.myvariant.info/en/latest/), φτιάξτε μία συνάρτηση η οποία θα παιρνει ένα χρωμόσωμα μία αρχή και ένα τέλος και θα επιστρέφει μία λίστα με γνωστές μεταλλάξεις που ανήκουν σε αυτή τη περιοχή. Κάθε μετάλλαξη θα πρέπει να έχει τον κωδικό ```rs<Number>```.

Προσοχή το myvariant.info δεν επιστρέφει όλες τις μεταλλάξεις γιατί ειδικά σε μεγάλες περιοχές αυτή η λίστα μπορεί να έχει τεράστιο μέγεθος. Αντίθετα έχει δύο διαφορετικούς μηχανισμούς ώστε να μπορεί να πάρει κάποιος όλα τα αποτελέσματα.

Ο πρώτος μηχανισμός περιγράφεται εδώ:
http://docs.myvariant.info/en/latest/doc/variant_query_service.html#faceted-queries

Και ο δεύτερος περιγράφεται εδώ:
http://docs.myvariant.info/en/latest/doc/variant_query_service.html#scrolling-queries 

Εσείς μπορείτε να υλοποιήσετε όποιον θέλετε (ή και τους δύο..)

### Μέρος 3
Χρησιμοποιώντας το REST API του myvariant.info, φτιάξτε μία συνάρτηση η οποία θα παίρνει μία μετάλλαξη με τη μορφή ```rs<number>``` και θα επιστρέφει την ασθένεια με την οποία σχετίζεται. 

Για παράδειγμα για το rs374032054 [θα πρέπει να βγάλει](http://myvariant.info/v1/query?q=rs374032054): ```["Congenital disorder of glycosylation type Ir (CDG1R)"]```. Το αποτέλεσμα θα είναι μία λίστα με όλες τις πιθανές ασθένειες (μπορεί να είναι πάνω από μία). Η λίστα μπορεί να είναι και άδεια.


### Μέρος 4
Έστω ότι έχουμε μία ακολουθία DNA. Δίνεται ο παρακάτω κώδικας για τη μετατροπή της ακολουθίας σε φορμάτ fasta


```python
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord

def convert_sequence_to_fast(sequence, fasta_filename, id, description):
    sequence = Seq(sequence)
    # http://biopython.org/DIST/docs/tutorial/Tutorial.html#htoc16
    sequence_record = SeqRecord(sequence, id=id, description=description)

    with open(fasta_filename, "w") as output_handle:
        SeqIO.write(sequence_record, output_handle, "fasta")


```


```python
convert_sequence_to_fast('AGAAGACGATGCTGTAGATGAAGAGCCCCA', 'example.fasta', 'mitsos', 'my precious sequence')
```


```python
!cat example.fasta
```

    >mitsos my precious sequence
    AGAAGACGATGCTGTAGATGAAGAGCCCCA


Δίνεται επίσης ο παρακάτω κώδικας ο οποίος διαβάζει μία ακολουθία από ένα αρχείο fasta και τη κάνει [BLAT](https://en.wikipedia.org/wiki/BLAT_(bioinformatics) ) στο ανθρώπινο γονιδιώμα χρησιμοποιώντας την [αντίστοιχη υπηρεσία του NCBI](https://blast.ncbi.nlm.nih.gov/Blast.cgi)


```python
# Running BLAST over the Internet
# http://biopython.org/DIST/docs/tutorial/Tutorial.html#htoc16

from Bio.Blast import NCBIWWW

def blat_fasta(fasta_filename, output_filename):
    fasta_string = open(fasta_filename).read()
    #result_handle = NCBIWWW.qblast("blastn", "nt", fasta_string)
    #result_handle = NCBIWWW.qblast("blastn", "Human G+T", fasta_string)
    print ('fasta string:')
    print (fasta_string)
    result_handle = NCBIWWW.qblast(
        "blastn", 
        #"Human G+T",
        #"GPIPE/9606/current/ref_top_level", # GRCH38
        "GPIPE/9606/105/ref_top_level", #GRCH37
        fasta_string, 
        short_query=True,
        expect=1000,
        nucl_reward=1,
        nucl_penalty=-3,
        filter='F',
    )
    
    # Gia th diafora meta3u 'nt' kai 'Human G+T' deite edw:
    # https://ftp.ncbi.nlm.nih.gov/pub/factsheets/HowTo_BLASTGuide.pdf 
    # Source code of qblast: https://biopython.org/DIST/docs/api/Bio.Blast.Applications-pysrc.html
    with open(output_filename, "w") as out_handle:
        out_handle.write(result_handle.read())

    
```


```python
blat_fasta('example.fasta', 'example_blat_results.xml')
```

    fasta string:
    >mitsos my precious sequence
    AGAAGACGATGCTGTAGATGAAGAGCCCCA
    


Επίσης δίνεται και ο παρακάτω **ενδεικτικός** κώδικας ο οποίος διαβάζει και "παρσάρει" τα αποτελέσματα του BLAT alignment:


```python
# http://biopython.org/DIST/docs/tutorial/Tutorial.html#htoc16
# 7.3  Parsing BLAST output
from Bio.Blast import NCBIWWW
from Bio.Blast import NCBIXML

def parse_BLAT_output(blat_filename):
    result_handle = open(blat_filename)
    blast_records = NCBIXML.parse(result_handle)
    
    E_VALUE_THRESH = 0.04
    for blast_record in blast_records:
        for alignment in blast_record.alignments:
            for hsp in alignment.hsps:
                if hsp.expect < E_VALUE_THRESH:
                    print("****Alignment****")
                    print ('Query start:', hsp.query_start)
                    print ('Query end:', hsp.query_end)
                    print ('Subject start:', hsp.sbjct_start)
                    print ('Subject end:', hsp.sbjct_end)
                    print("sequence:", alignment.title)
                    print("length:", alignment.length)
                    print("e value:", hsp.expect)
                    print(hsp.query)
                    print(hsp.match)
                    print(hsp.sbjct)
                    #print (dir(hsp))
                    return alignment, hsp
        
```


```python
parse_BLAT_output('example_blat_results.xml')
```

    ****Alignment****
    Query start: 1
    Query end: 30
    Subject start: 20978904
    Subject end: 20978933
    sequence: gi|224589800|ref|NC_000001.10| Homo sapiens chromosome 1, GRCh37.p13 Primary Assembly
    length: 249250621
    e value: 8.41803e-06
    AGAAGACGATGCTGTAGATGAAGAGCCCCA
    |||||||||||||| |||||||||||||||
    AGAAGACGATGCTGAAGATGAAGAGCCCCA





    (<Bio.Blast.Record.Alignment at 0x106817810>,
     <Bio.Blast.Record.HSP at 0x103fe5090>)



Προσέχτε ότι:
* Tο hsp.sbjct_start περιέχει τη θέση τη θέση της ακολουθίας όπου έγινε το allignment
* Από τα hsp.query, hsp.match, hsp.sbjct μπορούμε να δούμε που έγινε misalignment
* Το blast_records είναι τόσα όσα οι ακολουθίες του fasta αρχείου (στη περίπτωσή μας 1)
* Το blast_record.alignments περιέχει όλα τα alignments που βρέθηκαν για τη κάθε ακολουθία. Μία ακολουθία μπορεί να έχει γίνει align σε παραπάνω από μία περιοχή του γονιδιώματος
* Το alignment.hsps περιέχει όλες τις διαφορετικές ακολουθίες του κάθε algignment.
* Το hsp.expect είναι ένα metric του πόσο καλά πήγε το alignment, όσο μικρότερο τόσο το καλύτερο..

Χρησιμοποιώντας τα παραπάνω φτιάξτε μία συνάρτηση η οποία θα πάρει ένα DNA sequence και θα επιστρέφει τη θέση στο ανθρώπινο γονιδίωμα με τις οποίες διαφέρει. 

Για να γίνει αυτό θα πρέπει να βρείτε ένα κατάλληλο alignment. Το aligment αυτό θα πρέπει να έχει μικρό hsp.expect και επίσης να έχει στη περιγραφή του το "Primary Assembly".

Πάρτε μόνο το πρώτο blast_record.alignments και από αυτό, πάρτε μόνο το πρώτο alignment.hsps. 

Για να τα υλοποιήσετε θα πρέπει ίσως να χρειαστεί να αλλάξετε τη συνάρτηση parse_BLAT_output. Επίσης η δυνάρτησή σας θα πρέπει να επιτρέφει μία μόνο μετάλλαξη (αν βρει πολλές απλά πάρτε τη πρώτη).

Για παράδειγμα για το sequence 'AGAAGACGATGCTGTAGATGAAGAGCCCCA'. Είδαμε ότι η αρχή το (Α) έγινε allign στη θέση 20652411. Επίσης βλέπουμε ότι στη θέση 15 της ακολουθίας υπάρχει ένα misalignment:



```python
alignment, hsp = parse_BLAT_output('example_blat_results.xml')
```

    ****Alignment****
    Query start: 1
    Query end: 30
    Subject start: 20978904
    Subject end: 20978933
    sequence: gi|224589800|ref|NC_000001.10| Homo sapiens chromosome 1, GRCh37.p13 Primary Assembly
    length: 249250621
    e value: 8.41803e-06
    AGAAGACGATGCTGTAGATGAAGAGCCCCA
    |||||||||||||| |||||||||||||||
    AGAAGACGATGCTGAAGATGAAGAGCCCCA



```python
print (hsp.query)
print (hsp.match)
print (hsp.sbjct)
```

    AGAAGACGATGCTGTAGATGAAGAGCCCCA
    |||||||||||||| |||||||||||||||
    AGAAGACGATGCTGAAGATGAAGAGCCCCA



```python
print (hsp.query[14])
print (hsp.match[14])
print (hsp.sbjct[14])
```

    T
     
    A


H θέση αυτή του misalignment είναι η:


```python
position = hsp.sbjct_start + 14
position
```




    20978918



Και σύμφωνα με το ID της ακολουθίας:


```python
alignment.title
```




    'gi|224589800|ref|NC_000001.10| Homo sapiens chromosome 1, GRCh37.p13 Primary Assembly'



Το χρωμόσωμα είναι το 1 και η έκδοση του γονιδιώματος είναι η 37. Επίσης είδαμε ότι το reference είναι το A και το alternative το T (που έχει η ακολουθία μας)

Άρα θα πρέπει να φτιάξετε μία συνάρτηση η οποία παίρνει ένα sequence και θα πρέπει να επιστρέφει τη μετάλλαξη που περιέχει αυτό το sequence αν το συγκρίνουμε με το γονδίωμα αναφοράς. Για παράδειγμα αν f είναι αυτή η συνάρτηση τότε θα πρέπει:

```python
f('AGAAGACGATGCTGTAGATGAAGAGCCCCA')
```

Αυτό θα πρέπει να επιστρέφει:
```
{
    'chromosome': 1,
    'position': 20978918,
    'reference: 'A',
    'alternative': 'T',
    'assembly': 'GRCh37',
}
```

Αν δεν βρει μετάλλαξη τότε θα επιστρέφει None.

## Μέρος 5
(συνέχεια από το προηγούμενο μέρος)

Άραγε αυτή η μετάλλαξη που βρήκαμε στο 4ο μέρος, είναι γνωστή, και αν είναι σχετίζεται με κάποια ασθένεια; Ας ψάξουμε αν το myvariant.info έχει πληροφορία από τη clinvar:


```python
import requests

r = requests.get("http://myvariant.info/v1/variant/chr1:g.20978918A>T", headers={ "Content-Type" : "application/json"})
```


```python
data = r.json()
'clinvar' in data
```




    True



Παρατηρούμε ότι όντως έχει πληροφορία!


```python
data['clinvar']
```




    {'_license': 'http://bit.ly/2SQdcI0',
     'allele_id': 576081,
     'alt': 'T',
     'chrom': '1',
     'cytogenic': '1p36.12',
     'gene': {'id': '1650', 'symbol': 'DDOST'},
     'hg19': {'end': 20978918, 'start': 20978918},
     'hg38': {'end': 20652425, 'start': 20652425},
     'hgvs': {'coding': 'NM_005216.4:c.1325T>A',
      'genomic': ['NC_000001.10:g.20978918A>T',
       'NC_000001.11:g.20652425A>T',
       'NG_008164.1:g.23971A>T',
       'NG_032064.1:g.14120T>A']},
     'rcv': {'accession': 'RCV000709770',
      'clinical_significance': 'not provided',
      'conditions': {'identifiers': {'medgen': 'C3281084',
        'omim': '614507',
        'orphanet': '300536'},
       'name': 'Congenital disorder of glycosylation type Ir (CDG1R)'},
      'number_submitters': 1,
      'origin': 'unknown',
      'preferred_name': 'NM_005216.4(DDOST):c.1325T>A (p.Phe442Tyr)',
      'review_status': 'no assertion provided'},
     'ref': 'A',
     'type': 'single nucleotide variant',
     'variant_id': 585026}



Με ποιες παθήσεις έχει συνδεθεί αυτή η μετάλλαξη;


```python
data['clinvar']['rcv']['conditions']['name']
```




    'Congenital disorder of glycosylation type Ir (CDG1R)'



Άρα βρήκαμε ότι αν ένας άνθρωπος έχει το sequence: ```AGAAGACGATGCTGTAGATGAAGAGCCCCA```, τότε μπορεί να έχει το condition: ```'Congenital disorder of glycosylation type Ir (CDG1R)'```

Εσείς θα πρέπει να φτιάξετε μία συνάρτηση η οποία θα παίρνει ως είσοδο ένα DNA sequence. Στη συνέχεια θα χρησιμοποιεί τη συνάρτηση του μέρους 4 για να βρει (αν υπάρχει) τη μετάλλαξη που περιέχει το sequence. Στη συνέχεια θα ψάχνει τη myvariant.info για να βρει (αν υπάρχει) τις ασθένειες με τις οποίες έχει συνδεθεί, σύμφωνα με τη clinvar. Αν f είναι αυτή η συνάρτηση, τότε Θα πρέπει να μπορώ να γράφω:

```python
f('AGAAGACGATGCTGTAGATGAAGAGCCCCA')
```

Αυτό θα πρέπει να επιστρέφει
```
['Congenital disorder of glycosylation type Ir (CDG1R)']
```

Παρατηρήστε ότι επιτρέφει λίστα. Δηλαδή μπορεί να υπάρχουν περισσότερες από μία ασθένειες. Εννοείται ότι μπορείτε να χρησιμοποιήσετε τη συνάρτηση του 3ου μέρους.


Σε αυτό το project θα πρέπει να φτιάξετε ένα πρόγραμμα το οποίο θα παίρνει μία παράμετρο:
* --seq ΑΚΟΛΟΥΘΙΑ_DNA 

το πρόγραμμα θα τυπώνει μία αναφορά με:
* Σε ποιες περιοχές του γονιδιώματος έγινε allign αυτή η ακολουθία και με ποια ποιότητα (hsp).
* Ποιες μεταλλάξεις βρέθηκαν σε αυτή την ακολουθία
* Τι ασθένειες έχουν βρεθεί να έχουν συσχετιστεί με αυτές τις μεταλλάξεις. 

Δεν υπάρχει κάποιο συγκεκριμένο φορμάτ για την αναφορά. Ένα απλό αρχείο κειμένου αρκεί. 


