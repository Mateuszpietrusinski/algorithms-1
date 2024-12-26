# Task 1: Checking the Leap Year Condition

## Definition
A leap year is a year that meets the following conditions:
- It is divisible by 4 and not divisible by 100,  
  **or**  
- It is divisible by 400.

---

## Steps

1. **Describe the algorithm using a step-by-step list:**
   - Step 1: Read the input year (an integer value).
   - Step 2: Check if the year is divisible by 400. If true, the year is a leap year. End.
   - Step 3: Otherwise, check if the year is divisible by 4 and not divisible by 100. If both conditions are true, the year is a leap year. End.
   - Step 4: If neither condition is satisfied, the year is not a leap year. End.

---

## Block Diagram
- **Create a flowchart to check the leap year condition:**
  - Input: An integer representing the year.
  - Output: Information about whether the given year is a leap year or not.
  - **Note:** Use arithmetic expressions and the `mod` function to calculate the remainder of division.

---

## Testing the Algorithm

1. **Analyze the problem.**
   - Understand the leap year rules and how they apply to different cases.
   
2. **Develop test scenarios.**
   - Select representative year values to check the algorithm's correctness.
   - Example test cases:
     - Year = 2000 (divisible by 400, should be a leap year)
     - Year = 1900 (divisible by 100 but not 400, should not be a leap year)
     - Year = 2024 (divisible by 4 and not 100, should be a leap year)
     - Year = 2023 (not divisible by 4, should not be a leap year)

3. **Perform the test for the selected values.**
   - Check if the algorithm correctly identifies leap years and non-leap years for all test cases.


---
## Solution:

```plantUML
@startuml
start
:Wprowadz rok (liczba);
if (Czy rok jest podzielny 400?) then (tak)
  :Rok przestepny;
  stop
else (nie)
  if (Czy rok jest podzielny przez 4?) then (tak)
    if (Czy rok jest podzielny przez 100?) then (tak)
      :Rok nie przestepny;
      stop
    else (nie)
      :Rok przestepny;
      stop
    endif
  else (nie)
    :Rok nie przestepny;
    stop
  endif
endif
@enduml
```