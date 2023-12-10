'''
Typ sekwencyjny - listy
'''
'''
lista1 = [1,4,3,5]
lista2 = [2,4.7,"tekst"]
lista3 = [1, 3.4, [4,6,"coś"]]

print(type(lista1))
print(type(lista2))
print(type(lista3)) 

print(lista2[1])
print(lista3[2][2])

#lewa 0 1 2 3 ....
#prawa ... -3 -2 -1

print(lista2[-1])
'''
'''
moja_lista = [1,4,2,5,3,6,3]
print(moja_lista[1:4])

#[6,3,5]
print(moja_lista[-2:-5:-1])

#[3,3,2,1] od prawej
print(moja_lista[::-2])

#[3,3,2] od prawej
print(moja_lista[:1:-2])
'''

nowa=['a','b','c','d','e','f','g']

#b d f
print(nowa[1::2])

#e c a
print(nowa[-3::-2])

#f d b
print(nowa[-2::-2])

