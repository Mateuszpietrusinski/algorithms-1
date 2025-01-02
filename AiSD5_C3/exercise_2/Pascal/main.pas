program SilniaPomiarCzasu;

uses CRT, math, sysUtils;

{ Deklaracje wyprzedzające funkcji i procedur }
function WczytajLiczbe(const komunikat: string; minWartosc: Int64; maxWartosc: Int64): Int64; forward;
function SilniaRekurencyjna(n: Int64): Int64; forward;
function SilniaIteracyjna(n: Int64): Int64; forward;
procedure WykonajPomiaryCzasu(n: Int64; liczbaPowtorzen: Int64); forward;
procedure WyswietlWyniki(n: Int64; liczbaPowtorzen: Int64; wartoscSilni: Int64; czasIteracyjny: Double; czasRekurencyjny: Double); forward;
procedure Kontroler; forward;

{ Funkcja sprawdzająca, czy wynik nie przekroczy zakresu Int64 }
function CzyMoznaObliczyc(n: Int64): Boolean;
begin
    CzyMoznaObliczyc := n <= 20; { Empirycznie ustalone maksimum dla Int64 }
end;

{ Funkcja do wczytywania i walidacji liczby wejściowej }
function WczytajLiczbe(const komunikat: string; minWartosc: Int64; maxWartosc: Int64): Int64;
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

{ Obliczanie silni metodą iteracyjną }
function SilniaIteracyjna(n: Int64): Int64;
var
    wynik: Int64;
    i: Int64;
begin
    if not CzyMoznaObliczyc(n) then
    begin
        WriteLn('Błąd: Wartość zbyt duża dla typu Int64');
        Halt(1);
    end;
    
    wynik := 1;
    for i := 2 to n do
        wynik := wynik * i;
    SilniaIteracyjna := wynik;
end;

{ Obliczanie silni metodą rekurencyjną }
function SilniaRekurencyjna(n: Int64): Int64;
begin
    if not CzyMoznaObliczyc(n) then
    begin
        WriteLn('Błąd: Wartość zbyt duża dla typu Int64');
        Halt(1);
    end;
    
    if n <= 1 then
        SilniaRekurencyjna := 1
    else
        SilniaRekurencyjna := n * SilniaRekurencyjna(n - 1);
end;

{ Procedura wykonująca pomiary czasu }
procedure WykonajPomiaryCzasu(n: Int64; liczbaPowtorzen: Int64);
var
    i: Int64;
    czasStartowy, czasKoncowy: QWord;
    wartoscSilni: Int64;
    czasIteracyjny, czasRekurencyjny: Double;
begin
    { Pomiar czasu dla metody iteracyjnej }
    czasStartowy := GetTickCount64;
    wartoscSilni := SilniaIteracyjna(n);
    for i := 2 to liczbaPowtorzen do
        SilniaIteracyjna(n);
    czasKoncowy := GetTickCount64;
    czasIteracyjny := (czasKoncowy - czasStartowy) / 1000.0;

    { Pomiar czasu dla metody rekurencyjnej }
    czasStartowy := GetTickCount64;
    for i := 1 to liczbaPowtorzen do
        SilniaRekurencyjna(n);
    czasKoncowy := GetTickCount64;
    czasRekurencyjny := (czasKoncowy - czasStartowy) / 1000.0;

    { Wyświetl wyniki }
    WyswietlWyniki(n, liczbaPowtorzen, wartoscSilni, czasIteracyjny, czasRekurencyjny);
end;

{ Wyświetlanie wyników z odpowiednim formatowaniem }
procedure WyswietlWyniki(n: Int64; liczbaPowtorzen: Int64; wartoscSilni: Int64; czasIteracyjny: Double; czasRekurencyjny: Double);
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
    else if czasRekurencyjny < czasIteracyjny then
        WriteLn('Metoda iteracyjna jest wolniejsza o ', (czasIteracyjny/czasRekurencyjny):0:2, ' razy')
    else
        WriteLn('Obie metody mają podobny czas wykonania');
end;

{ Procedura sterująca }
procedure Kontroler;
var
    n, liczbaPowtorzen: Int64;
    maxDozwolonyArgument: Int64;
begin
    maxDozwolonyArgument := 20;  { Maksymalna bezpieczna wartość dla Int64 }
    
    n := WczytajLiczbe('Podaj argument silni (0-' + IntToStr(maxDozwolonyArgument) + '): ', 0, maxDozwolonyArgument);
    liczbaPowtorzen := WczytajLiczbe('Podaj liczbę powtórzeń (min. 1): ', 1, High(Int64));  { Bez górnego limitu }
    
    WykonajPomiaryCzasu(n, liczbaPowtorzen);
end;

begin
    Kontroler;
    Write('Naciśnij Enter, aby zakończyć...');
    ReadLn;
end.