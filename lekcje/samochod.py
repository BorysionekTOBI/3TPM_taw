'''
Tobiasz Borysionek 2 3TPM
'''

class Samochod:
        def __init__(self, marka, model, rocznik, pojemnosc_silnika, przebieg, wlasciciel):
            self.marka = marka
            self.model = model
            self.rocznik = rocznik
            self.pojemnosc_silnika = pojemnosc_silnika
            self.przebieg = przebieg
            self.wlasciciel = wlasciciel


def pokaz_samochod(self):
        print(f"Marka: {self.marka}\nModel: {self.model}\nRocznik: {self.rocznik}\nPojemność silnika: {self.pojemnosc_silnika}\nPrzebieg: {self.przebieg}\nWłaściciel: {self.wlasciciel}")

def zmien_przebieg(self, nowy_przebieg):
    self.przebieg = nowy_przebieg
    print(f"Przebieg został zmieniony na {nowy_przebieg} km.")

def zmien_wlasciciela(self, nowy_wlasciciel):
    self.wlasciciel = nowy_wlasciciel
    print(f"Właściciel został zmieniony na {nowy_wlasciciel}.")

def zapisz_pojazd(self):
    with open("samochod.txt", "a") as file:
        file.write(f"Marka: {self.marka}, Model: {self.model}, Rocznik: {self.rocznik}, Pojemność silnika: {self.pojemnosc_silnika}, Przebieg: {self.przebieg}, Właściciel: {self.wlasciciel}\n")
        print("Informacje o samochodzie zostały zapisane do pliku samochod.txt.")


    class Osobowy(Samochod):
        def __init__(self, marka, model, rocznik, pojemnosc_silnika, przebieg, wlasciciel, liczba_miejsc):
            super().__init__(marka, model, rocznik, pojemnosc_silnika, przebieg, wlasciciel)
            self.liczba_miejsc = liczba_miejsc

        def pokaz_osobowy(self):
            self.pokaz_samochod()
            print(f"Liczba miejsc: {self.liczba_miejsc}")

        def zmien_liczbe_miejsc(self, nowa_liczba_miejsc):
            self.liczba_miejsc = nowa_liczba_miejsc
            print(f"Liczba miejsc została zmieniona na {nowa_liczba_miejsc}.")

        def zapisz_pojazd(self):
            with open("osobowy.txt", "a") as file:
                file.write(f"Marka: {self.marka}, Model: {self.model}, Rocznik: {self.rocznik}, Pojemność silnika: {self.pojemnosc_silnika}, Przebieg: {self.przebieg}, Właściciel: {self.wlasciciel}, Liczba miejsc: {self.liczba_miejsc}\n")
                print("Informacje o pojeździe osobowym zostały zapisane do pliku osobowy.txt.")


    def main():
        # Tworzenie obiektu Samochod
        samochod = Samochod("Porsche", "911 GT3 RS", 2023, 4.0, 1000, "Adolf Śląski")

        # Wywołanie metody pokaz_samochod
        samochod.pokaz_samochod()

        # Zmiana przebiegu
        samochod.zmien_przebieg(5000)

        # Zmiana właściciela
        samochod.zmien_wlasciciela("Donald Tupet")

        # Zapis do pliku
        samochod.zapisz_pojazd()  # Zapisze do pliku samochod.txt

        # Czynności się powtarzają:
        osobowy_samochod = Osobowy("Rolls-Royce", "Phantom", 2022, 6.75, 20000, "Błażej Angielski", 5)

        osobowy_samochod.pokaz_osobowy()

        osobowy_samochod.zmien_liczbe_miejsc(4)

        osobowy_samochod.zapisz_pojazd()

    if __name__ == "__main__":
        main()
    