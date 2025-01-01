program PairwiseSum;

type
    { Definiujemy typ tablicy dla naszych liczb zmiennoprzecinkowych }
    TNumberArray = array of Single;

var
    Numbers: TNumberArray;
    FinalSum, Product, Difference: Single;

{ Procedura wykonująca sumowanie parami }
procedure PairwiseSum(var Arr: TNumberArray; var Sum: Single);
var
    EvenSum, OddSum: Single;
    i: Integer;
begin
    { Inicjalizacja sum częściowych }
    EvenSum := 0.0;
    OddSum := 0.0;
    
    { Obliczanie sum częściowych }
    for i := 0 to Length(Arr) - 1 do
    begin
        { Indeksy parzyste (0, 2, 4, ...) dodajemy do EvenSum }
        if i mod 2 = 0 then
            EvenSum := EvenSum + Arr[i]
        { Indeksy nieparzyste (1, 3, 5, ...) dodajemy do OddSum }
        else
            OddSum := OddSum + Arr[i];
    end;
    
    { Suma końcowa to suma obu sum częściowych }
    Sum := EvenSum + OddSum;
end;

{ Funkcja obliczająca iloczyn elementów tablicy }
function CalculateProduct(var Arr: TNumberArray): Single;
var
    Prod: Single;
    i: Integer;
begin
    Prod := 1.0;
    for i := 0 to Length(Arr) - 1 do
        Prod := Prod * Arr[i];
    CalculateProduct := Prod;
end;

{ Program główny }
begin
    { Inicjalizacja tablicy testowej }
    SetLength(Numbers, 5);
    Numbers[0] := 1.1;
    Numbers[1] := 2.2;
    Numbers[2] := 3.3;
    Numbers[3] := 4.4;
    Numbers[4] := 5.5;
    
    { Obliczanie sumy metodą sumowania parami }
    PairwiseSum(Numbers, FinalSum);
    
    { Obliczanie iloczynu }
    Product := CalculateProduct(Numbers);
    
    { Obliczanie różnicy }
    Difference := Product - FinalSum;
    
    { Wyświetlanie wyników z 10 miejscami po przecinku }
    writeln('Wyniki z dokładnością do 10 miejsc po przecinku:');
    writeln('Suma: ', FinalSum:20:10);
    writeln('Iloczyn: ', Product:20:10);
    writeln('Różnica (Iloczyn - Suma): ', Difference:20:10);
    
    { Oczekiwanie na wciśnięcie klawisza Enter przed zamknięciem }
    writeln;
    writeln('Naciśnij Enter, aby zakończyć...');
    readln;
end.