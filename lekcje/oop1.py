class Osoba:
    def __init__(self, imie, nazwisko, wiek=16):
        self.imie = imie
        self.nazwisko = nazwisko
        self.wiek = wiek
    def przedstaw_sie(self):
        return f"Nazywam siec {self.imie} {self.nazwisko} i mam {self.wiek} lat."
    
    def zwieksz_wiek(self, ile=0):
        self.wiek+=ile
        return self.wiek
    
class Uczen(Osoba):
    def __init__(self, imie, nazwisko, wiek, klasa):
        super().__init__(imie, nazwisko, wiek)
        self.klasa = klasa
        
    def przedstaw_sie(self):
        return f"Nazywam sie {self.imie} {self.nazwisko} mam {self.wiek} lat i jestem uczniem klasy {self.klasa}. "
    
class Nauczyciel(Osoba):
    def __init__(self, imie, nazwisko, wiek, przedmiot):
        super().__init__(imie, nazwisko, wiek)
        self.przedmiot = przedmiot
    
    def przedstaw_sie(self):
        return f"Nazywam sie {self.imie} {self.nazwisko} mam {self.wiek} lat i jestem nauczycielem {self.przedmiot}. "
    
#------------------------------------------------------------------------

