# Adjust the program to the standard described in the manual

Perform the following steps sequentially:
1. In the first line of the source code, put a comment containing the name of the program,
program version, date of execution. The comment block is marked with brackets
curly braces {} or double slash // if you are commenting one line of the program.
2. In the second line of the source code, place a comment containing: the name of the author of the
of the program, index number, academic year, department, group, semester.
3. The program must display the following message on the console after running:
“Program: “ <program_name> “Author: ” <author_name, index_number,
academic_year, department, group, semester>. Write a procedure that performs this
functionality and call it first from the main program.

Tip:
Program should use following modules:
```pascal
uses CRT, sysUtils;
```
Useful functions:
```pascal
function Time: TdateTime - zwraca bieżący czas 
```
Converting time into seconds:
```pascal
CzasS:=Time*24*60*60;
```
Position the cursor on the indicated place (this is where the values will be displayed):
```pascal
gotoXY(X,Y); //współrzędne X i Y podaje się w znakach (nie pikselach)
```