# Task 2: Rozwiazania

## Linki do plików z rozwiązanimi
* [Pascal](./Pascal/main.pas)
* [Python](./Python/main.py) 

## Test poprawności programu
Program sprawdza czy podany rok jest przestępny według następujących warunków:
- Jest podzielny przez 400 (jest przestępny)
- Jest podzielny przez 4 i niepodzielny przez 100 (jest przestępny)
- W pozostałych przypadkach rok nie jest przestępny

### Scenariusze i przykładowe wartości

#### Scenariusz 1: Rok podzielny przez 400
Testujemy rok, który jest podzielny przez 400 - powinien być rokiem przestępnym.

##### Dane wejściowe:
```text
2000
```

###### Oczekiwane wyniki:
**Rok jest przestępny**

###### Rezultat:
Python:
```text
Wprowadz rok do sprawdzenia: 2000
Rok 2000 jest rokiem przestepnym.
```

Pascal:
```text
Wprowadz rok do sprawdzenia: 2000
Rok 2000 jest rokiem przestepnym.
```
---

#### Scenariusz 2: Rok podzielny przez 4 i niepodzielny przez 100
Testujemy rok, który jest podzielny przez 4 ale nie przez 100 - powinien być rokiem przestępnym.

##### Dane wejściowe:
```text
2024
```

###### Oczekiwane wyniki:
**Rok jest przestępny**

###### Rezultat:
Python:
```text
Wprowadz rok do sprawdzenia: 2024
Rok 2024 jest rokiem przestepnym.
```
Pascal:
```text
Wprowadz rok do sprawdzenia: 2024
Rok 2024 jest rokiem przestepnym.
```
---

#### Scenariusz 3: Rok podzielny przez 100 ale nie przez 400
Testujemy rok, który jest podzielny przez 100 ale nie przez 400 - nie powinien być rokiem przestępnym.

##### Dane wejściowe:
```text
2100
```

###### Oczekiwane wyniki:
**Rok nie jest przestępny**

###### Rezultat:
Python:
```text
Wprowadz rok do sprawdzenia: 2100
Rok 2100 jest rokiem przestepnym.
```
Pascal:
```text
Wprowadz rok do sprawdzenia: 2100
Rok 2100 jest rokiem przestepnym.
```
---

#### Scenariusz 4: Rok niepodzielny przez 4
Testujemy rok, który nie jest podzielny przez 4 - nie powinien być rokiem przestępnym.

##### Dane wejściowe:
```text
2023
```

###### Oczekiwane wyniki:
**Rok nie jest przestępny**

###### Rezultat:
Python:
```text
Wprowadz rok do sprawdzenia: 2023
Rok 2023 nie jest rokiem przestepnym.
```
Pascal:
```text
Wprowadz rok do sprawdzenia: 2023
Rok 2023 nie jest rokiem przestepnym.
```
---