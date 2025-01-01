def bubble_sort(arr):
    """
    # Funkcja realizująca sortowanie bąbelkowe
    
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
    
    n = len(arr)     # długość tablicy
    
    # Pętla zewnętrzna - określa ile razy będziemy przechodzić przez tablicę
    for i in range(n):
        # Flaga sprawdzająca czy była zamiana w danym przejściu
        was_swap = False
        
        # Pętla wewnętrzna - porównywanie par elementów
        # Odejmujemy 'i' bo po każdym przejściu ostatnie 'i' elementów jest już posortowane
        for j in range(0, n-i-1):
            # Zwiększamy licznik porównań
            comparisons += 1
            
            # Jeśli element bieżący jest większy od następnego
            if arr[j] > arr[j+1]:
                # Zamiana miejscami
                arr[j], arr[j+1] = arr[j+1], arr[j]
                # Zwiększamy licznik zamian
                swaps += 1
                # Ustawiamy flagę, że była zamiana
                was_swap = True
        
        # Jeśli w danym przejściu nie było żadnej zamiany,
        # tablica jest już posortowana i możemy zakończyć
        if not was_swap:
            break
            
    return arr, comparisons, swaps