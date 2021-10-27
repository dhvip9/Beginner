import random
import replit
all_cards = [
	11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 
	11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 
	11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 
	11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10
            ]

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
	"""Return Nearest Number"""
	sort_list = [abs(value - number) for value in num_list]
	Index = sort_list.index(min(sort_list))
	return num_list[Index]	


def cards(number_cards):
	"""Return Random cards"""
	global card_2
	card_2 = [random.choice(all_cards) for _ in range(number_cards)]
	return card_2



def sub(num_1, num_2):
	"""Return subtraction of Two Number"""
	return num_1 - num_2


def winner(player, computer):
	"""Retrun winner"""
	total = [sum(player), sum(computer)]
	near = nearest_number(21,total)
	win = total.index(near)
	if sub(sum(player), sum(computer)) == 0:
		return "Draw!"
	elif sum(computer) == 21:
		return "Computer [ BlackJack ]!"
	elif sum(player) == 21:
		return "You [ BlackJack ]!"
	elif sum(computer) > 21:
		return "[ Computer Bust! ]\nYou Win! "
	elif sum(player) > 21:
		return "[ you Bust! ]\nComputer Win! "				
	elif win == 0:
		return "You Win!"
	else:
		return "computer Win!"	


def blackjack():
	print(logo())
	player_card = cards(2)
	print(f"Your Cards: {player_card}  =  Total [{sum(player_card)}]")
	computer_card = cards(2)

	# for computer extra card  
	while sum(computer_card) <= 15 and sum(computer_card) != 21:
		c_more_card = random.choice(all_cards)
		computer_card.append(c_more_card)
		if 11 in computer_card:
			if sum(computer_card) > 21:
				Index = computer_card.index(11)
				player_card[Index] = 1	

	print(f"Computer Cards: [{computer_card[0]}]")

	user_option = "h"
	while user_option != "s":
		user_option = input("\n[ Type |h| for HIT   ]\n[ Type |s| for STAND ]\n>> ").lower()
		if user_option == "h":
			p_more_card = random.choice(all_cards)
			player_card.append(p_more_card)
		elif user_option != "s" and user_option != "h":
			print("[ Enter Valid Option ]")
		# for check sum of card > 21
		if 11 in player_card:
			if sum(player_card) > 21:
				p_Index = player_card.index(11)
				player_card[p_Index] = 1 
		if sum(player_card) > 21:
			break	

		print(f"\nYour Cards: {player_card}  =  Total [{sum(player_card)}]")

       
	
	print(f"\nYour Final Cards: {player_card}  =  Total [{sum(player_card)}]")
	print(f"Computer Final Cards: {computer_card}  =  Total [{sum(computer_card)}]")

	print("\n"+ winner(player_card, computer_card))
	
	while True:
		user_option = input("\n[ Do You Want Play Game of BlackJack ]\nType |y| or |n|\n>> ").lower()
		if user_option == "y":
			replit.clear()
			blackjack()
		if	user_option == "n":
			break


blackjack()

