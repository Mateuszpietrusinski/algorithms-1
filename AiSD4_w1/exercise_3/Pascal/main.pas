program Rownanie_kwadratowe;

procedure CzytajDane(var a, b, c: real);
begin
  writeln('Podaj wartosc wspolczynnikow rownania kwadratowego');
  write('a: ');
  readln(a);
  write('b: ');
  readln(b);
  write('c: ');
  readln(c);
end;

function ObliczRownanie(a, b, c: real; var x1, x2: real): boolean;
var
  Delta: real;
begin
  Delta := b * b - 4 * a * c;
  if Delta >= 0 then
  begin
    x1 := (-1 * b - sqrt(Delta)) / (2 * a);
    x2 := (-1 * b + sqrt(Delta)) / (2 * a);
    ObliczRownanie := TRUE;
  end
  else
    ObliczRownanie := FALSE;
end;

procedure PiszWyniki(x1, x2: real; CzyPisac: boolean);
begin
  writeln('Wyniki obliczen');
  if CzyPisac then
  begin
    writeln('x1=', x1:6:2);
    writeln('x2=', x2:6:2);
  end
  else
    writeln('Brak rozwiazan.');
end;

procedure Rownanie;
var
  a, b, c, x1, x2: real;
  CzyJestRozwiazanie: boolean;
begin
  CzytajDane(a, b, c);
  CzyJestRozwiazanie := ObliczRownanie(a, b, c, x1, x2);
  PiszWyniki(x1, x2, CzyJestRozwiazanie);
end;

begin
  writeln('Rozwiazanie rownania kwadratowego');
  Rownanie;
  readln;
end.