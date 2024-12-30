program PowerConsumption;
uses
  SysUtils, Math, DateUtils, Crt;

const
  INSTALLED_POWER = 3.0; // 3 kW installed power
  SIMULATION_SECONDS = 100; // Simulation time in seconds (instead of 365 days)
  REACTIVE_POWER_RATIO = 0.1; // Reactive power is 10% of active power

type
  TPowerData = record
    ActivePowerSum1: Double;    // Sum of active power in tariff I
    ActivePowerSum2: Double;    // Sum of active power in tariff II
    ReactivePowerSum1: Double;  // Sum of reactive power in tariff I
    ReactivePowerSum2: Double;  // Sum of reactive power in tariff II
    MaxActivePower: Double;     // Maximum active power in current month
    LastMaxPowerDate: TDateTime;// Date of last maximum power recording
    LastMonthMaxPower: Double;  // Maximum active power from previous month
    StartDate: TDateTime;       // Counter start date
  end;

// Function to check if current time is in Tariff I (6:00-13:00 or 15:00-22:00)
function IsInTariffI(Hour: Integer): Boolean;
begin
  IsInTariffI := ((Hour >= 6) and (Hour < 13)) or ((Hour >= 15) and (Hour < 22));
end;

// Function to simulate instantaneous power consumption
function SimulateActivePower(Time: Integer): Double;
begin
  // Simulate power consumption using sine function (between 0 and INSTALLED_POWER)
  SimulateActivePower := (Sin(Time * PI / 180) + 1) * INSTALLED_POWER / 2;
end;

// Procedure to process power readings
procedure ProcessPowerReadings(var Data: TPowerData; ActivePower, ReactivePower: Double; 
                             CurrentTime: TDateTime; CurrentHour: Integer);
var
  CurrentMonth, LastMaxMonth: Integer;
begin
  // Update power sums based on tariff
  if IsInTariffI(CurrentHour) then
  begin
    Data.ActivePowerSum1 := Data.ActivePowerSum1 + ActivePower;
    Data.ReactivePowerSum1 := Data.ReactivePowerSum1 + ReactivePower;
  end
  else
  begin
    Data.ActivePowerSum2 := Data.ActivePowerSum2 + ActivePower;
    Data.ReactivePowerSum2 := Data.ReactivePowerSum2 + ReactivePower;
  end;

  CurrentMonth := MonthOf(CurrentTime);
  LastMaxMonth := MonthOf(Data.LastMaxPowerDate);

  // Update maximum power values
  if (CurrentMonth <> LastMaxMonth) or (Data.LastMonthMaxPower = 0) then
  begin
    Data.LastMonthMaxPower := Data.MaxActivePower;
    Data.MaxActivePower := ActivePower;
    Data.LastMaxPowerDate := CurrentTime;
  end
  else if (ActivePower > Data.MaxActivePower) then
  begin
    Data.MaxActivePower := ActivePower;
    Data.LastMaxPowerDate := CurrentTime;
  end;
end;

// Procedure to display results
procedure DisplayResults(const Data: TPowerData);
begin
  ClrScr;
  WriteLn('=== Raport zużycia energii ===');
  WriteLn(Format('Moc Czynna (Taryfa I): %.2f kWh', [Data.ActivePowerSum1]));
  WriteLn(Format('Moc Bierna (Taryfa I): %.2f kVArh', [Data.ReactivePowerSum1]));
  WriteLn(Format('Moc Czynna (Taryfa II): %.2f kWh', [Data.ActivePowerSum2]));
  WriteLn(Format('Moc Bierna (Taryfa II): %.2f kVArh', [Data.ReactivePowerSum2]));
  WriteLn(Format('Moc maksymalna w ostatnim miesiącu: %.2f kW', [Data.LastMonthMaxPower]));
  WriteLn(Format('Moc maksymalna w obecnym miesiącu: %.2f kW', [Data.MaxActivePower]));
  WriteLn('==============================');
end;

// Main control procedure
procedure ControlProgram(var Data: TPowerData);
var
  CurrentTime: TDateTime;
  ElapsedSeconds: Integer;
  ActivePower, ReactivePower: Double;
  CurrentHour: Integer;
begin
  // Initialize data
  Data.ActivePowerSum1 := 0;
  Data.ActivePowerSum2 := 0;
  Data.ReactivePowerSum1 := 0;
  Data.ReactivePowerSum2 := 0;
  Data.MaxActivePower := 0;
  Data.LastMonthMaxPower := 0;
  Data.StartDate := Now;
  Data.LastMaxPowerDate := Data.StartDate;

  // Main simulation loop
  for ElapsedSeconds := 0 to SIMULATION_SECONDS do
  begin
    CurrentTime := IncSecond(Data.StartDate, ElapsedSeconds);
    CurrentHour := HourOf(CurrentTime);
    
    // Get power readings
    ActivePower := SimulateActivePower(ElapsedSeconds);
    ReactivePower := ActivePower * REACTIVE_POWER_RATIO;

    // Process readings
    ProcessPowerReadings(Data, ActivePower, ReactivePower, CurrentTime, CurrentHour);
    
    // Display current state
    DisplayResults(Data);
    
    // Add small delay to simulate real-time processing
    Sleep(100);
  end;
end;

var
  PowerData: TPowerData;

begin
  ControlProgram(PowerData);
  ReadLn; // Wait for user input before closing
end.