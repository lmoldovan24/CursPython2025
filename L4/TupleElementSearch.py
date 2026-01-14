#Scrie un program care creeaza o tupla din inputul primit de la
#tastatura (valori separate prin virgula). Apoi, cere utilizatorului sa introduca o valoare care sa
#fie cautata in tupla. Printeaza daca valoarea se regaseste in tupla sau nu, iar daca da, printeaza
#indexul la care se gaseste aceasta.
#ex: input: 1, 2
#search for: 2
#tupla: (1, 2)
#output: 2 se regaseste in tupla la indexul 1.

def citeste_tupla():
    while True:
        try:
            text = input("Introdu valori separate prin virgulă: ")
            elemente = text.split(",")

            tupla = tuple(
                int(float(elem.strip().replace(",", ".")))
                for elem in elemente
            )

            if len(tupla) == 0:
                raise ValueError

            return tupla

        except ValueError:
            print("Input invalid. Introdu doar numere separate prin virgulă.")


def citeste_valoare():
    while True:
        try:
            valoare = input("Introdu valoarea de căutat: ")
            valoare = valoare.replace(",", ".")
            return int(float(valoare))
        except ValueError:
            print("Valoare invalidă. Introdu un număr.")


# Program principal
tupla = citeste_tupla()
valoare = citeste_valoare()

print(f"\nTupla este: {tupla}")

try:
    index = tupla.index(valoare)
    print(f"{valoare} se regăsește în tuplă la indexul {index}.")
except ValueError:
    print(f"{valoare} NU se regăsește în tuplă.")
