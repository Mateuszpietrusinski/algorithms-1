def f(x):
    """
    Funkcja do znalezienia miejsca zerowego: f(x) = x³ - x² - x + 2
    Args:
        x (float): Wartość x dla której obliczamy wartość funkcji
    Returns:
        float: Wartość funkcji w punkcie x
    """
    return x**3 - x**2 - x + 2

def check_interval(a, b):
    """
    Sprawdza, czy w podanym przedziale [a,b] istnieje miejsce zerowe
    (czy funkcja zmienia znak na końcach przedziału)
    Args:
        a (float): Początek przedziału
        b (float): Koniec przedziału
    Returns:
        bool: True jeśli istnieje miejsce zerowe, False w przeciwnym razie
    """
    return f(a) * f(b) < 0

def bisection_method(a, b, accuracy):
    """
    Implementacja metody bisekcji
    Args:
        a (float): Początek przedziału
        b (float): Koniec przedziału
        accuracy (float): Żądana dokładność
    Returns:
        tuple: (przybliżone miejsce zerowe, liczba iteracji)
    """
    iterations = 0
    
    while abs(b - a) > accuracy:
        x = (a + b) / 2  # Środek przedziału
        iterations += 1
        
        if abs(f(x)) <= accuracy:  # Sprawdzamy czy znaleźliśmy wystarczająco dokładne rozwiązanie
            return x, iterations
            
        if f(a) * f(x) < 0:  # Miejsce zerowe jest w lewej połowie
            b = x
        else:  # Miejsce zerowe jest w prawej połowie
            a = x
            
    return (a + b) / 2, iterations

def get_valid_input():
    """
    Pobiera od użytkownika poprawne dane wejściowe
    Returns:
        tuple: (a, b, accuracy) - końce przedziału i dokładność
    """
    while True:
        try:
            print("\nPodaj końce przedziału [a,b] oraz dokładność:")
            a = float(input("a = "))
            b = float(input("b = "))
            accuracy = float(input("Dokładność = "))
            
            if a >= b:
                print("Błąd: a musi być mniejsze od b!")
                continue
                
            if accuracy <= 0:
                print("Błąd: dokładność musi być większa od 0!")
                continue
                
            if not check_interval(a, b):
                print("Błąd: w podanym przedziale nie ma miejsca zerowego!")
                continue
                
            return a, b, accuracy
            
        except ValueError:
            print("Błąd: wprowadź poprawne liczby!")

def main():
    """
    Główna funkcja programu
    """
    print("Program do znajdowania miejsca zerowego funkcji f(x) = x³ - x² - x + 2")
    print("metodą bisekcji")
    
    while True:
        a, b, accuracy = get_valid_input()
        x, iterations = bisection_method(a, b, accuracy)
        
        print(f"\nWyniki:")
        print(f"Znalezione miejsce zerowe: {x:.6f}")
        print(f"Wartość funkcji w tym punkcie: {f(x):.6f}")
        print(f"Liczba wykonanych iteracji: {iterations}")
        
        if input("\nCzy chcesz wykonać obliczenia dla innych danych? (t/n): ").lower() != 't':
            break
    
    print("\nDziękuję za skorzystanie z programu!")

if __name__ == "__main__":
    main()