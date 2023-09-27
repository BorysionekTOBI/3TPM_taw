'''
Listy jako obiekty
'''
'''
lista1 = [2,3,5,7,9]

print(type(lista1))
print(lista1)

lista1.append(33)
print(lista1)

lista1.pop()
print(lista1)

lista1.remove(5)
print(lista1)


lista2 = []
lista2 = lista1
print(lista2)
lista1.append(33)
print(lista2)



lista3=lista1.copy()
print(lista3)
lista1.append(44)
print(lista1)
print(lista3)

lista4=[]
lista4.extend(lista1)
print(lista1)


lista5 = []
#dodaj 6 do listy5
#poszerz liste 5 o elementy z listy 1 w kolejnosci 7,5,3

lista1 = [2,3,5,7,9]

lista5.append(6)
lista5.extend(lista1[-2:-5:-1])
print(lista5)

lista5.clear()
print(lista5)

lista1.insert(2,0)
print(lista1)
'''

lista1 = [2,3,5,7,9]
#count
m=lista1.count(3)


print(f"Trójek w liscie jest {m}")


n=len(lista1)
print(f"Elementów w liscie jest {n}")


lista1.reverse()
print(lista1)


lista1.sort()
print(lista1)

