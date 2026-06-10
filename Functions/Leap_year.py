user_is_year = int(input("Please enter one year: "))

def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

print(is_leap_year(user_is_year))