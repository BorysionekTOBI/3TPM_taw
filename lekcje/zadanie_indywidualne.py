"""
Zadanie zaliczeniowe z języka Python
Imię i nazwisko ucznia: Tobiasz Borysionek
Data wykonania zadania: 06.12.2023
Treść zadania: Hurtownia materiałów budowlanych
Opis funkcjonalności aplikacji: Aplikacja reprezentuje system hurtowni materiałów budowlanych, 
umożliwiający zarządzanie dostępnymi produktami, składanie zamówień oraz śledzenie stanu magazynowego.
"""

import json

class Produkt:
    def __init__(self, nazwa, cena, ilosc):
        """
        Inicjalizacja obiektu Produkt.

        :param nazwa: Nazwa produktu.
        :param cena: Cena produktu.
        :param ilosc: Ilość produktu dostępna w magazynie.
        """
        self.nazwa = nazwa
        self.cena = max(0, cena)  # Walidacja: cena nie może być ujemna
        self.ilosc = max(0, ilosc)  # Walidacja: ilość nie może być ujemna

    def __str__(self):
        """
        Zwraca reprezentację napisową obiektu Produkt.

        :return: Napis reprezentujący produkt.
        """
        return f"{self.nazwa} - Cena: {self.cena} zł, Ilość: {self.ilosc} sztuk"

    def to_dict(self):
        """
        Zwraca reprezentację obiektu Produkt jako słownik.

        :return: Słownik z danymi produktu.
        """
        return {
            "nazwa": self.nazwa,
            "cena": self.cena,
            "ilosc": self.ilosc
        }

class Zamowienie:
    RABAT_PROGOWY = 1000  # Rabat przy zamówieniu powyżej 1000 zł
    RABAT_WARTOSC = 0.1  # 10% rabatu

    def __init__(self):
        """
        Inicjalizacja obiektu Zamowienie.
        """
        self.zamowione_produkty = {}

    def dodaj_produkt(self, produkt, ilosc):
        """
        Dodaje produkt do zamówienia.

        :param produkt: Obiekt Produkt.
        :param ilosc: Ilość zamawianego produktu.
        """
        if ilosc > 0:
            if produkt.nazwa in self.zamowione_produkty:
                self.zamowione_produkty[produkt.nazwa]["ilosc"] += ilosc
            else:
                self.zamowione_produkty[produkt.nazwa] = {"produkt": produkt, "ilosc": ilosc}

    def koszt_produktu(self, produkt):
        """
        Oblicza koszt danego produktu w zamówieniu.

        :param produkt: Obiekt Produkt.
        :return: Koszt produktu w zamówieniu.
        """
        return produkt.cena * self.zamowione_produkty[produkt.nazwa]["ilosc"]

    def koszt_calkowity(self):
        """
        Oblicza całkowity koszt zamówienia, uwzględniając ewentualny rabat.

        :return: Całkowity koszt zamówienia.
        """
        koszty_produktow = [self.koszt_produktu(produkt["produkt"]) for produkt in self.zamowione_produkty.values()]
        calkowity_koszt = sum(koszty_produktow)
        
        # Rabat
        if calkowity_koszt > self.RABAT_PROGOWY:
            calkowity_koszt -= calkowity_koszt * self.RABAT_WARTOSC

        return calkowity_koszt

    def wyswietl_zamowienie(self):
        """
        Wyświetla szczegóły zamówienia w konsoli.
        """
        print("Zamówienie:")
        for produkt, dane in self.zamowione_produkty.items():
            koszt_produktu = self.koszt_produktu(dane["produkt"])
            print(f"{produkt} - Ilość: {dane['ilosc']}, Koszt: {koszt_produktu} zł")
        print(f"Całkowity koszt zamówienia: {self.koszt_calkowity()} zł (rabat uwzględniony)")

class Hurtownia:
    def __init__(self):
        """
        Inicjalizacja obiektu Hurtownia.
        """
        self.produkty = []

    def dodaj_produkt(self, produkt):
        """
        Dodaje produkt do oferty hurtowni.

        :param produkt: Obiekt Produkt.
        """
        if produkt not in self.produkty:
            self.produkty.append(produkt)

    def usun_produkt(self, nazwa_produktu):
        """
        Usuwa produkt z oferty hurtowni.

        :param nazwa_produktu: Nazwa produktu do usunięcia.
        """
        for produkt in self.produkty:
            if produkt.nazwa == nazwa_produktu:
                self.produkty.remove(produkt)
                print(f"Produkt {nazwa_produktu} został usunięty.")
                return
        print(f"Produkt {nazwa_produktu} nie istnieje w magazynie.")

    def edytuj_produkt(self, nazwa_produktu, nowa_cena, nowa_ilosc):
        """
        Edytuje informacje o produkcie w ofercie hurtowni.

        :param nazwa_produktu: Nazwa produktu do edycji.
        :param nowa_cena: Nowa cena produktu.
        :param nowa_ilosc: Nowa ilość produktu.
        """
        for produkt in self.produkty:
            if produkt.nazwa == nazwa_produktu:
                produkt.cena = max(0, nowa_cena)  # Walidacja: cena nie może być ujemna
                produkt.ilosc = max(0, nowa_ilosc)  # Walidacja: ilość nie może być ujemna
                print(f"Informacje o produkcie {nazwa_produktu} zostały zaktualizowane.")
                return
        print(f"Produkt {nazwa_produktu} nie istnieje w magazynie.")

    def wyswietl_produkty(self):
        """
        Wyświetla dostępne produkty w ofercie hurtowni.
        """
        print("Dostępne produkty:")
        for produkt in self.produkty:
            print(produkt)

    def przyjmij_zamowienie(self, zamowienie):
        """
        Przyjmuje zamówienie od klienta, zmniejsza ilości produktów w magazynie.

        :param zamowienie: Obiekt Zamowienie.
        """
        print("Przyjęto zamówienie:")
        for produkt, dane in zamowienie.zamowione_produkty.items():
            for dostepny_produkt in self.produkty:
                if dostepny_produkt.nazwa == produkt and dostepny_produkt.ilosc >= dane["ilosc"]:
                    dostepny_produkt.ilosc -= dane["ilosc"]
                    print(f"{produkt} - Ilość: {dane['ilosc']}")
                    break
            else:
                print(f"Brak wystarczającej ilości produktu {produkt}")

    def zapisz_do_pliku(self, nazwa_pliku="hurtownia.json"):
        """
        Zapisuje stan oferty hurtowni do pliku JSON.

        :param nazwa_pliku: Nazwa pliku do zapisu.
        """
        with open(nazwa_pliku, "w") as plik:
            produkty_dict = [produkt.to_dict() for produkt in self.produkty]
            json.dump(produkty_dict, plik, indent=2)

    def wczytaj_z_pliku(self, nazwa_pliku="hurtownia.json"):
        """
        Wczytuje stan oferty hurtowni z pliku JSON.

        :param nazwa_pliku: Nazwa pliku do wczytania.
        """
        try:
            with open(nazwa_pliku, "r") as plik:
                dane = json.load(plik)
                for produkt_data in dane:
                    produkt = Produkt(**produkt_data)
                    self.dodaj_produkt(produkt)
        except FileNotFoundError:
            print("Plik nie istnieje. Tworzona nowa hurtownia.")

def interfejs_uzytkownika():
    """
    Prosty interfejs użytkownika w wierszu poleceń.
    """
    hurtownia = Hurtownia()
    hurtownia.wczytaj_z_pliku()

    while True:
        print("\n======== MENU ========"
              "\n1. Wyświetl dostępne produkty"
              "\n2. Dodaj zamówienie"
              "\n3. Usuń produkt z oferty hurtowni"
              "\n4. Edytuj produkt w ofercie hurtowni"
              "\n5. Zakończ program")

        wybor = input("Wybierz opcję: ")

        if wybor == "1":
            hurtownia.wyswietl_produkty()

        elif wybor == "2":
            zamowienie = Zamowienie()
            print("\nDodawanie zamówienia:")
            while True:
                nazwa_produktu = input("Podaj nazwę produktu (wpisz 'koniec' aby zakończyć dodawanie): ")
                if nazwa_produktu.lower() == 'koniec':
                    break
                ilosc = int(input("Podaj ilość: "))
                produkt = None

                for dostepny_produkt in hurtownia.produkty:
                    if dostepny_produkt.nazwa == nazwa_produktu and dostepny_produkt.ilosc >= ilosc:
                        produkt = dostepny_produkt
                        break

                if produkt:
                    zamowienie.dodaj_produkt(produkt, ilosc)
                    hurtownia.przyjmij_zamowienie(zamowienie)
                    zamowienie.wyswietl_zamowienie()
                else:
                    print(f"Produkt {nazwa_produktu} niedostępny w wymaganej ilości.")

        elif wybor == "3":
            nazwa_produktu = input("Podaj nazwę produktu do usunięcia: ")
            hurtownia.usun_produkt(nazwa_produktu)

        elif wybor == "4":
            nazwa_produktu = input("Podaj nazwę produktu do edycji: ")
            nowa_cena = float(input("Podaj nową cenę: "))
            nowa_ilosc = int(input("Podaj nową ilość: "))
            hurtownia.edytuj_produkt(nazwa_produktu, nowa_cena, nowa_ilosc)

        elif wybor == "5":
            hurtownia.zapisz_do_pliku()
            print("Do widzenia!")
            break

        else:
            print("Nieprawidłowy wybór. Spróbuj ponownie.")

if __name__ == "__main__":
    interfejs_uzytkownika()