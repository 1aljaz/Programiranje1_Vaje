def samo_enkrat(s):
    """Vrne True, ce se vsak znak pojavi samo enkrat, drugace False."""
    crke = set()
    for c in s:
        if c in crke:
            return False
        crke.add(c)
    return True

