from datetime import datetime

def wczytaj_liczbe(komunikat, min_wartosc, max_wartosc):
    while True:
        try:
            n = int(input(komunikat))
            if n < min_wartosc or n > max_wartosc:
                raise ValueError
            return n
        except ValueError:
            print(f'Proszę podać liczbę z zakresu [{min_wartosc}, {max_wartosc}]')

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

def wykonaj_pomiary_czasu(n, liczba_powtorzen):
    # Pomiar czasu dla metody iteracyjnej
    start_time = datetime.now()
    for _ in range(liczba_powtorzen):
        wartosc_silni = silnia_iteracyjna(n)
    end_time = datetime.now()
    czas_iteracyjny = (end_time - start_time).total_seconds()

    # Pomiar czasu dla metody rekurencyjnej
    start_time = datetime.now()
    for _ in range(liczba_powtorzen):
        wartosc_silni = silnia_rekurencyjna(n)
    end_time = datetime.now()
    czas_rekurencyjny = (end_time - start_time).total_seconds()

    # Wyświetl wyniki
    wyswietl_wyniki(n, liczba_powtorzen, wartosc_silni, czas_iteracyjny, czas_rekurencyjny)

def wyswietl_wyniki(n, liczba_powtorzen, wartosc_silni, czas_iteracyjny, czas_rekurencyjny):
    print()
    print('Wyniki pomiarów:')
    print('---------------')
    print(f'Argument funkcji silnia: {n}')
    print(f'Liczba powtórzeń: {liczba_powtorzen}')
    print(f'Wartość silni: {wartosc_silni}')
    print(f'Czas obliczeń (metoda iteracyjna): {czas_iteracyjny:.3f} sekund')
    print(f'Czas obliczeń (metoda rekurencyjna): {czas_rekurencyjny:.3f} sekund')
    print('---------------')
    
    if czas_rekurencyjny > czas_iteracyjny:
        print(f'Metoda rekurencyjna jest wolniejsza o {(czas_rekurencyjny / czas_iteracyjny):.2f} razy')
    else:
        print(f'Metoda iteracyjna jest wolniejsza o {(czas_iteracyjny / czas_rekurencyjny):.2f} razy')

def kontroler():
    max_dozwolony_argument = 20  # Dla Int64 - ustalono empirycznie
    
    # Wczytaj parametry
    n = wczytaj_liczbe(f'Podaj argument silni (0-{max_dozwolony_argument}): ', 0, max_dozwolony_argument)
    liczba_powtorzen = wczytaj_liczbe('Podaj liczbę powtórzeń (min. 1): ', 1, 2**63 - 1)
    
    # Wykonaj pomiary
    wykonaj_pomiary_czasu(n, liczba_powtorzen)

if __name__ == "__main__":
    kontroler()