```python
import os
```


```python
os
```




    <module 'os' from '/Users/admin/anaconda3/lib/python3.8/os.py'>




```python
def f(a,b):
    '''
    This is an amazing function
    '''
    return a+b
```


```python
f.__doc__
```




    '\n    This is an amazing function\n    '




```python
print (f.__doc__)
```

    
        This is an amazing function
        



```python
3 +4
```




    7




```python
int(3).__add__(4)
```




    7




```python
int(3).__add__ = lambda x,y : x-y
```


    ---------------------------------------------------------------------------

    AttributeError                            Traceback (most recent call last)

    <ipython-input-9-6bb31bbfdefc> in <module>
    ----> 1 int(3).__add__ = lambda x,y : x-y
    

    AttributeError: 'int' object attribute '__add__' is read-only



```python
a = [1,2,3]
```


```python
len(a)
```




    3




```python
a.append(6)
```


```python
a.append
```




    <function list.append(object, /)>




```python

class Person:
    
    ADULT_AGE = 18
    
    def is_adult(self, ):
        return self.age>self.ADULT_AGE
    
    def set_age(self, age):
        self.age = age
        
    def get_age(self,):
        return self.age
```


```python
mitsos = Person()
```


```python
#mitsos.is_adult(50)
```




    True




```python
mitsos.set_age(50)
```


```python
mitsos.get_age()
```




    50




```python
mitsos.is_adult()
```




    True




```python
mitsos = Person()
kostas = Person()
```


```python
mitsos.set_age(50)
kostas.set_age(15)
```


```python
mitsos.is_adult()
```




    True




```python
kostas.is_adult()
```




    False




```python

class Person:
    
    ADULT_AGE = 18
    
    def __init__(self, name, age):
        self.set_age(age)
        self.name  = name
        
    def __str__(self,):
        return f'Name: {self.name} Age: {self.age}'
    
    def __len__(self,):
        return 100
    
    def __add__(self, another_person):
        return Person(
            age=self.age + another_person.age,
            name = f'{self.name} {another_person.name}'
        )
    
    def is_adult(self, ):
        # All these three are equivalent
        #return self.age>self.ADULT_AGE
        
        #return self.is_adult_2(self.age)
    
        return Person.is_adult_2(self.age)
    
    @staticmethod
    def is_adult_2(age):
        return age>Person.ADULT_AGE
    
    def set_age(self, age):
        self.age = age
        
    def get_age(self,):
        return self.age
```


```python
Person.is_adult_2(40)
```




    True




```python
import this
```

    The Zen of Python, by Tim Peters
    
    Beautiful is better than ugly.
    Explicit is better than implicit.
    Simple is better than complex.
    Complex is better than complicated.
    Flat is better than nested.
    Sparse is better than dense.
    Readability counts.
    Special cases aren't special enough to break the rules.
    Although practicality beats purity.
    Errors should never pass silently.
    Unless explicitly silenced.
    In the face of ambiguity, refuse the temptation to guess.
    There should be one-- and preferably only one --obvious way to do it.
    Although that way may not be obvious at first unless you're Dutch.
    Now is better than never.
    Although never is often better than *right* now.
    If the implementation is hard to explain, it's a bad idea.
    If the implementation is easy to explain, it may be a good idea.
    Namespaces are one honking great idea -- let's do more of those!



```python
Protein.structure.length.visualize
```


```python
mitsos = Person()
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-47-8fa818a94c26> in <module>
    ----> 1 mitsos = Person()
    

    TypeError: __init__() missing 1 required positional argument: 'age'



```python
mitsos = Person(50)
```


```python
mitsos = Person(age=50)
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-52-a6bdf12f0997> in <module>
    ----> 1 mitsos = Person(age=50)
    

    TypeError: __init__() missing 1 required positional argument: 'name'



```python
mitsos.is_adult()
```




    True




```python
mitsos = Person(age=50, name='Mitsos')
```


```python
print (mitsos)
```

    Name: Mitsos Age: 50



```python
len(mitsos)
```




    100




```python
class Gene:
    
    def __init__(self, start, end):
        self.start = start
        self.end = end
        
    def __len__(self, ):
        return self.end - self.start
    
    def __iter__(self,):
        self.i = self.start
        return self
        
    def __next__(self):
        r = self.i
        self.i += 1
        
        if self.i > self.end:
            raise StopIteration
        
        return r
    
    def __str__(self,):
        return (f'This is a gene: start: {self.start} end: {self.end}')
    
    def __getitem__(self, index):
        r = self.start + index
        if r > self.end:
            raise IndexError 
        return r
```


```python
class Protein(Gene):
    
    def __init__(self, start, end, name):
        super().__init__(start, end)
        self.name = name
    
    def __str__(self,):
        return (f'This is a protein: start: {self.start} end: {self.end}')
    
    def __len__(self, ):
        return (self.end - self.start)//3

```


```python
class New_Class(Protein):
    pass
```


```python
class Amazing_Class(Gene, Person):
    pass
```


```python
p = Amazing_Class(100, 150)
```


```python
Amazing_Class.is_adult_2(30)
```




    True




```python
P1 = Protein(100,160, 'P1')
APOE = Gene(1000, 1500)
```


```python
print (len(P1))
print (len(APOE))
```

    20
    500



```python

```


```python
print (P1)
```

    This is a protein: start: 100 end: 160



```python
print (APOE)
```

    This is a gene: start: 1000 end: 1500



```python
len(P1)
```




    150




```python
APOE = Gene(1000, 1500)
```


```python
for i in APOE:
    print (i)
```

    1000
    1001
    1002
    1003
    1004
    1005
    1006
    1007
    1008
    1009
    1010
    1011
    1012
    1013
    1014
    1015
    1016
    1017
    1018
    1019
    1020
    1021
    1022
    1023
    1024
    1025
    1026
    1027
    1028
    1029
    1030
    1031
    1032
    1033
    1034
    1035
    1036
    1037
    1038
    1039
    1040
    1041
    1042
    1043
    1044
    1045
    1046
    1047
    1048
    1049
    1050
    1051
    1052
    1053
    1054
    1055
    1056
    1057
    1058
    1059
    1060
    1061
    1062
    1063
    1064
    1065
    1066
    1067
    1068
    1069
    1070
    1071
    1072
    1073
    1074
    1075
    1076
    1077
    1078
    1079
    1080
    1081
    1082
    1083
    1084
    1085
    1086
    1087
    1088
    1089
    1090
    1091
    1092
    1093
    1094
    1095
    1096
    1097
    1098
    1099
    1100
    1101
    1102
    1103
    1104
    1105
    1106
    1107
    1108
    1109
    1110
    1111
    1112
    1113
    1114
    1115
    1116
    1117
    1118
    1119
    1120
    1121
    1122
    1123
    1124
    1125
    1126
    1127
    1128
    1129
    1130
    1131
    1132
    1133
    1134
    1135
    1136
    1137
    1138
    1139
    1140
    1141
    1142
    1143
    1144
    1145
    1146
    1147
    1148
    1149
    1150
    1151
    1152
    1153
    1154
    1155
    1156
    1157
    1158
    1159
    1160
    1161
    1162
    1163
    1164
    1165
    1166
    1167
    1168
    1169
    1170
    1171
    1172
    1173
    1174
    1175
    1176
    1177
    1178
    1179
    1180
    1181
    1182
    1183
    1184
    1185
    1186
    1187
    1188
    1189
    1190
    1191
    1192
    1193
    1194
    1195
    1196
    1197
    1198
    1199
    1200
    1201
    1202
    1203
    1204
    1205
    1206
    1207
    1208
    1209
    1210
    1211
    1212
    1213
    1214
    1215
    1216
    1217
    1218
    1219
    1220
    1221
    1222
    1223
    1224
    1225
    1226
    1227
    1228
    1229
    1230
    1231
    1232
    1233
    1234
    1235
    1236
    1237
    1238
    1239
    1240
    1241
    1242
    1243
    1244
    1245
    1246
    1247
    1248
    1249
    1250
    1251
    1252
    1253
    1254
    1255
    1256
    1257
    1258
    1259
    1260
    1261
    1262
    1263
    1264
    1265
    1266
    1267
    1268
    1269
    1270
    1271
    1272
    1273
    1274
    1275
    1276
    1277
    1278
    1279
    1280
    1281
    1282
    1283
    1284
    1285
    1286
    1287
    1288
    1289
    1290
    1291
    1292
    1293
    1294
    1295
    1296
    1297
    1298
    1299
    1300
    1301
    1302
    1303
    1304
    1305
    1306
    1307
    1308
    1309
    1310
    1311
    1312
    1313
    1314
    1315
    1316
    1317
    1318
    1319
    1320
    1321
    1322
    1323
    1324
    1325
    1326
    1327
    1328
    1329
    1330
    1331
    1332
    1333
    1334
    1335
    1336
    1337
    1338
    1339
    1340
    1341
    1342
    1343
    1344
    1345
    1346
    1347
    1348
    1349
    1350
    1351
    1352
    1353
    1354
    1355
    1356
    1357
    1358
    1359
    1360
    1361
    1362
    1363
    1364
    1365
    1366
    1367
    1368
    1369
    1370
    1371
    1372
    1373
    1374
    1375
    1376
    1377
    1378
    1379
    1380
    1381
    1382
    1383
    1384
    1385
    1386
    1387
    1388
    1389
    1390
    1391
    1392
    1393
    1394
    1395
    1396
    1397
    1398
    1399
    1400
    1401
    1402
    1403
    1404
    1405
    1406
    1407
    1408
    1409
    1410
    1411
    1412
    1413
    1414
    1415
    1416
    1417
    1418
    1419
    1420
    1421
    1422
    1423
    1424
    1425
    1426
    1427
    1428
    1429
    1430
    1431
    1432
    1433
    1434
    1435
    1436
    1437
    1438
    1439
    1440
    1441
    1442
    1443
    1444
    1445
    1446
    1447
    1448
    1449
    1450
    1451
    1452
    1453
    1454
    1455
    1456
    1457
    1458
    1459
    1460
    1461
    1462
    1463
    1464
    1465
    1466
    1467
    1468
    1469
    1470
    1471
    1472
    1473
    1474
    1475
    1476
    1477
    1478
    1479
    1480
    1481
    1482
    1483
    1484
    1485
    1486
    1487
    1488
    1489
    1490
    1491
    1492
    1493
    1494
    1495
    1496
    1497
    1498
    1499



```python
len(APOE)
```




    500




```python
mitsos = Person(age=50, name='Mitsos')
kostas = Person(age=15, name='Kwstas')
```


```python
new_person = mitsos + kostas
```


```python
print (new_person)
```

    Name: Mitsos Kwstas Age: 65



```python
for i in mitsos:
    print (i)
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-79-f24fb0255b90> in <module>
    ----> 1 for i in mitsos:
          2     print (i)


    TypeError: 'Person' object is not iterable



```python
APOE[100]
```




    1100




```python
APOE[1000]
```


    ---------------------------------------------------------------------------

    IndexError                                Traceback (most recent call last)

    <ipython-input-107-0bea4233ac89> in <module>
    ----> 1 APOE[1000]
    

    <ipython-input-104-3e543d6f2487> in __getitem__(self, index)
         24         r = self.start + index
         25         if r > self.end:
    ---> 26             raise IndexError
         27         return r


    IndexError: 



```python
a = [1,2,3]
a[100]
```


    ---------------------------------------------------------------------------

    IndexError                                Traceback (most recent call last)

    <ipython-input-103-7e439a244abe> in <module>
          1 a = [1,2,3]
    ----> 2 a[100]
    

    IndexError: list index out of range



```python
dir(mitsos)
```




    ['ADULT_AGE',
     '__add__',
     '__class__',
     '__delattr__',
     '__dict__',
     '__dir__',
     '__doc__',
     '__eq__',
     '__format__',
     '__ge__',
     '__getattribute__',
     '__gt__',
     '__hash__',
     '__init__',
     '__init_subclass__',
     '__le__',
     '__len__',
     '__lt__',
     '__module__',
     '__ne__',
     '__new__',
     '__reduce__',
     '__reduce_ex__',
     '__repr__',
     '__setattr__',
     '__sizeof__',
     '__str__',
     '__subclasshook__',
     '__weakref__',
     'age',
     'get_age',
     'is_adult',
     'name',
     'set_age']



## API calls


```python
import requests, sys
 
server = "https://rest.ensembl.org"
ext = "/vep/human/hgvs/ENSP00000401091.1:p.Tyr124Cys?"
 
r = requests.get(server+ext, headers={ "Content-Type" : "application/json"})
 
if not r.ok:
  r.raise_for_status()
  #sys.exit()
 
decoded = r.json()
#print(repr(decoded))
```


```python
#decoded
```


```python
import requests, sys
 
server = "https://rest.ensembl.org"
ext = "/sequence/region/human/X:1000000..1000100:1?"
 
r = requests.get(server+ext, headers={ "Content-Type" : "text/plain"})
 
if not r.ok:
  r.raise_for_status()
  #sys.exit()
 
 
print(r.text)
```

    CTGTAGAAACATTAGCCTGGCTAACAAGGTGAAACCCCATCTCTACTAACAATACAAAATATTGGTTGGGCGTGGTGGCGGGTGCTTGTAATCCCAGCTAC



```python
import pandas as pd
```


```python
dfs = pd.read_html('https://en.wikipedia.org/wiki/List_of_busiest_airports_by_passenger_traffic')
```


```python
len(dfs)
```




    8




```python
dfs.__len__()
```




    8




```python
dfs[2]
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Rank</th>
      <th>Airport</th>
      <th>Location</th>
      <th>Country</th>
      <th>Code(IATA/ICAO)</th>
      <th>Totalpassengers</th>
      <th>RankChange</th>
      <th>%change</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1.0</td>
      <td>Hartsfield–Jackson Atlanta International Airport</td>
      <td>Atlanta, Georgia</td>
      <td>United States</td>
      <td>ATL/KATL</td>
      <td>107394029</td>
      <td>NaN</td>
      <td>3.3%</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2.0</td>
      <td>Beijing Capital International Airport</td>
      <td>Chaoyang-Shunyi, Beijing</td>
      <td>China</td>
      <td>PEK/ZBAA</td>
      <td>100983290</td>
      <td>NaN</td>
      <td>5.4%</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3.0</td>
      <td>Dubai International Airport</td>
      <td>Garhoud, Dubai</td>
      <td>United Arab Emirates</td>
      <td>DXB/OMDB</td>
      <td>89149387</td>
      <td>NaN</td>
      <td>1.0%</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4.0</td>
      <td>Los Angeles International Airport</td>
      <td>Los Angeles, California</td>
      <td>United States</td>
      <td>LAX/KLAX</td>
      <td>87534384</td>
      <td>NaN</td>
      <td>3.5%</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5.0</td>
      <td>Tokyo Haneda Airport</td>
      <td>Ōta, Tokyo</td>
      <td>Japan</td>
      <td>HND/RJTT</td>
      <td>87502720</td>
      <td>2.0</td>
      <td>2.5%</td>
    </tr>
    <tr>
      <th>5</th>
      <td>6.0</td>
      <td>O'Hare International Airport</td>
      <td>Chicago, Illinois</td>
      <td>United States</td>
      <td>ORD/KORD</td>
      <td>83339186</td>
      <td>1.0</td>
      <td>4.4%</td>
    </tr>
    <tr>
      <th>6</th>
      <td>7.0</td>
      <td>Heathrow Airport</td>
      <td>Hillingdon, London</td>
      <td>United Kingdom</td>
      <td>LHR/EGLL</td>
      <td>80126320</td>
      <td>1.0</td>
      <td>2.7%</td>
    </tr>
    <tr>
      <th>7</th>
      <td>8.0</td>
      <td>Hong Kong International Airport</td>
      <td>Chek Lap Kok, Islands, New Territories</td>
      <td>Hong Kong SAR, China</td>
      <td>HKG/VHHH</td>
      <td>74517402</td>
      <td>NaN</td>
      <td>2.6%</td>
    </tr>
    <tr>
      <th>8</th>
      <td>9.0</td>
      <td>Shanghai Pudong International Airport</td>
      <td>Pudong, Shanghai</td>
      <td>China</td>
      <td>PVG/ZSPD</td>
      <td>74006331</td>
      <td>NaN</td>
      <td>5.7%</td>
    </tr>
    <tr>
      <th>9</th>
      <td>10.0</td>
      <td>Charles de Gaulle Airport</td>
      <td>Roissy-en-France, Île-de-France</td>
      <td>France</td>
      <td>CDG/LFPG</td>
      <td>72229723</td>
      <td>NaN</td>
      <td>4.0%</td>
    </tr>
    <tr>
      <th>10</th>
      <td>11.0</td>
      <td>Amsterdam Airport Schiphol</td>
      <td>Haarlemmermeer, North Holland</td>
      <td>Netherlands</td>
      <td>AMS/EHAM</td>
      <td>71053147</td>
      <td>NaN</td>
      <td>3.7%</td>
    </tr>
    <tr>
      <th>11</th>
      <td>12.0</td>
      <td>Indira Gandhi International Airport</td>
      <td>Delhi</td>
      <td>India</td>
      <td>DEL/VIDP</td>
      <td>69900938</td>
      <td>4.0</td>
      <td>10.2%</td>
    </tr>
    <tr>
      <th>12</th>
      <td>13.0</td>
      <td>Guangzhou Baiyun International Airport</td>
      <td>Baiyun-Huadu, Guangzhou, Guangdong</td>
      <td>China</td>
      <td>CAN/ZGGG</td>
      <td>69769497</td>
      <td>NaN</td>
      <td>6.0%</td>
    </tr>
    <tr>
      <th>13</th>
      <td>14.0</td>
      <td>Frankfurt Airport</td>
      <td>Frankfurt, Hesse</td>
      <td>Germany</td>
      <td>FRA/EDDF</td>
      <td>69510269</td>
      <td>NaN</td>
      <td>7.8%</td>
    </tr>
    <tr>
      <th>14</th>
      <td>15.0</td>
      <td>Dallas/Fort Worth International Airport</td>
      <td>Dallas-Fort Worth, Texas</td>
      <td>United States</td>
      <td>DFW/KDFW</td>
      <td>69112607</td>
      <td>3.0</td>
      <td>3.0%</td>
    </tr>
    <tr>
      <th>15</th>
      <td>16.0</td>
      <td>Seoul Incheon International Airport</td>
      <td>Incheon</td>
      <td>South Korea</td>
      <td>ICN/RKSI</td>
      <td>68350784</td>
      <td>3.0</td>
      <td>10.0%</td>
    </tr>
    <tr>
      <th>16</th>
      <td>17.0</td>
      <td>Istanbul Atatürk Airport</td>
      <td>Yeşilköy, Istanbul</td>
      <td>Turkey</td>
      <td>IST/LTBA</td>
      <td>68192683</td>
      <td>2.0</td>
      <td>6.4%</td>
    </tr>
    <tr>
      <th>17</th>
      <td>18.0</td>
      <td>Soekarno–Hatta International Airport</td>
      <td>Tangerang, Banten</td>
      <td>Indonesia</td>
      <td>CGK/WIII</td>
      <td>66908159</td>
      <td>1.0</td>
      <td>6.2%</td>
    </tr>
    <tr>
      <th>18</th>
      <td>19.0</td>
      <td>Singapore Changi Airport</td>
      <td>Changi, East Region</td>
      <td>Singapore</td>
      <td>SIN/WSSS</td>
      <td>65628000</td>
      <td>1.0</td>
      <td>5.5%</td>
    </tr>
    <tr>
      <th>19</th>
      <td>20.0</td>
      <td>Denver International Airport</td>
      <td>Denver, Colorado</td>
      <td>United States</td>
      <td>DEN/KDEN</td>
      <td>64494613</td>
      <td>NaN</td>
      <td>5.1%</td>
    </tr>
    <tr>
      <th>20</th>
      <td>21.0</td>
      <td>Suvarnabhumi Airport</td>
      <td>Bang Phli, Samut Prakan</td>
      <td>Thailand</td>
      <td>BKK/VTBS</td>
      <td>63378923</td>
      <td>NaN</td>
      <td>4.1%</td>
    </tr>
    <tr>
      <th>21</th>
      <td>22.0</td>
      <td>John F. Kennedy International Airport</td>
      <td>Queens, New York, New York</td>
      <td>United States</td>
      <td>JFK/KJFK</td>
      <td>61623756</td>
      <td>NaN</td>
      <td>3.6%</td>
    </tr>
    <tr>
      <th>22</th>
      <td>23.0</td>
      <td>Kuala Lumpur International Airport</td>
      <td>Sepang, Selangor</td>
      <td>Malaysia</td>
      <td>KUL/WMKK</td>
      <td>60013397</td>
      <td>NaN</td>
      <td>2.5%</td>
    </tr>
    <tr>
      <th>23</th>
      <td>24.0</td>
      <td>Madrid Barajas Airport</td>
      <td>Barajas, Madrid</td>
      <td>Spain</td>
      <td>MAD/LEMD</td>
      <td>57862951</td>
      <td>1.0</td>
      <td>8.4%</td>
    </tr>
    <tr>
      <th>24</th>
      <td>25.0</td>
      <td>San Francisco International Airport</td>
      <td>San Mateo County, California</td>
      <td>United States</td>
      <td>SFO/KSFO</td>
      <td>57708196</td>
      <td>1.0</td>
      <td>3.4%</td>
    </tr>
    <tr>
      <th>25</th>
      <td>26.0</td>
      <td>Chengdu Shuangliu International Airport</td>
      <td>Shuangliu-Wuhou, Chengdu, Sichuan</td>
      <td>China</td>
      <td>CTU/ZUUU</td>
      <td>52950529</td>
      <td>NaN</td>
      <td>6.3%</td>
    </tr>
    <tr>
      <th>26</th>
      <td>27.0</td>
      <td>Barcelona–El Prat Airport</td>
      <td>Barcelona</td>
      <td>Spain</td>
      <td>BCN/LEBL</td>
      <td>50148228</td>
      <td>1.0</td>
      <td>6.1%</td>
    </tr>
    <tr>
      <th>27</th>
      <td>28.0</td>
      <td>Chhatrapati Shivaji Maharaj International Airport</td>
      <td>Mumbai, Maharashtra</td>
      <td>India</td>
      <td>BOM/VABB</td>
      <td>49876769</td>
      <td>1.0</td>
      <td>5.7%</td>
    </tr>
    <tr>
      <th>28</th>
      <td>29.0</td>
      <td>McCarran International Airport</td>
      <td>Las Vegas, Nevada</td>
      <td>United States</td>
      <td>LAS/KLAS</td>
      <td>49863090</td>
      <td>2.0</td>
      <td>2.7%</td>
    </tr>
    <tr>
      <th>29</th>
      <td>30.0</td>
      <td>Seattle–Tacoma International Airport</td>
      <td>SeaTac, Washington</td>
      <td>United States</td>
      <td>SEA/KSEA</td>
      <td>49849520</td>
      <td>1.0</td>
      <td>6.2%</td>
    </tr>
    <tr>
      <th>30</th>
      <td>31.0</td>
      <td>Toronto Pearson International Airport</td>
      <td>Mississauga, Ontario</td>
      <td>Canada</td>
      <td>YYZ/CYYZ</td>
      <td>49467097</td>
      <td>1.0</td>
      <td>5.0%</td>
    </tr>
    <tr>
      <th>31</th>
      <td>32.0</td>
      <td>Shenzhen Bao'an International Airport</td>
      <td>Bao'an, Shenzhen, Guangdong</td>
      <td>China</td>
      <td>SZX/ZGSZ</td>
      <td>49348950</td>
      <td>2.0</td>
      <td>8.3%</td>
    </tr>
    <tr>
      <th>32</th>
      <td>33.0</td>
      <td>Mexico City International Airport</td>
      <td>Venustiano Carranza, Mexico City</td>
      <td>Mexico</td>
      <td>MEX/MMMX</td>
      <td>47700834</td>
      <td>3.0</td>
      <td>6.6%</td>
    </tr>
    <tr>
      <th>33</th>
      <td>34.0</td>
      <td>Orlando International Airport</td>
      <td>Orlando, Florida</td>
      <td>United States</td>
      <td>MCO/KMCO</td>
      <td>47694573</td>
      <td>5.0</td>
      <td>7.2%</td>
    </tr>
    <tr>
      <th>34</th>
      <td>35.0</td>
      <td>Kunming Changshui International Airport</td>
      <td>Guandu, Kunming, Yunnan</td>
      <td>China</td>
      <td>KMG/ZPPP</td>
      <td>47215986</td>
      <td>2.0</td>
      <td>5.6%</td>
    </tr>
    <tr>
      <th>35</th>
      <td>36.0</td>
      <td>Taiwan Taoyuan International Airport</td>
      <td>Dayuan, Taoyuan</td>
      <td>Taiwan</td>
      <td>TPE/RCTP</td>
      <td>46535180</td>
      <td>1.0</td>
      <td>3.7%</td>
    </tr>
    <tr>
      <th>36</th>
      <td>37.0</td>
      <td>Charlotte Douglas International Airport</td>
      <td>Charlotte, North Carolina</td>
      <td>United States</td>
      <td>CLT/KCLT</td>
      <td>46446721</td>
      <td>5.0</td>
      <td>1.2%</td>
    </tr>
    <tr>
      <th>37</th>
      <td>38.0</td>
      <td>London Gatwick Airport</td>
      <td>Crawley, West Sussex</td>
      <td>United Kingdom</td>
      <td>LGW/EGKK</td>
      <td>46432630</td>
      <td>6.0</td>
      <td>1.9%</td>
    </tr>
    <tr>
      <th>38</th>
      <td>39.0</td>
      <td>Munich Airport</td>
      <td>Freising, Bavaria</td>
      <td>Germany</td>
      <td>MUC/EDDM</td>
      <td>46253623</td>
      <td>1.0</td>
      <td>3.8%</td>
    </tr>
    <tr>
      <th>39</th>
      <td>40.0</td>
      <td>Newark Liberty International Airport</td>
      <td>Newark, New Jersey</td>
      <td>United States</td>
      <td>EWR/KEWR</td>
      <td>46065175</td>
      <td>3.0</td>
      <td>6.6%</td>
    </tr>
    <tr>
      <th>40</th>
      <td>41.0</td>
      <td>Sheremetyevo International Airport</td>
      <td>Khimki, Moscow Oblast</td>
      <td>Russia</td>
      <td>SVO/UUEE</td>
      <td>45836255</td>
      <td>9.0</td>
      <td>14.3%</td>
    </tr>
    <tr>
      <th>41</th>
      <td>42.0</td>
      <td>Miami International Airport</td>
      <td>Miami-Dade County, Florida</td>
      <td>United States</td>
      <td>MIA/KMIA</td>
      <td>45044312</td>
      <td>2.0</td>
      <td>2.1%</td>
    </tr>
    <tr>
      <th>42</th>
      <td>43.0</td>
      <td>Phoenix Sky Harbor International Airport</td>
      <td>Phoenix, Arizona</td>
      <td>United States</td>
      <td>PHX/KPHX</td>
      <td>44943686</td>
      <td>2.0</td>
      <td>2.3%</td>
    </tr>
    <tr>
      <th>43</th>
      <td>44.0</td>
      <td>Xi'an Xianyang International Airport</td>
      <td>Weicheng, Xianyang, Shaanxi</td>
      <td>China</td>
      <td>XIY/ZLXY</td>
      <td>44653927</td>
      <td>2.0</td>
      <td>6.7%</td>
    </tr>
    <tr>
      <th>44</th>
      <td>45.0</td>
      <td>Ninoy Aquino International Airport</td>
      <td>Pasay/Parañaque, Metro Manila</td>
      <td>Philippines</td>
      <td>MNL/RPLL</td>
      <td>44488321</td>
      <td>1.0</td>
      <td>5.9%</td>
    </tr>
    <tr>
      <th>45</th>
      <td>46.0</td>
      <td>Sydney Kingsford-Smith Airport</td>
      <td>Mascot, New South Wales</td>
      <td>Australia</td>
      <td>SYD/YSSY</td>
      <td>44475976</td>
      <td>4.0</td>
      <td>2.5%</td>
    </tr>
    <tr>
      <th>46</th>
      <td>47.0</td>
      <td>George Bush Intercontinental Airport</td>
      <td>Houston, Texas</td>
      <td>United States</td>
      <td>IAH/KIAH</td>
      <td>43807539</td>
      <td>1.0</td>
      <td>7.7%</td>
    </tr>
    <tr>
      <th>47</th>
      <td>48.0</td>
      <td>Shanghai Hongqiao International Airport</td>
      <td>Changning-Minhang, Shanghai</td>
      <td>China</td>
      <td>SHA/ZSSS</td>
      <td>43628004</td>
      <td>3.0</td>
      <td>4.2%</td>
    </tr>
    <tr>
      <th>48</th>
      <td>49.0</td>
      <td>Rome–Fiumicino International Airport "Leonardo...</td>
      <td>Rome-Fiumicino, Lazio</td>
      <td>Italy</td>
      <td>FCO/LIRF</td>
      <td>42991056</td>
      <td>2.0</td>
      <td>4.9%</td>
    </tr>
    <tr>
      <th>49</th>
      <td>50.0</td>
      <td>Narita International Airport</td>
      <td>Narita, Chiba</td>
      <td>Japan</td>
      <td>NRT/RJAA</td>
      <td>42549173</td>
      <td>1.0</td>
      <td>4.7%</td>
    </tr>
  </tbody>
</table>
</div>




```python

```
