'''
Dictionary
key : value
'''

slownik1 ={'imie': 'Anna', 'wiek': 18, 'wzrost': 1.76}
#print(type(slownik1))
#print(f"Mój słownik to: {slownik1}")

print(f"Klucze: {slownik1.keys()}")
print(f"Wartości: {slownik1.values()}")

#print(f"Wiek: {slownik1['wiek']}") #1 metoda wyciągania elementów 
#print(f"Wiek: {slownik1.get('wiek')}") #2 metdona wyciągania elementów

#print(f"Słwonik: {slownik1.items()}") #wyświetla liste tupli

#for k,v in slownik1.items():
#   print(f"{k} - {v}")

#slownik1.pop('wiek') #pop wyciąga ostatni element w listach, w pop potrzebujesz argumentu w tym przypadku wiek
#print(slownik1)


#zmiana kolejności kluczy wiek i wzrost

# wiek=slownik1['wiek']
# wzrost=slownik1['wzrost']
# slownik1.pop('wzrost')
# slownik1.pop('wiek')
# print(slownik1.items())
# slownik1['wiek'] =wiek
# slownik1['wzrost'] =wzrost
# print(slownik1.items())

#tu zamieni wartości a nie klucze 

#slownik1['wiek'], slownik1['wzrost'] = slownik1['wzrost'], slownik1['wiek']
#print(slownik1.itmes())

# tup = ('miejscowosc', 'Chojnice')
# print(tup)
# slownik1[tup[0]] = tup[1]
# print(slownik1)

li = list(slownik1.items())
li[1], li[2] = li[2], li[1]
slownik1 = dict(li)
print(slownik1.items())