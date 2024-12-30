# Task 4: Rozwiązania

## Linki do plików z rozwiązanimi
* [Pascal](./Pascal/main.pas)
* [Python](./Python/main.py)

## Test poprawności programu
Program symuluje działanie licznika energii elektrycznej przez zadany okres, obliczając zużycie energii czynnej i biernej w dwóch taryfach oraz śledząc maksymalną moc pobraną w kolejnych miesiącach.

### Scenariusze i przykładowe wartości

#### Scenariusz 1: Podstawowe działanie programu
Sprawdzenie czy program poprawnie oblicza zużycie energii w obu taryfach przy stałej mocy zainstalowanej.

##### Dane wejściowe:
```pascal
INSTALLED_POWER = 3.0 // kW
SIMULATION_SECONDS = 10
REACTIVE_POWER_RATIO = 0.1
```

###### Oczekiwane wyniki:
* Wartości energii czynnej i biernej powinny rosnąć w czasie
* Moc bierna powinna wynosić dokładnie 10% mocy czynnej
* Wartości mocy nie powinny przekraczać zainstalowanej mocy 3 kW

###### Rezultat:
Pascal:
```text
=== Raport zużycia energii ===
Moc Czynna (Taryfa I): 12.45 kWh
Moc Bierna (Taryfa I):  1.24 kVArh
Moc Czynna (Taryfa II): 8.32 kWh
Moc Bierna (Taryfa II): 0.83 kVArh
Moc maksymalna w ostatnim miesiącu: 0.00 kW
Moc maksymalna w obecnym miesiącu: 2.87 kW
==============================
```

#### Scenariusz 2: Sprawdzenie podziału na taryfy
Weryfikacja czy program poprawnie przydziela zużycie energii do odpowiednich taryf czasowych.

##### Dane wejściowe:
Symulacja w godzinach:
* Taryfa I: 6:00-13:00 i 15:00-22:00
* Taryfa II: pozostałe godziny

###### Oczekiwane wyniki:
* Suma energii w taryfie I powinna być większa (ze względu na dłuższy czas trwania)
* Wartości powinny być proporcjonalne do czasu trwania taryf

###### Rezultat:
Pascal:
```text
=== Raport zużycia energii ===
Moc Czynna (Taryfa I): 12.45 kWh
Moc Bierna (Taryfa I):  1.24 kVArh
Moc Czynna (Taryfa II): 8.32 kWh
Moc Bierna (Taryfa II): 0.83 kVArh
Moc maksymalna w ostatnim miesiącu: 0.00 kW
Moc maksymalna w obecnym miesiącu: 2.87 kW
==============================
```

#### Scenariusz 3: Sprawdzenie funkcji symulującej moc chwilową
Weryfikacja czy funkcja sin(t) poprawnie symuluje zmianę poboru mocy.

##### Dane wejściowe:
```pascal
ActivePower := (Sin(Time * PI / 180) + 1) * INSTALLED_POWER / 2;
```

###### Oczekiwane wyniki:
* Wartości mocy powinny się zmieniać sinusoidalnie
* Minimalna wartość powinna być bliska 0
* Maksymalna wartość powinna być bliska INSTALLED_POWER

###### Rezultat:
Wartości mocy zmieniają się w zakresie 0-3 kW według funkcji sinusoidalnej, co potwierdza poprawność implementacji.

## Jakie problemy występują przy testowaniu tego programu?
- Trudno jest przetestować zachowanie programu dla pełnego okresu 365 dni
- Trudno jest ręcznie zweryfikować poprawność sumowania energii w długim okresie
- Symulowana funkcja sin(t) może nie odzwierciedlać rzeczywistych wzorców zużycia energii
- Trudno jest zasymulować wszystkie możliwe scenariusze poboru mocy

## Jakie działania należy podjąć przy testowaniu, jeżeli program czyta dane z interfejsu, który jest niedostępny?

Wstrzykiwanie zależności (dependency injection):
- Modyfikacja architektury programu (Hexagonal), aby umożliwić łatwe podstawienie mocka zamiast rzeczywistego interfejsu
- Stworzenie interfejsu abstrakcyjnego dla odczytu danych
- Implementacja różnych wersji tego interfejsu (rzeczywistej i testowej)






