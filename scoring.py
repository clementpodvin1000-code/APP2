from APP2_projet_complet.data import AVIONS_INITIAL


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

        if avion["diplomatic_level"] >= 4:
            scoring += 5
        elif avion["diplomatic_level"] >= 2:
            scoring += 3    
        else:
            scoring += 1

        if avion["fuel"] < 10:
            scoring += 5
        elif avion["fuel"] < 20:
            scoring += 3
        else:            
            scoring += 1

        avion_copie = avion.copy()
        avion_copie["scoring"] = scoring
        copie.append(avion_copie)
    return copie
print(avions_scoring(AVIONS_INITIAL))

