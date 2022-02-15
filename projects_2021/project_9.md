
# Project 9
<!-- https://github.com/kantale/python_lessons/blob/master/assignment_5.ipynb -->


Όπως γνωρίζουμε από τη βιολογία στο τέλος κάθε μετάγραφου υπάρχει η περιοχή 3'UTR. Σύμφωνα με τη wikipedia: https://en.wikipedia.org/wiki/Three_prime_untranslated_region 

> The length of the 3′-UTR is significant since longer 3′-UTRs are associated with lower levels of gene expression. 

Δηλαδή όσο πιο μεγάλη αυτή η περιοχή τόσο μεγαλύτερη η έκφραση του μετάγραφου. Νομίζω ότι μπορούμε να ερευνήσουμε λίγο αυτή τη διαπίστωση..

Καταρχή μπορούμε να πάμε στο [Expression Atlas](https://www.ebi.ac.uk/gxa/experiments/E-MTAB-5214/Downloads) και να κατεβάσουμε τα δεδομένα από [αυτό το paper](https://europepmc.org/article/MED/25954001). Σε αυτό το πείραμα οι συγγραφείς μελέτησαν την έκφραση σχεδόν όλων των γονιδίων σε 53 διαφορετικούς ιστούς. Μπορείτε να κατεβάσετε το αρχείο [Expression values across all genes (TPM)](https://www.ebi.ac.uk/gxa/experiments-content/E-MTAB-5214/resources/ExperimentDownloadSupplier.RnaSeqBaseline/tpms.tsv) και να το μελετήσετε.. Θα δείτε ότι η πρώτη στήλη είναι το ENSEMBL code για το γονίδιο, η 2η στήλη έχει το όνομα του γονιδίου και οι υπόλοιπες στήλες έχουν την έκφραση του γονιδίου σε διάφορους ιστούς (δεν μας ενδιαφέρει εδώ πως το μετρήσανε ή τι δείχνουν αυτές οι ποσότητες). 

Τώρα αυτό που χρειάζεται να βρούμε είναι το μήκος της περιοχής 3'UTR για όλα αυτά τα γονίδια. Μπορούμε να πάμε στη GENCODE: https://www.gencodegenes.org/human/  και να κατεβάσουμε το αρχείο GFF3 Comprehensive gene annotation (this is the main annotation file for most users): ftp://ftp.ebi.ac.uk/pub/databases/gencode/Gencode_human/release_36/gencode.v36.annotation.gff3.gz . Μέσα σε αυτό το αρχείο υπάρχουν πληροφορίες για όλα τα γονίδια / μετάγραφα / εξόνια / 5'UTR / 3'UTR του ανθρώπινου γονιδιώματος. 

Η δομή του αρχείου εξηγείται [εδώ](https://www.gencodegenes.org/pages/data_format.html) (παρόλο που αναφέρεται στο GTF format, το φορμάτ GFF3 είναι παρόμοιο), και [εδώ](https://www.gencodegenes.org/pages/faq.html)

Στο αρχείο αυτό υπάρχει για παράδειγμα η εγγραφή:
```
chrX  HAVANA  three_prime_UTR 100627108 100629986 . - . ID=UTR3:ENST00000373020.9;Parent=ENST00000373020.9;gene_id=ENSG00000000003.15;transcript_id=ENST00000373020.9;gene_type=protein_coding;gene_name=TSPAN6;transcript_type=protein_coding;transcript_name=TSPAN6-201;exon_number=8;exon_id=ENSE00001459322.5;level=2;protein_id=ENSP00000362111.4;transcript_support_level=1;hgnc_id=HGNC:11858;tag=basic,MANE_Select,appris_principal_1,CCDS;ccdsid=CCDS14470.1;havana_gene=OTTHUMG00000022002.2;havana_transcript=OTTHUMT00000057483.2
```

Το οποίο σημαίνει ότι το γονίδο με κωδικό gene_id=ENSG00000000003.15, έχει ένα μετάγραφο (transcript) με κωδικό transcript_id=ENST00000373020.9 το οποίο έχει ένα 3'UTR (three_prime_UTR) το οποίο ξεκινάει από τη θέση 100627108 και τελειώνει στη θέση 100629986. 


Άρα ξέρουμε ότι το γονίδιο ENSG00000000003 (είναι το πρώτο γονίδιο που αναφέρεται στο Expression Atlas) έχει ένα 3'UTR μς μέγεθος 100629986-100627108=2878. 

Εδώ όμως υπάρχει ένα πρόβλημα:
* Ένα γονίδιο (μπορεί να) έχει πολλά μετάγραφα
* Ένα μετάγραφο (μπορεί να) έχει πολλά 3'UTR

Για το 2ο πρόβλημα η απάντηση είναι εύκολη. Παίρνουμα απλά το "τελευταίο" 3'UTR (το οποίο είναι και συνήθως το μεγαλύτερο). 

Για το 1ο η απάντηση είναι πιο πολύπλοκη. Όπως παρατηρούμε στα πεδία της εγγραφής του ENSG00000000003 στο GFF3 αρχείο, βλέπουμε διάφορα πεδία. Μερικά από αυτά είναι:
* tag=basic,MANE_Select,appris_principal_1,CCDS
* transcript_support_level=1 
* level=2 

Εσείς θα πρέπει να ιεραρχήσετε τα μετάγραφα με βάση αυτή τη πληροφορία! Ο αλγόριθμος που θα χρησιμοποιήσουμε είναι ο εξής:
* Πάρε αυτό που έχει tag MANE_Select
* Αν υπάρχουν παραπάνω από 1 μετάγραφα με MANE_Select, ή κανένα:
   * Πάρε αυτό που έχει tag appris_principal_1 
   * Αν υπάρχουν παραπάνω 1 μετάγραφα με tag appris_principal_1 ή κανένα:
      * Πάρε αυτό που έχει tag basic 
      * Αν υπάρχουν παραπάνω από 1 μετάγραφα με tag basic, ή κανένα:
         * Πάρε αυτό που έχει tag CCDS.
         * Αν υπάρχουν παραπάνω από 1 μετάγραφα με tag CCDS ή κανένα: 
            * Πάρε αυτό που έχει το μεγαλύτερο transcript_support_level 
            * Αν υπάρχουν παραπάνω από 1 με το ίδιο (μεγαλύτερο) transcript_support_level ή κανένα:
               * Πάρε αυτό με το μεγαλύτερο level
               * Αν υπάρχει παραπάνω από 1 με το ίδιο (μεγαλύτερο) level ή κανένα:
                  * Αγνόησε αυτό το transcript, αφού τυπώσεις ένα μήνυμα!
                     
Και αφού αυτή η εκφώνηση με βοήθησε να φτάσω τα markdown bullets του Jupyter στα άκρα μπορούμε να συνεχίσουμε. 

Φτιάξτε ένα πρόγραμμα το οποίο θα παίρνει μία μόνο προαιρετική παράμετρο:
* ```--tissues```: λίστα με ονόματα ιστών που υπάρχουν στο Expression Atlas. Η λίστα πρέπει να είναι διαχωρίσμένη με κενά (space separated)

Το πρόγραμμά σας λοιπόν θα πρέπει για κάθε γονίδιο που υπάρχει στο Expression Atlas να υπολογίζει τον μέσο όρο της έκφρασής του για όλους τους ιστούς της παραμέτρους ```--tissues```. Αν δεν υπάρχει καθόλου η παράμετρος αυτή τότε θα παίρνει όλους τους ιστούς. Στη συνέχεια θα βρίσκει το μέγεθος του 3'UTR του κάθε γονιδίου από το GENCODE με βάση τη μέθοδο που περιγράψαμε πριν. Το πρόγραμμα θα φτιάχνει και θα σώζει σε ένα αρχείο ένα scatter plot για όλα τα γονίδια όπου X=μήκος 3'UTR του γονιδίου και Y=μέσος όρος της έκφρασης. 

Προαιρετικά:
* Ποιοι ιστοί φαίνονται να εξαρτώνται περισσότερο από το μέγεθος του 3'UTR και ποιοι το λιγότερο;


