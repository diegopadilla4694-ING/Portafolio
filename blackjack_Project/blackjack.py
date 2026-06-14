import random
import logo


def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
        return f"You Lose, you score is {sum(cards)}"
    

    return sum(cards)


def compare(u_score, c_score):
    if u_score == c_score:
        return "DRAW "
    
    elif c_score == 0:
        return "YOU LOSE AHAHAHAHAHA"
    elif u_score == 0:
        return "YOU WIN CONGRATULATIONS"
    elif u_score > 21:
        return "YOU LOSE SORRY"
    elif c_score > 21:
        return "You opponent over, YOU WIN COOL"
    elif u_score > c_score:
        return "YOU WIN"
    else:
        return "YOU LOSE"
    
    
def play_game():
    print(logo.logo_blackjack)
    user_cards = []
    computer_cards = []
    user_score = -1
    computer_score = -1
    GAME_OVER = False


    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())
        

    while not GAME_OVER:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"The computer cards: {computer_cards[0]}")


        if user_score == 0 or computer_score == 0 or user_score > 21:
            GAME_OVER = True
            
        else:
            user_selection = input("You want star other play 'Yes' but confirm and 'no' but exit of terminal: ").lower()
            if user_selection == "yes":
                user_selection.append(deal_card())
                
            else:
                GAME_OVER = True
                

    while computer_score != 0 and computer_cards < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)
        

    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))

while input("Do you to play a game a Blackjack? Type 'yes' or 'no': ") ==  "yes":
    print("\n * 20")
    play_game()