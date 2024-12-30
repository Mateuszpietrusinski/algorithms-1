program ObliczaniePotegi;

type
    TwynikObliczen = record
        wynik: real;
        licznik: integer;
    end;

{ Metoda iteracyjna }
function PotegaIteracyjnie(a: real; n: integer): TwynikObliczen;
var
    i: integer;
begin
    PotegaIteracyjnie.wynik := 1.0;
    PotegaIteracyjnie.licznik := 0;
    
    for i := 1 to n do
    begin
        PotegaIteracyjnie.wynik := PotegaIteracyjnie.wynik * a;
        PotegaIteracyjnie.licznik := PotegaIteracyjnie.licznik + 1;
    end;
end;

{ Metoda rekurencyjna }
function PotegaRekurencyjnie(a: real; n: integer): TwynikObliczen;
begin
    if n = 0 then
    begin
        PotegaRekurencyjnie.wynik := 1.0;
        PotegaRekurencyjnie.licznik := 0;
    end
    else
    begin
        PotegaRekurencyjnie := PotegaRekurencyjnie(a, n-1);
        PotegaRekurencyjnie.wynik := PotegaRekurencyjnie.wynik * a;
        PotegaRekurencyjnie.licznik := PotegaRekurencyjnie.licznik + 1;
    end;
end;

{ Metoda iteracyjna z podnoszeniem do kwadratu }
function PotegaKwadratowaIteracyjnie(a: real; n: integer): TwynikObliczen;
begin
    PotegaKwadratowaIteracyjnie.wynik := 1.0;
    PotegaKwadratowaIteracyjnie.licznik := 0;
    
    while n > 0 do
    begin
        if (n mod 2 = 1) then
        begin
            PotegaKwadratowaIteracyjnie.wynik := PotegaKwadratowaIteracyjnie.wynik * a;
            PotegaKwadratowaIteracyjnie.licznik := PotegaKwadratowaIteracyjnie.licznik + 1;
        end;
        a := a * a;
        PotegaKwadratowaIteracyjnie.licznik := PotegaKwadratowaIteracyjnie.licznik + 1;
        n := n div 2;
    end;
end;

{ Metoda rekurencyjna z podnoszeniem do kwadratu }
function PotegaKwadratowaRekurencyjnie(a: real; n: integer): TwynikObliczen;
var
    temp: TwynikObliczen;
begin
    if n = 0 then
    begin
        PotegaKwadratowaRekurencyjnie.wynik := 1.0;
        PotegaKwadratowaRekurencyjnie.licznik := 0;
    end
    else if n mod 2 = 0 then
    begin
        temp := PotegaKwadratowaRekurencyjnie(a * a, n div 2);
        PotegaKwadratowaRekurencyjnie.wynik := temp.wynik;
        PotegaKwadratowaRekurencyjnie.licznik := temp.licznik + 1;
    end
    else
    begin
        temp := PotegaKwadratowaRekurencyjnie(a, n - 1);
        PotegaKwadratowaRekurencyjnie.wynik := temp.wynik * a;
        PotegaKwadratowaRekurencyjnie.licznik := temp.licznik + 1;
    end;
end;

{ Procedura wyświetlająca wyniki }
procedure WyswietlWyniki(a: real; n: integer; wynik: TwynikObliczen; metoda: string);
begin
    write(metoda);
    write(': a=', a:4:1);
    write(' n=', n:2);
    write(' wynik=', wynik.wynik:10:1);
    writeln(' licznik=', wynik.licznik);
end;

{ Program główny }
var
    a: real;
    n, i: integer;
    wynik: TwynikObliczen;
begin
    a := 2.0;
    writeln('Porownanie metod obliczania potegi');
    writeln('----------------------------------');
    
    for n := 0 to 15 do
    begin
        writeln;
        writeln('Dla n = ', n, ':');
        
        wynik := PotegaIteracyjnie(a, n);
        WyswietlWyniki(a, n, wynik, 'Metoda iteracyjna        ');
        
        wynik := PotegaRekurencyjnie(a, n);
        WyswietlWyniki(a, n, wynik, 'Metoda rekurencyjna      ');
        
        wynik := PotegaKwadratowaIteracyjnie(a, n);
        WyswietlWyniki(a, n, wynik, 'Metoda kwadr. iter.      ');
        
        wynik := PotegaKwadratowaRekurencyjnie(a, n);
        WyswietlWyniki(a, n, wynik, 'Metoda kwadr. rekur.     ');
    end;
    
    writeln;
    writeln('Nacisnij Enter aby zakonczyc...');
    readln;
end.