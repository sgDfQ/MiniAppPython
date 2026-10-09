def palindrome(chaine):
    chaine = chaine.lower()
    i, longueur = 0, len(chaine)

    while i < longueur:
        if chaine[i] != chaine[-i - 1]:
            return False
        i += 1

    return True


if __name__ == "__main__":
    if palindrome(input()):
        print("Palindrome.")
    else:
        print("Pas palindrome.")