import math

def f(x: float) -> float:
    """
    Oblicza wartość funkcji f(x) = x³ - x² - x + 2
    
    Argumenty:
        x (float): Punkt, w którym obliczamy wartość funkcji
        
    Zwraca:
        float: Wartość funkcji w punkcie x
    """
    return x**3 - x**2 - x + 2

def f_derivative(x: float) -> float:
    """
    Oblicza pochodną funkcji f(x)
    f'(x) = 3x² - 2x - 1
    
    Argumenty:
        x (float): Punkt, w którym obliczamy pochodną
        
    Zwraca:
        float: Wartość pochodnej w punkcie x
    """
    return 3*x**2 - 2*x - 1

def check_root_exists(a: float, b: float) -> bool:
    """
    Sprawdza, czy w przedziale [a,b] istnieje miejsce zerowe 
    używając twierdzenia o wartości pośredniej
    
    Argumenty:
        a (float): Lewy kraniec przedziału
        b (float): Prawy kraniec przedziału
        
    Zwraca:
        bool: True jeśli miejsce zerowe istnieje, False w przeciwnym razie
    """
    return f(a) * f(b) <= 0

def newton_method(x0: float, epsilon: float, max_iterations: int) -> tuple[float, int]:
    """
    Implementacja metody Newtona znajdowania miejsca zerowego funkcji
    
    Argumenty:
        x0 (float): Początkowe przybliżenie
        epsilon (float): Oczekiwana dokładność
        max_iterations (int): Maksymalna dozwolona liczba iteracji
        
    Zwraca:
        tuple[float, int]: (Przybliżenie miejsca zerowego, Liczba wykonanych iteracji)
    """
    iteration = 0
    x = x0
    
    while iteration < max_iterations:
        fx = f(x)
        # Sprawdzamy czy znaleźliśmy miejsce zerowe z zadaną dokładnością
        if abs(fx) <= epsilon:
            return x, iteration
            
        fx_prime = f_derivative(x)
        # Zabezpieczenie przed dzieleniem przez zero
        if fx_prime == 0:
            raise ValueError("Pochodna równa zero. Nie można kontynuować obliczeń.")
            
        # Wzór metody Newtona
        x_new = x - fx / fx_prime
        x = x_new
        iteration += 1
        
    raise ValueError(f"Metoda nie osiągnęła zbieżności po {max_iterations} iteracjach")

def get_valid_float_input(prompt: str) -> float:
    """
    Pobiera i waliduje dane wejściowe typu float od użytkownika
    
    Argumenty:
        prompt (str): Komunikat wyświetlany użytkownikowi
        
    Zwraca:
        float: Poprawna wartość liczby zmiennoprzecinkowej
    """
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Błąd: Proszę wprowadzić poprawną liczbę.")

def main():
    """Główna pętla programu"""
    while True:
        print("\nProgram do znajdowania miejsc zerowych funkcji metodą Newtona")
        print("f(x) = x³ - x² - x + 2")
        
        # Pobieranie danych wejściowych
        a = get_valid_float_input("Podaj wartość początkową przedziału (a): ")
        b = get_valid_float_input("Podaj wartość końcową przedziału (b): ")
        
        # Sprawdzanie poprawności przedziału
        if not check_root_exists(a, b):
            print("W podanym przedziale nie ma miejsca zerowego. Spróbuj ponownie.")
            continue
            
        epsilon = get_valid_float_input("Podaj dokładność (epsilon > 0): ")
        if epsilon <= 0:
            print("Dokładność musi być większa od 0. Spróbuj ponownie.")
            continue
            
        max_iter = int(get_valid_float_input("Podaj maksymalną liczbę iteracji: "))
        if max_iter <= 0:
            print("Liczba iteracji musi być większa od 0. Spróbuj ponownie.")
            continue
            
        try:
            # Używamy lewego końca przedziału jako pierwszego przybliżenia
            root, iterations = newton_method(a, epsilon, max_iter)
            print(f"\nZnalezione miejsce zerowe: {root:.6f}")
            print(f"Liczba wykonanych iteracji: {iterations}")
            print(f"Wartość funkcji w znalezionym punkcie: {f(root):.6e}")
            
        except ValueError as e:
            print(f"Błąd: {e}")
            
        # Pytanie o kontynuację
        if input("\nCzy chcesz spróbować ponownie? (t/n): ").lower() != 't':
            break

if __name__ == "__main__":
    main()