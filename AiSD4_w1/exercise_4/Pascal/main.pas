program Timer;

// Including required library modules
uses 
  CRT,     // For screen manipulation and delay functions
  sysutils; // For additional system utilities

var
  totalSeconds: Integer;  // Stores the total number of seconds to count
  currentSecond: Integer; // Keeps track of elapsed seconds

begin
  // Clear the screen at program start
  ClrScr;
  
  // Get input from user
  write('Wprowadź liczbę sekund do zliczenia: ');
  readln(totalSeconds);
  
  // Input validation
  if totalSeconds <= 0 then
  begin
    writeln('Wprowadź dodatnią liczbę sekund.');
    readln;  // Pause to show error message
    exit;    // Exit program if input is invalid
  end;
  
  // Initialize counter
  currentSecond := 0;
  
  // Infinite loop for countdown
  while True do
  begin
    // Clear screen for each update
    ClrScr;
    
    // Display current progress
    writeln('Uplynelo... ', currentSecond, ' sekund z ', totalSeconds, 'sekund.');
    
    // Check if we've reached the target time
    if currentSecond >= totalSeconds then
    begin
      writeln('Czas minal! Program zakonczony.');
      readln;  // Pause to show final message
      exit;    // Exit the program when done
    end;
    
    // Wait for one second
    delay(1000);  // Delay for 1000 milliseconds (1 second)
    
    // Increment the counter
    inc(currentSecond);
  end;
end.