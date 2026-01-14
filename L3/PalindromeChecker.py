#PalindromeChecker.py: Scrie o functie is_palindrome(word) ce verifica daca un cuvant
#dat este palindrom (se citeste la fel si de la stanga la dreapta, dar si de la dreapta la stanga).
#Functia trebuie sa returneze True cand cuvantul dat este palindrom si False cand nu este
#palindrom. Folositi functia definita intr-un program ce preia de la tastatura un cuvant dat si il
#verifica.

def is_palindrome(word):
    # eliminăm spațiile și transformăm în litere mici
    word = word.replace(" ", "").lower()

    # verificăm dacă este egal cu inversul său
    return word == word[::-1]


# Program principal
cuvant = input("Introdu un cuvânt: ")

if is_palindrome(cuvant):
    print("Cuvântul este palindrom.")
else:
    print("Cuvântul NU este palindrom.")
