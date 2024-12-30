program Silnia;

{ Deklaracje wyprzedzające funkcji i procedur }
function WczytajLiczbe: Int64; forward;
function SilniaRekurencyjna(n: Int64): Int64; forward;
function SilniaIteracyjna(n: Int64): Int64; forward;
procedure WyswietlWyniki(iteracyjna, rekurencyjna: Int64); forward;
procedure Kontroler; forward;

{ Funkcja do wczytywania i walidacji liczby wejściowej }
function WczytajLiczbe: Int64;
var
    n: Int64;
    kod: Integer;
    s: string;
begin
    repeat
        Write('Podaj nieujemną liczbę do obliczenia silni: ');
        ReadLn(s);
        Val(s, n, kod);
        
        if (kod <> 0) or (n < 0) then
            WriteLn('Proszę podać prawidłową liczbę nieujemną!');
            
    until (kod = 0) and (n >= 0);
    
    WczytajLiczbe := n;
end;

{ Obliczanie silni metodą rekurencyjną }
function SilniaRekurencyjna(n: Int64): Int64;
begin
    { Warunek bazowy: dla n = 0 zwracamy 1 }
    if n = 0 then
        SilniaRekurencyjna := 1
    else
        { Przypadek rekurencyjny: n! = n * (n-1)! }
        SilniaRekurencyjna := n * SilniaRekurencyjna(n - 1);
end;

{ Obliczanie silni metodą iteracyjną }
function SilniaIteracyjna(n: Int64): Int64;
var
    wynik: Int64;
    i: Int64;
begin
    { Inicjalizacja wyniku jako 1 (uwzględnia przypadek n = 0) }
    wynik := 1;
    
    { Mnożenie liczb od 1 do n }
    for i := 1 to n do
        wynik := wynik * i;
        
    SilniaIteracyjna := wynik;
end;

{ Wyświetlanie wyników z odpowiednim formatowaniem }
procedure WyswietlWyniki(iteracyjna, rekurencyjna: Int64);
begin
    WriteLn('Silnia iteracyjnie:   ', iteracyjna);
    WriteLn('Silnia rekurencyjnie: ', rekurencyjna);
end;

{ Procedura sterująca }
procedure Kontroler;
var
    n: Int64;
    wynikIteracyjny, wynikRekurencyjny: Int64;
begin
    { Wczytaj dane wejściowe }
    n := WczytajLiczbe;
    
    { Oblicz silnię obiema metodami }
    wynikIteracyjny := SilniaIteracyjna(n);
    wynikRekurencyjny := SilniaRekurencyjna(n);
    
    { Wyświetl wyniki }
    WyswietlWyniki(wynikIteracyjny, wynikRekurencyjny);
end;

{ Program główny }
begin
    Kontroler;
end.