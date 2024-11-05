import math

def nicleKvEnacbe(a:int,b:int,c:int):
    """
        Vrne nicle kvadratne enacbe.
    """

    D = b**2 - 4*a*c
    if D < 0:
        raise ValueError("Determinata je negativna zato ima kvadratna enacba kompleksne resitve")
    
    return [(-b + math.sqrt(D))/2*a, (-b - math.sqrt(D))/2*a]
