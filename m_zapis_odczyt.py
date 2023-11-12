def zapis(nazwapliku, tryb, rodzaj, tresc):
    try:
        with open(nazwapliku, tryb) as f:
            if rodzaj in ("txt", "lista", "slownik"):
                if rodzaj == "txt":
                    f.write(tresc)
                elif rodzaj == "lista":
                    for tr in tresc:
                        if isinstance(tr, str):
                            f.write(tr + "\n")
                        else:
                            f.write(str(tr) + "\n")
                            
                    
                    print(f"Zawartość została zapisana do pliku {nazwapliku}.")
            else:
                print(f"Nie potrafie obsłużyć pliku z tymi danymi: {rodzaj}.")
            
    except FileNotFoundError:
        print("Problem z dostępem do pliku...")
    except Exception as e:
        print(f"Wystąpił bład {e}...")



def odczytaj(nazwapliku, rodzaj):
        try:
            with open(nazwapliku, 'r') as f:
                if rodzaj == "txt":
                    data = f.read()
                elif rodzaj == "lista":
                    data = [line.strip() for line in f]
                elif rodzaj == "slownik":
                    data = {}
                    for line in f:
                        key, value = line.strip().split(' : ')
                        data[key] = value
                else:
                    print(f"Nie potrafię odczytać pliku z danymi: {rodzaj}.")
                return None
                return data
        except FileNotFoundError:
            print("Problem z dostępem do pliku...")
            return None
        except Exception as e:
            print(f"Wystąpił błąd {e}...")
            return None

nazwapliku = "sample.txt"
rodzaj = "txt"
dane = odczytaj(nazwapliku, rodzaj)
if dane is not None:
    print(f"Odczytano dane z pliku {nazwapliku}:")
    print(dane)