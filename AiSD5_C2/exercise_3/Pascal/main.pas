program Suma_cyfr_liczby;

function CzytajLiczbe: integer;
var
  Liczba: integer;
begin
    writeln;
    writeln('Oblicznaie sumy cyfr liczby calkowitej');
    write('Podaj liczbe:'); readln(Liczba);
    CzytajLiczbe:=Liczba;
end;

function SumaCyfr(Liczba: integer): integer;
var
  Suma: integer;
begin
    Suma := 0;
    repeat
        Suma := Suma + ( Liczba mod 10 );
        Liczba := Liczba div 10;
    until Liczba = 0;
    SumaCyfr := Suma;
end;

procedure PiszSume(Liczba, SumaCyfr: integer);
begin
    writeln('Suma cyfr liczby ', Liczba, ' wynosi ', SumaCyfr);
end;

procedure SumaCyfrLiczby;
var
  liczba, suma: integer;
begin
    Liczba:=CzytajLiczbe;
    Suma :=SumaCyfr(liczba);
    PiszSume(Liczba, Suma)
end;

begin
SumaCyfrLiczby;
readln;
end.