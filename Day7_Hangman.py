import random 
from replit import clear 

def if_life(life):
    if life == 5:
      draw = '''
          +---+  
          |   |  
          o   |  
              |  
              |  
              |  
              |  
        =========
            '''
    elif life == 4:
      draw = '''
          +---+  
          |   |  
          o   |  
          |   |  
              |  
              |  
              |  
        =========
            '''
    elif life == 3:
      draw = '''
          +---+  
          |   |  
          o   |  
         /|   |  
              |  
              |  
              |  
        =========
            '''
    elif life == 2:
      draw = '''
          +---+  
          |   |  
          o   |  
         /|\\  |  
              |  
              |  
              |  
        =========
            '''
    elif life == 1:
      draw = '''
          +---+  
          |   |  
          o   |  
         /|\\  |  
         /    |  
              |  
              |  
        =========
            '''
    elif life == 0:
      draw = '''
          +---+  
          |   |  
          o   |  
         /|\\  |  
         / \\  |  
              |  
              |  
        =========
            '''
    else:
      draw = '''
          +---+  
          |   |  
              |  
              |  
              |  
              |  
              |  
        =========
            '''         
    return draw

print('''
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/      
      ''')

words = ["dhvip", "ardvark", "acknowledgement", "enclose", "baboon", "camel", "furore", "glamor", "judgement", "lambast", "lynchpin", "omelet", "theater", "woolen", "yoghurt"]

spelling = list(random.choice(words))
copy_spell = " ".join(spelling)
print(copy_spell)

find_word = []
for i in range(len(spelling)):
  find_word.append("_")

Life = 6
while True:
    user_letter = input("Guess a Letter :- ").lower()
    clear()
    Index = 0

    if user_letter in find_word:
        print(f"You've Already Guessed {user_letter}")     
    elif user_letter not in spelling:
        print(f"You Guessed {user_letter}, That's Not in Word. You Lose a Life")
        Life -= 1 
   

    for i in spelling:
      if i == user_letter:
        Index = spelling.index(i)
        spelling[Index] = "0"
        find_word[Index] = i
  
    final_word = " ".join(find_word)
    print(f"[  {final_word}  ]")

    print(if_life(Life))
  
    if final_word == copy_spell:
      print("[ YOUR MAN SAVED! ]")
      break
    elif Life == 0:
      print("[ YOUR MAN DIED! ]")
      break
      
    print("+--------------------------------------------------+") 
