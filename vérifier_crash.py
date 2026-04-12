def verifier_crash(AVIONS_INITIAL):
    crash = []
    for avion in AVIONS_INITIAL:
        if avion["fuel"] < 1:
            crash.append(avion["id"])
            print(f"CRASH: L'avion {avion['id']} s'est écrasé en raison d'un manque de carburant.")
    return crash