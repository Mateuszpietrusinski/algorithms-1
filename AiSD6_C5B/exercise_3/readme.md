# Porównanie metod numerycznych znajdowania miejsc zerowych funkcji f(x) = x³ - x² - x + 2

## 1. Porównanie dla różnych przedziałów początkowych (ε = 0.0001)

### Test 1: Przedział [-5, 5]
| Metoda    | Miejsce zerowe | Wartość funkcji    | Liczba iteracji |
|-----------|----------------|-------------------|-----------------|
| Newton    | -1.205585      | -8.698100e-05     | 6              |
| Euler     | -1.205570      | -6.146669e-06     | 16             |
| Bisekcja  | -1.205559      | 0.000061          | 17             |

### Test 2: Przedział [-212, 33]
| Metoda    | Miejsce zerowe | Wartość funkcji    | Liczba iteracji |
|-----------|----------------|-------------------|-----------------|
| Newton    | -1.205569      | -6.722657e-09     | 16             |
| Euler     | -1.205570      | -2.149541e-06     | 26             |
| Bisekcja  | -1.205573      | -0.000018         | 21             |

### Test 3: Przedział [-3, 3]
| Metoda    | Miejsce zerowe | Wartość funkcji    | Liczba iteracji |
|-----------|----------------|-------------------|-----------------|
| Newton    | -1.205572      | -1.217744e-05     | 5              |
| Euler     | -1.205569      | 4.224086e-06      | 21             |
| Bisekcja  | -1.205566      | 0.000017          | 12             |

## 2. Porównanie dla różnych dokładności (przedział [-22, 2])

### Test 4: ε = 0.1
| Metoda    | Miejsce zerowe | Wartość funkcji    | Liczba iteracji |
|-----------|----------------|-------------------|-----------------|
| Newton    | -1.206169      | -3.460235e-03     | 9              |
| Euler     | -1.204252      | 7.593611e-03      | 9              |
| Bisekcja  | -1.234375      | -0.170101         | 8              |

### Test 5: ε = 1
| Metoda    | Miejsce zerowe | Wartość funkcji    | Liczba iteracji |
|-----------|----------------|-------------------|-----------------|
| Newton    | -1.233381      | -1.640996e-01     | 8              |
| Euler     | -1.238606      | -1.957426e-01     | 7              |
| Bisekcja  | -1.000000      | 1.000000          | 3              |

## 3. Analiza i wnioski

### Szybkość zbieżności:
1. **Metoda Newtona**:
   - Najszybsza zbieżność (5-16 iteracji)
   - Najmniej wrażliwa na szerokość przedziału
   - Najefektywniejsza dla wysokich dokładności

2. **Metoda Eulera (siecznych)**:
   - Średnia szybkość zbieżności (7-26 iteracji)
   - Może mieć problemy ze zbieżnością dla dużych przedziałów
   - Efektywność spada wraz z szerokością przedziału

3. **Metoda bisekcji**:
   - Najwolniejsza zbieżność (3-21 iteracji)
   - Najbardziej przewidywalna liczba iteracji
   - Gwarantowana zbieżność, ale wolniejsza

### Dokładność wyników:
1. Dla wysokiej dokładności (ε = 0.0001):
   - Wszystkie metody znajdują zbliżone wartości (-1.2055 do -1.2056)
   - Metoda Newtona daje najdokładniejsze wyniki
   - Metoda bisekcji ma największe wahania wartości funkcji

2. Dla niskiej dokładności (ε = 0.1, ε = 1):
   - Znaczące różnice między metodami
   - Metoda Newtona zachowuje najlepszą precyzję
   - Metoda bisekcji daje najmniej dokładne wyniki

### Zalety i wady poszczególnych metod:

#### Metoda Newtona:
✓ Najszybsza zbieżność
✓ Najwyższa dokładność
✗ Wymaga obliczania pochodnej
✗ Może być wrażliwa na wybór punktu startowego

#### Metoda Eulera:
✓ Nie wymaga obliczania pochodnej
✓ Dobra dokładność dla małych przedziałów
✗ Może mieć problemy ze zbieżnością
✗ Wymaga dwóch punktów startowych

#### Metoda bisekcji:
✓ Gwarantowana zbieżność
✓ Prosta implementacja
✗ Najwolniejsza zbieżność
✗ Najmniejsza dokładność dla dużych ε

### Podsumowanie:
1. **Najszybciej zbieżna** jest metoda Newtona - osiąga najlepsze wyniki przy najmniejszej liczbie iteracji.
2. Metoda bisekcji, choć najwolniejsza, jest najbardziej niezawodna i zawsze znajdzie rozwiązanie.
3. Metoda Eulera stanowi kompromis między szybkością a niezawodnością, ale może mieć problemy ze zbieżnością.

Dla rozważanej funkcji f(x) = x³ - x² - x + 2, **metoda Newtona** okazała się najefektywniejsza, oferując najlepszy stosunek szybkości zbieżności do dokładności wyników.