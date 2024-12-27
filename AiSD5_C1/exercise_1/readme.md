# Task 1: Checking the Leap Year Condition

## Definition
A leap year is a year that meets the following conditions:
* It is divisible by 4 and not divisible by 100,  
  **or**  
* It is divisible by 400.

1. Describe the algorithm using a step-by-step list.
2. Draw a block diagram for checking the condition for leap year.
* Draw a block diagram for checking the condition whether the given year is leap year.
* The input parameter is an integer specifying the year number.
* The result of the algorithm is whether the given year is leap year or not.

> **Warning:**
> **In the flowchart, use arithmetic expressions and the mod function to calculate the remainder of the division.**

3. Perform an algorithm validity test
*  Conduct an analysis of the issue
*  Develop test scenarios and select representative values of years for which you will check the correctness of the algorithm through the test.
*  Perform the test for the selected test values


---
# Task 1: Solution

## Steps list

Polish:
1. Podaj Rok (wartość całkowita).
2. Jezeli rok mod 400 = 0 to pisz 'Rok przestepny'. Stop
3. Jezeli rok mod 4 = 0 to idz do krok 5.
4. Pisz 'Rok nieprzestępny'. Stop
5. Jezeli rok mod 100 <> 0 to pisz: 'Rok przstepny'. Stop
6. Pisz 'Rok nieprzestepny'.


## Diagram 

```mermaid
flowchart TD
    Start([Start]) --> Input["Podaj Rok (wartość całkowita)"]
    Input --> Check400{Jezeli rok mod 400 = 0?}
    Check400 -- Tak --> LeapYear1["Rok przestepny"]
    LeapYear1 --> End1([Stop])
    Check400 -- Nie --> Check4{Jezeli rok mod 4 = 0?}
    Check4 -- Nie --> NotLeapYear1["Rok nieprzestepny"]
    NotLeapYear1 --> End2([Stop])
    Check4 -- Tak --> Check100{Jezeli rok mod 100 <> 0?}
    Check100 -- Tak --> NotLeapYear2["Rok nieprzestepny"]
    NotLeapYear2 --> End3([Stop])
    Check100 -- Nie --> LeapYear2["Rok przestepny"]
    LeapYear2 --> End4([Stop])
```
## Tests

Example test cases:
* Year = 2000 (divisible by 400, should be a leap year)
* Year = 1900 (divisible by 100 but not 400, should not be a leap year)
* Year = 2024 (divisible by 4 and not 100, should be a leap year)
* Year = 2023 (not divisible by 4, should not be a leap year)


The results of the test cases are as follows:
1.	Year = 2000
* Expected: "Rok przestepny"
* Result: "Rok przestepny" ✅

2.	Year = 1900
* Expected: "Rok nie przestepny"
* Result: "Rok nie przestepny" ✅

3.	Year = 2024
* Expected: "Rok przestepny"
* Result: "Rok przestepny" ✅

4.	Year = 2023
* Expected: "Rok nie przestepny"
* Result: "Rok nie przestepny" ✅