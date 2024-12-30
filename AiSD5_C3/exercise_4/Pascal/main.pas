program SumaCyfrDwiemetody;

{ Deklaracje wyprzedzające }
function CzytajLiczbe: integer; forward;
function SumaCyfrIteracyjnie(Liczba: integer): integer; forward;
function SumaCyfrRekurencyjnie(Liczba: integer): integer; forward;
procedure WyswietlWyniki(Liczba, SumaIteracyjna, SumaRekurencyjna: integer); forward;
procedure Kontroler; forward;

{ Funkcja do wczytywania liczby }
function CzytajLiczbe: integer;
var
    Liczba: integer;
begin
    writeln;
    writeln('Obliczanie sumy cyfr liczby calkowitej');
    write('Podaj liczbe: '); 
    readln(Liczba);
    CzytajLiczbe := Liczba;
end;

{ Funkcja obliczająca sumę cyfr metodą iteracyjną }
function SumaCyfrIteracyjnie(Liczba: integer): integer;
var
    Suma: integer;
begin
    Suma := 0;
    repeat
        Suma := Suma + (Liczba mod 10);
        Liczba := Liczba div 10;
    until Liczba = 0;
    SumaCyfrIteracyjnie := Suma;
end;

{ Funkcja obliczająca sumę cyfr metodą rekurencyjną }
function SumaCyfrRekurencyjnie(Liczba: integer): integer;
begin
    if Liczba = 0 then
        SumaCyfrRekurencyjnie := 0
    else
        SumaCyfrRekurencyjnie := (Liczba mod 10) + SumaCyfrRekurencyjnie(Liczba div 10);
end;

{ Procedura wyświetlająca wyniki }
procedure WyswietlWyniki(Liczba, SumaIteracyjna, SumaRekurencyjna: integer);
begin
    writeln;
    writeln('Dla liczby: ', Liczba);
    writeln('Suma cyfr (metoda iteracyjna):   ', SumaIteracyjna);
    writeln('Suma cyfr (metoda rekurencyjna): ', SumaRekurencyjna);
    
    if SumaIteracyjna = SumaRekurencyjna then
        writeln('Obie metody dały ten sam wynik.')
    else
        writeln('UWAGA: Wyniki są różne!');
end;

{ Procedura sterująca }
procedure Kontroler;
var
    Liczba, SumaIter, SumaRek: integer;
begin
    Liczba := CzytajLiczbe;
    SumaIter := SumaCyfrIteracyjnie(Liczba);
    SumaRek := SumaCyfrRekurencyjnie(Liczba);
    WyswietlWyniki(Liczba, SumaIter, SumaRek);
end;

{ Program główny }
begin
    Kontroler;
    readln;
end.