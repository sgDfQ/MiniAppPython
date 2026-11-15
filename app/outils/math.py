FACTORIELLE_MAX = 100
EST_PREMIER_MAX = 1_000_000_000_000


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


def est_premier(n: int) -> bool:
    """Indique si n est premier, par division jusqu'à la racine de n.

    0 et 1 ne sont pas premiers. La borne EST_PREMIER_MAX limite
    le temps de calcul (environ 500 000 divisions au maximum).
    """
    if n < 0:
        raise ValueError("Le nombre doit être positif ou nul.")
    if n > EST_PREMIER_MAX:
        raise ValueError(f"Le nombre doit être inférieur ou égal à {EST_PREMIER_MAX}.")
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2

    diviseur = 3
    while diviseur * diviseur <= n:
        if n % diviseur == 0:
            return False
        diviseur += 2
    return True


def pgcd(a: int, b: int) -> int:
    """Calcule le PGCD par l'algorithme d'Euclide.

    Les signes sont ignorés : pgcd(-12, 18) == 6.
    pgcd(0, 0) n'est pas défini et lève une erreur.
    """
    if a == 0 and b == 0:
        raise ValueError("Le PGCD de 0 et 0 n'est pas défini.")

    a, b = abs(a), abs(b)
    while b != 0:
        a, b = b, a % b
    return a