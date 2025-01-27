def insertion_sort(arr, n):
    """
    Funkcja realizująca sortowanie przez wstawianie zgodnie ze schematem blokowym
    
    Parametry:
    arr (list): Lista liczb do posortowania
    n (int): Długość listy
    
    Zwraca:
    tuple: (posortowana_lista, liczba_porównań, liczba_zamian)
    """
    # Tworzymy kopię listy
    arr = arr.copy()
    
    # Inicjalizacja liczników
    comparisons = 0
    swaps = 0
    
    # Rozpoczynamy od i=2 zgodnie ze schematem
    i = 2
    while i <= n:
        # Pobieramy element do wstawienia
        x = arr[i-1]  # i-1 bo indeksujemy od 0
        
        # Wstawianie x w odpowiednie miejsce tablicy
        j = i - 2  # Zaczynamy od elementu przed x
        
        # Przesuwamy elementy większe od x
        while j >= 0:
            comparisons += 1
            if arr[j] > x:
                # Przesuwamy element w prawo
                arr[j + 1] = arr[j]
                swaps += 1
                j -= 1
            else:
                break
                
        # Wstawiamy x w znalezione miejsce
        if j + 1 != i - 1:  # Jeśli pozycja się zmieniła
            arr[j + 1] = x
            swaps += 1
            
        i += 1
        
    return arr, comparisons, swaps