#DistanceBetweenPoints.py: Scrie o functie distance(x1, y1, x2, y2) ce calculeaza distanta
#euclideana intre doua puncte (x1, y1) si (x2, y2). Foloseste aceasta functie intr-un program
#care cere coordonatele a doua puncte si printeaza distanta intre ele.

import math

def distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


def citeste_numar(mesaj):
    while True:
        try:
            valoare = input(mesaj)
            valoare = valoare.replace(",", ".")  # acceptă , și .
            return float(valoare)
        except ValueError:
            print("Introdu un număr valid (întreg sau zecimal).")


# Program principal
print("Introdu coordonatele primului punct:")
x1 = citeste_numar("x1 = ")
y1 = citeste_numar("y1 = ")

print("\nIntrodu coordonatele celui de-al doilea punct:")
x2 = citeste_numar("x2 = ")
y2 = citeste_numar("y2 = ")

distanta = distance(x1, y1, x2, y2)

print(f"\n Distanța dintre puncte este: {distanta:.2f}")
