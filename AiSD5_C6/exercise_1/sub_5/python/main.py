class QuickSort:
    def __init__(self):
        self.comparisons = 0
        self.swaps = 0
    
    def partition(self, arr, low, high):
        i = (low-1)		 # index of smaller element
        pivot = arr[high]	 # pivot

        for j in range(low, high):
            self.comparisons += 1
            # If current element is smaller than or
            # equal to pivot
            if arr[j] <= pivot:
                pivot += 1
                # increment index of smaller element
                i = i+1
                arr[i], arr[j] = arr[j], arr[i]

        arr[i+1], arr[high] = arr[high], arr[i+1]
        return (i+1)

    def _quicksort(self, array, begin, end):
     
        if begin >= end:
            return
        pivot = self.partition(array, begin, end)
        self._quicksort(array, begin, pivot-1)
        self._quicksort(array, pivot+1, end)

    def sort(self, array):
        # Tworzymy kopię tablicy
        array_copy = array.copy()
        # Resetujemy liczniki
        self.comparisons = 0
        self.swaps = 0
        # Sortujemy
        self._quicksort(array_copy, 0, len(array_copy) - 1)
        return array_copy, self.comparisons, self.swaps

def quick_sort(array, n):
    """
    Funkcja opakowująca sortowanie szybkie
    
    Parametry:
    array (list): Lista do posortowania
    n (int): Długość listy
    
    Zwraca:
    tuple: (posortowana_lista, liczba_porównań, liczba_zamian)
    """
    sorter = QuickSort()
    return sorter.sort(array)