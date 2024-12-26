// Program Minutnik, v.1.0, 2024-12-25
// Mateusz Pietrusinski, nr ind. XXX, rok. 2024/2025, Informatyka, PUW D2, Semestr 1

program Minutnik;
uses CRT, sysutils, Dos;

// Wyswietlanie informacji o autorze
procedure Info;
begin
    writeln('Program Minutnik');
    writeln('Autor: Mateusz Pietrusinski, nr ind. XXX, rok. 2024/2025, Informatyka, PUW D2, Semestr 1');
writeln;
end;
// Odczytanie podanej przez użytkownika liczby sekund
function IleSekund : real;
var IleS : real;
begin
    write( 'Podaj liczbe sekund:' );
    readln( IleS );
    IleSekund:=IleS
end;
// Procedura odlicza podaną liczbe sekund i wyswietla upływ czasu na konsoli
procedure Odliczaj( Czas : real );
var T0,T : real;
begin
    T0:=Time*24*60*60;
    repeat
        T:=Time*24*60*60 - T0;
        gotoXY(3,5);
        write(T:5:1);
        if T>=Czas then exit;
    until 1=0;
end;
begin
    Info;
    Odliczaj( IleSekund );
    writeln;
    writeln( 'Czas minal' );
    readln
end.