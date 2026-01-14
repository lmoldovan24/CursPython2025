#Scrie un program care cere de la tastatura o lista de numere
#separate de virgula. Programul trebuie sa converteasca inputul intr-o lista de numere intregi si
#sa afiseze maximul si minimul din lista.

def citeste_lista_numere():
    while True:
        try:
            text = input("Introdu o listă de numere separate prin virgulă: ")
            elemente = text.split(",")

            numere = []
            for elem in elemente:
                elem = elem.strip().replace(",", ".")
                numere.append(int(float(elem)))  # acceptă 1, 1.28, 1,28

            if len(numere) == 0:
                raise ValueError

            return numere

        except ValueError:
            print(" Input invalid. Introdu doar numere separate prin virgulă.")


# Program principal
lista = citeste_lista_numere()

print(f"\nLista de numere (convertite la întregi): {lista}")
print(f" Maximul: {max(lista)}")
print(f" Minimul: {min(lista)}")
