program Kwadraty_szesciany;

procedure Wariant1;
var
  i: integer;
  x, x2, x3: real;
begin
  x := 0;
  writeln('Petla for');
  writeln(' x x2 x3');
  for i := 0 to 9 do
  begin
    x2 := x * x;
    x3 := x * x * x;
    writeln(x:7:2, x2:7:2, x3:7:2);
    x := x + 0.1;
  end;
end;

procedure Wariant2;
var
  x, x2, x3: real;
begin
  x := 0;
  writeln('Petla repeat');
  writeln(' x x2 x3');
  repeat
    x2 := x * x;
    x3 := x * x * x;
    writeln(x:7:2, x2:7:2, x3:7:2);
    x := x + 0.1;
  until x > 0.9;
end;

procedure Wariant3;
var
  x, x2, x3: real;
begin
  x := 0;
  writeln('Petla while');
  writeln(' x x2 x3');
  while x < 0.9 do
  begin
    x2 := x * x;
    x3 := x * x * x;
    writeln(x:7:2, x2:7:2, x3:7:2);
    x := x + 0.1;
  end;
end;

begin
  writeln('Kwadraty i szesciany');
  Wariant1;
  Wariant2;
  Wariant3;
  readln;
end.