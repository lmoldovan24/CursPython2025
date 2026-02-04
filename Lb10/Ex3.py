#Problema 3. Creeaza un program care simuleaza un sistem de gestionare a unui
#inventar de produse. Utilizatorul va putea adauga produse, cauta produse
#dupa nume si va putea actualiza cantitatea unui produs. Programul va gestiona
#exceptiile pentru intrari nevalide si produse inexistente.

def citeste_text(mesaj):
    while True:
        s = input(mesaj).strip()
        if s:
            return s
        print("Nu poți lăsa gol.")


def citeste_int(mesaj, minim=None):
    while True:
        s = input(mesaj).strip()
        try:
            x = int(s)
            if minim is not None and x < minim:
                print(f"Introdu un număr >= {minim}.")
                continue
            return x
        except ValueError:
            print("Valoare invalidă. Introdu un număr întreg (ex: 0, 3, 10).")


def adauga_produs(inventar):
    nume = citeste_text("Nume produs: ").lower()

    if nume in inventar:
        print("⚠️ Produsul există deja. Poți folosi 'Actualizează cantitate'.")
        return

    cant = citeste_int("Cantitate: ", minim=1)
    inventar[nume] = cant
    print("Produs adăugat.")


def cauta_produs(inventar):
    nume = citeste_text("Caută produs (nume): ").lower()

    if nume not in inventar:
        print("Produs inexistent.")
        return

    print(f"✅ {nume} -> cantitate: {inventar[nume]}")


def actualizeaza_cantitate(inventar):
    nume = citeste_text("Produs de actualizat (nume): ").lower()

    if nume not in inventar:
        print("Produs inexistent.")
        return

    cant_noua = citeste_int("Cantitate nouă: ", minim=0)
    inventar[nume] = cant_noua
    print("✅ Cantitate actualizată.")


def afiseaza_inventar(inventar):
    if not inventar:
        print("📦 Inventarul este gol.")
        return

    print("\n📦 Inventar:")
    for nume, cant in inventar.items():
        print(f" - {nume}: {cant}")
    print()


def meniu():
    inventar = {}

    while True:
        print("\n=== MENIU INVENTAR ===")
        print("1. Adaugă produs")
        print("2. Caută produs după nume")
        print("3. Actualizează cantitatea unui produs")
        print("4. Afișează inventarul")
        print("0. Ieșire")

        opt = input("Alege opțiunea: ").strip()

        try:
            if opt == "1":
                adauga_produs(inventar)
            elif opt == "2":
                cauta_produs(inventar)
            elif opt == "3":
                actualizeaza_cantitate(inventar)
            elif opt == "4":
                afiseaza_inventar(inventar)
            elif opt == "0":
                print(" La revedere!")
                break
            else:
                print("Opțiune invalidă. Alege 0-4.")
        except Exception as e:
            # „plasă de siguranță”, ca să nu crape programul din orice motiv neașteptat
            print(f" Eroare neașteptată: {e}")


# rulează programul
meniu()
