def game():
    def leaf_characters(leaf):
        my_leaf = leaf
        return type(my_leaf) == int 
    
    def value_True(value_booleano):
        return True if type(value_booleano) == int else False
    
    leaf = int(input("Your life is: "))
    leaf_characters(leaf)    
    print(value_True(leaf))



game()



