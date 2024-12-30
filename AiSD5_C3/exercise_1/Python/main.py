def wczytaj_liczbe():
    while True:
        try:
            n = int(input('Podaj nieujemną liczbę do obliczenia silni: '))
            if n < 0:
                raise ValueError
            return n
        except ValueError:
            print('Proszę podać prawidłową liczbę nieujemną!')

def silnia_rekurencyjna(n):
    if n == 0:
        return 1
    else:
        return n * silnia_rekurencyjna(n - 1)

def silnia_iteracyjna(n):
    wynik = 1
    for i in range(1, n + 1):
        wynik *= i
    return wynik

def wyswietl_wyniki(iteracyjna, rekurencyjna):
    print(f'Silnia iteracyjnie:   {iteracyjna}')
    print(f'Silnia rekurencyjnie: {rekurencyjna}')

def kontroler():
    n = wczytaj_liczbe()
    wynik_iteracyjny = silnia_iteracyjna(n)
    wynik_rekurencyjny = silnia_rekurencyjna(n)
    wyswietl_wyniki(wynik_iteracyjny, wynik_rekurencyjny)

if __name__ == "__main__":
    kontroler()