class WynikObliczen:
    def __init__(self, wynik=1.0, licznik=0):
        self.wynik = wynik
        self.licznik = licznik

def potega_iteracyjnie(a, n):
    wynik = WynikObliczen()
    for i in range(n):
        wynik.wynik *= a
        wynik.licznik += 1
    return wynik

def potega_rekurencyjnie(a, n):
    if n == 0:
        return WynikObliczen(1.0, 0)
    else:
        wynik = potega_rekurencyjnie(a, n - 1)
        wynik.wynik *= a
        wynik.licznik += 1
        return wynik

def potega_kwadratowa_iteracyjnie(a, n):
    wynik = WynikObliczen()
    while n > 0:
        if n % 2 == 1:
            wynik.wynik *= a
            wynik.licznik += 1
        a *= a
        wynik.licznik += 1
        n //= 2
    return wynik

def potega_kwadratowa_rekurencyjnie(a, n):
    if n == 0:
        return WynikObliczen(1.0, 0)
    elif n % 2 == 0:
        temp = potega_kwadratowa_rekurencyjnie(a * a, n // 2)
        return WynikObliczen(temp.wynik, temp.licznik + 1)
    else:
        temp = potega_kwadratowa_rekurencyjnie(a, n - 1)
        return WynikObliczen(temp.wynik * a, temp.licznik + 1)

def wyswietl_wyniki(a, n, wynik, metoda):
    print(f'{metoda}: a={a:4.1f} n={n:2} wynik={wynik.wynik:10.1f} licznik={wynik.licznik}')

def main():
    a = 2.0
    print('Porownanie metod obliczania potegi')
    print('----------------------------------')
    
    for n in range(16):
        print(f'\nDla n = {n}:')
        
        wynik = potega_iteracyjnie(a, n)
        wyswietl_wyniki(a, n, wynik, 'Metoda iteracyjna        ')
        
        wynik = potega_rekurencyjnie(a, n)
        wyswietl_wyniki(a, n, wynik, 'Metoda rekurencyjna      ')
        
        wynik = potega_kwadratowa_iteracyjnie(a, n)
        wyswietl_wyniki(a, n, wynik, 'Metoda kwadr. iter.      ')
        
        wynik = potega_kwadratowa_rekurencyjnie(a, n)
        wyswietl_wyniki(a, n, wynik, 'Metoda kwadr. rekur.     ')
    
    input('\nNacisnij Enter aby zakonczyc...')

if __name__ == "__main__":
    main()