import random
def game():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    print("Do you want to play a game of Blackjack? Type 'y' or 'n': ")

    def deal_card():
        return random.choice(cards)

    user_cards = []
    computer_cards = []
    for i in range(2):
        user_cards.append(deal_card())
        computer_cards.append((deal_card()))
    print(user_cards)
    print(computer_cards)

    def calculate_score(cards_of):
        if sum(cards_of) > 21:
            cards.remove(11)
        if sum(cards_of) == 21:
            return 0
        else:
            return sum(cards_of)
    score_computer = calculate_score(computer_cards)
    score_user = calculate_score(user_cards)
    print(f"your score is {score_user}")
    print(score_computer)


    game_over = False
    while not game_over:
        choose1 = input("do you wanna draw another card? y or n?")
        if choose1 == "y":
            user_cards.append(deal_card())
            print(user_cards)
            print(sum(user_cards))
            if sum(user_cards) == 21:
                print(f"your score is {sum(user_cards)}")
                print("its a blackjack")
                break
            elif sum(user_cards) > 21:
                print(f"your score is {sum(user_cards)}")
                print("game over you loose")
                break
        if choose1 == "n":
            break
    print(user_cards)
    print(computer_cards)
    while not game_over:
        if sum(computer_cards) < 17:
            computer_cards.append(deal_card())
            print(computer_cards)
            print(sum(computer_cards))
        else:
            print("computer wins")
            print(sum(computer_cards))
            break

while True:
        game()
        restart = input('do you want to restart y/n?')
        if restart == 'n'.lower():
            break
        elif restart == 'y'.lower():
            continue
