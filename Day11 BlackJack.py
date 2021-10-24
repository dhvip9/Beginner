import random
import replit
all_cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def logo():
	return """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/ 
	       """

def nearest_number(number, num_list):
	sort_list = [abs(value - number) for value in num_list]
	Index = sort_list.index(min(sort_list))
	return num_list[Index]	


def cards(number_cards):
	card_2 = [random.choice(all_cards) for _ in range(number_cards)]
	return card_2


def sub(num_1, num_2):
	"""Return subtraction of Two Number"""
	return num_1 - num_2


def winner(player, computer):
	total = [sum(player), sum(computer)]
	near = nearest_number(21,total)
	win = total.index(near)
	if sub(sum(player), sum(computer)) == 0:
		return "Draw!"
	elif win == 0:
		return "You Win!"
	else:
		return "computer Win!"	


def blackjack():
	player_card = cards(2)
	print(f"Your Cards: {player_card}")
	computer_card = cards(2)
	print(f"Computer Cards: [{computer_card[0]}]")

	user_option = input("\n[ Type |y| for Another Card ]\n[ Type |n| for Pass\n>> ").lower()
	if user_option == "y":
		more_card = random.choice(all_cards)
		player_card.append(more_card)

	print(f"\nYour Final Cards: {player_card}")
	print(f"Computer Final Cards: {computer_card}")

	print(winner(player_card, computer_card))
	
	while True:
		user_option = input("\n[ Do You Want Play Game of BlackJack ]\nType |y| or |n|\n>> ").lower()
		if user_option == "y":
			replit.clear()
			print(logo())
			blackjack()
		elif	user_option == "n":
			break
    else:
      break

print(logo())
blackjack()

