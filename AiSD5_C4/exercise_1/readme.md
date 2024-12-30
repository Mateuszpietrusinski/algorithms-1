# Task 1: Rozwiazanie

## Pascal
## Analiza ograniczeń silni dla typu Int64 w Pascalu

### 1. Największa wartość argumentu dla poprawnego obliczenia silni

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

### 2. Zachowanie programu przy przekroczeniu zakresu Int64

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

### Wnioski

1. Typ Int64 pozwala na bezpieczne obliczenie silni tylko do n=20
2. Dla większych wartości należy:
   - Implementować kontrolę zakresu
   - Rozważyć użycie innych typów danych
   - Zastosować alternatywne metody obliczeniowe

---
## Python
### Wyjaśnienie zachowania zmiennych w języku Python

### Dlaczego możliwe jest obliczenie funkcji silnia dla dużych wartości argumentu?

Python obsługuje liczby całkowite o praktycznie nieograniczonej wielkości dzięki implementacji tzw. "arbitrary-precision arithmetic". Oznacza to, że:

1. Python automatycznie zarządza pamięcią dla liczb całkowitych (integers)
2. Gdy liczba przekracza standardowy rozmiar int, Python automatycznie alokuje więcej pamięci
3. Nie ma standardowego ograniczenia jak w innych językach (np. w C/C++ gdzie int ma typowo 32 lub 64 bity)
4. Jedynym praktycznym ograniczeniem jest dostępna pamięć komputera

W przeciwieństwie do języków takich jak C++ czy Java, gdzie występuje przepełnienie (overflow) przy przekroczeniu maksymalnej wartości typu int, Python dynamicznie dostosowuje ilość pamięci potrzebnej do przechowania dużych liczb.

### Dlaczego mała liczba całkowita zajmuje tak dużą liczbę bajtów?

Mała liczba całkowita w Pythonie zajmuje stosunkowo dużo pamięci (zwykle 28 bajtów na systemach 64-bitowych) z kilku powodów:

1. **Overhead obiektowy:**
   - W Pythonie wszystko jest obiektem, nawet proste liczby
   - Każdy obiekt zawiera dodatkowe informacje jak:
     - Licznik referencji (reference count)
     - Wskaźnik do typu obiektu
     - Flagi i metadane

2. **Struktura PyObject:**
   - Każda liczba całkowita jest reprezentowana jako struktura PyObject
   - Zawiera ona:
     - Nagłówek obiektu (object header)
     - Wartość liczby
     - Dodatkowe pola wymagane przez interpreter

3. **Optymalizacja dla małych liczb:**
   - Python stosuje technikę "small integer caching" dla często używanych małych liczb
   - Liczby z zakresu [-5, 256] są zwykle współdzielone między zmiennymi
   - To zwiększa podstawowy rozmiar obiektu, ale optymalizuje używanie pamięci w praktyce

Ta dodatkowa złożoność jest ceną za elastyczność i wygodę programowania w Pythonie. Dzięki temu otrzymujemy:
- Automatyczne zarządzanie pamięcią
- Dynamiczne typowanie
- Brak ograniczeń na wielkość liczb
- Łatwiejsze debugowanie i introspection