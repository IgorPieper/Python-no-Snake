import math
from zmienne_globalne import dokladnosc, maks

liczby = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", ".", 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


def zabezpiecz(co):
    if str(co).lower() == "e":
        return round(2.71828, dokladnosc)
    elif str(co).lower() == "pi":
        return round(math.pi, dokladnosc)

    tablica_znakow = list(str(co))
    wynikowa_tablica = []
    kropka_wystapila = False

    for n in tablica_znakow:
        if str(n) in map(str, liczby):
            if n == '.':
                if kropka_wystapila:
                    continue
                else:
                    kropka_wystapila = True
            wynikowa_tablica.append(n)

    wynik = "".join(wynikowa_tablica)
    if wynik == "" or wynik == ".":
        wynik = "0"

    wynik = round(float(wynik), dokladnosc)

    if wynik > maks:
        wynik = maks

    if wynik.is_integer():  # jeżeli wynik jest liczbą całkowitą
        return int(wynik)  # konwertujemy go na typ int

    return wynik
