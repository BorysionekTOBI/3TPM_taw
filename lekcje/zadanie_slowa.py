'''
Wygeneruj 1000 słów z losowych liter o długościach od 3 do 10 znaków i zapisz je do pliku 
w koejnych liniach.
Sprawdź czy w pliku znajdują się wyrazy, które mają długość większą niż 4 znaki i są jednocześnie palindromami.
Wypisz liczbę słów spełniających ww. warunek.

'''

# chr - konwertowanie na ASCII print(chr(97))

# import random as rd
# wyrazy = []
# for i in range(1000):
#     dl = rd.randint(3, 10)
#     wyraz = ''
#     for j in range(dl):
#         wyraz += chr(rd.randint(97, 122))
#     wyrazy.append(wyraz)
    
# print(wyrazy)

# for wyraz in wyrazy:
#     if len(wyraz) > 4 and wyraz == wyraz[::-1]:
#         print(wyraz) 

import random as rd
with open("wyrazy.txt", "wt") as f:
    for i in range(1000):
        dl = rd.randint(3, 10)
        wyraz = ''
        for j in range(dl):
            wyraz += chr(rd.randint(97, 122))
        f.write(wyraz + "\n")

with open("wyrazy.txt", "rt") as f:
    wyrazy = f.readlines()
    for i in range(len(wyrazy)):
        wyrazy[i] = wyrazy[i].replace("\n", "")
        if len(wyrazy[i]) > 4 and wyrazy[i] == wyrazy[i][::-1]:
            print(wyrazy[i])
            
