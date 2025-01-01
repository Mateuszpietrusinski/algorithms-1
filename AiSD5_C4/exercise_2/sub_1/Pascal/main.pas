program FloatingSumComparison;

{ Program demonstrujący różnice w obliczeniach zmiennoprzecinkowych }

const
  n = 1000000;    { Stała określająca liczbę sumowań }
  s = 1.23456789; { Liczba, która będzie sumowana }

var
  Suma: single;    { Zmienna przechowująca wynik sumowania iteracyjnego }
  Iloczyn: single; { Zmienna przechowująca wynik mnożenia }
  i: longint;      { Zmienna iteracyjna dla pętli }
  Roznica: single; { Zmienna przechowująca różnicę między iloczynem a sumą }

begin
  { Inicjalizacja zmiennej Suma }
  Suma := 0.0;
  
  { Wykonanie sumowania n razy }
  for i := 1 to n do
    Suma := Suma + s;
    
  { Obliczenie iloczynu }
  Iloczyn := s * n;
  
  { Obliczenie różnicy między iloczynem a sumą }
  Roznica := Iloczyn - Suma;
  
  { Wyświetlenie wyników }
  writeln('Wyniki obliczeń:');
  writeln('1) Suma      = ', Suma:15:8);
  writeln('2) Iloczyn   = ', Iloczyn:15:8);
  writeln('3) Różnica   = ', Roznica:15:8);
  
  { Poczekaj na naciśnięcie klawisza przed zakończeniem }
  writeln;
  writeln('Naciśnij Enter, aby zakończyć...');
  readln;
end.