#Problema 2: Scrierea scripturilor Python ca module
#Descriere:
#Scrie un script Python numit math_operations.py care conține funcții pentru următoarele
#operații:
#1. Adunare
#2. Scădere
#3. Înmulțire
#4. Împărțire
#Apoi, scrie un alt script care importă modulul math_operations și folosește aceste funcții.

import math_operations

try:
    a = float(input("Introdu primul număr: "))
    b = float(input("Introdu al doilea număr: "))

    print("Adunare:", math_operations.adunare(a, b))
    print("Scădere:", math_operations.scadere(a, b))
    print("Înmulțire:", math_operations.inmultire(a, b))
    print("Împărțire:", math_operations.impartire(a, b))

except ValueError:
    print("Eroare: trebuie să introduci numere!")

except ZeroDivisionError as zde:
    print("Eroare:", zde)

except Exception as e:
    print("Eroare neașteptată:", e)
