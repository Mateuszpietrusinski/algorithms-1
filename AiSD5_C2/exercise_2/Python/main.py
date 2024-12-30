def read_year():
    year = int(input('Wprowadz rok do sprawdzenia: '))
    return year

def is_leap_year(year):
    if year % 400 == 0:
        return True
    elif year % 4 == 0:
        if year % 100 != 0:
            return True
        else:
            return False
    else:
        return False

def display_result(year, is_leap):
    if is_leap:
        print(f'Rok {year} jest rokiem przestepnym.')
    else:
        print(f'Rok {year} nie jest rokiem przestepnym.')

def process_leap_year_check():
    year = read_year()
    is_leap = is_leap_year(year)
    display_result(year, is_leap)

if __name__ == "__main__":
    process_leap_year_check()
    input('Wcisnij Enter aby wyjść z programu...')