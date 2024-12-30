def czytaj_liczbe():
    print('\nObliczanie sumy cyfr liczby calkowitej')
    liczba = int(input('Podaj liczbe: '))
    return liczba

def suma_cyfr(liczba):
    suma = 0
    liczba = abs(liczba)  # Użyj wartości bezwzględnej
    while liczba != 0:
        suma += liczba % 10
        liczba //= 10
    return suma

def pisz_sume(liczba, suma_cyfr):
    print(f'Suma cyfr liczby {liczba} wynosi {suma_cyfr}')

def suma_cyfr_liczby():
    liczba = czytaj_liczbe()
    suma = suma_cyfr(liczba)
    pisz_sume(liczba, suma)

if __name__ == "__main__":
    suma_cyfr_liczby()