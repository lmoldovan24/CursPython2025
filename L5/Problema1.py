#Problema 1: Scrie o funcție word_frequency care primește un șir de caractere și returnează un dicționar ce conține frecvența fiecărui cuvânt din text. Ignoră majusculele
#și semnele de punctuație.
#Ex: Input
#text = "Ana si Maria au plecat la mare. Maria are rau de mare."
#Output
#{'ana': 1, 'si': 1, 'maria': 2, 'au': 1, 'plecat': 1, 'la': 1, 'mare': 2, 'are': 1, 'rau': 1, 'de': 1}

import string


def word_frequency(text):
    # transformăm textul în litere mici
    text = text.lower()

    # eliminăm semnele de punctuație
    for semn in string.punctuation:
        text = text.replace(semn, "")

    # separăm cuvintele
    cuvinte = text.split()

    # construim dicționarul de frecvență
    frecventa = {}
    for cuvant in cuvinte:
        if cuvant in frecventa:
            frecventa[cuvant] += 1
        else:
            frecventa[cuvant] = 1

    return frecventa

text = input("Interodu textul: ")
frecventa = word_frequency(text)
rezultat = word_frequency(text)
print(rezultat)
