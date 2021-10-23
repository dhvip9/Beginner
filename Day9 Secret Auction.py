from replit import clear

def logo():
	print("""
	______   __    __   ______   ________  ______   ______   __    __             
	/      \ |  \  |  \ /      \ |        \|      \ /      \ |  \  |  \            
	|  $$$$$$\| $$  | $$|  $$$$$$\ \$$$$$$$$ \$$$$$$|  $$$$$$\| $$\ | $$            
	| $$__| $$| $$  | $$| $$   \$$   | $$     | $$  | $$  | $$| $$$\| $$            
	| $$    $$| $$  | $$| $$         | $$     | $$  | $$  | $$| $$$$\ $$            
	| $$$$$$$$| $$  | $$| $$   __    | $$     | $$  | $$  | $$| $$\$$ $$            
	| $$  | $$| $$__/ $$| $$__/  \   | $$    _| $$_ | $$__/ $$| $$ \$$$$            
	| $$  | $$ \$$    $$ \$$    $$   | $$   |   $$ \ \$$    $$| $$  \$$$            
	\$$   \$$  \$$$$$$   \$$$$$$     \$$    \$$$$$$  \$$$$$$  \$$   \$$ 
		
	""")
	

def bid_winner(participate):
	win_amt = 0
	for key in participate:
		bid_amt = participate[key]
		if bid_amt > win_amt:
			win_amt = bid_amt
	print(f"<[ The Winner is | {key} | With a Bid of | ${win_amt} | ]>")		

logo()
print("Wellcome To Secret Auction")	

bid_participate = {}
continue_bid = True

while continue_bid:
	name = input("| What is your [ Name ]. |\n>> ")
	bid = int(input("| what is your [ Bid ].  |\n>> $")) 
	bid_participate[name] = bid
	print()
	next_bid = input("| Are there any other bidder? |\n[ Type |y| or |n| ].\n>> ").lower()
	if next_bid == "n":
		continue_bid = False
	elif next_bid == "y":
		continue_bid = True
		clear()
		logo()
		print("Wellcome To Secret Auction")
	else:
		print("Select Valid Option")	

clear()
logo()
bid_winner(bid_participate)
	

