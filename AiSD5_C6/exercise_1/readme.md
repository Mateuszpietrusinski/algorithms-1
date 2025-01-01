# 📊 Analiza Porównawcza Algorytmów Sortowania

## 1. Wprowadzenie
W analizie porównano pięć różnych algorytmów sortowania, testując je na dwóch zestawach danych:
- Dane nieuporządkowane (losowe)
- Dane wstępnie posortowane

## 2. Analiza Wyników dla Danych Nieuporządkowanych

### Liczba porównań:
1. **Sortowanie szybkie**: 63 porównania
   - Najefektywniejszy algorytm pod względem liczby porównań
   - Wykorzystuje strategię "dziel i zwyciężaj"

2. **Proste wstawianie**: 127 porównań
   - Drugi najlepszy wynik
   - Dobra wydajność dla małych zbiorów danych

3. **Wstawianie ze strażnikiem**: 129 porównań
   - Podobna wydajność do prostego wstawiania
   - Niewielki narzut związany z obsługą strażnika

4. **Sortowanie bąbelkowe**: 189 porównań
   - Znacznie więcej porównań niż poprzednie metody
   - Typowa cecha tego algorytmu

5. **Proste wybieranie**: 190 porównań
   - Największa liczba porównań
   - Zawsze wykonuje pełny przebieg przez tablicę

### Liczba zamian:
1. **Proste wybieranie**: 16 zamian
   - Najmniejsza liczba zamian
   - Efektywne pod względem operacji przenoszenia danych

2. **Sortowanie szybkie**: 20 zamian
   - Bardzo dobra wydajność
   - Zoptymalizowane operacje zamiany

3. **Sortowanie bąbelkowe**: 110 zamian
   - Znaczna liczba zamian
   - Charakterystyczna cecha algorytmu bąbelkowego

4. **Proste wstawianie i Wstawianie ze strażnikiem**: 127 zamian
   - Najwięcej operacji zamiany
   - Wynika z natury algorytmu wstawiania

## 3. Analiza Wyników dla Danych Posortowanych

### Kluczowe obserwacje:
1. **Algorytmy wstawiania i bąbelkowe**:
   - Tylko 19 porównań
   - Brak zamian
   - Optymalna wydajność dla posortowanych danych

2. **Sortowanie przez wybieranie i szybkie**:
   - 190 porównań
   - Brak zamian
   - Nie wykorzystują faktu, że dane są już posortowane

## 4. Wnioski Końcowe

### Efektywność algorytmów:
1. **Sortowanie szybkie** (QuickSort):
   - Najlepszy wybór dla losowych danych
   - Najniższa liczba porównań w przypadku danych nieuporządkowanych
   - Słabsza wydajność dla danych posortowanych

2. **Algorytmy wstawiania**:
   - Bardzo dobre dla małych zbiorów danych
   - Doskonała wydajność dla danych prawie posortowanych
   - Strażnik nie wnosi znaczącej poprawy wydajności

3. **Sortowanie bąbelkowe**:
   - Prosta implementacja, ale niska wydajność
   - Duża liczba zamian dla danych nieuporządkowanych
   - Efektywne tylko dla danych prawie posortowanych

4. **Proste wybieranie**:
   - Stała liczba porównań niezależnie od uporządkowania danych
   - Najmniejsza liczba zamian dla danych nieuporządkowanych
   - Nie adaptuje się do stopnia uporządkowania danych

### Rekomendacje:
1. **Dla małych zbiorów danych**:
   - Proste wstawianie lub wstawianie ze strażnikiem
   - Prosta implementacja i dobra wydajność

2. **Dla średnich i dużych zbiorów**:
   - Sortowanie szybkie (QuickSort)
   - Najlepsza ogólna wydajność

3. **Dla prawie posortowanych danych**:
   - Algorytmy wstawiania
   - Sortowanie bąbelkowe

4. **Gdy liczy się minimalna liczba zamian**:
   - Sortowanie przez wybieranie
   - Sortowanie szybkie