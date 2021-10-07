from random import randint

def pick(number):
  if number == 0:
    choice = '''
        _______
    ---'   ____)
          (_____)
          (ROCK_)
          (____)
    ---.__(___)
    '''
  elif number == 1:
    choice = '''
        _______
    ---'   ____)____
              ______)
              _PAPER_)
            _______)
    ---.__________)
    '''
  elif number == 2:
    choice = '''
        _______
    ---'   ____)____
              ______)
          _SCISSOR___)
          (____)
    ---.__(___)
    '''
  else:
    choice = """  [ Incorrect Choice! ]
-------------------------"""  
  return choice
 



def winner(player, computer):
  win = ""
  if player == 2 and computer == 1:
    win = "[ YOU WIN! ]"
  elif player == 1 and computer == 2:
    win = "[ YOU LOSE! ]"

  elif player == 1 and computer == 0:
    win = "[ YOU WIN! ]" 
  elif player == 0 and computer == 1:
    win = "[ YOU LOSE! ]"  

  elif player == 0 and computer == 2:
    win = "[ YOU WIN! ]"  
  elif player == 2 and computer == 0:
    win = "[ YOU LOSE! ]"

  else:
    win = "[ DRAW! ]"    
  
  return win 


print(" |                What Do You Choose?                 | ")
print(" TYPE [ 0 for ROCK ] [ 1 for PAPER ] [ 2 for SCISSOR ]  \n")
print("Exit from 'RPS' Write [ -1 ]")
# player = int(input(f"Enter Number\n>> "))

while True:
  player = int(input(f"Enter Number\n>> "))
  if player == -1:
    break
  while True:
    print()
    print("Player Choice")  
    print(pick(player), "\n\n")

    if player >= 3 or player <= -1:
      player = int(input(f"Enter Number\n>> "))
      
    else:  
      print("Computer Choice")
      computer = randint(0, 2)
      print(pick(computer))

      print(winner(player, computer))
      print("----------------------\n")
      break
