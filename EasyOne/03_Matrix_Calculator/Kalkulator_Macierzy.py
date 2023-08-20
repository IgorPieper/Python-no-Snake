def wielkosc(nazwa):
    try:
        liczba = int(input(f"Proszę podać {nazwa} macierza: "))
    except ValueError:
        liczba = 1

    if liczba <= 0:
        liczba = 1
    return liczba


def pusta_macierz(szerokosc, wysokosc):
    macierz = []
    helper = []

    for n in range(0, wysokosc):
        for m in range(0, szerokosc):
            helper.append("")
        macierz.append(helper)
        helper = []

    return macierz


def stworz_macierz():
    szerokosc = wielkosc("szerokość")
    wysokosc = wielkosc("wysokość")

    macierz = pusta_macierz(szerokosc, wysokosc)

    for n in range(0, wysokosc):
        for m in range(0, szerokosc):
            try:
                helperr = float(input("Proszę podać wartość: "))
                if helperr - int(helperr) == 0:
                    macierz[n][m] = int(helperr)
                else:
                    macierz[n][m] = helperr
            except ValueError:
                macierz[n][m] = 0
            pokaz_macierz(macierz)

    return macierz, wysokosc, szerokosc


def pokaz_macierz(macierz):
    for n in macierz:
        print(n)


input("Witamy w kalkulatorze macierzy")
input("Właśnie tworzysz pierwszą macierz ")
macierz1, wysokosc1, szerokosc1 = stworz_macierz()
input("Właśnie tworzysz drugą macierz ")
macierz2, wysokosc2, szerokosc2 = stworz_macierz()

while True:

    print("+-----------------------------------------+")
    print("|1. Zobacz pierwszą macierz               |")
    print("|2. Zobacz drugą macierz                  |")
    print("|3. Zaaktualizuj pierwszą macierz         |")
    print("|4. Zaaktualizuj drugą macierz            |")
    print("|5. Dodaj macierze                        |")
    print("|6. Odejmij macierze (pierwszy - drugi)   |")
    print("|7. Odejmij macierze (drugi - pierwszy)   |")
    print("|8. Pomnóż macierz przez liczbę           |")
    print("|9. Wyłącz program                        |")
    print("+-----------------------------------------+")
    try:
        wybor = int(input("Twój wybór: "))
    except ValueError:
        wybor = 0

    if wybor == 1:
        pokaz_macierz(macierz1)
        input()
    elif wybor == 2:
        pokaz_macierz(macierz2)
        input()
    elif wybor == 3:
        macierz1, wysokosc1, szerokosc1 = stworz_macierz()
    elif wybor == 4:
        macierz2, wysokosc2, szerokosc2 = stworz_macierz()
    elif wybor == 5:
        if szerokosc1 == szerokosc2 and wysokosc1 == wysokosc2:
            macierz3 = pusta_macierz(szerokosc1, wysokosc1)
            for n in range(0, wysokosc1):
                for m in range(0, szerokosc1):
                    macierz3[n][m] = macierz1[n][m] + macierz2[n][m]
            pokaz_macierz(macierz3)
            macierz3 = []
        else:
            print("Macierze można do siebie dodać tylko gdy mają identyczną szerokość i wysokość")
        input()
    elif wybor == 6:
        if szerokosc1 == szerokosc2 and wysokosc1 == wysokosc2:
            macierz3 = pusta_macierz(szerokosc1, wysokosc1)
            for n in range(0, wysokosc1):
                for m in range(0, szerokosc1):
                    macierz3[n][m] = macierz1[n][m] - macierz2[n][m]
            pokaz_macierz(macierz3)
            macierz3 = []
        else:
            print("Macierze można od siebie odjąć tylko gdy mają identyczną szerokość i wysokość")
        input()
    elif wybor == 7:
        if szerokosc1 == szerokosc2 and wysokosc1 == wysokosc2:
            macierz3 = pusta_macierz(szerokosc1, wysokosc1)
            for n in range(0, wysokosc1):
                for m in range(0, szerokosc1):
                    macierz3[n][m] = macierz2[n][m] - macierz1[n][m]
            pokaz_macierz(macierz3)
            macierz3 = []
        else:
            print("Macierze można od siebie odjąć tylko gdy mają identyczną szerokość i wysokość")
        input()
    elif wybor == 8:
        try:
            ktory_macierz = int(input("Którą macierz chcesz pomnożyć?: "))
        except ValueError:
            ktory_macierz = 1
        try:
            mnoznik = int(input("O ile chcesz pomnożyć?: "))
        except ValueError:
            mnoznik = 1

        macierz3 = pusta_macierz(szerokosc1, wysokosc1)

        for n in range(0, wysokosc1):
            for m in range(0, szerokosc1):
                if ktory_macierz == 1:
                    macierz3[n][m] = macierz1[n][m] * mnoznik
                else:
                    macierz3[n][m] = macierz2[n][m] * mnoznik

        pokaz_macierz(macierz3)
        macierz3 = []
        input()
    elif wybor == 9:
        break
