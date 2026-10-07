def factorielle(n: int) -> int:
    if n < 0:
        raise ValueError("Le nombre doit être positif ou nul.")
    if n <= 1:
        return 1
    return n * factorielle(n - 1)
