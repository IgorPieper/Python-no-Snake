from strategie import wszystkie_strategie

def dylemat_wieznia(gracz1_odpowiedz, gracz2_odpowiedz):
    pkt_gracz_1 = 0
    pkt_gracz_2 = 0

    if gracz1_odpowiedz == 1 and gracz2_odpowiedz == 1:
        pkt_gracz_1 = 0
        pkt_gracz_2 = 0
    elif gracz1_odpowiedz == 1 and gracz2_odpowiedz == 0:
        pkt_gracz_1 = 30
        pkt_gracz_2 = 0
    elif gracz1_odpowiedz == 0 and gracz2_odpowiedz == 1:
        pkt_gracz_1 = 0
        pkt_gracz_2 = 30
    elif gracz1_odpowiedz == 0 and gracz2_odpowiedz == 0:
        pkt_gracz_1 = 10
        pkt_gracz_2 = 10
    elif gracz1_odpowiedz == 0.7 and gracz2_odpowiedz == 0:
        pkt_gracz_1 = 20
        pkt_gracz_2 = 10
    elif gracz1_odpowiedz == 0 and gracz2_odpowiedz == 0.7:
        pkt_gracz_1 = 10
        pkt_gracz_2 = 20
    elif gracz1_odpowiedz == 0.7 and gracz2_odpowiedz == 1:
        pkt_gracz_1 = 0
        pkt_gracz_2 = 0
    elif gracz1_odpowiedz == 1 and gracz2_odpowiedz == 0.7:
        pkt_gracz_1 = 0
        pkt_gracz_2 = 0

    return pkt_gracz_1, pkt_gracz_2

def graj(liczba_gier, strategia_gracz_1, strategia_gracz_2):
    suma_pkt_gracz_1 = 0
    suma_pkt_gracz_2 = 0
    historia = []

    for _ in range(liczba_gier):
        odp_gracz_1 = strategia_gracz_1(historia)
        odp_gracz_2 = strategia_gracz_2(historia)
        wynik = dylemat_wieznia(odp_gracz_1, odp_gracz_2)
        suma_pkt_gracz_1 += wynik[0]
        suma_pkt_gracz_2 += wynik[1]
        historia.append((odp_gracz_1, odp_gracz_2))

    return suma_pkt_gracz_1, suma_pkt_gracz_2, historia

def zapisz_historie(historia, plik, strategia1, strategia2):
    with open(plik, 'a') as f:
        f.write(f"Historia gry: {strategia1} vs {strategia2}\n")
        for runda in historia:
            f.write(f"{runda}, ")
        f.write("\n\n")

def zapisz_wyniki(wyniki, plik):
    with open(plik, 'w') as f:
        f.write("Wyniki rozgrywek:\n")
        f.write("=" * 20 + "\n")
        for para, wynik in wyniki.items():
            f.write(f"Strategia 1: {para[0]}\n")
            f.write(f"Strategia 2: {para[1]}\n")
            f.write(f"Wynik Gracz 1: {wynik[0]} pkt\n")
            f.write(f"Wynik Gracz 2: {wynik[1]} pkt\n")
            f.write("-" * 20 + "\n")

def zapisz_podium(wyniki, plik):
    sumy_punktow = {}
    for (strategia1, strategia2), (pkt1, pkt2) in wyniki.items():
        if strategia1 not in sumy_punktow:
            sumy_punktow[strategia1] = 0
        if strategia2 not in sumy_punktow:
            sumy_punktow[strategia2] = 0
        sumy_punktow[strategia1] += pkt1
        sumy_punktow[strategia2] += pkt2

    sorted_sumy_punktow = sorted(sumy_punktow.items(), key=lambda x: x[1], reverse=True)

    with open(plik, 'w') as f:
        f.write("Podium:\n")
        f.write("=" * 20 + "\n")
        for strategia, suma in sorted_sumy_punktow:
            f.write(f"{strategia}: {suma} pkt\n")

def rozegraj_turniej():
    liczba_gier = 30
    wyniki = {}

    open('historia.txt', 'w').close()
    open('wyniki.txt', 'w').close()
    open('podium.txt', 'w').close()

    for i, strategia1 in enumerate(wszystkie_strategie):
        for j, strategia2 in enumerate(wszystkie_strategie):
            if i != j:  # Każda strategia gra z każdą inną strategią dokładnie raz
                nazwa_strategii1 = strategia1.__name__
                nazwa_strategii2 = strategia2.__name__
                wynik_gracz_1, wynik_gracz_2, historia = graj(liczba_gier, strategia1, strategia2)
                wyniki[(nazwa_strategii1, nazwa_strategii2)] = (wynik_gracz_1, wynik_gracz_2)
                zapisz_historie(historia, 'historia.txt', nazwa_strategii1, nazwa_strategii2)
                print(f"{nazwa_strategii1} vs {nazwa_strategii2} -> Gracz 1: {wynik_gracz_1} pkt, Gracz 2: {wynik_gracz_2} pkt")

    zapisz_wyniki(wyniki, 'wyniki.txt')
    zapisz_podium(wyniki, 'podium.txt')

if __name__ == "__main__":
    rozegraj_turniej()
