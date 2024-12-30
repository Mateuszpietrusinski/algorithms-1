
## Diagram
```mermaid
flowchart TD
    %% Metoda iteracyjna
    subgraph metoda_iteracyjna["Metoda iteracyjna"]
        A1([Start]) --> B1[/"Czytaj: a, n"/]
        B1 --> C1[wynik = 1]
        C1 --> D1[licznik = 0]
        D1 --> E1{"n = 0?"}
        E1 -->|Tak| G1[/"Pisz: wynik, licznik"/]
        E1 -->|Nie| F1["wynik = wynik * a\nlicznik = licznik + 1"]
        F1 --> H1["n = n - 1"]
        H1 --> E1
        G1 --> I1([Stop])
    end

    %% Metoda z podnoszeniem do kwadratu
    subgraph metoda_kwadratowa["Metoda z podnoszeniem do kwadratu"]
        A2([Start]) --> B2[/"Czytaj: a, n"/]
        B2 --> C2[wynik = 1]
        C2 --> D2[licznik = 0]
        D2 --> E2{"n = 0?"}
        E2 -->|Tak| G2[/"Pisz: wynik, licznik"/]
        E2 -->|Nie| F2{"n mod 2 = 1?"}
        F2 -->|Tak| H2["wynik = wynik * a\nlicznik = licznik + 1"]
        F2 -->|Nie| I2["a = a * a\nlicznik = licznik + 1"]
        H2 --> J2["n = n div 2"]
        I2 --> J2
        J2 --> E2
        G2 --> K2([Stop])
    end
```

## Omówienie wyników

> Zadanie: Potwierdź, podając przykłady, w jakim stopniu użycie podnoszenia liczby do kwadratu ograniczyło liczbę mnożeń w procedurze.

```text
Dla n = 8:
```

Metody klasyczne (iteracyjna i rekurencyjna): 8 mnożeń
Metoda kwadratowa iteracyjna: 5 mnożeń
Metoda kwadratowa rekurencyjna: 4 mnożenia
Redukcja: z 8 do 4 mnożeń (50% redukcja)

```text
Dla n = 15:
```

Metody klasyczne: 15 mnożeń
Metoda kwadratowa iteracyjna: 8 mnożeń
Metoda kwadratowa rekurencyjna: 7 mnożeń
Redukcja: z 15 do 7 mnożeń (53% redukcja)