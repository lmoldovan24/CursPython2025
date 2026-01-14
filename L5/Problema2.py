#Problema 2: Scrie o funcție unique_pair_sum care primește o listă de numere întregi și
#o valoare țintă. Funcția returnează o mulțime de perechi unice de numere care adunate
#dau valoarea țintă. Fiecare pereche trebuie să fie reprezentată ca un tuplu (a, b) unde a <= b.
#Ex:
#Input:
#numbers = [1, 2, 3, 4, 3, 5, 6]
#target = 7
#Output:
#{(1, 6), (2, 5), (3, 4)}

def citeste_lista():
    while True:
        try:
            text = input("Introdu o listă de numere întregi separate prin virgulă: ")
            elemente = text.split(",")

            numbers = []
            for elem in elemente:
                elem = elem.strip()
                if elem == "":
                    continue  # ignorăm virgule duble sau la final
                numbers.append(int(elem))

            if len(numbers) < 2:
                raise ValueError

            return numbers

        except ValueError:
            print("Input invalid. Introdu doar numere întregi separate prin virgulă.")


def citeste_target():
    while True:
        try:
            return int(input("Introdu valoarea țintă: "))
        except ValueError:
            print("Introdu un număr întreg valid.")


def unique_pair_sum(numbers, target):
    perechi = set()
    vazute = set()

    for numar in numbers:
        complement = target - numar

        if complement in vazute:
            a = min(numar, complement)
            b = max(numar, complement)
            perechi.add((a, b))

        vazute.add(numar)

    return perechi


# ===== Program principal =====
numbers = citeste_lista()
target = citeste_target()

rezultat = unique_pair_sum(numbers, target)

print("\nPerechi unice cu suma egală cu ținta:")
if rezultat:
    print(rezultat)
else:
    print("Nu există perechi care să dea suma cerută.")
