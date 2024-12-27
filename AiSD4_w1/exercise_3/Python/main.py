# Kwadraty i sześciany
def PetlaFor():
 print('\nPętla for')
 print(' x x2 x3')
 x=0
 for i in range(0,10):
    x2=x**2
    x3=x**3
    print(f'{x:7.2f}{x2:7.2f}{x3:7.2f}')
    x=x+0.1
def PetlaWhile():
 print('\nPętla while')
 print(' x x2 x3')
 x=0
 while x<0.9:
    x2=x**2
    x3=x**3
    print(f'{x:7.2f}{x2:7.2f}{x3:7.2f}')
    x=x+0.1

#=== Program główny ===
print('Kwadraty i sześciany')
PetlaFor()
PetlaWhile()