'''
Typ sekwencyjny krotki - immutable!!!!!!
TUPLA
'''

# moja_tupla = (3,4,5)
# print(type(moja_tupla))
# print(moja_tupla)

# moja_tupla2 = moja_tupla
# print(moja_tupla2)

# lista=list(moja_tupla)
# lista.append(8)
# moja_tupla=tuple(lista)
# print(moja_tupla)

moja_tupla = (3,4,5)
moja_tupla = moja_tupla + (8,)
print(moja_tupla)


x, y = 3,4
x, y = y, x
print(x,y)


