def calculate_love_score(name1, name2, word1, word2):
    names_combinated = (name1 + name2).lower()

    score_true = 0
    score_love = 0

    for letter in word1:
        letters = names_combinated.count(letter)
        score_true += letters

    
    for letter in word2:
        letters = names_combinated.count(letter)
        score_love += letters
    
    love_score = str(score_true) + str(score_love)
    print(love_score)
    

calculate_love_score(name1="Diego", name2="Camila", word1="true", word2="love")