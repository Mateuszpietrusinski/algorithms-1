# Wyjaśnienie różnicy między sumą a iloczynem

Różnica między wartością sumy a iloczynem wynika z kilku kluczowych czynników związanych z arytmetyką zmiennoprzecinkową w komputerach:

## 1. Ograniczona precyzja

- Typ `single` w Pascalu przechowuje liczby zmiennoprzecinkowe z ograniczoną precyzją (około 7-8 cyfr znaczących)
- Każda operacja arytmetyczna może wprowadzać małe błędy zaokrągleń

## 2. Akumulacja błędów

- W przypadku sumowania, błędy zaokrągleń akumulują się przy każdej iteracji pętli
- Wykonujemy 1000000 operacji dodawania, gdzie każda może wprowadzić mały błąd
- Te małe błędy sumują się, prowadząc do większego błędu końcowego

## 3. Bezpośrednie mnożenie vs. iteracyjne sumowanie

- Iloczyn `n * s` wykonuje tylko jedną operację arytmetyczną
- Sumowanie wykonuje milion operacji, każda z potencjalnym błędem
- Dlatego iloczyn jest zazwyczaj dokładniejszy niż suma iteracyjna

## 4. Kolejność operacji

- W przypadku sumowania, kolejność wykonywania operacji wpływa na wynik końcowy
- Każde dodanie małej liczby do dużej może prowadzić do utraty precyzji

## Jak testować program

1. Skompiluj i uruchom program
2. Sprawdź wyniki dla różnych wartości `s` (możesz zmodyfikować stałą)
3. Zwróć uwagę na różnicę między sumą a iloczynem
4. Eksperymentuj z różnymi wartościami `n` aby zaobserwować, jak wielkość różnicy zmienia się wraz z liczbą iteracji

## Przykładowe wyniki

Wyniki mogą się różnić w zależności od kompilatora i platformy:

```
Wyniki obliczeń:
1) Suma      = 1234567.87500000
2) Iloczyn   = 1234567.89000000
3) Różnica   = 0.01500000
```

Jest to klasyczny przykład pokazujący, dlaczego w obliczeniach numerycznych ważne jest zrozumienie ograniczeń arytmetyki zmiennoprzecinkowej i wybór odpowiednich metod obliczeniowych w zależności od wymagań dokładności.