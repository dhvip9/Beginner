import random
from replit import clear
Score = 0

celebrity = [
	   {
		'name': 'Dhvip patel, a Developer, from India',
		'follower_count' : 50000000,
		'description': 'Web Developer',
		'country': 'india' 
	   },
	   {
        'name': 'Ariana Grande',
        'follower_count': 27300000,
        'description': 'Musician and actress',
        'country': 'United States'
	   },
	   {
        'name': 'Cristiano Ronaldo',
        'follower_count': 48600000,
        'description': 'Footballer',
        'country': 'Portugal'	
	   },
	   {
        'name': 'Instagram,',
        'follower_count': 34600000,
        'description': 'Social media platform',
        'country': 'United States'
       },
	   {
        'name': 'Dwayne Johnson',
        'follower_count': 18100000,
        'description': 'Actor and professional wrestler',
        'country': 'United States'
    },
    {
        'name': 'Selena Gomez',
        'follower_count': 17400000,
        'description': 'Musician and actress',
        'country': 'United States'
    },
    {
        'name': 'Kylie Jenner',
        'follower_count': 17200000,
        'description': 'Reality TV personality and businesswoman and Self-Made Billionaire',
        'country': 'United States'
    },
    {
        'name': 'Kim Kardashian',
        'follower_count': 16700000,
        'description': 'Reality TV personality and businesswoman',
        'country': 'United States'
    },
    {
        'name': 'Lionel Messi',
        'follower_count': 27700000,
        'description': 'Footballer',
        'country': 'Argentina'
    },
    {
        'name': 'Beyoncé',
        'follower_count': 14500000,
        'description': 'Musician',
        'country': 'United States'
    },
    {
        'name': 'Neymar',
        'follower_count': 13800000,
        'description': 'Footballer',
        'country': 'Brasil'
    },
    {
        'name': 'National Geographic',
        'follower_count': 13500000,
        'description': 'Magazine',
        'country': 'United States'
    },
    {
        'name': 'Justin Bieber',
        'follower_count': 13300000,
        'description': 'Musician',
        'country': 'Canada'
    },
    {
        'name': 'Taylor Swift',
        'follower_count': 13100000,
        'description': 'Musician',
        'country': 'United States'
    },
    {
        'name': 'Kendall Jenner',
        'follower_count': 12700000,
        'description': 'Reality TV personality and Model',
        'country': 'United States'
    },
    {
        'name': 'Jennifer Lopez',
        'follower_count': 11900000,
        'description': 'Musician and actress',
        'country': 'United States'
    },
	    {
        'name': 'Nicki Minaj',
        'follower_count': 11300000,
        'description': 'Musician',
        'country': 'Trinidad and Tobago'
    },
    {
        'name': 'Nike',
        'follower_count': 10900000,
        'description': 'Sportswear multinational',
        'country': 'United States'
    },
    {
        'name': 'Khloé Kardashian',
        'follower_count': 10800000,
        'description': 'Reality TV personality and businesswoman',
        'country': 'United States'
    },
    {
        'name': 'Miley Cyrus',
        'follower_count': 10700000,
        'description': 'Musician and actress',
        'country': 'United States'
    },
    {
        'name': 'Katy Perry',
        'follower_count': 9400000,
        'description': 'Musician',
        'country': 'United States'
    }
]

def logo(serial_num):
	if serial_num == 1:
		logo = """
    __  ___       __             
   / / / (_)___ _/ /_  ___  _____
  / /_/ / / __ `/ __ \/ _ \/ ___/
 / __  / / /_/ / / / /  __/ /    
/_/ ///_/\__, /_/ /_/\___/_/     
   / /  /____/_      _____  _____
  / /   / __ \ | /| / / _ \/ ___/
 / /___/ /_/ / |/ |/ /  __/ /    
/_____/\____/|__/|__/\___/_/     
"""
	if serial_num == 2:
		
		logo = """                   _    __    
                  | |  / /____
                  | | / / ___/
                  | |/ (__  ) 
                  |___/____(_)
"""
	return logo


def compare(person_1, person_2):
	"""Return greater person"""
	if person_1 > person_2:
		return "a"
	elif person_1 < person_2:
		return "b"
	else:
		return "error"


def score(raw_score):
	"""Return score"""
	return raw_score + 1

 
def index_checking(sqence):
	global celebrity
	while sqence[0] == sqence[1]:
		sqence.remove(sqence[1])
		sqence.append(random.randint(0, len(celebrity) - 1))

print(logo(1))

Index = [random.randint(0, len(celebrity) - 1) for i in range(2)]
index_checking(Index)
check_index = Index

while True:
	a_person = celebrity[Index[0]]
	b_person = celebrity[Index[1]]
	Ans = compare(a_person["follower_count"], b_person["follower_count"])
	print(Ans)

	print(f"[ Compare A: {celebrity[Index[0]]['name']}, a{celebrity[Index[0]]['description']}, from {celebrity[Index[0]]['country']} ]")
	print(logo(2))
	print(f"[ Against B: {celebrity[Index[1]]['name']}, a{celebrity[Index[1]]['description']}, from {celebrity[Index[1]]['country']} ]")
	
	user_ans = input("\nWho Has More Follower ?\n[ Type |a| or |b| ]\n>> ").lower()
	if Ans == user_ans:
		Score = score(Score)
		clear()
		print(f"Your Right! current Score {Score}")
		if Ans == "a":
			Index.remove(Index[1])
		else:
			Index.remove(Index[0])
		Index.append(random.randint(0, len(celebrity) - 1))
		index_checking(Index)
	else:
		break
clear()
print(logo(1))		
print(f"Final Score [{Score}]")
