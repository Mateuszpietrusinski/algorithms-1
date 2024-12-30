import sys
from time import time

def wczytaj_liczbe():
    while True:
        try:
            n = int(input('Podaj nieujemną liczbę do obliczenia silni: '))
            if n < 0:
                raise ValueError
            if n > 998:
                print('Uwaga: Wartości powyżej 998 mogą przekroczyć limit rekurencji!')
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
        if i % 100 == 0:  # pokazuj postęp co 100 iteracji
            print(f'Postęp: obliczono {i}!')
    return wynik

def wyswietl_wyniki(n, iteracyjna, rekurencyjna=None):
    print(f'\nWyniki dla n = {n}:')
    print(f'Liczba cyfr w wyniku: {len(str(iteracyjna))}')
    
    if n <= 20:  # dla małych liczb pokazuj pełny wynik
        print(f'Silnia iteracyjnie:   {iteracyjna}')
        if rekurencyjna:
            print(f'Silnia rekurencyjnie: {rekurencyjna}')
    else:  # dla dużych liczb pokazuj tylko pierwsze i ostatnie cyfry
        start = str(iteracyjna)[:10]
        end = str(iteracyjna)[-10:]
        print(f'Pierwsze 10 cyfr wyniku: {start}...')
        print(f'Ostatnie 10 cyfr wyniku: ...{end}')

def kontroler():
    n = wczytaj_liczbe()
    
    print("\nRozpoczynam obliczenia...")
    start_time = time()
    
    wynik_iteracyjny = silnia_iteracyjna(n)
    
    if n <= 998:  # tylko dla wartości nieprzekraczających limitu rekurencji
        try:
            wynik_rekurencyjny = silnia_rekurencyjna(n)
            wyswietl_wyniki(n, wynik_iteracyjny, wynik_rekurencyjny)
        except RecursionError:
            print("Przekroczono limit rekurencji dla metody rekurencyjnej!")
            wyswietl_wyniki(n, wynik_iteracyjny)
    else:
        wyswietl_wyniki(n, wynik_iteracyjny)
    
    end_time = time()
    print(f'\nCzas wykonania: {end_time - start_time:.2f} sekund')

if __name__ == "__main__":
    print("Program do obliczania silni w Pythonie")
    print("Uwaga: Python obsługuje dowolnie duże liczby całkowite")
    kontroler()