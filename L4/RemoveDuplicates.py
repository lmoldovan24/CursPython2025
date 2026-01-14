#Scrie un program ce primeste a input o lista de numere separate de
#virgula, inlatura duplicatele si afiseaza lista cu valori unice in aceeasi ordine in care au aparut
#prima data.
#ex: 1, 1, 2, 3, 4, 4, 5, 4
#output: 1, 2, 3, 4, 5

def citeste_lista():
    while True:
        try:
            text = input("Introdu o listă de numere separate prin virgulă: ")
            elemente = text.split(",")

            lista = []
            for elem in elemente:
                elem = elem.strip()
                if elem == "":
                    continue  # IGNORĂ elementele goale (,, sau , la final)

                elem = elem.replace(",", ".")
                numar = int(float(elem))
                lista.append(numar)

            if len(lista) == 0:
                raise ValueError

            return lista

        except ValueError:
            print("❌ Input invalid. Introdu doar numere separate prin virgulă.")


def elimina_duplicate(lista):
    rezultat = []
    for numar in lista:
        if numar not in rezultat:
            rezultat.append(numar)
    return rezultat


# Program principal
lista_initiala = citeste_lista()
lista_unica = elimina_duplicate(lista_initiala)

print("\nLista fără duplicate:")
print(", ".join(str(x) for x in lista_unica))


