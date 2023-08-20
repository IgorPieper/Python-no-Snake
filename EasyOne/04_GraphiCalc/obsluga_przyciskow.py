from zabezpieczenia import zabezpiecz
from zmienne_globalne import dokladnosc, nieokreslone, dlugie
import math


def przyciski(licz1, licz2, licz3, jaki):
    liczba1 = zabezpiecz(licz1.get())
    liczba2 = zabezpiecz(licz2.get())

    if jaki == 1:

        wynik = liczba1 + liczba2

    elif jaki == 2:

        wynik = liczba1 - liczba2

    elif jaki == 3:

        wynik = liczba1 * liczba2

    elif jaki == 4:

        try:
            wynik = liczba1 / liczba2
        except:
            wynik = nieokreslone

    elif jaki == 5:

        wynik = math.pow(liczba1, liczba2)

    elif jaki == 6:

        try:
            wynik = math.pow(liczba1, 1/liczba2)
        except:
            wynik = nieokreslone

    elif jaki == 6:

        wynik = math.pow(liczba1, 1/liczba2)

    elif jaki == 7:

        wynik = (liczba1 / 100) * liczba2

    elif jaki == 8:

        if liczba1 <= 100:
            try:
                wynik = math.factorial(liczba1)
            except:
                wynik = nieokreslone
        else:
            wynik = dlugie

    elif jaki == 9:

        try:
            wynik = math.log(liczba1, liczba2)
        except:
            wynik = nieokreslone

    elif jaki == 10:

        try:
            wynik = liczba1 % liczba2
        except:
            wynik = nieokreslone
    elif jaki == 11:

        try:
            radians = math.radians(liczba1)

            wynik = math.sin(radians)
        except:
            wynik = nieokreslone
    elif jaki == 12:

        try:
            radians = math.radians(liczba1)

            wynik = math.cos(radians)
        except:
            wynik = nieokreslone
    elif jaki == 13:

        try:
            radians = math.radians(liczba1)

            wynik = math.tan(radians)
        except:
            wynik = nieokreslone

    else:
        wynik = 0

    try:
        licz3.set(round(wynik, dokladnosc))
        licz1.set(round(wynik, dokladnosc))
    except TypeError:
        licz3.set(wynik)
        licz1.set("")
    finally:
        licz2.set("")
    return 0


def usun_wynik(licz3):
    licz3.set("")

