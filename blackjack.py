import random
import os
logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""


def cls():
    os.system('cls' if os.name=='nt' else 'clear')
                  

	
def deal_card(cards_held):
	cards = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
	cards_held.append(random.choice(cards))
	return cards_held

def calculate_score(cards_held):
	score = 0
	flag = 0
	for i in cards_held:
		if i != 'A':
			score += i
		else: 
			flag += 1
	if score > 10:
		score += 1 * flag
	else:
		score += (11 + (1*(flag - 1)))
	if score == 21:
		return 0
	return score

def compare(player_score,computer_score):
	
	if computer_score == player_score:
		return("It's a draw, what were the odds of that?")
	elif computer_score == 0 or player_score > 21:
		return("You lose, wanna try again?")
	elif player_score == 0 or computer_score > 21:
		return("Woohoooo! You win!!!") 
	elif player_score > computer_score:
		return("Close but you win")
	else:
		return("FeelsBadMan")

def play():
	computer_cards = []
	player_cards = []
	isGameOver = False
	for i in range(2):
		deal_card(computer_cards)
		deal_card(player_cards)

	while not isGameOver:
		player_score = calculate_score(player_cards)
		computer_score = calculate_score(computer_cards)

		print(f"Your cards are {player_cards} and your current score is: {player_score}")
		print(f"Computer's hand is {computer_cards[0]}")

		if player_score == 0 or computer_score == 0 or player_score > 21:
			isGameOver = True
		else: 
			player_asks_deal = input("Enter 'y' if you want to draw another card or 'n' to end drawing cards: ").lower()
			if player_asks_deal == 'y':
				deal_card(player_cards)
			else:
				isGameOver = True

	while(computer_score != 0) and (computer_score < 17):
		deal_card(computer_cards)
		computer_score = calculate_score(computer_cards)

	print(f"Your final hand: {player_cards} and final score: {player_score}")
	print(f"Computer's final hand:{computer_cards} and final score: {computer_score}")
	print(compare(player_score,computer_score))

while input("Do you wanna play a game of Blackjack? Type 'y' or 'n': ") == 'y':
	cls()
	print(logo)
	play()


