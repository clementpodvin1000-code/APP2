def avions_scoring(AVIONS_INITIAL):
    """
    Calcule le score d'un avion en fonction de ses caractéristiques.
    Le score est une combinaison linéaire de différents paramètres, pondérés par des coefficients en fonction de leur importance (policies).
    """
    copie = []
    for avion in AVIONS_INITIAL:
        scoring = 0
        if avion["medical"]:
            scoring += 5
        else:
            scoring += 1
        if avion["technical_issue"]:
            scoring += 5
        else:
            scoring += 1

        avion_copie = avion.copy()
        avion_copie["scoring"] = scoring
        copie.append(avion_copie)
    return copie
