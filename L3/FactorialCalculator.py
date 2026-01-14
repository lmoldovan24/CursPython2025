#FactorialCalculator.py: Scrie o functie factorial(n) care calculeaza factorialul unui numar
#n. Folositi aceasta functie intr-un program care cere de la tastatura un numar intreg si
#returneaza factorialul acestuia.

def factorial(n):
    rezultat = 1
    for i in range(1, n + 1):
        rezultat *= i
    return rezultat


# Program principal
while True:
    try:
        n = int(input("Introdu un număr întreg: "))
        if n < 0:
            print("Factorialul este definit doar pentru numere ≥ 0.")
        else:
            break
    except ValueError:
        print("Introdu un număr întreg valid.")

print(f"Factorialul lui {n} este: {factorial(n)}")
