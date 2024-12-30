import math

def czytaj_dane():
    print('Czytaj: a, b, c')
    a = float(input('a: '))
    b = float(input('b: '))
    c = float(input('c: '))
    return a, b, c

def oblicz_rownanie_delta(a, b, c):
    delta = b * b - 4 * a * c
    if delta > 0:
        x1 = (-b - math.sqrt(delta)) / (2 * a)
        x2 = (-b + math.sqrt(delta)) / (2 * a)
        return True, x1, x2
    elif delta == 0:
        x1 = -b / (2 * a)
        return True, x1, None
    else:
        return False, None, None

def pisz_wyniki(x1, x2, czy_pisac):
    print('Wyniki obliczen')
    if czy_pisac & (x2 != None):
        print(f'Dwa pierwiastki: x1 = {x1:.2f}, x2 = {x2:.2f}')
    elif czy_pisac & (x2 == None):
        print(f'Jeden pierwiastek: x = {x1:.2f}')
    else:
        print('Brak rozwiazan.')

def rownanie():
    a, b, c = czytaj_dane()
    if a == 0:
        if b != 0:
            x = -c / b
            print(f'To jest rownanie liniowe, x = {x:.2f}')
        else:
            print('To nie jest rownanie.')
    else:
        czy_jest_rozwiazanie, x1, x2 = oblicz_rownanie_delta(a, b, c)
        pisz_wyniki(x1, x2, czy_jest_rozwiazanie)

if __name__ == "__main__":
    print('Rozwiazanie rownania kwadratowego')
    rownanie()