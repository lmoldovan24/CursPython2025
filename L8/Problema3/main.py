from geometry.circle import aria_cercului, circumferinta_cercului
from geometry.rectangle import aria_dreptunghiului, perimetru_dreptunghiului

try:
    r = float(input("Introdu raza cercului: "))
    l = float(input("Introdu lungimea dreptunghiului: "))
    L = float(input("Introdu lățimea dreptunghiului: "))

    print("Aria cercului:", aria_cercului(r))
    print("Circumferința cercului:", circumferinta_cercului(r))

    print("Aria dreptunghiului:", aria_dreptunghiului(l, L))
    print("Perimetrul dreptunghiului:", perimetru_dreptunghiului(l, L))

except ValueError as ve:
    print("Eroare:", ve)

except Exception as e:
    print("Eroare neașteptată:", e)
