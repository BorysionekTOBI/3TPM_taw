'''
sets = zbiory
'''

#zbiory nigdy nie maja duplikatów


#zbiór nie powtarzają się i segregują rosnąco 
# zb = {2, 5, 1, 3, 5, 1 }
# print(zb)

# zb1 = set() #tworzenie pustego zbioru
# print(zb1)

# print(type(zb))
# print(type(zb1))


# zb.add(4) #dodawanie do zbioru
# zb.add(5)
# print(zb)

# zb.remove(2) #usuwanie ze zbioru
# print(zb)

# zb.remove(2) #tutaj bedzie błąd poniewaz nie ma elementu w zbiorze
# zb.discard(2) #tutaj nie bedzie błędu nawet jezeli nie ma elementu w zbiorze
# print(zb)

a = {1, 3, 5}
b = {2, 3, 6}
print(f"a: {a}, b: {b}")

# wspolna = a.intersection(b) #część wspolna
# print(wspolna)

# suma = a.union(b) #dodawanie
# print(suma)

# roznica = a.difference(b) #odejmoanie
# print(roznica)
# roznica2 = b.difference(a)
# print(roznica2)

# if 3 in b:
#         b.remove(3)

# if 3 in b:
#         b.remove(3)
        
# print(b)

# lista1 = {2, 4, 5, 6, 9}
# if 1 in lista1:
#     print("Jest")
# else:
#     print("Nie")

#Zadanie usuń z listy elementy powtarzające się 

listaX = [2, 3, 4, 2, 3, 4, 2, 3, 4]

listaX = list(set(listaX)) #zamiana listy na set (zbiór)
print(listaX)

