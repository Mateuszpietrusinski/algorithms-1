'''
Program Minutnik, v.1.0, 2021-10-01
Mateusz Pietrusinski, nr ind. xxxx, rok. 2024/2025, Informatyka, PUW D1, Semestr 1
'''
# Minutnik
from datetime import datetime as dt
def Info():
    print('Program Minutnik')
    print('Autor: Mateusz Pietrusinski, nr ind. xxxx, rok. 2024/2025, Informatyka, PUW D1, Semestr 1')
    print()
def IleSekund():
    sek=float(input('Podaj liczbę sekund:'))
    return sek
def Minutnik(sek):
    t0=dt.today()
    t3sek=0
    while 1==1:
        t=dt.today()-t0
        tsek=t.seconds+0.000001*t.microseconds
        if tsek-t3sek>=3:
            print(f'{tsek:3.0f}',end='\r')
            t3sek=tsek
        if tsek>sek:
            break
    print(f'\nOdliczono {tsek:3.0f} sekund')
#=== Program główny ===
Info()
sek=IleSekund()
Minutnik(sek)