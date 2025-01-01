import random
import time
from sub_1.python.main import bubble_sort
from sub_2.python.main import insertion_sort
from sub_3.python.main import insertion_sort_sentinel
from sub_4.python.main import selection_sort
from sub_5.python.main import quick_sort

def generate_random_array(size, min_val, max_val):
    """
    # Funkcja generująca losową tablicę liczb
    
    Parametry:
    size (int): Rozmiar tablicy
    min_val (int): Minimalna wartość
    max_val (int): Maksymalna wartość
    
    Zwraca:
    list: Wygenerowana tablica losowych liczb
    """
    return [random.randint(min_val, max_val) for _ in range(size)]

def print_sorting_results(original, sorted_array, algorithm_name, stats):
    """
    # Funkcja wyświetlająca wyniki sortowania dla jednego algorytmu
    
    Parametry:
    original (list): Oryginalna tablica
    sorted_array (list): Posortowana tablica
    algorithm_name (str): Nazwa algorytmu
    stats (tuple): Krotka (liczba_porównań, liczba_zamian)
    """
    print(f"\n{'='*13} {algorithm_name} {'='*13}")
    print(f"{'Przed':15} {'Po':15}")
    print("="*30)
    
    for i in range(len(original)):
        print(f"{i+1:2d}: {original[i]:4d}     {i+1:2d}: {sorted_array[i]:4d}")
    
    comparisons, swaps = stats
    print(f"\nPorównań: {comparisons}")
    print(f"Zamian:    {swaps}")

def main():
    """
    # Główna funkcja programu
    """
    # Ustawienie ziarna dla powtarzalności wyników
    random.seed(42)
    
    # Generowanie danych testowych
    SIZE = 20
    MIN_VAL = 0
    MAX_VAL = 999
    test_array = generate_random_array(SIZE, MIN_VAL, MAX_VAL)
    
    # Lista funkcji sortujących
    sorting_functions = {
        'Bąbelkowe': bubble_sort,
        'Proste wstawianie': insertion_sort,
        'Wstawianie ze strażnikiem': insertion_sort_sentinel,
        'Proste wybieranie': selection_sort,
        'Sortowanie szybkie': quick_sort
    }
    
    # Nagłówek programu
    print("\n" + "="*13 + " Sortowanie " + "="*13)
    
    # Wykonanie sortowania każdą metodą
    for name, sort_func in sorting_functions.items():
        # Sortowanie i pomiar czasu
        start_time = time.time()
        sorted_arr, comparisons, swaps = sort_func(test_array.copy())
        end_time = time.time()
        
        # Wyświetlenie wyników
        print_sorting_results(
            test_array,
            sorted_arr,
            name,
            (comparisons, swaps)
        )
        print(f"Czas: {(end_time - start_time)*1000:.2f} ms\n")

if __name__ == "__main__":
    main()