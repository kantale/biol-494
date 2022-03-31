```python
!cd
```

    C:\Users\user



```python
f = open('mitsos.txt')
```


```python
f = open('C:/Users/user/Downloads/gwas_catalog_v1.0-associations_e105_r2022-03-23.tsv')
```


```python
f.close()
```


```python
f = open(r'C:\Users\user\Downloads\')
```


      Input In [6]
        f = open(r'C:\Users\user\Downloads\')
                                             ^
    SyntaxError: EOL while scanning string literal




```python
f = open('C:/Users/user/results.txt')
```


```python
f
```




    <_io.TextIOWrapper name='C:/Users/user/results.txt' mode='r' encoding='cp1253'>




```python
type(f)
```




    _io.TextIOWrapper




```python
s = f.read()
```


```python
s
```




    'this is a fantastic file\nvery precious data\nmuch science\nnobel\n'




```python
print (s)
```

    this is a fantastic file
    very precious data
    much science
    nobel
    



```python
g = f.read()
```


```python
print (g)
```

    



```python
len(g)
```




    0




```python
f.close()
```


```python
f = open('C:/Users/user/results.txt')
```


```python
g = f.read()
```


```python
g
```




    'this is a fantastic file\nvery precious data\nmuch science\nnobel\n'




```python
f.close()
```


```python
f = open('C:/Users/user/results.txt')
```


```python
line = f.readline()
```


```python
print (line)
```

    this is a fantastic file
    



```python
g = f.read()
```


```python
print (g)
```

    very precious data
    much science
    nobel
    



```python
f.close()
```


```python
f = open('C:/Users/user/results.txt')
```


```python
a = f.readline()
```


```python
b = f.readline()
```


```python
print (b)
```

    very precious data
    



```python
print (f.read())
```

    much science
    nobel
    



```python
f.seek(10)
```




    10




```python
f.readline()
```




    'fantastic file\n'




```python
f.close()
```


```python
f = open('C:/Users/user/results.txt')
```


```python
f = open('C:/Users/user/results.txt')
while True:
    line = f.readline()
    print (line)
    if not line:
        break
f.close()
```

    this is a fantastic file
    
    very precious data
    
    much science
    
    nobel
    
    



```python
f = open('C:/Users/user/results.txt')
while True:
    line = f.readline()
    print (line)
    if len(line) == 0:
        break
f.close()
```

    this is a fantastic file
    
    very precious data
    
    much science
    
    nobel
    
    



```python
f = open('C:/Users/user/results.txt')
while True:
    line = f.readline()
    print (line)
    if line == '':
        break
f.close()
```

    this is a fantastic file
    
    very precious data
    
    much science
    
    nobel
    
    



```python
for x in 'SDAFGFDS':
    print (x)
```

    S
    D
    A
    F
    G
    F
    D
    S



```python
for x in [5,6,7,]:
    print (x)
```

    5
    6
    7



```python
f = open('C:/Users/user/results.txt')
for line in f:
    print (line)
f.close()
```

    this is a fantastic file
    
    very precious data
    
    much science
    
    nobel
    



```python
with open('C:/Users/user/results.txt') as f:
    for l in f:
        print (l)
```

    this is a fantastic file
    
    very precious data
    
    much science
    
    nobel
    



```python
l = []
```


```python
with open('C:/Users/user/results.txt') as f:
    lc = 0
    for l in f:
        lc += 1
        if lc<3:
            continue
        print (l)
        break
```

    much science
    



```python
with open('C:/Users/user/results.txt') as f:

    for lc, l in enumerate(f):
        if lc < 6:
            continue
        print (l)
        break
```

    dyjfjfghjfkhjthjhkhkhjfgfgmgdd.fgjdalkgjshdlfkgjhsdlkfjghsldkfjghsldkjghskldfjghlsdkfjhglskdfjghlskdfjghskldjfghsldkfjghsldkjgh sljgsldkj ghskldjgh sldkgjh skldfjgh skldfjghsldkjghsldkfjgh skldjg hsldfkjghsldkjg hsldfkjgh sldkjgh sldkgjh sldkjg hsdlfkjgh sdfkjg hsldkfjg hsldkfjg hsldkfjg hsldkfjg hsldkfjgh sldkfjg sldkfjgh sldkjgh sldfjgh sldkfjgh sldkfjgh sldkfjg hsldkfjg hsldkfjgh sldkfjgh sldkfjgh fjkldh
    



```python

```


```python
my_list = [] 
with open('C:/Users/user/results.txt') as f:

    for lc, l in enumerate(f):
        if lc in {1,2}:
            my_list.append(l)
        
        
```


```python
my_list
```




    ['very precious data\n', 'much science. bravo!\n']




```python
with open('C:/Users/user/results.txt') as f:

    my_list = [l for lc, l in enumerate(f) if lc in {1,2}]

```


```python
my_list
```




    ['very precious data\n', 'much science. bravo!\n']




```python
 my_list = [l for lc, l in enumerate(open('C:/Users/user/results.txt')) if lc in {1,2}]
```


```python
my_list
```




    ['very precious data\n', 'much science. bravo!\n']




```python
a = 'ghjkgfghj\n'
```


```python
a
```




    'ghjkgfghj\n'




```python
a.strip()
```




    'ghjkgfghj'




```python
'   sfdagsagszdfg          '.strip()
```




    'sfdagsagszdfg'




```python
'sadfasdfasdf\n'[:-1]
```




    'sadfasdfasdf'




```python
'sadfasdfasdf\n'.replace('\n', '')
```




    'sadfasdfasdf'




```python

```


```python

```


```python

```


```python
print ('mitsos', end=' - ')
print ('alex')
```

    mitsos - alex



```python
bool('sdfsdfg')
```




    True




```python
bool('')
```




    False




```python
my_list = [] 
with open('C:/Users/user/results.txt') as f:

    data = f.read()
print (len(data))
```

    488



```python
my_list = [] 
with open('C:/Users/user/alex.docx') as f:

    data = f.read()
print (len(data))
```


    ---------------------------------------------------------------------------

    UnicodeDecodeError                        Traceback (most recent call last)

    Input In [93], in <cell line: 2>()
          1 my_list = [] 
          2 with open('C:/Users/user/alex.docx') as f:
    ----> 4     data = f.read()
          5 print (len(data))


    File ~\miniconda3\lib\encodings\cp1253.py:23, in IncrementalDecoder.decode(self, input, final)
         22 def decode(self, input, final=False):
    ---> 23     return codecs.charmap_decode(input,self.errors,decoding_table)[0]


    UnicodeDecodeError: 'charmap' codec can't decode byte 0xd2 in position 16: character maps to <undefined>



```python
my_list = [] 
with open('C:/Users/user/alex2.txt') as f:

    data = f.read()
print (len(data))
```

    379



```python
print (data)
```

    Xf/lgk jh;flsgkhjsfkj ghsfkldghsldkjghsldkfjg hldakfjgh sldfkj ghsldkfjgh skldfjgh skldfjgh skldfjgh ldskfj ghsldkfj ghsldkfjg sldkfjgh sdljgh sldjgh sldkfjgh sldkjgh sldkjgh sldkfjg sldkfjg hsldkjgh sldkfjg hsldfjkg hsldkjgh ldfjgh sldkfjgh 
    1. Xghfg
    2. Hfd
    3. Hfd
    4. Ghfd
    5. Ghd
    6. Fghfg
    7. h
    sldkfjg sldkfjgh slkdfjg sdfklgh skldfgh sdlkjg hsldfjgh sldkfjgh sldj ghlsdkf h
    
    
    
    



```python
def f(l):
    return sum(l)
```


```python
f([10, 20, 30])
```




    60




```python
def f(l):
    if not len(l):
        return 0
    return l[0] + f(l[1:])

f([10, 20, 30])
```




    60




```python
l = [['Helen', 23, 8], ['Kostas', 25, 9], ['Alex', 22, 9], ['Maria', 24, 7]]
```


```python
s = 'a σρετςερτςρε σδφγ zfdgsdfg'
```


```python
l = [4,5,4,3,4,5,6,7,6,1,5,4]
```


```python
min(l)
```




    1




```python
def f(l):
    if len(l) ==2:
        if l[0] < l[1]:
            return l[0]
        return l[1]
    
    if l[0] < l[1]:
        return f( [l[0]] + l[2:] )
    
    return f([l[1]] + l[2:])
    
    
f(l)
```




    1




```python
my_list = [] 
with open('C:/Users/user/findings.txt', 'w') as f:

    f.write('cvghjklcvbnjkfyucvhjkcvhcgh')

```


```python

```


```python

```


```python

```


```python
my_list = [] 
with open('C:/Users/user/findings.txt', 'x') as f:

    f.write('SUCH RESEARCH! WOW!!!!')

```


    ---------------------------------------------------------------------------

    FileExistsError                           Traceback (most recent call last)

    Input In [115], in <cell line: 2>()
          1 my_list = [] 
    ----> 2 with open('C:/Users/user/findings.txt', 'x') as f:
          4     f.write('SUCH RESEARCH! WOW!!!!')


    FileExistsError: [Errno 17] File exists: 'C:/Users/user/findings.txt'



```python
my_list = [] 
with open('C:/Users/user/findings.txt', 'w') as f:

    f.write('SUCH RESEARCH! WOW!!!!\n')
    f.write('cannot get better than this!\n')

```


```python

```


```python
data = []
with open('C:/Users/user/Downloads/gwas_catalog_v1.0-associations_e105_r2022-03-23.tsv', 
          encoding='iso-8859-1') as f:
    line = f.readline()
    header = line.strip().split('\t')

    for line_counter, line in enumerate(f):
        l = f.readline()
            
        if line_counter % 10_000 == 0:            
            print (f'Progress: {line_counter}')

        l_list = l.strip().split('\t')
        
        data.append(l_list)
    
print (f' read {line_counter} lines')
```

    Progress: 0
    Progress: 10000
    Progress: 20000
    Progress: 30000
    Progress: 40000
    Progress: 50000
    Progress: 60000
    Progress: 70000
    Progress: 80000
    Progress: 90000
    Progress: 100000
    Progress: 110000
    Progress: 120000
    Progress: 130000
    Progress: 140000
    Progress: 150000
    Progress: 160000
    Progress: 170000
     read 175920 lines



```python
data[100]
```




    ['2019-02-14',
     '29507422',
     'Hoffmann TJ',
     '2018-03-05',
     'Nat Genet',
     'www.ncbi.nlm.nih.gov/pubmed/29507422',
     'A large electronic-health-record-based genome-wide study of serum lipids.',
     'High density lipoprotein cholesterol levels',
     '76,627 European ancestry individuals, 7,795 Hispanic individuals, 6,855 East Asian ancestry individuals, 2,958 African American individuals, 439 South Asian ancestry individuals',
     'NA',
     '2p24.1',
     '2',
     '21041028',
     'NR',
     'APOB',
     '',
     '',
     'ENSG00000084674',
     '',
     '',
     'rs1367117-G',
     'rs1367117',
     '0',
     '1367117',
     'missense_variant',
     '0',
     'NR',
     '3E-6',
     '5.522878745280337',
     '',
     '0.018',
     'unit increase',
     'Affymetrix [at least 7091467] (imputed)',
     'N']




```python
''.strip().split('\t')
```




    ['']




```python
dict(zip(header, data[100]))
```




    {'DATE ADDED TO CATALOG': '2019-02-14',
     'PUBMEDID': '29507422',
     'FIRST AUTHOR': 'Hoffmann TJ',
     'DATE': '2018-03-05',
     'JOURNAL': 'Nat Genet',
     'LINK': 'www.ncbi.nlm.nih.gov/pubmed/29507422',
     'STUDY': 'A large electronic-health-record-based genome-wide study of serum lipids.',
     'DISEASE/TRAIT': 'High density lipoprotein cholesterol levels',
     'INITIAL SAMPLE SIZE': '76,627 European ancestry individuals, 7,795 Hispanic individuals, 6,855 East Asian ancestry individuals, 2,958 African American individuals, 439 South Asian ancestry individuals',
     'REPLICATION SAMPLE SIZE': 'NA',
     'REGION': '2p24.1',
     'CHR_ID': '2',
     'CHR_POS': '21041028',
     'REPORTED GENE(S)': 'NR',
     'MAPPED_GENE': 'APOB',
     'UPSTREAM_GENE_ID': '',
     'DOWNSTREAM_GENE_ID': '',
     'SNP_GENE_IDS': 'ENSG00000084674',
     'UPSTREAM_GENE_DISTANCE': '',
     'DOWNSTREAM_GENE_DISTANCE': '',
     'STRONGEST SNP-RISK ALLELE': 'rs1367117-G',
     'SNPS': 'rs1367117',
     'MERGED': '0',
     'SNP_ID_CURRENT': '1367117',
     'CONTEXT': 'missense_variant',
     'INTERGENIC': '0',
     'RISK ALLELE FREQUENCY': 'NR',
     'P-VALUE': '3E-6',
     'PVALUE_MLOG': '5.522878745280337',
     'P-VALUE (TEXT)': '',
     'OR or BETA': '0.018',
     '95% CI (TEXT)': 'unit increase',
     'PLATFORM [SNPS PASSING QC]': 'Affymetrix [at least 7091467] (imputed)',
     'CNV': 'N'}




```python
d = {}

for item in data:
    for h, v in zip(header, item):
        if not h in d:
            d[h] = []
        
        d[h].append(v)
    
```


```python
len(set(d['FIRST AUTHOR']))
```




    123




```python
set(d['FIRST AUTHOR'])
```




    {'Ahmed S',
     'Allen RJ',
     'Almgren P',
     'Almli LM',
     'Anney RJL',
     'Arpawong TE',
     'Astle WJ',
     'Bei JX',
     'Benyamin B',
     'Biernacka JM',
     'Bonas-Guarch S',
     'Cha S',
     'Chan JP',
     'Chang X',
     'Chaturvedi S',
     'Chen H',
     'Chenoweth MJ',
     'Christophersen IE',
     'Clarke TK',
     'Coleman JRI',
     'Conti DV',
     'Cooper JD',
     'Corre T',
     'Darlow JM',
     'Day FR',
     'Delgado DA',
     'Dong C',
     'Dudenkov TM',
     'Ferreira MA',
     'Gao B',
     'Gorski M',
     'Graff M',
     'Guo Q',
     'Hammerschlag AR',
     'Haryono SJ',
     'Hinks A',
     'Hofer P',
     'Hoffmann TJ',
     'Hong X',
     'Hu X',
     'Ikram MA',
     'Ilboudo Y',
     'Jia P',
     'Jonsson L',
     'Jun GR',
     'Justice AE',
     'Kawaguchi T',
     'Kerr KF',
     'Kim KW',
     'Kim M',
     'Kimura M',
     'Konte B',
     'Kristiansen W',
     'Kunz M',
     'Lee MH',
     'Lee MK',
     'Lee TH',
     'Lencer R',
     'Lessard CJ',
     'Li C',
     'Li D',
     'Li J',
     'Li M',
     'Litchfield K',
     'Liu JZ',
     'Liu Y',
     'Lu AT',
     'Lutz SM',
     'Lv H',
     'Mack S',
     'Magvanjav O',
     'Marenholz I',
     'McKay JD',
     'Michailidou K',
     'Milne RL',
     'Miron J',
     'Moore CB',
     'Moore KN',
     'Morris AP',
     'Morton LM',
     'Munz M',
     'Nakada TA',
     'Ng E',
     'Nolte IM',
     'Persad PJ',
     'Qian DC',
     'Randall CL',
     'Ravenhall M',
     'Ren HY',
     'Saccone NL',
     'Sakamoto Y',
     'Sanchez-Juan P',
     'Sanchez-Roige S',
     'Scelo G',
     'Seyerle AA',
     'Shah AA',
     'Shen X',
     'Sobota RS',
     'Sud A',
     'Sugier PE',
     'Suh Y',
     'Suhre K',
     'Sun Y',
     'Tachmazidou I',
     'Tapper W',
     'Thompson AG',
     'Tian C',
     'Tomer Y',
     'Turley P',
     'Wang Z',
     'Ward-Caviness CK',
     'Wattacheril J',
     'Winkler TW',
     'Witt SH',
     'Xu W',
     'Yashin AI',
     'Yeo A',
     'Yin X',
     'Yucesoy B',
     'Zai CC',
     'Zhang Y',
     'Zhang YB',
     'Zhou H'}




```python
set([x for x in d['FIRST AUTHOR'] if 'idou' in x])
```




    {'Michailidou K', 'Tachmazidou I'}




```python
line
```




    'DATE ADDED TO CATALOG\tPUBMEDID\tFIRST AUTHOR\tDATE\tJOURNAL\tLINK\tSTUDY\tDISEASE/TRAIT\tINITIAL SAMPLE SIZE\tREPLICATION SAMPLE SIZE\tREGION\tCHR_ID\tCHR_POS\tREPORTED GENE(S)\tMAPPED_GENE\tUPSTREAM_GENE_ID\tDOWNSTREAM_GENE_ID\tSNP_GENE_IDS\tUPSTREAM_GENE_DISTANCE\tDOWNSTREAM_GENE_DISTANCE\tSTRONGEST SNP-RISK ALLELE\tSNPS\tMERGED\tSNP_ID_CURRENT\tCONTEXT\tINTERGENIC\tRISK ALLELE FREQUENCY\tP-VALUE\tPVALUE_MLOG\tP-VALUE (TEXT)\tOR or BETA\t95% CI (TEXT)\tPLATFORM [SNPS PASSING QC]\tCNV\n'




```python
line.strip().split('\t')
```




    ['DATE ADDED TO CATALOG',
     'PUBMEDID',
     'FIRST AUTHOR',
     'DATE',
     'JOURNAL',
     'LINK',
     'STUDY',
     'DISEASE/TRAIT',
     'INITIAL SAMPLE SIZE',
     'REPLICATION SAMPLE SIZE',
     'REGION',
     'CHR_ID',
     'CHR_POS',
     'REPORTED GENE(S)',
     'MAPPED_GENE',
     'UPSTREAM_GENE_ID',
     'DOWNSTREAM_GENE_ID',
     'SNP_GENE_IDS',
     'UPSTREAM_GENE_DISTANCE',
     'DOWNSTREAM_GENE_DISTANCE',
     'STRONGEST SNP-RISK ALLELE',
     'SNPS',
     'MERGED',
     'SNP_ID_CURRENT',
     'CONTEXT',
     'INTERGENIC',
     'RISK ALLELE FREQUENCY',
     'P-VALUE',
     'PVALUE_MLOG',
     'P-VALUE (TEXT)',
     'OR or BETA',
     '95% CI (TEXT)',
     'PLATFORM [SNPS PASSING QC]',
     'CNV']




```python

```


```python

```


```python

```


```python

```
