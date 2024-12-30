# Taks 2: Rozwiazania

## Wyniki
Podaj argument silni (0-20): 18
Podaj liczbę powtórzeń (min. 1): 10000000

Wyniki pomiarów:
---------------
Argument funkcji silnia: 18
Liczba powtórzeń: 10000000
Wartość silni: 6402373705728000
Czas obliczeń (metoda iteracyjna): 0.498 sekund
Czas obliczeń (metoda rekurencyjna): 0.425 sekund
---------------
Metoda iteracyjna jest wolniejsza o 1.17 razy


## Jeżeli czasy obliczeń wykonanych przez program implementujący poszczególne algorytmy różnią się, wyjaśnij dlaczego.
* Kompilator Free Pascal może generować bardziej zoptymalizowany kod dla wywołań rekurencyjnych na architekturze ARM
* Zaawansowany predyktor skoków (branch predictor) w M1 może bardzo efektywnie obsługiwać wzorzec wywołań rekurencyjnych
* M1 może efektywniej przetwarzać wzorzec wywołań rekurencyjnych

Jest to dość nietypowa sytuacja, ponieważ zazwyczaj na większości architektur metoda iteracyjna jest szybsza. Pokazuje to, jak ważne jest testowanie wydajności na konkretnej platformie docelowej, ponieważ różne architektury mogą mieć różne charakterystyki wydajnościowe dla tych samych algorytmów.