FACTORIELLE_MAX = 100


def factorielle(n: int) -> int:
    """Calcule n! de façon itérative.

    Une boucle évite le RecursionError de la version récursive.
    La borne FACTORIELLE_MAX renvoie une erreur 400 claire au lieu
    de calculer des nombres gigantesques.
    """
    if n < 0:
        raise ValueError("Le nombre doit être positif ou nul.")
    if n > FACTORIELLE_MAX:
        raise ValueError(f"Le nombre doit être inférieur ou égal à {FACTORIELLE_MAX}.")

    resultat = 1
    for i in range(2, n + 1):
        resultat *= i
    return resultat