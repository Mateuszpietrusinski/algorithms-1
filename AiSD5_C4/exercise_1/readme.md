# Task 1: Rozwiazanie

## Pascal
## Analiza ograniczeń silni dla typu Int64 w Pascalu

## 1. Największa wartość argumentu dla poprawnego obliczenia silni

Największa wartość argumentu, dla której można poprawnie obliczyć silnię w typie Int64, to **20**.

Uzasadnienie:
- 20! = 2,432,902,008,176,640,000 (mieści się w zakresie Int64)
- 21! = 51,090,942,171,709,440,000 (przekracza zakres Int64)

Możemy to zweryfikować używając następującego kodu:

```pascal
program SilniaZWeryfikacja;

function SilniaIteracyjna(n: Int64): Int64;
var
    wynik: Int64;
    i: Int64;
begin
    wynik := 1;
    for i := 1 to n do
    begin
        wynik := wynik * i;
        WriteLn('n = ', i, ': ', wynik);
    end;
    SilniaIteracyjna := wynik;
end;

var
    n: Int64;
begin
    n := 21; // Testujemy dla wartości 21
    WriteLn('Próba obliczenia silni dla n = ', n);
    try
        WriteLn('Wynik: ', SilniaIteracyjna(n));
    except
        WriteLn('Wystąpił błąd: Przekroczenie zakresu');
    end;
end.
```

## 2. Zachowanie programu przy przekroczeniu zakresu Int64

Gdy argument przekracza maksymalną wartość (n > 20), występują następujące konsekwencje:

1. **Przepełnienie arytmetyczne (Integer Overflow):**
   - Typ Int64 ma zakres od -9,223,372,036,854,775,808 do 9,223,372,036,854,775,807
   - Przy próbie obliczenia 21! wynik przekracza ten zakres
   - Program zwraca nieprawidłową wartość ze względu na przepełnienie

2. **Przykładowe wartości:**
   - 20! = 2,432,902,008,176,640,000 (ostatnia poprawna wartość)
   - 21! próba obliczenia powoduje przepełnienie i zwraca nieprawidłową wartość

3. **Zachowanie programu:**
   - Program nie zgłasza błędu automatycznie
   - Wynik jest nieprawidłowy ze względu na przepełnienie typu Int64
   - Wartości są "zawijane" w zakresie typu Int64

## Rekomendacje

1. **Zabezpieczenie programu:**
   ```pascal
   if n > 20 then
       WriteLn('Wartość przekracza maksymalny zakres dla typu Int64!')
   else
       // wykonaj obliczenia
   ```

2. **Alternatywne rozwiązania dla większych wartości:**
   - Użycie bibliotek do obliczeń na bardzo dużych liczbach
   - Implementacja własnego typu do obsługi większych liczb
   - Zastosowanie logarytmów dla przybliżonych wyników

## Wnioski

1. Typ Int64 pozwala na bezpieczne obliczenie silni tylko do n=20
2. Dla większych wartości należy:
   - Implementować kontrolę zakresu
   - Rozważyć użycie innych typów danych
   - Zastosować alternatywne metody obliczeniowe

---
## Python

## Analiza obliczeń silni w Pythonie

## 1. Największa wartość argumentu dla poprawnego obliczenia silni

W przeciwieństwie do Pascala, Python nie ma standardowego ograniczenia na wielkość liczb całkowitych. Python automatycznie przechodzi na typ long integer, gdy liczby przekraczają zakres standardowego integera. Teoretycznie jedynym ograniczeniem jest dostępna pamięć komputera.

Jednak w praktyce występują inne ograniczenia:

1. **Ograniczenie rekurencji:**
   - Domyślny limit rekurencji w Pythonie to 1000
   - Dla funkcji `silnia_rekurencyjna` to ograniczenie pojawi się przy n ≈ 998
   - Można to zmienić używając `sys.setrecursionlimit()`

2. **Ograniczenie pamięci:**
   - Bardzo duże wartości silni zajmują znaczącą ilość pamięci
   - Przykładowo, 100000! ma około 456574 cyfr

## 2. Zachowanie programu dla dużych wartości

Python radzi sobie z dużymi liczbami znacznie lepiej niż Pascal. 

## 3. Porównanie z Pascalem

1. **Zakres wartości:**
   - Pascal (Int64): Maksymalnie 20!
   - Python: Praktycznie nieograniczony (ograniczony tylko pamięcią)

2. **Obsługa przepełnienia:**
   - Pascal: Zwraca nieprawidłowe wyniki po przekroczeniu zakresu
   - Python: Automatycznie obsługuje duże liczby

3. **Ograniczenia:**
   - Pascal: Ograniczenie typu Int64
   - Python: Ograniczenie rekurencji i pamięci

## 4. Przykładowe wyniki

```python
# Dla n = 20 (maksymalna wartość Pascala)
20! = 2432902008176640000

# Dla n = 100
100! = 93326215443944152681699238856266700490715968264381621468592963895217599993229915608941463976156518286253697920827223758251185210916864000000000000000000000000

# Liczba cyfr w 100! = 158 cyfr
```

## 5. Rekomendacje

1. **Dla dużych wartości:**
   - Używać wersji iteracyjnej zamiast rekurencyjnej
   - Monitorować zużycie pamięci
   - Rozważyć pokazywanie tylko części wyniku (pierwsze/ostatnie cyfry)

2. **Optymalizacja:**
   - Dla bardzo dużych liczb rozważyć użycie bibliotek matematycznych (np. math.factorial)
   - Implementować postęp obliczeń dla długich operacji
   - Dodać pomiar czasu wykonania

## Wnioski

1. Python jest znacznie lepiej przystosowany do obliczeń silni niż Pascal
2. Główne ograniczenia w Pythonie to:
   - Limit rekurencji (dla metody rekurencyjnej)
   - Dostępna pamięć (dla bardzo dużych liczb)
3. Dla praktycznych zastosowań Python może obsłużyć znacznie większe wartości silni niż Pascal