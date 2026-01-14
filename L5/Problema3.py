#Problema 3: Scrie o funcție inverted_index care primește o listă de șiruri de caractere
#(fiecare șir reprezentând un document) și returnează un dicționar. Dicționarul trebuie să
#asocieze fiecărui cuvânt unic un set de indici ai documentelor în care apare acel cuvânt.
#Ex:
#Input:
#documents = [
#"pisica a stat pe covor",
#"cainele a stat în ceață",
#"pisica și câinele s-au jucat împreună"
#]
#Output:
#{
#'pisica': {0, 2},
#'a': {0, 1},
#'stat': {0, 1},
#'pe': {0},
#'covor': {0},
#'cainele': {1, 2}, 'în': {1},
#'ceață': {1},
#'și': {2},
#'s-au': {2},
#'jucat': {2},
#'împreună': {2} }

import string

def inverted_index(documents):
    index = {}

    for i, doc in enumerate(documents):
        # normalizăm textul
        doc = doc.lower()

        # eliminăm semnele de punctuație
        for semn in string.punctuation:
            doc = doc.replace(semn, "")

        # separăm cuvintele
        cuvinte = doc.split()

        for cuvant in cuvinte:
            if cuvant not in index:
                index[cuvant] = set()
            index[cuvant].add(i)

    return index
documents = [
    "pisica a stat pe covor",
    "cainele a stat în ceață",
    "pisica și cainele s-au jucat împreună"
]

rezultat = inverted_index(documents)
print(rezultat)
