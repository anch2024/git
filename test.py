
from random import *

ar_com = []
for i in range(6):
    rd = randint(1,46)
    while rd in ar_com:
        rd = randint(1,46)
    ar_com.append(rd)

print(ar_com)
ar_2=set(ar_com)

ar=ar_1 & ar_2