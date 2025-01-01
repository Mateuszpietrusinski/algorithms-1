import random

# Stałe programu
C_IleLiczb = 25  # Ilość elementów w tablicy
C_ZakresMax = 1000  # Maksymalna wartość losowanej liczby

def TworzTab():
    """
    Funkcja tworzy tablicę losowych liczb z zakresu <0,1000)
    Zwraca: lista 25 losowych liczb całkowitych
    """
    return [random.randint(0, C_ZakresMax-1) for _ in range(C_IleLiczb)]

def WyswietlTab(tab_przed, tab_po):
    """
    Funkcja wyświetla zawartość tablicy przed i po sortowaniu w dwóch kolumnach
    Parametry:
        tab_przed: lista liczb przed sortowaniem
        tab_po: lista liczb po sortowaniu
    """
    print("=" * 11, "Przeszukiwanie binarne", "=" * 11)
    print("\n===== Tablica przed i po sortowaniu =====")
    for i in range(len(tab_przed)):
        print(f"{tab_przed[i]:4d}     | {i:2d}: {tab_po[i]:4d}")

def SzukajBinarnieIteracyjnie(tab, szukana):
    """
    Funkcja przeszukuje binarnie tablicę metodą iteracyjną
    Parametry:
        tab: posortowana lista liczb
        szukana: wartość poszukiwana
    Zwraca: (pozycja, liczba_krokow) lub (-1, liczba_krokow) jeśli nie znaleziono
    """
    lewy, prawy = 0, len(tab) - 1
    kroki = 0
    
    while lewy <= prawy:
        kroki += 1
        srodek = (lewy + prawy) // 2
        
        if tab[srodek] == szukana:
            return srodek, kroki
        elif tab[srodek] < szukana:
            lewy = srodek + 1
        else:
            prawy = srodek - 1
            
    return -1, kroki

def SzukajBinarnieRekurencyjnie(tab, szukana, lewy, prawy, kroki=0):
    """
    Funkcja przeszukuje binarnie tablicę metodą rekurencyjną
    Parametry:
        tab: posortowana lista liczb
        szukana: wartość poszukiwana
        lewy, prawy: granice przeszukiwania
        kroki: licznik kroków
    Zwraca: (pozycja, liczba_krokow) lub (-1, liczba_krokow) jeśli nie znaleziono
    """
    if lewy > prawy:
        return -1, kroki
        
    srodek = (lewy + prawy) // 2
    kroki += 1
    
    if tab[srodek] == szukana:
        return srodek, kroki
    elif tab[srodek] < szukana:
        return SzukajBinarnieRekurencyjnie(tab, szukana, srodek + 1, prawy, kroki)
    else:
        return SzukajBinarnieRekurencyjnie(tab, szukana, lewy, srodek - 1, kroki)
    
def SortowanieBabelkowe(tab):
    """
    Funkcja sortuje tablicę metodą bąbelkową
    Parametry:
        tab: lista liczb do posortowania
    Zwraca: posortowaną listę liczb
    """
    # Tworzymy kopię tablicy, aby nie modyfikować oryginału
    tab_sort = tab.copy()
    n = len(tab_sort)
    
    # Przechodzimy przez tablicę n-1 razy
    for i in range(n-1):
        # Flaga sprawdzająca czy były zamiany w danym przejściu
        zamiana = False
        
        # Porównujemy pary sąsiednich elementów
        for j in range(0, n-i-1):
            # Jeśli element jest większy od następnego, zamieniamy je miejscami
            if tab_sort[j] > tab_sort[j+1]:
                tab_sort[j], tab_sort[j+1] = tab_sort[j+1], tab_sort[j]
                zamiana = True
                
        # Jeśli w danym przejściu nie było zamian, tablica jest już posortowana
        if not zamiana:
            break
            
    return tab_sort

def main():
    # Generowanie i sortowanie tablicy
    tab_oryginalna = TworzTab()
    tab_posortowana = SortowanieBabelkowe(tab_oryginalna)
    
    # Wyświetlenie tablic
    WyswietlTab(tab_oryginalna, tab_posortowana)
    
    # Pobranie liczby do wyszukania
    try:
        szukana = int(input("\nLiczba szukana:"))
    except ValueError:
        print("Błąd: Proszę wprowadzić poprawną liczbę całkowitą!")
        return
        
    # Wyszukiwanie iteracyjne
    print("\n------- iteracyjnie ----------")
    pozycja, kroki = SzukajBinarnieIteracyjnie(tab_posortowana, szukana)
    if pozycja != -1:
        print(f"Znaleziono na {pozycja} pozycji w {kroki} krokach")
    else:
        print(f"Nie znaleziono liczby {szukana}")
        
    # Wyszukiwanie rekurencyjne
    print("\n------- rekurencyjnie ----------")
    pozycja, kroki = SzukajBinarnieRekurencyjnie(tab_posortowana, szukana, 0, len(tab_posortowana)-1)
    if pozycja != -1:
        print(f"Znaleziono na {pozycja} pozycji w {kroki} krokach")
    else:
        print(f"Nie znaleziono liczby {szukana}")

if __name__ == "__main__":
    main()