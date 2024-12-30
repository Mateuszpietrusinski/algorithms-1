program SilniaPomiarCzasu;

uses CRT, math, sysUtils;

{ Deklaracje wyprzedzające funkcji i procedur }
function WczytajLiczbe(komunikat: string; minWartosc, maxWartosc: Int64): Int64; forward;
function SilniaRekurencyjna(n: Int64): Int64; forward;
function SilniaIteracyjna(n: Int64): Int64; forward;
procedure WykonajPomiaryCzasu(n, liczbaPowtorzen: Int64); forward;
procedure WyswietlWyniki(n, liczbaPowtorzen: Int64; wartoscSilni: Int64; czasIteracyjny, czasRekurencyjny: Double); forward;
procedure Kontroler; forward;

{ Funkcja do wczytywania i walidacji liczby wejściowej }
function WczytajLiczbe(komunikat: string; minWartosc, maxWartosc: Int64): Int64;
var
    n: Int64;
    kod: Integer;
    s: string;
begin
    repeat
        Write(komunikat);
        ReadLn(s);
        Val(s, n, kod);
        
        if (kod <> 0) or (n < minWartosc) or (n > maxWartosc) then
            WriteLn('Proszę podać liczbę z zakresu [', minWartosc, ', ', maxWartosc, ']');
            
    until (kod = 0) and (n >= minWartosc) and (n <= maxWartosc);
    
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

{ Obliczanie silni metodą iteracyjną }
function SilniaIteracyjna(n: Int64): Int64;
var
    wynik: Int64;
    i: Int64;
begin
    wynik := 1;
    for i := 1 to n do
        wynik := wynik * i;
    SilniaIteracyjna := wynik;
end;

{ Procedura wykonująca pomiary czasu }
procedure WykonajPomiaryCzasu(n, liczbaPowtorzen: Int64);
var
    i: Int64;
    czasStartowy, czasKoncowy: Int64;
    wartoscSilni: Int64;
    czasIteracyjny, czasRekurencyjny: Double;
begin
    { Pomiar czasu dla metody iteracyjnej }
    czasStartowy := GetTickCount64;
    for i := 1 to liczbaPowtorzen do
        wartoscSilni := SilniaIteracyjna(n);
    czasKoncowy := GetTickCount64;
    czasIteracyjny := (czasKoncowy - czasStartowy) / 1000.0; // Konwersja na sekundy

    { Pomiar czasu dla metody rekurencyjnej }
    czasStartowy := GetTickCount64;
    for i := 1 to liczbaPowtorzen do
        wartoscSilni := SilniaRekurencyjna(n);
    czasKoncowy := GetTickCount64;
    czasRekurencyjny := (czasKoncowy - czasStartowy) / 1000.0; // Konwersja na sekundy

    { Wyświetl wyniki }
    WyswietlWyniki(n, liczbaPowtorzen, wartoscSilni, czasIteracyjny, czasRekurencyjny);
end;

{ Wyświetlanie wyników z odpowiednim formatowaniem }
procedure WyswietlWyniki(n, liczbaPowtorzen: Int64; wartoscSilni: Int64; czasIteracyjny, czasRekurencyjny: Double);
begin
    WriteLn;
    WriteLn('Wyniki pomiarów:');
    WriteLn('---------------');
    WriteLn('Argument funkcji silnia: ', n);
    WriteLn('Liczba powtórzeń: ', liczbaPowtorzen);
    WriteLn('Wartość silni: ', wartoscSilni);
    WriteLn('Czas obliczeń (metoda iteracyjna): ', czasIteracyjny:0:3, ' sekund');
    WriteLn('Czas obliczeń (metoda rekurencyjna): ', czasRekurencyjny:0:3, ' sekund');
    WriteLn('---------------');
    
    if czasRekurencyjny > czasIteracyjny then
        WriteLn('Metoda rekurencyjna jest wolniejsza o ', (czasRekurencyjny/czasIteracyjny):0:2, ' razy')
    else
        WriteLn('Metoda iteracyjna jest wolniejsza o ', (czasIteracyjny/czasRekurencyjny):0:2, ' razy');
end;

{ Procedura sterująca }
procedure Kontroler;
var
    n, liczbaPowtorzen: Int64;
    maxDozwolonyArgument: Int64;
begin
    { Ustaw maksymalną dozwoloną wartość argumentu }
    maxDozwolonyArgument := 20; { Dla Int64 - ustalono empirycznie }
    
    { Wczytaj parametry }
    n := WczytajLiczbe('Podaj argument silni (0-' + IntToStr(maxDozwolonyArgument) + '): ', 0, maxDozwolonyArgument);
    liczbaPowtorzen := WczytajLiczbe('Podaj liczbę powtórzeń (min. 1): ', 1, High(Int64));
    
    { Wykonaj pomiary }
    WykonajPomiaryCzasu(n, liczbaPowtorzen);
end;

{ Program główny }
begin
    Kontroler;
end.