def palindrome(chaine):
    chaine = chaine.lower()
    i, longueur = 0, len(chaine)

    while i < longueur:
        if chaine[i] != chaine[-i - 1]:
            return False
        i += 1

    return True


VOYELLES = "aeiouyàâäéèêëîïôöùûüÿ"


def compter_voyelles(chaine):
    total = 0
    for caractere in chaine.lower():
        if caractere in VOYELLES:
            total += 1
    return total


def inverser(chaine):
    return chaine[::-1]


if __name__ == "__main__":
    if palindrome(input()):
        print("Palindrome.")
    else:
        print("Pas palindrome.")