from typing import Final
import sys

# Program demonstrating differences in floating-point calculations
# Type hints are added for better code clarity and IDE support

# Constants defined with type hints
N: Final[int] = 1000000    # Constant defining number of additions
S: Final[float] = 1.23456789  # Number that will be summed

# Initialize sum variable with explicit float type
suma: float = 0.0

# Perform addition n times
for i in range(N):
    suma += S

# Calculate product
iloczyn: float = S * N

# Calculate difference between product and sum
roznica: float = iloczyn - suma

# Display results with formatting
print('Calculation results:')
print(f'1) Sum       = {suma:15.8f}')
print(f'2) Product   = {iloczyn:15.8f}')
print(f'3) Difference= {roznica:15.8f}')

# Display the size of float variable 'suma' in bytes
print(f'\nSize of Sum variable (float type): {sys.getsizeof(suma)} bytes')

# Wait for user input before ending
input('\nPress Enter to exit...')