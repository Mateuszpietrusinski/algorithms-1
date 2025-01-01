def insertion_sort(arr):
    """
    # Funkcja realizująca sortowanie przez wstawianie
    
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
    
    # Przechodzimy przez wszystkie elementy począwszy od drugiego
    for i in range(1, len(arr)):
        # Zapamiętujemy aktualny element do wstawienia
        key = arr[i]
        
        # Inicjalizujemy indeks poprzedniego elementu
        j = i - 1
        
        # Przesuwamy elementy większe od key o jedną pozycję w prawo
        # dopóki nie znajdziemy właściwego miejsca dla key
        while j >= 0:
            # Zwiększamy licznik porównań
            comparisons += 1
            
            if arr[j] > key:
                # Przesuwamy element w prawo
                arr[j + 1] = arr[j]
                # Zwiększamy licznik zamian
                swaps += 1
                j -= 1
            else:
                # Znaleźliśmy właściwe miejsce - przerywamy pętlę
                break
        
        # Jeśli pozycja wstawienia jest inna niż początkowa,
        # liczymy to jako jedną operację zamiany
        if j + 1 != i:
            arr[j + 1] = key
            swaps += 1
            
    return arr, comparisons, swaps