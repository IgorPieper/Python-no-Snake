szerokosc = 25
wysokosc = szerokosc/2
powietrze = int(szerokosc/2-1)

if szerokosc % 2 == 0:
    piramida = 2
else:
    piramida = 1

while powietrze >= 0:
    print(" " * powietrze, end='')
    print("#" * piramida)
    piramida = piramida + 2
    powietrze = powietrze - 1
