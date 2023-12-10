'''
Tobiasz Borysionek 2 3TPM
'''

with open('slownik.txt', 'r') as plik:
    zawartosc = plik.read()

if '[' in zawartosc and ']' in zawartosc:
    print("Może to być lista. ")
 
elif '(' in zawartosc and ')' in zawartosc:
    print("Może to być tupla. ")
 
elif '{' in zawartosc and '}' in zawartosc:
    print("Może to być słownik. ")
else:
    print("To jest tekst. ")