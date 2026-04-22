import random

world_list = ['Carlos', ' BOETO', 'Administrador']

__chosen_word = random.choice(world_list)
print(chosen_word)


guess = input("Guess a letter: ").lower()
print(guess)