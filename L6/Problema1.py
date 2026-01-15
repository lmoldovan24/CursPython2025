#Problema 1: Scrie o funcție reverse_words care primește o propoziție (un șir de caractere) și
#returnează o propoziție nouă în care ordinea cuvintelor este inversată, dar ordinea literelor în
#fiecare cuvânt rămâne aceeași. Elimină spațiile suplimentare din propoziție dacă există. Ex:
#sentence = "soricel un cu joaca se pisica", OUTPUT: “pisica se joaca cu un soricel”

def reverse_words(sentence: str) -> str:
    # Elimină spațiile suplimentare și separă cuvintele
    words = sentence.split()

    # Inversează ordinea cuvintelor
    reversed_words = words[::-1]

    # Reconstruiește propoziția
    return " ".join(reversed_words)
def reverse_words(sentence: str) -> str:
    return " ".join(sentence.split()[::-1])


# Teste
print(reverse_words("soricel un cu joaca se pisica"))   # pisica se joaca cu un soricel
print(reverse_words("   hello   world   "))             # world hello
print(reverse_words("un_cuvant"))                        # un_cuvant
