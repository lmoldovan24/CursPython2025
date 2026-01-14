#Scrie un program care citeste un nr n de la tastatura si afiseaza toate numerele impare pana la  n.
#ex: n = 10
#rezultat: 1, 3, 5, 7, 9

def citeste_numar():
    while True:
        try:
            n = input("Introdu un număr n: ")
            n = n.replace(",", ".")   # acceptă , și .
            n = float(n)
            return int(n)            # luăm doar partea întreagă
        except ValueError:
            print(" Introdu un număr valid (întreg sau zecimal).")

n = citeste_numar()

print("Numerele impare până la n sunt:")
for i in range(1, n + 1, 2):
    print(i, end=", ")

