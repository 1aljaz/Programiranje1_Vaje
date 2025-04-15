def pokaziCrke(beseda, crke):
    """Vrne niz, ki je sestavljen iz crk ki v mn. crke. Ce kaksne crke ni je tam '.'. """
    return "".join(crka if crka in crke else '.' for crka in beseda)
