'''
Sprawdzian 01 liczby, listy, krotki
    Tobiasz Borysionek
    3TPM
    28.09.2023
'''

kkadowski@gmail.com

#1
lista1=(2,4,6, 'Anna', 'Zenon')

#2
print("Twoja lista: " +str(lista1))

#3
lista1.remove(4)
print("Twoja lista: " +str(lista1))

#4
lista1.append(99)

#5
lista2=(100, 200, 300)

#6
lista1.extend(lista2)
print("Twoja lista: " +str(lista1))

#7
print("Twoje listy: " +str(lista1, lista2))

#8
lista2.reverse()
print("Twoja lista: " +str(lista2))

#9
print("Twoja lista: " +str(lista2))

#10
listasort=lista1[2:4]
lista1.sort()
print(listasort)
listaint1=lista1[0:2]
listaint2=lista1[4::]
listaint1.extend(listaint2)
listaint1.sort()
listaint1.extend(lista1)
lista = listaint1

#11
print("Twoja lista: " +str(lista1))

#12
moja_tupla=('A', 'B', 'C')

#13
moja_tupla = moja_tupla('D',)

#14
print("Twoja krotka: " +str(moja_tupla))

#BONUS
listaX