def life_in_weeks(age):
    leaf_weeks = 52 * 90
    age = age * 52
    age = leaf_weeks - age 
    print(f"Your life in the weeks is the {age}")
    
    
age = int(input("Register You Age: "))
life_in_weeks(age)