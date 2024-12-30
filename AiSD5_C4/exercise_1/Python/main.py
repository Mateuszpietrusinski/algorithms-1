import sys

def silnia_rekurencyjna(n):
    """
    Calculates factorial using recursive approach
    Args:
        n (int): Non-negative integer to calculate factorial for
    Returns:
        int: Factorial of n
    """
    if n == 0:
        return 1
    else:
        return n * silnia_rekurencyjna(n - 1)

def silnia_iteracyjna(n):
    """
    Calculates factorial using iterative approach
    Args:
        n (int): Non-negative integer to calculate factorial for
    Returns:
        int: Factorial of n
    """
    wynik = 1
    for i in range(1, n + 1):
        wynik *= i
    return wynik

def analyze_factorial(n):
    """
    Analyzes factorial calculation for a given number, including memory usage
    Args:
        n (int): Number to analyze factorial for
    """
    # Calculate factorial (using iterative method for large numbers)
    S = silnia_iteracyjna(n)
    
    # Print all required values in a formatted way
    print("\nWyniki dla silni:")
    print("-" * 50)
    print(f"Wartość argumentu funkcji silnia: {n}")
    print(f"Wartość obliczonej silni: {S}")
    print(f"Typ zmiennej argumentu: {type(n)}")
    print(f"Typ zmiennej wartości funkcji silnia: {type(S)}")
    print(f"Liczba bajtów zmiennej argumentu: {sys.getsizeof(n)}")
    print(f"Liczba bajtów zmiennej wartości funkcji: {sys.getsizeof(S)}")
    print("-" * 50)

def main():
    """
    Main function to run factorial analysis for specified values
    """
    # Test values as specified in the requirements
    test_values = [2, 20, 50, 100]
    
    print("Analiza funkcji silnia dla różnych wartości:")
    for value in test_values:
        analyze_factorial(value)

if __name__ == "__main__":
    main()