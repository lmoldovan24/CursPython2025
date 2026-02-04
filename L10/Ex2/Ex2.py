#Problema 2. Creeaza o functie care citeste un fisier text ce contine
#numere pe fiecare linie. Functia ar trebui sa calculeze suma acestor numere,
#gestionand exceptiile pentru fisier inexistent, erori de citire si valori nevalide.

def suma_din_fisier(nume_fisier):
    suma = 0

    try:
        with open(nume_fisier, "r") as fisier:
            for linie in fisier:
                linie = linie.strip()

                # acceptăm și 2,5 ca 2.5
                linie = linie.replace(",", ".")

                try:
                    numar = float(linie)
                    suma += numar
                except ValueError:
                    print(f"⚠️ Valoare invalidă ignorată: {linie}")

        return suma

    except FileNotFoundError:
        print("Eroare: fișierul nu există.")
    except IOError:
        print("Eroare la citirea fișierului.")
    except Exception as e:
        print(f"Eroare neașteptată: {e}")

rezultat = suma_din_fisier("numere.txt")
if rezultat is not None:
    print("✅ Suma numerelor este:", rezultat)
