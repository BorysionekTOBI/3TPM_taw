'''
Ćwiczenie z funkcji
'''

# def srednia(lista):
#     ilosc = len(lista)
#     suma = sum(lista)
#     if ilosc == 0:
#         return 0
#     else:
#         return suma/ilosc

# liczby = [2,3,5,3,5]
# print(srednia(liczby))


#Średnia z dowolnych liczb
# def srednia2(*args):
#     suma = 0
#     ilosc = len(args)
#     for i in args:
#         suma += i
#     return suma/ilosc

# print(srednia2(3,4,5,6,7,8,9,0,1,2,3,4,9,8,8))

#Liczenie liter:

def zlicz_cechy(tekst):
    liczba_liter = 0
    liczba_liczb = 0
    liczba_spacji = 0
    liczba_wyrazow = 0
    
    for znak in tekst:
        if znak.isalpha():
            liczba_liter += 1
        elif znak.isdigit():
            liczba_liczb += 1
        elif znak.isspace():
            liczba_spacji += 1
            
    slowa=tekst.spilt()
    liczba_wyrazow = len(slowa)
    
    return liczba_liczb, liczba_liter, liczba_spacji, liczba_wyrazow

tekst = input("Wpisz jakiś tekst: ")

litery, liczby, spacje, wyrazyc = zlicz_cechy(tekst)

print("Ilość liter:")