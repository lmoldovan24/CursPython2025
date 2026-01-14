#Ex3: 3. InterestCalculator: Scrie un program ce calculeaza dobanda. Programul va
# cere utilizatorului principalul, rata anuala a dobanzii (ex 5, 6, 10) si timpul in ani.
# Formula: Interest = (Principal x Rate x Time)/100


while True:
    raw = input("Suma: ").strip()
    if raw == "":
        print("Nu ai introdus nicio valoare. Încearcă din nou.")
        continue

    raw = raw.replace(",", ".")  # acceptăm 3,5 -> 3.5

    try:
        principal_float = float(raw)
    except ValueError:
        print("Valoare invalidă! Introdu o sumă numerică.")
        continue
    except OverflowError:
        print("Valoare prea mare pentru a fi procesată!")
        continue

    if principal_float <= 0:
        print("Suma trebuie să fie pozitivă.")
        continue

    principal = principal_float
    break


# --- Citire Rată (doar 5, 6, 10) ---
while True:
    raw = input("Rata (5/6/10): ").strip()
    if raw == "":
        print("Te rog introdu o rată.")
        continue

    raw = raw.replace(",", ".")

    try:
        rate_float = float(raw)
    except ValueError:
        print("Valoare invalidă! Rata trebuie să fie 5, 6 sau 10.")
        continue

    # Acceptăm și formate ca 5.0, 6.00 etc.
    if not rate_float.is_integer():
        print("Rata trebuie să fie un număr întreg: 5, 6 sau 10.")
        continue

    rate = int(rate_float)

    if rate not in (5, 6, 10):
        print("Rata trebuie să fie 5, 6 sau 10.")
        continue

    break


# --- Citire timp (în ani, doar întreg pozitiv) ---
while True:
    raw = input("Timpul (în ani): ").strip()
    if raw == "":
        print("Te rog introdu timpul în ani.")
        continue

    raw = raw.replace(",", ".")

    try:
        time_float = float(raw)
    except ValueError:
        print("Valoare invalidă! Introdu un număr de ani.")
        continue

    if not time_float.is_integer():
        print("Timpul trebuie să fie un număr întreg (ex: 1, 2, 5).")
        continue

    time = int(time_float)

    if time <= 0:
        print("Timpul trebuie să fie pozitiv.")
        continue

    break


# --- Calcul dobândă ---
interest = (principal * rate * time) / 100
print("Dobânda:", interest)
