program SumowanieZPoprawkami;

type
    { Definiujemy typ tablicy dla naszych liczb zmiennoprzecinkowych }
    TNumberArray = array of Single;

var
    Numbers: TNumberArray;
    FinalSum, Product, Difference: Single;

{ Procedura wykonująca sumowanie z poprawkami }
procedure CorrectedSum(var Arr: TNumberArray; var Sum: Single);
var
    Poprawka, Sumai: Single;
    i: Integer;
begin
    { Inicjalizacja sumy i poprawki }
    Sum := 0.0;
    Poprawka := 0.0;
    
    { Wykonujemy sumowanie z poprawkami }
    for i := 0 to Length(Arr) - 1 do
    begin
        { Obliczamy sumę częściową }
        Sumai := Sum + Arr[i];
        
        { Obliczamy poprawkę:
          - (Sum - Sumai) to błąd zaokrąglenia w bieżącym kroku
          - Arr[i] to aktualny element
          - Poprawka to skumulowany błąd z poprzednich kroków 
        }
        Poprawka := Sum - Sumai + Arr[i] + Poprawka;
        
        { Aktualizujemy sumę }
        Sum := Sumai;
    end;
    
    { Dodajemy skumulowaną poprawkę do końcowej sumy }
    Sum := Sum + Poprawka;
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
    
    { Obliczanie sumy metodą z poprawkami }
    CorrectedSum(Numbers, FinalSum);
    
    { Obliczanie iloczynu }
    Product := CalculateProduct(Numbers);
    
    { Obliczanie różnicy }
    Difference := Product - FinalSum;
    
    { Wyświetlanie wyników z 10 miejscami po przecinku }
    writeln('Wyniki z dokładnością do 10 miejsc po przecinku:');
    writeln('Suma (z poprawkami): ', FinalSum:20:10);
    writeln('Iloczyn: ', Product:20:10);
    writeln('Różnica (Iloczyn - Suma): ', Difference:20:10);
    
    { Oczekiwanie na wciśnięcie klawisza Enter przed zamknięciem }
    writeln;
    writeln('Naciśnij Enter, aby zakończyć...');
    readln;
end.