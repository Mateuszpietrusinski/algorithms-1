# Porównanie metod obliczania sumy cyfr

## Analiza złożoności kodu

### Metoda Iteracyjna
```pascal
function SumaCyfrIteracyjnie(Liczba: integer): integer;
var
    Suma: integer;
begin
    Suma := 0;
    repeat
        Suma := Suma + (Liczba mod 10);
        Liczba := Liczba div 10;
    until Liczba = 0;
    SumaCyfrIteracyjnie := Suma;
end;
```

### Metoda Rekurencyjna
```pascal
function SumaCyfrRekurencyjnie(Liczba: integer): integer;
begin
    if Liczba = 0 then
        SumaCyfrRekurencyjnie := 0
    else
        SumaCyfrRekurencyjnie := (Liczba mod 10) + SumaCyfrRekurencyjnie(Liczba div 10);
end;
```

## Porównanie metod pod względem komplikacji kodu

### 1. Długość kodu
- Metoda iteracyjna wymaga więcej linii kodu (7 linii)
- Metoda rekurencyjna jest krótsza (6 linii)
- Metoda rekurencyjna nie wymaga deklaracji zmiennych pomocniczych

### 2. Złożoność logiczna
- Metoda iteracyjna:
  - Wykorzystuje zmienną pomocniczą (Suma)
  - Zawiera pętlę repeat-until
  - Operacje są liniowe i przewidywalne
  
- Metoda rekurencyjna:
  - Nie wymaga zmiennych pomocniczych
  - Wykorzystuje warunek bazowy i przypadek rekurencyjny
  - Wymaga zrozumienia koncepcji rekurencji

### 3. Czytelność kodu

#### Metoda iteracyjna jest bardziej czytelna dla początkujących programistów ponieważ:
- Proces jest widoczny "krok po kroku"
- Wykorzystuje podstawowe konstrukcje programistyczne (pętla, zmienne)
- Łatwiej jest śledzić przepływ danych
- Przypomina sposób, w jaki człowiek liczyłby sumę cyfr na papierze

#### Metoda rekurencyjna jest bardziej elegancka matematycznie ponieważ:
- Kod jest bardziej zwięzły
- Rozwiązanie jest bliższe matematycznej definicji problemu
- Nie wymaga zarządzania stanem (zmiennymi pomocniczymi)
- Bazuje na dekompozycji problemu na mniejsze podproblemy

## Wnioski

1. **Krótkość kodu**: 
   - Metoda rekurencyjna wygrywa, będąc bardziej zwięzłą

2. **Komplikacja**:
   - Metoda iteracyjna jest prostsza koncepcyjnie
   - Metoda rekurencyjna wymaga głębszego zrozumienia programowania

3. **Czytelność**:
   - Dla początkujących: metoda iteracyjna jest bardziej czytelna
   - Dla doświadczonych programistów: metoda rekurencyjna może być bardziej czytelna ze względu na jej elegancję i matematyczne podejście