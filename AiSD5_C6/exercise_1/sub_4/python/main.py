def selection_sort(arr):
    """
    # Funkcja realizująca sortowanie przez wybieranie
    
    Parametry:
    arr (list): Lista liczb do posortowania
    
    Zwraca:
    tuple: (posortowana_lista, liczba_porównań, liczba_zamian)
    """
    # Tworzymy kopię listy, aby nie modyfikować oryginału
    arr = arr.copy()
    
    # Inicjalizacja liczników
    comparisons = 0  # licznik porównań
    swaps = 0        # licznik zamian
    
    n = len(arr)
    
    # Przechodzimy przez wszystkie elementy oprócz ostatniego
    for i in range(n - 1):
        # Zakładamy, że bieżący element jest minimalny
        min_idx = i
        
        # Szukamy minimum w nieposortowanej części tablicy
        for j in range(i + 1, n):
            # Zwiększamy licznik porównań
            comparisons += 1
            
            # Jeśli znajdziemy element mniejszy od aktualnego minimum
            if arr[j] < arr[min_idx]:
                min_idx = j
        
        # Jeśli znaleźliśmy nowe minimum, zamieniamy elementy miejscami
        if min_idx != i:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
            swaps += 1
            
    return arr, comparisons, swaps