#MultiplesFinder: Scrie un program care cere utilizatorului să introducă două numere, x și y,
#și afișează toate multiplurile lui x care sunt mai mici decât y.

def citeste_numar(mesaj):
    while True:
        try:
            valoare = input(mesaj)
            valoare = valoare.replace(",", ".")  # acceptă , și .
            return float(valoare)
        except ValueError:
            print(" Valoare invalidă. Introdu un număr întreg sau zecimal.")

# Citim x (o singură dată)
while True:
    x = citeste_numar("Introdu numărul x: ")
    if x != 0:
        break
    print(" x nu poate fi 0.")

# Citim y până când este mai mare decât x
while True:
    y = citeste_numar("Introdu numărul y: ")
    if y > x:
        break
    print(" y trebuie să fie mai mare decât x. Încearcă din nou.")

# Afișăm multiplii
print(f"\nMultiplii lui {x} mai mici decât {y}:")
multiplu = x
while multiplu < y:
    print(multiplu)
    multiplu += x

