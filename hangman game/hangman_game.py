import random

from hangman_words import word_list
from hangman_art import LIFE_STAGE, LOGO

chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ""
word_length = len(chosen_word)

for position in range(word_length):
    placeholder += "_"

print(placeholder)


lives = 6


game_over = False
correct_letters = []

print(LOGO)

while not game_over:
     print(f"You have {lives} lives left")
     guess = input("Guess a letter: ").lower()

     
     display = ""



     for letter in chosen_word:
          if letter == guess:
              display += letter
              correct_letters.append(guess)
          elif letter in correct_letters:
              display += letter
          else:
              display += "_"    
        
     print(display)

     if guess in correct_letters:
          print("You already posted this letter :)")


     if guess not in chosen_word:
          lives -= 1
        
          if lives == 0:
               game_over = True
               print("*********YOU LOSE*********")    

          
     if "_" not in display:
          game_over = True
          print("***********YOU WIN************")


     print(LIFE_STAGE[lives])







  
             

