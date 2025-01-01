# Analiza porównawcza implementacji metody bisekcji

#### Test metody rekurencyjnej
![test results](./test.png)

#### Test metody iteracyjnej
![test results](../exercise_1/test.png)

## 1. Główne różnice między implementacjami

### Metoda rekurencyjna:
- Wykorzystuje stos wywołań rekurencyjnych
- Warunek stopu: `abs(b - a) < precision`
- Nie sprawdza wartości funkcji w punkcie środkowym

### Metoda iteracyjna:
- Wykorzystuje pętlę while
- Dodatkowy warunek stopu: `abs(f(x)) <= accuracy`
- Bardziej efektywna pamięciowo

## 2. Problem z warunkiem stopu ustawionym na 0

### Przykład z wyników testów:
- Gdy dokładność = 0
- Program nie może osiągnąć dokładnie zera
- Prowadzi do nieskończonej pętli lub przepełnienia stosu

### Powody:
1. Ograniczenia arytmetyki zmiennoprzecinkowej
2. Niedokładności numeryczne w obliczeniach
3. Brak gwarancji osiągnięcia dokładnie zera

### Prawidłowe podejście:
- Używanie małej, niezerowej wartości dokładności (np. 0.0001)
- Sprawdzanie zarówno szerokości przedziału jak i wartości funkcji
- Unikanie porównań z dokładnym zerem

## 3. Analiza efektywności

### Liczba iteracji:
- Metoda rekurencyjna: zazwyczaj mniej iteracji - (w przypadku testu na procesorze m1 wyszło odwrotnie)
- Metoda iteracyjna: więcej iteracji, ale bezpieczniejsza

### Zużycie pamięci:
- Metoda rekurencyjna: O(log n) na stosie
- Metoda iteracyjna: O(1) pamięci

## 4. Wnioski

1. Metoda iteracyjna jest bezpieczniejsza w praktycznym zastosowaniu
2. Dokładność = 0 jest nieprawidłowym warunkiem stopu
3. Obie metody znajdują podobne wyniki, ale różnią się w szczegółach implementacji
4. Zalecane jest używanie małej, niezerowej wartości dokładności

## 5. Rekomendacje

1. Preferować metodę iteracyjną w praktycznych zastosowaniach
2. Zawsze używać niezerowej wartości dokładności
3. Implementować oba warunki stopu:
   - Szerokość przedziału
   - Wartość funkcji w przybliżonym miejscu zerowym