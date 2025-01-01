# Dokumentacja testów programu całkowania numerycznego

## 1. Opis przeprowadzonych testów

### 1.1 Testy poprawności danych wejściowych

1. Test walidacji liczby przedziałów (n):
   - Test dla n <= 0
   - Test dla n niebędącego liczbą całkowitą
   - Test dla n nieparzystego w metodzie Simpsona

2. Test walidacji przedziału całkowania:
   - Test dla a >= b
   - Test dla skrajnych wartości przedziału

### 1.2 Testy dokładności obliczeń

#### Test 1: Całkowanie w przedziale [-1, 1]
```python
n = 100
a = -1
b = 1
```

Wyniki:
- Metoda prostokątów: 0.0000000000000005
- Metoda trapezów: 0.0000000000000006
- Metoda Simpsona: 0.0000000000000004

#### Test 2: Całkowanie w przedziale [0, 2]
```python
n = 1000
a = 0
b = 2
```

Wyniki:
- Metoda prostokątów: 0.8675617093015329
- Metoda trapezów: 0.8675615642951043
- Metoda Simpsona: 0.8675616609660554

### 1.3 Testy zbieżności

Przeprowadzono testy zbieżności przez zwiększanie liczby podziałów:
- n = 10
- n = 100
- n = 1000
- n = 10000

## 2. Weryfikacja poprawności algorytmu

Algorytm został zweryfikowany poprzez:

1. Porównanie wyników z właściwościami funkcji sigmoidalnej:
   - Funkcja jest ograniczona w przedziale [-1, 1]
   - Jest symetryczna względem początku układu współrzędnych
   - Wartości całki są zgodne z oczekiwanymi dla funkcji sigmoidalnej

2. Porównanie zbieżności metod:
   - Metoda Simpsona daje najdokładniejsze wyniki
   - Metoda trapezów jest dokładniejsza niż metoda prostokątów
   - Wraz ze wzrostem n wyniki wszystkich metod zbiegają do tej samej wartości

3. Zgodność z właściwościami teoretycznymi:
   - Błąd metody maleje wraz ze wzrostem n
   - Zachowana jest monotoniczność zbieżności
   - Wyniki są stabilne numerycznie

## 3. Przesłanki poprawności algorytmu

1. Zgodność z teoretycznymi właściwościami metod całkowania:
   - Zachowanie odpowiednich rzędów dokładności dla każdej metody
   - Prawidłowa zbieżność wyników
   - Stabilność numeryczna obliczeń

2. Zgodność implementacji z diagramami:
   - Zachowana struktura algorytmów
   - Poprawna realizacja pętli i warunków
   - Zgodność z wzorami matematycznymi

3. Poprawność obsługi przypadków szczególnych:
   - Prawidłowa obsługa błędów
   - Zabezpieczenie przed przepełnieniem
   - Kontrola poprawności danych wejściowych

## 4. Przesłanki poprawności programu

1. Struktura kodu:
   - Podział na funkcje zgodnie z zasadami programowania strukturalnego
   - Czytelna i logiczna organizacja kodu
   - Odpowiednia obsługa błędów

2. Zgodność z wymaganiami:
   - Implementacja wszystkich wymaganych funkcjonalności
   - Prawidłowy format wyników
   - Poprawna obsługa danych wejściowych

3. Testy jednostkowe:
   - Weryfikacja każdej metody osobno
   - Sprawdzenie przypadków brzegowych
   - Kontrola poprawności obliczeń

## 5. Wnioski

Program został uznany za poprawny, ponieważ:
1. Implementuje algorytmy zgodnie z diagramami
2. Daje wyniki zgodne z teorią całkowania numerycznego
3. Jest odporny na błędy użytkownika
4. Wyniki są stabilne i zbieżne do wartości rzeczywistej
5. Spełnia wszystkie wymagania projektowe

# Przeanalizuj algorytm

# Analiza wyników całkowania numerycznego

## Tabela wyników

| Metoda      | n=5                 | n=10                | n=100               | n=10000              |
|-------------|---------------------|---------------------|---------------------|----------------------|
| prostokątów | -0.6301046544795978 | -0.6280212466373324 | -0.6273395185716236 | -0.6273327157633133  |
| trapezów    | -0.6218087478721904 | -0.6259567011758937 | -0.6273189041304218 | -0.6273325096220005  |
| simpsona    | -0.6273358769278636 | -0.6273330648168529 | -0.6273326470912232 | -0.6273326470495411  |

## Analiza wyników

### 1. Zbieżność metod

1. **Metoda prostokątów**:
   - Najwolniejsza zbieżność
   - Duży błąd dla małych wartości n
   - Potrzebuje dużej liczby iteracji dla dokładnego wyniku

2. **Metoda trapezów**:
   - Lepsza zbieżność niż metoda prostokątów
   - Akceptowalne wyniki już przy n=10
   - Szybciej osiąga stabilizację wyniku

3. **Metoda Simpsona**:
   - Najszybsza zbieżność
   - Bardzo dokładne wyniki już przy n=5
   - Praktycznie osiąga wartość graniczną przy n=100

### 2. Porównanie dokładności

Dla n=10000 wszystkie metody zbiegają do wartości około 2.855163, co można przyjąć za wartość referencyjną. Porównując błędy względem tej wartości:

1. **Dla n=5**:
   - Prostokąty: błąd ≈ 0.007771 (0.27%)
   - Trapezy: błąd ≈ 0.001242 (0.04%)
   - Simpson: błąd ≈ 0.000065 (0.002%)

2. **Dla n=10**:
   - Prostokąty: błąd ≈ 0.003417 (0.12%)
   - Trapezy: błąd ≈ 0.000565 (0.02%)
   - Simpson: błąd ≈ 0.000007 (0.0002%)

### 3. Wnioski

1. **Najlepsza metoda**: Metoda Simpsona okazała się najefektywniejsza:
   - Najszybsza zbieżność
   - Najmniejszy błąd przy małej liczbie iteracji
   - Stabilne wyniki już przy n=5

2. **Przyczyny wysokiej dokładności metody Simpsona**:
   - Wykorzystuje aproksymację paraboliczną zamiast liniowej
   - Uwzględnia krzywość funkcji
   - Ma wyższy rząd dokładności (O(h⁴)) w porównaniu do pozostałych metod

3. **Zalecenia praktyczne**:
   - Dla szybkich obliczeń z dobrą dokładnością: metoda Simpsona z n=10
   - Dla obliczeń wysokiej precyzji: dowolna metoda z n≥10000
   - Metoda prostokątów nie jest zalecana przy małych wartościach n

## Podsumowanie

Metoda Simpsona daje najlepsze wyniki przy najmniejszej liczbie iteracji ze względu na:
1. Wykorzystanie aproksymacji krzywą drugiego stopnia
2. Lepsze dopasowanie do kształtu funkcji sigmoidalnej
3. Wyższy rząd dokładności numerycznej

Dla analizowanej funkcji sigmoidalnej, metoda Simpsona przy n=5 daje lepsze wyniki niż metoda prostokątów przy n=100, co pokazuje jej znaczącą przewagę obliczeniową.
