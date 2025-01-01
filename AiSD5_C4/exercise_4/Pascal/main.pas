program CovidStatistics;

uses 
  Sysutils,  // Dla formatowanego wyjścia
  Math;      // Dla funkcji matematycznych

type
  // Typ wyliczeniowy dla płci
  TGender = (Female, Male);
  
  // Rekord do przechowywania danych dziennych
  TDailyData = record
    cases: Integer;    // Liczba zachorowań
    deaths: Integer;   // Liczba zgonów
  end;
  
  // Rekord dla wyników statystycznych - używamy Int64 dla sum
  TStatistics = record
    totalCasesFemale: Int64;     // Suma zachorowań kobiet
    totalCasesMale: Int64;       // Suma zachorowań mężczyzn
    totalCasesAll: Int64;        // Suma wszystkich zachorowań
    averageCasesDaily: Real;     // Średnia dzienna liczba zachorowań
    maxDeathsDay: Integer;       // Dzień z największą liczbą zgonów
    maxDeathsCount: Integer;     // Maksymalna liczba zgonów
  end;
  
  // Typ tablicowy dla danych COVID
  TCovidData = array[1..31, TGender] of TDailyData;

var
  covidData: TCovidData;
  stats: TStatistics;

// Funkcja generująca liczby losowe w zadanym zakresie
function GenerateRandomNumber(min, max: Integer): Integer;
var
  randomNumber: Integer;
begin
  randomNumber := min + Random(max - min + 1);
  GenerateRandomNumber := randomNumber;
end;

// Procedura generująca dane losowe
procedure GenerateData(var data: TCovidData);
var
  day: Integer;
  gender: TGender;
begin
  for day := 1 to 31 do
    for gender := Female to Male do
    begin
      data[day, gender].cases := GenerateRandomNumber(1000, 10000);
      data[day, gender].deaths := GenerateRandomNumber(20, 200);
    end;
end;

// Procedura obliczająca statystyki
procedure CalculateStatistics(const data: TCovidData; var results: TStatistics);
var
  day: Integer;
  dailyDeaths: Integer;
begin
  // Inicjalizacja statystyk
  with results do
  begin
    totalCasesFemale := 0;
    totalCasesMale := 0;
    maxDeathsCount := 0;
    maxDeathsDay := 1;
  end;
  
  // Obliczanie statystyk
  for day := 1 to 31 do
  begin
    // Dodawanie przypadków (używamy Int64 dla sum)
    results.totalCasesFemale := results.totalCasesFemale + 
      Int64(data[day, Female].cases);
    results.totalCasesMale := results.totalCasesMale + 
      Int64(data[day, Male].cases);
      
    // Sprawdzanie maksymalnej liczby zgonów
    dailyDeaths := data[day, Female].deaths + data[day, Male].deaths;
    if dailyDeaths > results.maxDeathsCount then
    begin
      results.maxDeathsCount := dailyDeaths;
      results.maxDeathsDay := day;
    end;
  end;
  
  // Obliczanie sum i średnich
  results.totalCasesAll := results.totalCasesFemale + results.totalCasesMale;
  results.averageCasesDaily := results.totalCasesAll / 31;
end;

// Procedura wyświetlająca dane
procedure DisplayData(const data: TCovidData; const results: TStatistics);
var
  day, group: Integer;
  lastDay: Integer;
begin
  // Nagłówek
  WriteLn('Nr_dnia  Zachorowania_K  Zachorowania_M  Smierć_K  Śmierć_M');
  WriteLn('----------------------------------------------------------');
  
  // Wyświetlanie danych w grupach po 10
  for group := 0 to 3 do
  begin
    // Obliczamy ostatni dzień w grupie (nie więcej niż 31)
    if (group + 1) * 10 > 31 then
      lastDay := 31
    else
      lastDay := (group + 1) * 10;
      
    for day := group * 10 + 1 to lastDay do
      WriteLn(Format('%2d %13d %14d %9d %9d',
        [day,
         data[day, Female].cases,
         data[day, Male].cases,
         data[day, Female].deaths,
         data[day, Male].deaths]));
    
    if group < 3 then
    begin
      WriteLn('Naciśnij Enter, aby kontynuować...');
      ReadLn;
    end;
  end;
  
  // Wyświetlanie statystyk
  WriteLn;
  WriteLn('Statystyki:');
  WriteLn('Suma zachorowań: kobiety: ', results.totalCasesFemale,
          ' mezczyzni: ', results.totalCasesMale,
          ' ogolem: ', results.totalCasesAll);
  WriteLn('Srednia liczba zachorowan dziennie: ', results.averageCasesDaily:0:2);
  WriteLn('Dzien maksymalnej liczby zgonow: ', results.maxDeathsDay,
          ' liczba: ', results.maxDeathsCount);
end;

begin
  // Inicjalizacja generatora liczb losowych
  Randomize;
  
  // Generowanie danych
  GenerateData(covidData);
  
  // Obliczanie statystyk
  CalculateStatistics(covidData, stats);
  
  // Wyświetlanie wyników
  DisplayData(covidData, stats);
  
  // Oczekiwanie na wejście użytkownika przed zakończeniem
  WriteLn;
  WriteLn('Naciśnij Enter, aby zakończyć...');
  ReadLn;
end.