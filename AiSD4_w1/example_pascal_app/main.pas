{ Program demonstruje podstawowe elementy
  składni i struktur języka Pascal }
program Pascal;

type
  tDniTygodnia = (pn, wt, sr, cz, pt, so, nd); // deklaracja globalnego typu

const
  cPi = 3.1415926526; // deklaracja stałej globalnej

var
  ZmiennaGlobalna: integer; // deklaracja zmiennej globalnej

function Max(x1, x2: integer): integer; // funkcja zwracająca wartość
begin
  if x1 > x2 then
    Max := x1
  else
    Max := x2;
end;

procedure Min(x1, x2: integer; var Xmin: integer); // procedura
begin
  if x1 < x2 then // instrukcja warunkowa
  begin
    Xmin := x1;
    ZmiennaGlobalna := x1;
  end
  else
  begin
    Xmin := x2;
    ZmiennaGlobalna := x2;
  end;
end;

procedure Przyklad1;
const
  cE = 2.718281; // deklaracja stałej lokalnej
var
  i: integer; // deklaracje zmiennych lokalnych
  R, R1, R2: real;
  S: string;
begin
  R := 0.0;
  for i := 1 to 10 do // pętla for inkrementacja zmiennej sterującej
  begin
    R1 := R1 + i * cPi;
  end;
  writeln('R1: ', R1);

  for i := 10 downto 1 do // pętla for dekrementacja zmiennej sterującej
  begin
    R2 := R2 - i * cPi;
  end;
  writeln('R2: ', R2);

  i := 33;
  S := '';
  while i <= 45 do // pętla while - warunek sprawdzany na początku pętli
  begin
    S := S + chr(i);
    i := i + 1;
  end;
  writeln('S: ', S);

  i := 0;
  repeat // pętla repeat - warunek sprawdzany na końcu pętli
    R := i * cE;
    i := i + 1;
  until i >= 10;
  writeln('R: ', R);
  writeln('ZmiennaGlobalna: ', ZmiennaGlobalna);
end;

procedure Przyklad2;
var
  Liczba: integer;
  Dzien: tDniTygodnia;
  TabDniTygodnia: array[tDniTygodnia] of string;
begin
  Liczba := Max(1, 2);
  writeln('Liczba: ', Liczba);
  Min(1, 2, Liczba);
  writeln('Liczba: ', Liczba);

  for Dzien := pn to nd do
    case Dzien of // instrukcja wyboru case
      pn: TabDniTygodnia[Dzien] := 'poniedzia'#179'ek'; // kodowanie Windows-1250
      wt: TabDniTygodnia[Dzien] := 'wtorek';
      sr: TabDniTygodnia[Dzien] := #156'roda'; // kodowanie Windows-1250
      cz: TabDniTygodnia[Dzien] := 'czwartek';
      pt: TabDniTygodnia[Dzien] := 'piątek';
      so: TabDniTygodnia[Dzien] := 'sobota';
      nd: TabDniTygodnia[Dzien] := 'niedziela';
    else
      Liczba := 0; // użycie else jest opcjonalne
    end;

  for Dzien := nd downto pn do
  begin
    writeln(ord(Dzien), ': ', TabDniTygodnia[Dzien]);
  end;
end;

var
  Stop: string;

begin // Blok startowy programu
  Przyklad1;
  Przyklad2;
  write('Nacisnij Enter by zakonczyc program');
  readln(Stop);
end. // Kropka kończy program