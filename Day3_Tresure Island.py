print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

direction = input("You're at a cross road. Where do you wnat go? Type [ left or right ]\n>> ")
direction = direction.lower()

if direction == "left": 
  step = input("You come lake. There is a island in the middle of the lake.\nType [wait] to wait for boat. Type [swim] to swim across.\n>> ")
  step = step.lower()
  
  if step == "wait":
    door = input("You arrive at the island unharmed.\nThere is a house with 3 doors. One RED, one YELLOW and one BLUE. Which colour do you choose?\n>> ")
    door = door.lower()
    
    if door == "yellow":
      print("[ YOU WIN! ]")
    elif door == "blue":
      print("You Enter a Room of Beasts.")
      print("      [ GAME OVER! ]       ") 
    elif door == "red":
      print("You Enter a Room of Fire.")
      print("     [ GAME OVER! ]      ")
    else:
      print("     [ GAME OVER! ]      ")  

  else:
    print("You Attacked by Trout")
    print("   [ GAME OVER! ]    ") 

else:
    print("You Fall Into a Hole.")
    print("   [ GAME OVER! ]    ") 
