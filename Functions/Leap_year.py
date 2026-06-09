user_is_year = int(input("Please enter one year: "))

def is_leap_year(year):
    if year % 4 == 0:
       return True
    
    else:
       return False


leap = is_leap_year(user_is_year)
print(leap)
