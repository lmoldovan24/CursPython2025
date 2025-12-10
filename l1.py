#Ex1: TemperatureConversion: Scrie un program care cere utilizatorului input
#grade Celsius si le converteste in grade farenheit.
#Farenheit = Celsius x 9/5 + 32

celsius = float(input("Temperatura in Celsius: "))
fahrenheit = celsius * 9 / 5 + 32
print("Fahrenheit: ", fahrenheit)

#Ex2: OddOrEven: Creeaza un program care cere userului un numar intreg si afiseaza
#daca acest numar este par sau impar. (hint, '%' returneaza restul impartirii)

numar = int(input("Introdu un numar: "))
if numar % 2 == 0:
    print("Numar par")
else:
    print("Numar impar")

#Ex3: 3. InterestCalculator: Scrie un program ce calculeaza dobanda. Programul va
# cere utilizatorului principalul, rata anuala a dobanzii (ex 5, 6, 10) si timpul in ani.
# Formula: Interest = (Principal x Rate x Time)/100

principal = int(input("Suma: "))
rate = int(input("Rata (5/6/10): "))
while rate not in (5, 6, 10):
    rate = int(input("Rata trebuie sa fie 5/6/10: "))

time = int(input("Timpul(in ani): "))
interest = (principal * rate * time)/100
print("Dobanda: ", interest)

#Ex4: Un program care verifică dacă un numar introdus de utilizator e prim sau nu.

nnumar = int(input("Introdu un numar: "))

if numar <= 1:
    print("Numarul NU este prim.")
else:
    este_prim = True

    for i in range(2, numar):
        if numar % i == 0:
            este_prim = False
            break

    if este_prim:
        print("Numarul ESTE prim.")
    else:
        print("Numarul NU este prim.")

