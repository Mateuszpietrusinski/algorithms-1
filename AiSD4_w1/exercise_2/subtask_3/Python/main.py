# Równanie kwadratowe
import math
def CzytajDane():
  a=float(input("a="))
  b=float(input("b="))
  c=float(input("c="))
  return a,b,c
def ObliczRownanie(a,b,c):
  Delta=(b*b-4*a*c)
  if Delta>=0:
    x1=(-b-math.sqrt(Delta))/(2*a)
    x2=(-b+math.sqrt(Delta))/(2*a)
    return x1,x2
  else:
    return False
def PiszWyniki(Wyniki):
  print('\nWyniki obliczeń:')
  if isinstance(Wyniki,tuple):
    print(f'x1={Wyniki[0]:.2f} x2={Wyniki[1]:.2f}')
  else: 
    print('Brak rozwiązań.')
#=== Program główny ===
a,b,c=CzytajDane()
Wyniki=ObliczRownanie(a,b,c)
PiszWyniki(Wyniki)