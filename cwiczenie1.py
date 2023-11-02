#Pobieramy liczbę od użytkownika
x = float(input("Podaj liczbę: "))
y = float(input("Podaj druga liczbę: "))

czesc_calkowita = int(x)

czesc_po_przecinku = x - czesc_calkowita

czesc_po_przecinku = int(czesc_po_przecinku * 100)


print(f"Dla liczby {x} część całkowita to: {czesc_calkowita}, część 'po przecinku': {czesc_po_przecinku}")

czesc_calkowita = int(y)

czesc_po_przecinku = y - czesc_calkowita

czesc_po_przecinku = int(czesc_po_przecinku * 100)

print(f"Dla liczby {y} część całkowita to: {czesc_calkowita}, część 'po przecinku': {czesc_po_przecinku}")


x = float(input("Podaj liczbę: "))
y = float(input("Podaj druga liczbę: "))

x=int(x)
y=int(y)


reszta=x%y

print(f"Reszta z dzielenia x={x} przez y={y} wynosi {reszta}")



masa=float(input("Podaj masę w kg"))
wzrost=int(input("Podaj wzrost w cm"))

wzrost=float(wzrost)/100


bmi=masa/wzrost**2


print(f"BMI wynosi: {bmi}")