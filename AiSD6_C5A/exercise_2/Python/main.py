import math

def f(x):
    """
    Funkcja sigmoidalna: f(x) = 2 * (e^x)/(1 + e^x) - 1
    """
    try:
        return 2 * (math.exp(x) / (1 + math.exp(x))) - 1
    except OverflowError:
        # Obsługa bardzo dużych wartości x
        return 1.0 if x > 0 else -1.0

def rectangle_method(a: float, b: float, n: int) -> float:
    """
    Implementacja metody prostokątów
    :param a: początek przedziału
    :param b: koniec przedziału
    :param n: liczba podprzedziałów
    :return: przybliżona wartość całki
    """
    s = 0.0
    h = (b - a) / n
    x = a + h/2  # Punkt środkowy pierwszego prostokąta
    
    for i in range(n):
        s += h * f(x)
        x += h
        
    return s

def trapezoidal_method(a: float, b: float, n: int) -> float:
    """
    Implementacja metody trapezów
    :param a: początek przedziału
    :param b: koniec przedziału
    :param n: liczba podprzedziałów
    :return: przybliżona wartość całki
    """
    s = 0.0
    h = (b - a) / n
    x = a
    
    for i in range(n):
        s += h * (f(x) + f(x + h)) / 2
        x += h
        
    return s

def simpson_method(a: float, b: float, n: int) -> float:
    """
    Implementacja metody Simpsona
    :param a: początek przedziału
    :param b: koniec przedziału
    :param n: liczba podprzedziałów (musi być parzysta)
    :return: przybliżona wartość całki
    """
    if n % 2 != 0:
        raise ValueError("Liczba podprzedziałów (n) musi być parzysta dla metody Simpsona")
        
    s = 0.0
    h = (b - a) / n
    x = a
    
    for i in range(n):
        x1 = x + h/2
        x2 = x1 + h/2
        s += (h/2) * (f(x) + 4*f(x1) + f(x2)) / 3
        x += h
        
    return s

def print_results(method_name: str, a: float, b: float, n: int, result: float):
    """
    Wypisuje wyniki zgodnie z wymaganiami, z dokładnością do 14 miejsc po przecinku
    """
    print("\nWyniki obliczeń:")
    print("1. Wzór funkcji: f(x) = 2 * e^x/(1 + e^x) - 1")
    print(f"2. Metoda obliczeń: {method_name}")
    print(f"3. Liczba podziałów (n): {n}")
    print(f"4. Przedział całkowania: [{a:}, {b:}]")
    print(f"5. Wartość całki: {result:.16f}")  # Zwiększona precyzja do 14 miejsc po przecinku

def format_table_results(value: float) -> str:
    """
    Formatuje wartość do tabeli z dokładnością 16 miejsc po przecinku
    """
    return f"{value:.16f}"

def main():
    """
    Główna funkcja programu
    """
    try:
        # Pobieranie danych wejściowych
        print("Program do obliczania całki oznaczonej funkcji sigmoidalnej")
        n = int(input("Podaj liczbę podziałów (n): "))
        a = float(input("Podaj początek przedziału (a): "))
        b = float(input("Podaj koniec przedziału (b): "))
        
        # Sprawdzenie poprawności danych
        if n <= 0:
            raise ValueError("Liczba podziałów musi być dodatnia")
        if a >= b:
            raise ValueError("Początek przedziału musi być mniejszy od końca")
            
        # Obliczenia i wyświetlenie wyników dla każdej metody
        rect_result = rectangle_method(a, b, n)
        print_results("Metoda prostokątów", a, b, n, rect_result)
        
        trap_result = trapezoidal_method(a, b, n)
        print_results("Metoda trapezów", a, b, n, trap_result)
        
        # Dla metody Simpsona n musi być parzyste
        n_simpson = n if n % 2 == 0 else n + 1
        simp_result = simpson_method(a, b, n_simpson)
        print_results("Metoda Simpsona", a, b, n_simpson, simp_result)
        
        # Wyświetlenie wyników w formie tabeli
        print("\nZestawienie wyników:")
        print("-" * 50)
        print(f"Metoda        | Wartość całki")
        print("-" * 50)
        print(f"Prostokątów   | {format_table_results(rect_result)}")
        print(f"Trapezów      | {format_table_results(trap_result)}")
        print(f"Simpsona      | {format_table_results(simp_result)}")
        print("-" * 50)
        
    except ValueError as e:
        print(f"Błąd: {e}")
    except Exception as e:
        print(f"Wystąpił nieoczekiwany błąd: {e}")

if __name__ == "__main__":
    main()