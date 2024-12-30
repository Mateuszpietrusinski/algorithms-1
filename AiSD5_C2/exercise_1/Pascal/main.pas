program RownanieKwadratowe;

procedure CzytajDane(var a, b, c: real);
begin
  writeln('Czytaj: a, b, c');
  write('a: ');
  readln(a);
  write('b: ');
  readln(b);
  write('c: ');
  readln(c);
end;

function ObliczRownanieDelta(a, b, c: real; var x1, x2: real): boolean;
var
  Delta: real;
begin
  Delta := b * b - 4 * a * c;
  if Delta > 0 then
  begin
    x1 := (-b - sqrt(Delta)) / (2 * a);
    x2 := (-b + sqrt(Delta)) / (2 * a);
    ObliczRownanieDelta := TRUE;
  end
  else if Delta = 0 then
  begin
    x1 := -b / (2 * a);
    x2 := x1;
    ObliczRownanieDelta := TRUE;
  end
  else
    ObliczRownanieDelta := FALSE;
end;

procedure PiszWyniki(x1, x2: real; CzyPisac: boolean);
begin
  writeln('Wyniki obliczen');
  if CzyPisac then
  begin
    if x1 <> x2 then
    begin
      writeln('Dwa pierwiastki: x1 = ', x1:6:2, ', x2 = ', x2:6:2);
    end
    else
    begin
      writeln('Jeden pierwiastek: x = ', x1:6:2);
    end;
  end
  else
    writeln('Brak rozwiazan.');
end;

procedure Rownanie;
var
  a, b, c, x, x1, x2: real;
  CzyJestRozwiazanie: boolean;
begin
  CzytajDane(a, b, c);
  if a = 0 then
  begin
    if b <> 0 then
    begin
      x := -c / b;
      writeln('To jest rownanie liniowe, x = ', x:6:2);
    end
    else
      writeln('To nie jest rownanie.');
  end
  else
  begin
    CzyJestRozwiazanie := ObliczRownanieDelta(a, b, c, x1, x2);
    PiszWyniki(x1, x2, CzyJestRozwiazanie);
  end;
end;

begin
  writeln('Rozwiazanie rownania kwadratowego');
  Rownanie;
end.