#Problema 1: Importarea modulelor și utilizarea acestora
#Descriere:
#Creează un script Python care folosește modulul math pentru a calcula:
#1. Rădăcina pătrată a unui număr dat.
#2. Factorialul unui număr întreg.
#3. Valoarea sinusului unui unghi dat în grade.
#Input: num = 25 angle = 30
#Output:
#Rădăcina pătrată a 25 este 5.0
#Factorialul lui 25 este 15511210043330985984000000
#Sinusul unghiului de 30 grade este 0.5
import math

try:
    # Citire date de la tastatură
    num = int(input("Introdu un număr întreg: "))
    angle = float(input("Introdu un unghi în grade: "))

    if num < 0:
        raise ValueError("Numărul trebuie să fie pozitiv")

    # Rădăcina pătrată
    radacina = math.sqrt(num)
    print(f"Rădăcina pătrată a {num} este {radacina}")

    # Factorial
    factorial = math.factorial(num)
    print(f"Factorialul lui {num} este {factorial}")

    # Sinus (grade → radiani)
    radiani = math.radians(angle)
    sinus = math.sin(radiani)
    print(f"Sinusul unghiului de {angle} grade este {sinus}")

except ValueError as ve:
    print("Eroare:", ve)

except Exception as e:
    print("Eroare neașteptată:", e)

