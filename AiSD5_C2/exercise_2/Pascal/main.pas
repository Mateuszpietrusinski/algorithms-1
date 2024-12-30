program LeapYearCheck;

uses 
  CRT, math, sysUtils;

// Function to read the year from user input
function ReadYear: integer;
begin
  write('Wprowadz rok do sprawdzenia: ');
  readln(ReadYear);
end;

// Function to check if a year is leap following the exact flowchart logic
function IsLeapYear(year: integer): boolean;
begin
  // First check: if year mod 400 = 0
  if (year mod 400 = 0) then
    IsLeapYear := true
  else
  begin
    // Second check: if year mod 4 = 0
    if (year mod 4 = 0) then
    begin
      // Third check: if year mod 100 <> 0
      if (year mod 100 <> 0) then
        IsLeapYear := true
      else
        IsLeapYear := false;
    end
    else
      IsLeapYear := false;
  end;
end;

// Procedure to display the result
procedure DisplayResult(year: integer; isLeap: boolean);
begin
  write('Rok ', year);
  if isLeap then
    writeln(' jest rokiem przestepnym.')
  else
    writeln(' nie jest rokiem przestepnym.');
end;

// Main procedure that coordinates all operations
procedure ProcessLeapYearCheck;
var
  year: integer;
  isLeap: boolean;
begin
  // Clear the screen for better visibility
  ClrScr;
  
  // Get the year from user ("Podaj Rok")
  year := ReadYear;
  
  // Check if it's a leap year following flowchart logic
  isLeap := IsLeapYear(year);
  
  // Display the result
  DisplayResult(year, isLeap);
  
  // Wait for user input before closing
  writeln;
  writeln('Wcisnij Enter aby wyjśc z programu...');
  readln;
end;

// Main program
begin
  ProcessLeapYearCheck;
end.