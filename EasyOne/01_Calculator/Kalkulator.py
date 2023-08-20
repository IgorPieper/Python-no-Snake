import math


def liczba():
    while True:
        print("Proszę podać liczbę: ", end="")
        wynik = input()
        if wynik == "pi" or wynik == "PI" or wynik == "Pi" or wynik == "pI":
            wynik = math.pi
            break
        elif wynik == "e" or wynik == "E":
            wynik = math.e
            break
        else:
            try:
                wynik = int(wynik)
                break
            except ValueError:
                print("Zła wartość zmiennej. Spróbuj jeszcze raz wpisać liczbę")
    return wynik


def trygonometria():
    print("+-------------------------------+")
    print("| 1.Sinus                       |")
    print("| 2.Cosinus                     |")
    print("| 3.Tangens                     |")
    print("| 4.Cotangens                   |")
    print("| 5.Arcus Sinus                 |")
    print("| 6.Arcus Cosinus               |")
    print("| 7.Arcus Tangens               |")
    print("| 8.Arcus Cotangens             |")
    print("| 9.Wróć                        |")
    print("+-------------------------------+")

    print("Twój wybór: ", end="")
    try:
        wybor2 = int(input())
    except ValueError:
        print("Niewłaściwa wartość")
        wybor2 = 10
    if 1 <= wybor2 <= 8:
        liczba1 = liczba()
        match wybor2:
            case 1:
                print(math.sin(liczba1))
            case 2:
                print(math.cos(liczba1))
            case 3:
                print(math.tan(liczba1))
            case 4:
                try:
                    print(1/math.tan(liczba1))
                except ZeroDivisionError:
                    print("Nie istnieje")
            case 5:
                try:
                    print(math.asin(liczba1))
                except ValueError:
                    print("Wartość musi się znajdować w przedziale od -1 do 1")
            case 6:
                try:
                    print(math.acos(liczba1))
                except ValueError:
                    print("Wartość musi się znajdować w przedziale od -1 do 1")
            case 7:
                 print(math.atan(liczba1))
            case 8:
                try:
                    print(1 / math.tan(liczba1))
                except ZeroDivisionError:
                    print("Nie istnieje")


while True:
    print("+-------------------------------+")
    print("| 1.Dodawanie                   |")
    print("| 2.Odejmowanie                 |")
    print("| 3.Mnożenie                    |")
    print("| 4.Dzielenie                   |")
    print("| 5.Potęgowanie                 |")
    print("| 6.Pierwiastkowanie            |")
    print("| 7.Funkcje Trygonometryczne    |")
    print("| 8.Logarytm                    |")
    print("| 9.Koniec                      |")
    print("+-------------------------------+")

    print("Twój wybór: ", end="")
    wybor = input()

    match wybor:
        case "1":
            liczba1 = liczba()
            liczba2 = liczba()
            print(liczba1+liczba2)
        case "2":
            liczba1 = liczba()
            liczba2 = liczba()
            print(liczba1 + liczba2)
        case "3":
            liczba1 = liczba()
            liczba2 = liczba()
            print(liczba1 * liczba2)
        case "4":
            liczba1 = liczba()
            liczba2 = liczba()
            try:
                print(liczba1 / liczba2)
            except ZeroDivisionError:
                print("Nie dzielimy przez zero")
        case "5":
            liczba1 = liczba()
            while True:
                print("Proszę podać potęgę: ", end="")
                liczba2 = input()
                if liczba2 == "pi" or liczba2 == "PI" or liczba2 == "Pi" or liczba2 == "pI":
                    liczba2 = math.pi
                    break
                elif liczba2 == "e" or liczba2 == "E":
                    liczba2 = math.e
                    break
                else:
                    try:
                        liczba2 = int(liczba2)
                        break
                    except ValueError:
                        print("Zła wartość zmiennej. Spróbuj jeszcze raz wpisać liczbę")
            print(math.pow(liczba1, liczba2))
        case "6":
            while True:
                liczba1 = liczba()
                if liczba1 >= 0:
                    break
                else:
                    print("Liczba pod pierwiastkiem musi być dodatnia")
            while True:
                print("Proszę podać pierwiastek: ", end="")
                liczba2 = input()
                if liczba2 == "pi" or liczba2 == "PI" or liczba2 == "Pi" or liczba2 == "pI":
                    liczba2 = math.pi
                    break
                elif liczba2 == "e" or liczba2 == "E":
                    liczba2 = math.e
                    break
                else:
                    try:
                        liczba2 = int(liczba2)
                        if liczba2 <= 0:
                            print("Wielkość pierwiastka musi być większa od zera")
                        else:
                            break
                    except ValueError:
                        print("Zła wartość zmiennej. Spróbuj jeszcze raz wpisać liczbę")
            print(math.pow(liczba1, 1/liczba2))
        case "7":
            trygonometria()
        case "8":
            liczba1 = liczba()
            while True:
                print("Proszę podać wykładnik: ", end="")
                liczba2 = input()
                if liczba2 == "pi" or liczba2 == "PI" or liczba2 == "Pi" or liczba2 == "pI":
                    liczba2 = math.pi
                    break
                elif liczba2 == "e" or liczba2 == "E":
                    liczba2 = math.e
                    break
                else:
                    try:
                        liczba2 = int(liczba2)
                        if liczba2 > 0:
                            break
                        else:
                            print("Wykładnik musi być większy od 0")
                    except ValueError:
                        print("Zła wartość zmiennej. Spróbuj jeszcze raz wpisać liczbę")
            print(math.log(liczba1, liczba2))
        case "9":
            break
    stop = input()
