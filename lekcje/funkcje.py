'''
funkcje
'''

def menu():
    print(f"Wybór: d - dodawanie, o - odejmowanie, m - mnożenie, s - dzielenie ")
    
def kalkulator(dzialanie, a, b):
    if dzialanie == 'd':
        return a+b
    elif dzialanie == 'o':
        return a-b
    elif dzialanie == 'm':
        return a*b
    elif dzialanie == 's':
        if b!=0:
            "Nie można dzielić przez 0! "
        return a/b
    else: 
        "Zły wybór działania... "

    return True

def funkcja_main():
    a=float(input("Podaj pierwszą liczbe: "))
    b=float(input("Podaj drugą liczbe: "))
    menu()
    dzialanie = input()

    print(f"Wynikiem działanie {dzialanie} dla liczb {a} i {b} jest {kalkulator(dzialanie, a,b)}")

funkcja_main()