print(r'''
                            _.--.
                        _.-'_:-'||
                    _.-'_.-::::'||
               _.-:'_.-::::::' ||
             .'`-.-:::::::' ||
            /.'`;|:::::::' ||_
           || ||::::::' _.;._'-._
           || ||:::::' _.-!oo @.!-._'-.
           \. ||:::::.-!()oo @!()@.-'_.|
            '.'-;|:.-'.&$@.& ()$%-'o.'\U||
              `>'-.!@%()@'@_%-'_.-o _.|'||
               ||-._'-.@.-'_.-' _.-o |'||
               ||=[ '-._.-\U/.-' o |'||
               || '-.]=|| |'| o |'||
               || || |'| _| ';
               || || |'| _.-'_.-'
               |'-._ || |'|_.-'_.-'
               '-._'-.|| |' `_.-'
                    '-.||_/.-'
''')


print("Welcome to Treasure Island. ")
print("Your mission is to find treasure. ")
choice1 = input('You\'re at a crossroad, where do you want to go?\n' \
                'Type "Left" or "Right"\n').lower()

if choice1 == "left":
     choice2 = input('You can to lake. There is an island '
          'in the middle of the lake. Type wait to wait '
          'for a boat. Type "swim" to swim across.\n').lower()
     
     if choice2 == "wait":
         choice3 = input('You arrive at the island unharmed. "'
                         'There is house with 3 doors. One red, '
                         'one yellow and one blue. '
                         'Which colour do you choose?\n').lower()
         
         if choice3 == "red":
             print("It's a room full of fire. GAME OVER")
         elif choice3 == "yellow":
             print("You found the tresure. YOU WIN!")
         elif choice3 == "blue":
             print("You enter a room of beast. GAME OVER")
         else:
             print("You choose a door that doesn't exist. GAME OVER")
     else:
        print("You attacked by an angry trout. Game over ")

else:
    print("You fell in to a hole. GAME OVER")



