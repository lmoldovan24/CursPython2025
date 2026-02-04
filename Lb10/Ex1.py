#Problema 1.Scrie o functie care imparte doua numere.
#Functia ar trebui sa gestioneze exceptia de impartire la zero.

def citeste_numar(mesaj):
    while True:
        valoare = input(mesaj).strip()

        # acceptăm și 2,5 și 2.5
        valoare = valoare.replace(",", ".")

        try:
            return float(valoare)
        except ValueError:
            print("Valoare invalidă. Introdu un număr (ex: 2, 2.5 sau 2,5).")


def imparte_numere():
    a = citeste_numar("Introdu primul număr: ")

    while True:
        b = citeste_numar("Introdu al doilea număr: ")
        if b == 0:
            print("Nu poți împărți la zero. Încearcă din nou.")
        else:
            break

    rezultat = a / b
    print(f"✅ Rezultatul este: {rezultat}")


imparte_numere()
