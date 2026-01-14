#3. NumberGuessing: Creează un joc simplu de ghicit un număr, unde programul alege un
#număr aleator între 1 și 20. Utilizatorul are 5 încercări pentru a ghici numărul. După fiecare
#încercare, programul va oferi feedback ("Prea mare", "Prea mic", sau "Corect!"

import random

numar_secret = random.randint(1, 20)
incercari_maxime = 5

print("Trebuie sa ghicesti un număr între 1 și 20.")
print(f"Ai {incercari_maxime} încercări.\n")

for incercare in range(1, incercari_maxime + 1):
    while True:
        try:
            ghicire = int(input(f"Încercarea {incercare}: Introdu un număr: "))
            if 1 <= ghicire <= 20:
                break
            else:
                print(" Numărul trebuie să fie între 1 și 20.")
        except ValueError:
            print(" Introdu un număr întreg valid.")

    if ghicire < numar_secret:
        print("📉 Prea mic!\n")
    elif ghicire > numar_secret:
        print("📈 Prea mare!\n")
    else:
        print(f"✅ Corect! Ai ghicit numărul {numar_secret} din {incercare} încercări!")
        break
else:
    print(f" Ai pierdut! Numărul era {numar_secret}.")
