Your_Pet = input("You have a Dog or a Cat?? ").lower()
name_pet = input("What your name pet?? ")


def dog(Pet, name):
    if Pet == "dog":
        return name + " Guaau"
    
    else:
        return name + " Miauu"
    


def cat(name):
    return name.title()



func = cat(dog(Your_Pet, name_pet))
print(func)




