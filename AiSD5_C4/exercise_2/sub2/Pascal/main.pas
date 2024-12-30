program FloatTypeComparison;

{ Program demonstrujący różnice między typami single i real }

const
  n = 1000000;    { Stała określająca liczbę sumowań }
  s = 1.23456789; { Liczba, która będzie sumowana }

var
  SumaReal: real;     { Zmienna typu real do sumowania }
  IloczynReal: real;  { Zmienna typu real do mnożenia }
  SumaSingle: single; { Zmienna typu single do sumowania }
  IloczynSingle: single; { Zmienna typu single do mnożenia }
  i: longint;        { Zmienna iteracyjna dla pętli }
  RoznicaReal: real;    { Różnica dla typu real }
  RoznicaSingle: single; { Różnica dla typu single }

begin
  { Inicjalizacja zmiennych }
  SumaReal := 0.0;
  SumaSingle := 0.0;
  
  { Obliczenia dla typu real }
  for i := 1 to n do
    SumaReal := SumaReal + s;
  IloczynReal := s * n;
  RoznicaReal := IloczynReal - SumaReal;
  
  { Obliczenia dla typu single }
  for i := 1 to n do
    SumaSingle := SumaSingle + s;
  IloczynSingle := s * n;
  RoznicaSingle := IloczynSingle - SumaSingle;
  
  { Wyświetlenie wyników }
  writeln('Rozmiary typów zmiennych:');
  writeln('SizeOf(single) = ', SizeOf(single), ' bajtów');
  writeln('SizeOf(real)   = ', SizeOf(real), ' bajtów');
  writeln;
  
  writeln('Wyniki dla typu SINGLE:');
  writeln('1) Suma      = ', SumaSingle:20:8);
  writeln('2) Iloczyn   = ', IloczynSingle:20:8);
  writeln('3) Różnica   = ', RoznicaSingle:20:8);
  writeln;
  
  writeln('Wyniki dla typu REAL:');
  writeln('1) Suma      = ', SumaReal:20:8);
  writeln('2) Iloczyn   = ', IloczynReal:20:8);
  writeln('3) Różnica   = ', RoznicaReal:20:8);
  
  { Poczekaj na naciśnięcie klawisza przed zakończeniem }
  writeln;
  writeln('Naciśnij Enter, aby zakończyć...');
  readln;
end.