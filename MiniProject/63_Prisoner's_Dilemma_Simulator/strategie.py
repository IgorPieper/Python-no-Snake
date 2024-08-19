def strategiaPawel(historia):
    if not historia:
        return 1
    if len(historia) >= 2 and historia[-1][1] == 1 and historia[-2][1] == 1:
        return 1
    if historia[-1][1] == 1:
        return 0
    if len(historia) >= 2 and historia[-1][1] == 0 and historia[-2][1] == 0:
        return 1
    return 1

def strategiaAsia(historia):
    if not historia:
        return 0
    if len(historia) >= 4 and all(runda[1] == 1 for runda in historia[-4:]):
        return 1
    return 0

def strategiaKarolina(historia):
    return 0

def strategiaMagda(historia):
    return 0

def strategiaAlbert(historia):
    if len(historia) % 4 == 3:
        return 1
    return 0

def strategiaAdam(historia):
    if not historia:
        return 0
    return historia[-1][1]

def strategiaOlaf(historia):
    return 1

def strategiaMichal(historia):
    if not historia:
        return 0
    if historia[-1][1] == 1:
        return 1
    return 0

def strategiaKuba(historia):
    if len(historia) % 3 == 2 and (len(historia) + 1) % 2 == 0:
        return 1
    return 0

def strategiaMateusz(historia):
    if not historia:
        return 0
    if len(historia) % 2 == 1:
        return 1
    return 0

def strategiaKajetan(historia):
    if not historia:
        return 0
    if len(historia) == 1:
        return 0
    if len(historia) == 2:
        return 1
    if historia[-1][1] == 0:
        return 0
    return 1

def strategiaEliasz(historia):

    if not historia:
        return 0.7
    if any(runda[1] == 1 for runda in historia):
        return 1
    return 0.7

wszystkie_strategie = [
    strategiaPawel,
    strategiaAsia,
    strategiaKarolina,
    strategiaMagda,
    strategiaAlbert,
    strategiaAdam,
    strategiaMichal,
    strategiaKuba,
    strategiaMateusz,
    strategiaKajetan,
    strategiaOlaf,
    strategiaEliasz,
]