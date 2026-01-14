#Ex1: TemperatureConversion: Scrie un program care cere utilizatorului input
#grade Celsius si le converteste in grade farenheit.
#Farenheit = Celsius x 9/5 + 32

while True:
    raw = input("Temperatura în Celsius: ").strip()

    # Dacă utilizatorul apasă direct Enter
    if raw == "":
        print("Nu ai introdus nicio valoare. Te rog introdu o temperatură.")
        continue

    # Înlocuim virgula cu punct
    raw = raw.replace(",", ".")

    # Verificăm dacă este număr valid
    try:
        celsius = float(raw)
        break
    except ValueError:
        print("Valoare invalidă! Te rog introdu un număr (ex: 3.5 sau 3,5).")

fahrenheit = celsius * 9 / 5 + 32
print("Fahrenheit:", fahrenheit)