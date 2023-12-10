class Osoba:
    def __init__(self, imie, nazwisko, wiek):
        self.imie = imie
        self.nazwisko = nazwisko
        self.wiek = wiek

class KontoBankowe:
    def __init__(self, imie, saldo=0):
        self.imie = imie
        self.saldo = saldo

    def wplac(self, kwota):
        self.saldo += kwota
        print(f'Wpłacono {kwota} PLN. Aktualne saldo: {self.saldo} PLN')

    def wyplac(self, kwota):
        if kwota <= self.saldo:
            self.saldo -= kwota
            print(f'Wypłacono {kwota} PLN. Aktualne saldo: {self.saldo} PLN')
        else:
            print('Brak wystarczających środków.')

    def dodaj_odejmij_kwote(self, kwota, operacja='dodaj'):
        if operacja == 'dodaj':
            self.saldo += kwota
            print(f'Dodano {kwota} PLN. Aktualne saldo: {self.saldo} PLN')
        elif operacja == 'odejmij':
            if kwota <= self.saldo:
                self.saldo -= kwota
                print(f'Odejmowano {kwota} PLN. Aktualne saldo: {self.saldo} PLN')
            else:
                print('Brak wystarczających środków.')
        else:
            print('Nieprawidłowa operacja. Dostępne operacje: dodaj, odejmij')

    def sprawdz_saldo(self):
        print(f'Aktualne saldo dla konta {self.imie}: {self.saldo} PLN')

def utworz_konto_dla_osoby(osoba, saldo_poczatkowe=0):
    imie_nazwisko = f"{osoba.imie} {osoba.nazwisko}"
    return KontoBankowe(imie_nazwisko, saldo_poczatkowe)


osoba = Osoba('Adam', 'Małysz', 30)
konto_osoby = utworz_konto_dla_osoby(osoba, 1500)

konto_osoby.sprawdz_saldo()

konto_osoby.dodaj_odejmij_kwote(4000, 'dodaj')

konto_osoby.dodaj_odejmij_kwote(2000, 'odejmij') 

konto_osoby.dodaj_odejmij_kwote(7000, 'odejmij')

konto_osoby.sprawdz_saldo()
