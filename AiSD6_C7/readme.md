# Analiza Algorytmów Wyszukiwania - Wnioski

## 1. Porównanie wyszukiwania binarnego: iteracyjne vs rekurencyjne

Na podstawie wyników z programu (szukana liczba 805, znaleziona na pozycji 20 w 5 krokach) możemy zauważyć, że:

### Podobieństwa
- Obie metody znalazły liczbę w tej samej liczbie kroków (5)
- Obie metody znalazły element na tej samej pozycji (20)
- Obie metody dają dokładnie te same wyniki

### Różnice
- Metoda iteracyjna:
  - Używa pętli while
  - Jest prostsza do zrozumienia
  - Zużywa mniej pamięci
  
- Metoda rekurencyjna:
  - Używa wywołań samej siebie
  - Jest bardziej skomplikowana
  - Zużywa więcej pamięci (każde wywołanie zajmuje pamięć)

## 2. Porównanie z wyszukiwaniem liniowym

Załóżmy, że szukamy liczby 805 w naszej tablicy:

### Wyszukiwanie binarne
- Znalazło liczbę w 5 krokach
- Musimy mieć posortowaną tablicę
- Sprawdza tylko kilka elementów

### Wyszukiwanie liniowe
- Musiałoby sprawdzić 21 elementów (pozycje 0-20)
- Działa na nieposortowanej tablicy
- Sprawdza każdy element po kolei

## Wnioski końcowe:

1. **Kiedy używać której metody?**
   - Wyszukiwanie binarne (iteracyjne) - gdy mamy posortowaną tablicę i chcemy szybko znaleźć element
   - Wyszukiwanie binarne (rekurencyjne) - gdy chcemy mieć bardziej elegancki kod
   - Wyszukiwanie liniowe - gdy mamy małą tablicę lub gdy nie chcemy sortować tablicy

2. **Co jest najszybsze?**
   - Dla mojej tablicy (25 elementów):
     - Wyszukiwanie binarne: maksymalnie 5 kroków
     - Wyszukiwanie liniowe: maksymalnie 25 kroków
   - Wniosek: wyszukiwanie binarne jest około 5 razy szybsze!

3. **Wskazówki praktyczne:**
   - Dla małych tablic (do 10 elementów) - używaj wyszukiwania liniowego (jest prostsze)
   - Dla większych tablic - warto posortować i użyć wyszukiwania binarnego
   - Wybieraj wersję iteracyjną zamiast rekurencyjnej (jest prostsza i używa mniej pamięci)