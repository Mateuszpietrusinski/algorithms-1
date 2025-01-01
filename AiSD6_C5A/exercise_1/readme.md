# Diagramy
`h` - reprezentuje szerokość pojedynczego podprzedziału
## Metoda Prostokątów
```mermaid
graph TD
    Start[("START")]
    Input["Dane wejściowe:
    n - liczba przedziałów
    a - początek przedziału
    b - koniec przedziału
    f(x) - funkcja całkowana"]
    CalcH["Oblicz h = (b-a)/n"]
    InitSum["Inicjalizacja: suma = 0"]
    InitI["Inicjalizacja: i = 0"]
    CheckI{"Czy i < n?"}
    CalcX["Oblicz xi = a + i×h"]
    CalcArea["Oblicz pole = h × f(xi)"]
    AddSum["suma = suma + pole"]
    IncrI["i = i + 1"]
    Return["Zwróć sumę"]
    End[("KONIEC")]

    Start --> Input
    Input --> CalcH
    CalcH --> InitSum
    InitSum --> InitI
    InitI --> CheckI
    CheckI -->|Tak| CalcX
    CalcX --> CalcArea
    CalcArea --> AddSum
    AddSum --> IncrI
    IncrI --> CheckI
    CheckI -->|Nie| Return
    Return --> End

    subgraph Inicjalizacja
        Input
        CalcH
        InitSum
        InitI
    end

    subgraph Obliczenia
        CheckI
        CalcX
        CalcArea
        AddSum
        IncrI
    end

    subgraph Wynik
        Return
    end
```

## Metoda Trapezów
```mermaid
graph TD
    Start[("START")]
    Input["Dane wejściowe:
    n - liczba przedziałów
    a - początek przedziału
    b - koniec przedziału
    f(x) - funkcja całkowana"]
    CalcH["Oblicz h = (b-a)/n"]
    InitSum["Inicjalizacja: suma = (f(a) + f(b))/2"]
    InitI["Inicjalizacja: i = 1"]
    CheckI{"Czy i < n?"}
    CalcX["Oblicz xi = a + i×h"]
    AddSum["suma = suma + f(xi)"]
    IncrI["i = i + 1"]
    MultH["Pomnóż: suma = h × suma"]
    Return["Zwróć sumę"]
    End[("KONIEC")]

    Start --> Input
    Input --> CalcH
    CalcH --> InitSum
    InitSum --> InitI
    InitI --> CheckI
    CheckI -->|Tak| CalcX
    CalcX --> AddSum
    AddSum --> IncrI
    IncrI --> CheckI
    CheckI -->|Nie| MultH
    MultH --> Return
    Return --> End

    subgraph Inicjalizacja
        Input
        CalcH
        InitSum
        InitI
    end

    subgraph Obliczenia
        CheckI
        CalcX
        AddSum
        IncrI
        MultH
    end

    subgraph Wynik
        Return
    end
```

## Metoda Simpsona
```mermaid
graph TD
    Start[("START")]
    Input["Dane wejściowe:
    n - liczba przedziałów
    a - początek przedziału
    b - koniec przedziału
    f(x) - funkcja całkowana"]
    CheckEven{"Czy n jest parzyste?"}
    Error["Błąd: n musi być parzyste"]
    CalcH["Oblicz h = (b-a)/n"]
    InitSum["Inicjalizacja: suma = f(a) + f(b)"]
    InitI["Inicjalizacja: i = 1"]
    CheckI{"Czy i < n?"}
    CheckOdd{"Czy i jest nieparzyste?"}
    Add4["suma += 4×f(a + i×h)"]
    Add2["suma += 2×f(a + i×h)"]
    IncrI["i = i + 1"]
    MultH["Pomnóż: suma = (h/3) × suma"]
    Return["Zwróć sumę"]
    End[("KONIEC")]
    EndError[("KONIEC")]

    Start --> Input
    Input --> CheckEven
    CheckEven -->|Nie| Error
    Error --> EndError
    CheckEven -->|Tak| CalcH
    CalcH --> InitSum
    InitSum --> InitI
    InitI --> CheckI
    CheckI -->|Tak| CheckOdd
    CheckOdd -->|Tak| Add4
    CheckOdd -->|Nie| Add2
    Add4 --> IncrI
    Add2 --> IncrI
    IncrI --> CheckI
    CheckI -->|Nie| MultH
    MultH --> Return
    Return --> End

    subgraph Inicjalizacja
        Input
        CheckEven
        CalcH
        InitSum
        InitI
    end

    subgraph Obliczenia
        CheckI
        CheckOdd
        Add4
        Add2
        IncrI
        MultH
    end

    subgraph Wynik
        Return
    end
```
