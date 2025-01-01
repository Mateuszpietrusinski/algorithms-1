class QuickSort:
    """
    # Klasa implementująca algorytm sortowania szybkiego
    
    Atrybuty:
    comparisons (int): licznik porównań
    swaps (int): licznik zamian
    """
    def __init__(self):
        # Inicjalizacja liczników
        self.comparisons = 0
        self.swaps = 0
        
    def partition(self, arr, low, high):
        """
        # Funkcja dzieląca tablicę na dwie części względem elementu osiowego (pivot)
        
        Parametry:
        arr (list): Lista do podziału
        low (int): Indeks początkowy zakresu
        high (int): Indeks końcowy zakresu
        
        Zwraca:
        int: Indeks elementu osiowego po podziale
        """
        # Wybieramy element osiowy (pivot) jako ostatni element
        pivot = arr[high]
        
        # Indeks mniejszych elementów
        i = low - 1
        
        # Przechodzimy przez wszystkie elementy oprócz pivota
        for j in range(low, high):
            # Zwiększamy licznik porównań
            self.comparisons += 1
            
            # Jeśli aktualny element jest mniejszy lub równy pivot
            if arr[j] <= pivot:
                # Przesuwamy indeks mniejszych elementów
                i += 1
                # Zamieniamy elementy miejscami
                if i != j:
                    arr[i], arr[j] = arr[j], arr[i]
                    self.swaps += 1
        
        # Wstawiamy pivot na właściwe miejsce
        if i + 1 != high:
            arr[i + 1], arr[high] = arr[high], arr[i + 1]
            self.swaps += 1
            
        return i + 1
        
    def quick_sort_recursive(self, arr, low, high):
        """
        # Rekurencyjna funkcja implementująca sortowanie szybkie
        
        Parametry:
        arr (list): Lista do posortowania
        low (int): Indeks początkowy zakresu
        high (int): Indeks końcowy zakresu
        """
        if low < high:
            # Znajdujemy indeks podziału
            pi = self.partition(arr, low, high)
            
            # Rekurencyjnie sortujemy elementy przed i po elemencie osiowym
            self.quick_sort_recursive(arr, low, pi - 1)
            self.quick_sort_recursive(arr, pi + 1, high)
            
    def sort(self, arr):
        """
        # Główna funkcja sortująca
        
        Parametry:
        arr (list): Lista do posortowania
        
        Zwraca:
        tuple: (posortowana_lista, liczba_porównań, liczba_zamian)
        """
        # Tworzymy kopię listy, aby nie modyfikować oryginału
        arr_copy = arr.copy()
        
        # Resetujemy liczniki
        self.comparisons = 0
        self.swaps = 0
        
        # Wywołujemy właściwe sortowanie
        self.quick_sort_recursive(arr_copy, 0, len(arr_copy) - 1)
        
        return arr_copy, self.comparisons, self.swaps

# Funkcja pomocnicza dla łatwiejszego użycia
def quick_sort(arr):
    """
    # Funkcja opakowująca sortowanie szybkie
    
    Parametry:
    arr (list): Lista do posortowania
    
    Zwraca:
    tuple: (posortowana_lista, liczba_porównań, liczba_zamian)
    """
    sorter = QuickSort()
    return sorter.sort(arr)