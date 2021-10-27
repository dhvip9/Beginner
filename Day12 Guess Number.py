import random
life = 10


def logo():
	return """
 _______  __   __  _______  _______  _______    _______  _______  __   __  _______ 
|       ||  | |  ||       ||       ||       |  |       ||   _   ||  |_|  ||       |
|    ___||  | |  ||    ___||  _____||  _____|  |    ___||  |_|  ||       ||    ___|
|   | __ |  |_|  ||   |___ | |_____ | |_____   |   | __ |       ||       ||   |___ 
|   ||  ||       ||    ___||_____  ||_____  |  |   ||  ||       ||       ||    ___|
|   |_| ||       ||   |___  _____| | _____| |  |   |_| ||   _   || ||_|| ||   |___ 
|_______||_______||_______||_______||_______|  |_______||__| |__||_|   |_||_______|
	       """


def guess_status(guess_num, actual_num):
	"""Return Status of Guess"""
	raw = actual_num - guess_num
	if (raw < 5 and raw > 0) or (raw > -5 and raw < 0):
		return "[ Very Close! ]"	
	elif raw < 0:
		return "[ HIGH! ]"
	elif raw > 0:
		return "[ LOW! ]"	
	else:
		return f"\n[ You Did It! |{guess_num}| ]"


def life_reaming(guess_num, actual_num):
	global life 
	if guess_num != actual_num:
		life -= 1
	return life


print(logo())
print("[ Welcome To Number Guessing Game ]")
print("[ I'm Thinking of a Number Between |1 to 100|. ]")
difficulty_level = input("[ Choose Difficulty Level ]\n[ Type |e| Easy or |h| Hard ]\n>> ").lower()
actual_number = random.randint(1, 100)
print(actual_number)
if difficulty_level == "h":
	life = 5

while life != 0:
	print(f"\n[ You Have |{life}| Life Remaning ]")
	guess_number = int(input("[ Make a Guess ]\n>> "))
	Guess_status = guess_status(guess_number, actual_number)
	print(Guess_status)
	if Guess_status == f"\n[ You Did It! |{guess_number}| ]":
		break
	life = life_reaming(guess_number, actual_number)

if life == 0:
	print("\n[ YOU lOSE! ]")	

  
  
