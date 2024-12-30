# Analiza porównawcza wydajności obliczania silni

## Wyniki pomiarów

### Pascal
```
Argument funkcji silnia: 18
Liczba powtórzeń: 10000000
Czas obliczeń (metoda iteracyjna): 0.498 sekund
Czas obliczeń (metoda rekurencyjna): 0.425 sekund
Metoda iteracyjna jest wolniejsza o 1.17 razy
```

### Python
```
Argument funkcji silnia: 18
Liczba powtórzeń: 10000000
Czas obliczeń (metoda iteracyjna): 4.354 sekund
Czas obliczeń (metoda rekurencyjna): 8.614 sekund
Metoda rekurencyjna jest wolniejsza o 1.98 razy
```

## Różnice między metodami w ramach jednego języka

### Pascal
W przypadku Pascala metoda rekurencyjna okazała się nieznacznie szybsza od iteracyjnej (o około 17%). Jest to dość nietypowy wynik, który może być związany z:

1. Optymalizacją kompilatora:
   - Free Pascal może szczególnie dobrze optymalizować wywołania rekurencyjne
   - Kompilator może generować bardziej efektywny kod maszynowy dla prostych funkcji rekurencyjnych

2. Architekturą procesora:
   - Na procesorach ARM (M1) wywołania rekurencyjne mogą być bardzo efektywne dzięki dużej liczbie rejestrów
   - Zaawansowany predyktor skoków może lepiej radzić sobie z przewidywalnym wzorcem wywołań rekurencyjnych

### Python
W Pythonie obserwujemy bardziej typowy wzorzec - metoda rekurencyjna jest prawie dwukrotnie wolniejsza od iteracyjnej. Wynika to z:

1. Narzutu interpretera:
   - Każde wywołanie rekurencyjne generuje nową ramkę stosu w interpreterze
   - Python ma limit głębokości rekursji i musi wykonywać dodatkowe sprawdzenia

2. Dynamicznej natury języka:
   - Python musi wykonywać więcej operacji w czasie wykonania
   - Brak optymalizacji na poziomie kodu maszynowego

## Porównanie między językami

1. Ogólna wydajność:
   - Pascal jest znacząco szybszy od Pythona (8-20 razy)
   - Metoda iteracyjna: Pascal 0.498s vs Python 4.354s (około 8.7 razy szybszy)
   - Metoda rekurencyjna: Pascal 0.425s vs Python 8.614s (około 20.3 razy szybszy)

2. Przyczyny różnic:
   - Kompilacja vs Interpretacja:
     - Pascal jest językiem kompilowanym do kodu maszynowego
     - Python jest językiem interpretowanym z dodatkowym narzutem JIT
   
   - Zarządzanie typami:
     - Pascal: statyczne typowanie, bezpośrednie operacje na typach maszynowych
     - Python: dynamiczne typowanie, overhead związany z kontrolą typów w runtime
   
   - Optymalizacje:
     - Pascal: optymalizacje na poziomie kompilatora i kodu maszynowego
     - Python: ograniczone możliwości optymalizacji ze względu na dynamiczną naturę języka

3. Wzorce wydajności:
   - Pascal wykazuje nietypowy wzorzec z szybszą rekursją
   - Python pokazuje typowy wzorzec z szybszą iteracją
   - Różnice między metodami są bardziej wyraźne w Pythonie (98%) niż w Pascalu (17%)

## Wnioski

1. Wybór języka ma większy wpływ na wydajność niż wybór metody (iteracyjna vs rekurencyjna)
2. Pascal, jako język kompilowany, oferuje znacząco lepszą wydajność w obliczeniach numerycznych
3. W Pythonie należy preferować podejście iteracyjne dla lepszej wydajności
4. Architektura sprzętowa (ARM M1) może mieć istotny wpływ na względną wydajność różnych podejść do implementacji