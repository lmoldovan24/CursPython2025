# Ex4: Verifică dacă un număr este prim

# --- Citire și validare număr ---
while True:
    raw = input("Introdu un număr: ").strip()

    if raw == "":
        print("Nu ai introdus nimic. Te rog introdu un număr.")
        continue

    raw = raw.replace(",", ".")  # acceptăm 5,0 -> 5.0

    try:
        num_float = float(raw)
    except ValueError:
        print("Valoare invalidă! Introdu un număr întreg (ex: 7, 11, 13).")
        continue
    except OverflowError:
        print("Număr prea mare pentru a fi procesat!")
        continue

    # Trebuie să fie întreg
    if not num_float.is_integer():
        print("Numărul trebuie să fie întreg, nu zecimal.")
        continue

    numar = int(num_float)
    break


# --- Determinare dacă numărul este prim ---
if numar <= 1:
    print("Numărul NU este prim.")
else:
    este_prim = True

    # Optimizare: verificăm doar până la rădăcina pătrată
    from math import isqrt
    for i in range(2, isqrt(numar) + 1):
        if numar % i == 0:
            este_prim = False
            break

    if este_prim:
        print("Numărul ESTE prim.")
    else:
        print("Numărul NU este prim.")
