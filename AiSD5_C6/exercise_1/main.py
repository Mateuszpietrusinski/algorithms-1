import random
import time
from sub_1.python.main import bubble_sort
from sub_2.python.main import insertion_sort
from sub_3.python.main import insertion_sort_sentinel
from sub_4.python.main import selection_sort
from sub_5.python.main import quick_sort

# Stała określająca ilość liczb
C_IleLiczb = 20

#--- Tworzenie tablicy losowych wartości
def TabLos():
    Tab = []
    Tab.append(-1)
    #random.seed(1) # Ustaw, by generować zawsze te same liczby
    for i in range(0, C_IleLiczb):
        Tab.append(random.randint(0, 999))
    return Tab

def print_sorting_results(T1, T2, algorithm_name, stats):
    """
    # Funkcja wyświetlająca wyniki sortowania dla jednego algorytmu
    
    Parametry:
    T1 (list): Tablica przed sortowaniem
    T2 (list): Tablica po sortowaniu
    algorithm_name (str): Nazwa algorytmu
    stats (tuple): Krotka (liczba_porównań, liczba_zamian)
    """
    print(f"\n{'='*13} {algorithm_name} {'='*13}")
    print("="*35)
    
    # Wyświetlanie elementów tablic od indeksu 1 do C_IleLiczb
    for i in range(0, C_IleLiczb + 0):
        print(f'{i:2}: {T1[i]:5} {T2[i]:5}')
    
    comparisons, swaps = stats
    print(f"\nPorównań: {comparisons}")
    print(f"Zamian:    {swaps}")

def main():
    """
    # Główna funkcja programu
    """
    # Generowanie tablicy testowej
    test_array = [654, 114, 25, 759, 281, 250, 228, 142, 754, 104, 692, 758, 913, 558, 89, 604, 432, 32, 30, 95]
    # test_array = [25, 30, 32, 89, 95, 104, 114, 142, 228, 250, 281, 432, 558, 604, 654, 692, 754, 758, 759, 913]
    # test_array = [521, 605, 13, 912, 757, 81, 296, 105, 775, 214, 218, 428, 759, 302, 835, 576, 607, 633, 109, 270]
    # print(test_array)
    
    # Lista funkcji sortujących
    sorting_functions = {
        'Sortowanie bąbelkowe': bubble_sort,
        'Proste wstawianie': insertion_sort,
        'Wstawianie ze strażnikiem': insertion_sort_sentinel,
        'Proste wybieranie': selection_sort,
        'Sortowanie szybkie': quick_sort
    }
    
    # Nagłówek programu
    print("\n" + "="*13 + " Sortowanie " + "="*13)
    
    # Wykonanie sortowania każdą metodą
    for name, sort_func in sorting_functions.items():
        # Kopiowanie tablicy do sortowania
        array_to_sort = test_array.copy()
        
        # Sortowanie i pomiar czasu
        start_time = time.time()
        sorted_arr, comparisons, swaps = sort_func(array_to_sort, len(test_array))
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