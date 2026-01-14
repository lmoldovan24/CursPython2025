
#1. GradingSystem: Scrie un program care cere utilizatorului să introducă un scor procentual
#(0-100). Pe baza scorului, programul va afișa nota corespunzătoare utilizând următoarele
#criterii:
#90 și peste: Nota A
#80 până la 89: Nota B
#70 până la 79: Nota C
#60 până la 69: Nota D
#Sub 60: Nota F

while True:
    inp = input("Introduceți scorul procentual (0-100): ").strip()

    # Caz: input gol sau doar spații
    if inp == "":
        print("Eroare: Nu ați introdus nicio valoare.\n")
        continue

    # Înlocuim virgula cu punct
    inp = inp.replace(",", ".")

    try:
        scor = float(inp)

        # Verificăm intervalul
        if scor < 0 or scor > 100:
            print("Eroare: Scorul trebuie să fie între 0 și 100.\n")
            continue

        # Dacă este valid, ieșim din while
        break

    except ValueError:
        print("Eroare: Vă rugăm să introduceți un număr valid.\n")

# Afișarea notei
if scor >= 90:
    print("Nota A")
elif scor >= 80:
    print("Nota B")
elif scor >= 70:
    print("Nota C")
elif scor >= 60:
    print("Nota D")
else:
    print("Nota F")
