def bubble_sort(arr, n):
    """
    Implementacja nauczyciela - zawsze stała liczba porównań
    """
    comparisons = 0
    swaps = 0
    
    for i in range(n):
        for j in range(1, n - i):
            comparisons += 1
            if arr[j-1] > arr[j]:
                arr[j-1], arr[j] = arr[j], arr[j-1]
                swaps += 1
    return arr, comparisons, swaps