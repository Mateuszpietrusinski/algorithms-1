def f(x):
    """
    # Funkcja obliczająca wartość wielomianu x^3 - x^2 - x + 2
    """
    return x**3 - x**2 - x + 2

def check_interval(a, b):
    """
    # Sprawdzanie, czy w podanym przedziale [a,b] jest miejsce zerowe
    # (czy wartości funkcji na krańcach przedziału mają przeciwne znaki)
    """
    return f(a) * f(b) < 0

def bisection_recursive(a, b, precision, iteration_count=0):
    """
    # Rekurencyjna implementacja metody bisekcji
    # a, b - granice przedziału
    # precision - zadana dokładność
    # iteration_count - licznik iteracji
    """
    # Obliczamy środek przedziału
    c = (a + b) / 2
    iteration_count += 1
    
    # Sprawdzamy warunek zakończenia (czy przedział jest wystarczająco mały)
    if abs(b - a) < precision:
        return c, iteration_count
    
    # Sprawdzamy, w której połowie jest miejsce zerowe i rekurencyjnie kontynuujemy
    if f(c) * f(a) < 0:
        return bisection_recursive(a, c, precision, iteration_count)
    else:
        return bisection_recursive(c, b, precision, iteration_count)

def main():
    """
    # Główna funkcja programu obsługująca wprowadzanie danych i wyświetlanie wyników
    """
    while True:
        try:
            # Pobieranie danych od użytkownika
            print("\nProgram do znajdowania miejsca zerowego metodą bisekcji")
            print("Funkcja: f(x) = x^3 - x^2 - x + 2")
            a = float(input("\nPodaj początek przedziału (a): "))
            b = float(input("Podaj koniec przedziału (b): "))
            
            # Sprawdzanie poprawności przedziału
            if not check_interval(a, b):
                print("\nUWAGA: W podanym przedziale nie ma miejsca zerowego!")
                print("Wartości funkcji na krańcach przedziału:")
                print(f"f({a}) = {f(a):.6f}")
                print(f"f({b}) = {f(b):.6f}")
                print("\nPrószę podać inny przedział.")
                continue
                
            precision = float(input("Podaj dokładność (np. 0.0001): "))
            if precision <= 0:
                print("\nDokładność musi być większa od 0!")
                continue
                
            # Obliczanie miejsca zerowego
            result, iterations = bisection_recursive(a, b, precision)
            
            # Wyświetlanie wyników
            print("\nWYNIKI:")
            print(f"Znalezione miejsce zerowe: {result:.6f}")
            print(f"Wartość funkcji w znalezionym punkcie: {f(result):.6f}")
            print(f"Liczba wykonanych iteracji: {iterations}")
            
            # Pytanie o kontynuację
            if input("\nCzy chcesz spróbować ponownie? (t/n): ").lower() != 't':
                break
                
        except ValueError:
            print("\nBłąd: Wprowadź poprawne liczby!")
            continue

if __name__ == "__main__":
    main()