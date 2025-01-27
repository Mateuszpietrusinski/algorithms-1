def insertion_sort_sentinel(arr, n):
    """
    # Funkcja realizująca sortowanie przez wstawianie ze strażnikiem
    
    Parametry:
    arr (list): Lista liczb do posortowania
    
    Zwraca:
    tuple: (posortowana_lista, liczba_porównań, liczba_zamian)
    """
    # Tworzymy nową listę z miejscem na strażnika na początku (indeks 0)
    # Strażnik eliminuje potrzebę sprawdzania warunku j >= 0
    working_arr = [0] + arr.copy()  # Element [0] to strażnik
    
    # Inicjalizacja liczników
    comparisons = 0  # licznik porównań
    swaps = 0        # licznik zamian
    
    # Przechodzimy przez wszystkie elementy począwszy od drugiego
    # Pamiętamy, że indeksy są przesunięte o 1 z powodu strażnika
    for i in range(2, len(working_arr)):
        # Zapamiętujemy aktualny element do wstawienia
        key = working_arr[i]
        
        # Ustawiamy strażnika jako element do wstawienia
        # To eliminuje potrzebę sprawdzania warunku j >= 0
        working_arr[0] = key
        
        # Inicjalizujemy indeks poprzedniego elementu
        j = i - 1
        
        # Przesuwamy elementy większe od key o jedną pozycję w prawo
        # Strażnik gwarantuje zakończenie pętli
        while working_arr[j] > key:
            # Zwiększamy licznik porównań
            comparisons += 1
            
            # Przesuwamy element w prawo
            working_arr[j + 1] = working_arr[j]
            # Zwiększamy licznik zamian
            swaps += 1
            j -= 1
        
        # Dodajemy jeszcze jedno porównanie (z ostatnim elementem)
        comparisons += 1
        
        # Jeśli pozycja wstawienia jest inna niż początkowa,
        # wstawiamy element i liczymy to jako zamianę
        if j + 1 != i:
            working_arr[j + 1] = key
            swaps += 1
            
    # Zwracamy posortowaną listę bez strażnika (element [0])
    return working_arr[1:], comparisons, swaps