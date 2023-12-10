from m_zapis_odczyt import zapis

tekst = """
    Pierwsza linia.
    Druga linia.
    Trzecia linia.
"""

liczby = [i**2 for i in range(100)]
# liczby = [2, 2, "rower", 3, "adam"]

sl = {"imie" : "Jan", "Nazwisko": "Kowalski", "Wiek": "18"}

zapis("text.txt", "wt", "txt", tekst)
zapis("liczby.txt", "wt", "lista", liczby)
zapis("slownik.txt", "wt", "slownik", sl)