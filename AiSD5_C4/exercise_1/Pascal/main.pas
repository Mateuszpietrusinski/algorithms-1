program SilniaZLimitami;

{ Deklaracje wyprzedzające funkcji i procedur }
function WczytajLiczbe: Int64; forward;
function SilniaRekurencyjna(n: Int64): Int64; forward;
function SilniaIteracyjna(n: Int64): Int64; forward;
procedure WyswietlWyniki(n: Int64; iteracyjna, rekurencyjna: Int64); forward;
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
            WriteLn('Proszę podać prawidłową liczbę nieujemną!')
        else if n > 20 then
            WriteLn('Uwaga: Wartości powyżej 20 spowodują przekroczenie zakresu Int64!');
            
    until (kod = 0) and (n >= 0);
    
    WczytajLiczbe := n;
end;

{ Obliczanie silni metodą rekurencyjną }
function SilniaRekurencyjna(n: Int64): Int64;
begin
    if n = 0 then
        SilniaRekurencyjna := 1
    else
        SilniaRekurencyjna := n * SilniaRekurencyjna(n - 1);
end;

{ Obliczanie silni metodą iteracyjną z wyświetlaniem kroków pośrednich }
function SilniaIteracyjna(n: Int64): Int64;
var
    wynik: Int64;
    i: Int64;
begin
    wynik := 1;
    WriteLn('Kroki obliczeniowe:');
    for i := 1 to n do
    begin
        wynik := wynik * i;
        WriteLn(i, '! = ', wynik);
    end;
    
    SilniaIteracyjna := wynik;
end;

{ Wyświetlanie wyników z odpowiednim formatowaniem }
procedure WyswietlWyniki(n: Int64; iteracyjna, rekurencyjna: Int64);
begin
    WriteLn;
    WriteLn('Dla n = ', n, ':');
    WriteLn('Silnia iteracyjnie:   ', iteracyjna);
    WriteLn('Silnia rekurencyjnie: ', rekurencyjna);
    if n > 20 then
        WriteLn('UWAGA: Wyniki są nieprawidłowe ze względu na przekroczenie zakresu Int64!');
end;

{ Procedura sterująca }
procedure Kontroler;
var
    n: Int64;
    wynikIteracyjny, wynikRekurencyjny: Int64;
begin
    n := WczytajLiczbe;
    
    wynikIteracyjny := SilniaIteracyjna(n);
    wynikRekurencyjny := SilniaRekurencyjna(n);
    
    WyswietlWyniki(n, wynikIteracyjny, wynikRekurencyjny);
end;

{ Program główny }
begin
    WriteLn('Program do obliczania silni z kontrolą zakresu Int64');
    WriteLn('Maksymalna poprawna wartość to 20');
    WriteLn;
    
    Kontroler;
end.