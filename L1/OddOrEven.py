#Ex2: OddOrEven: Creeaza un program care cere userului un numar intreg si afiseaza
#daca acest numar este par sau impar. (hint, '%' returneaza restul impartirii)


while True:
    raw = input("Introdu un număr întreg: ").strip()

    # Cazul Enter gol
    if raw == "":
        print("Nu ai introdus nicio valoare. Încearcă din nou.")
        continue

    # Acceptăm și virgula ca separator decimal
    raw = raw.replace(",", ".")

    try:
        # Încercăm conversia la float (permite 3.0, 3,0 etc.)
        valoare_float = float(raw)
    except ValueError:
        print("Valoare invalidă! Te rog introdu un număr întreg (ex: 3, -5, 4.0).")
        continue
    except OverflowError:
        print("Număr prea mare pentru a fi procesat!")
        continue

    # Verificăm dacă numărul este întreg (float.is_integer())
    if not valoare_float.is_integer():
        print("Numărul trebuie să fie întreg, nu zecimal (ex: 3, 5, 4.0).")
        continue

    numar = int(valoare_float)
    break


# Determinarea parității
if numar % 2 == 0:
    print("Număr par")
else:
    print("Număr impar")
