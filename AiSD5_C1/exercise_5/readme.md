# Task 5: Solution

## Diagram

```mermaid
flowchart TD
    Start(["Start"]) --> locationX["Wprowadz polozenie X robota"]
    locationX -->locationY["Wprowadz polozenie Y robota"]
    locationY --> goOneStepFurther["Robot: Idz krok w przód"]
    goOneStepFurther --> isRobotOnLeftSideOfTheWarehouse{"Czy robot znajduje się po lewej stronie magazynu?"}
    isRobotOnLeftSideOfTheWarehouse -- Tak --> turn90LeftHalf1["Wykonaj obrót w lewo -90°"]
    isRobotOnLeftSideOfTheWarehouse -- Nie --> turn90RightHalf2["Wykonaj obrót w prawo 90°"]
   
    turn90LeftHalf1 --> goTopStepsHalf1["Idz (Y / 0.75m) kroków do przodu"]
    goTopStepsHalf1 --> turn90RightHalf1["Wykonaj obrót w prawo 90°"]
    turn90RightHalf1 --> goRightStepsHalf1["Idz [([11 - X] * 2) / 0.75m] kroków do przodu"]
    goRightStepsHalf1 --> turn90RightHalf1
    turn90RightHalf1 --> goEndStepsHalf1["Idz (6 / 0.75m) kroków do przodu"]
    goEndStepsHalf1 --> turn90LeftHalf1Two["Wykonaj obrót w lewo -90°"]
    turn90LeftHalf1Two --> Stop([Stop])

    turn90RightHalf2 --> goBottomStepsHalf2["Idz (Y / 0.75m) kroków do przodu"]
    goBottomStepsHalf2 --> turn90LeftHalf2["Wykonaj obrót w lewo -90°"]
    turn90LeftHalf2 --> goRightStepsHalf2["Idz [([11 - X] * 2) / 0.75m] kroków do przodu"]
    goRightStepsHalf2 --> turn90LeftHalf2
    turn90LeftHalf2 --> goEndStepsHalf2["Idz (6 / 0.75m) kroków do przodu"]
    goEndStepsHalf2 --> turn90RightHalf2Two["Wykonaj obrót w prawo 90°"]
    turn90RightHalf2Two --> Stop([Stop])
```

## Opisz algorytm językiem naturalnym

1. Na początku należy wprowadzić aktualne położenie robota poprzez podanie jego współrzędnych X i Y.

2. Robot wykonuje jeden krok do przodu, aby wyjść z miejsca parkingowego.

3. Następnie algorytm sprawdza, czy robot znajduje się po lewej stronie magazynu.

4. Jeśli robot znajduje się po lewej stronie magazynu:
   - Robot wykonuje obrót w lewo o -90 stopni
   - Przemieszcza się do przodu o liczbę kroków równą (Y / 0.75m)
   - Wykonuje obrót w prawo o 90 stopni
   - Idzie do przodu o liczbę kroków wyliczoną ze wzoru [([11 - X] * 2) / 0.75m]
   - Wykonuje obrót w prawo o 90 stopni
   - Przemieszcza się do przodu o liczbę kroków równą (6 / 0.75m)
   - Na końcu wykonuje obrót w lewo o -90 stopni, aby ustawić się w kierunku wyjścia

5. Jeśli robot znajduje się po prawej stronie magazynu:
   - Robot wykonuje obrót w prawo o 90 stopni
   - Przemieszcza się do przodu o liczbę kroków równą (Y / 0.75m)
   - Wykonuje obrót w lewo o -90 stopni
   - Idzie do przodu o liczbę kroków wyliczoną ze wzoru [([11 - X] * 2) / 0.75m]
   - Wykonuje obrót w lewo o -90 stopni
   - Przemieszcza się do przodu o liczbę kroków równą (6 / 0.75m)
   - Na końcu wykonuje obrót w prawo o 90 stopni, aby ustawić się w kierunku wyjścia

Wszystkie ruchy są precyzyjnie wyliczane z uwzględnieniem długości kroku robota wynoszącej 0.75 metra. Algorytm zapewnia, że robot dotrze do wyjścia najkrótszą możliwą drogą, unikając kolizji z innymi zajętymi miejscami.

## Kroki Algorytmu

1. **Faza wprowadzania danych**
   1. Wprowadź położenie X robota
   2. Wprowadź położenie Y robota

2. **Ruch początkowy**
   1. Przesuń robota jeden krok do przodu, aby opuścić miejsce

3. **Sprawdzenie pozycji**
   1. Sprawdź, czy robot znajduje się po lewej stronie magazynu

4. **Ścieżka dla lewej strony** (jeśli robot jest po lewej stronie)
   1. Wykonaj obrót w lewo (-90°)
   2. Idź do przodu (Y / 0.75m) kroków
   3. Wykonaj obrót w prawo (90°)
   4. Idź do przodu [([11 - X] * 2) / 0.75m] kroków
   5. Wykonaj obrót w prawo (90°)
   6. Idź do przodu (6 / 0.75m) kroków
   7. Wykonaj obrót w lewo (-90°)
   8. Zatrzymaj się

5. **Ścieżka dla prawej strony** (jeśli robot jest po prawej stronie)
   1. Wykonaj obrót w prawo (90°)
   2. Idź do przodu (Y / 0.75m) kroków
   3. Wykonaj obrót w lewo (-90°)
   4. Idź do przodu [([11 - X] * 2) / 0.75m] kroków
   5. Wykonaj obrót w lewo (-90°)
   6. Idź do przodu (6 / 0.75m) kroków
   7. Wykonaj obrót w prawo (90°)
   8. Zatrzymaj się

Uwaga: Wszystkie ruchy są obliczane na podstawie długości kroku robota wynoszącej 0.75 metra.