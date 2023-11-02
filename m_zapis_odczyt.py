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