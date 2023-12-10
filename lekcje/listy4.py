'''
Porównanie pętli i list comprehension

Stwórz liste liczby składajaca sie z 1000 calkowitych liczb losowych z zakresu 1 do 100
'''

import random as rd
#from random import radiant as rdi

liczby=[]
for i in range(1000):
    liczby.append(rd.randint(1,100))

print(liczby)


#list comprehension

liczby_losowe =[rd.randint(1,100)for i in range(1000)]
print(liczby_losowe)