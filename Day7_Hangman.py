from random import randint 

def if_false(life):
  if life == 1:
    print("  +---+  ")
    print("  |   |  ")
    print("  o   |  ")
    print("      |  ")
    print("      |  ")
    print("      |  ")
    print("      |  ")
    print("=========")
  elif life == 2:
    print("  +---+  ")
    print("  |   |  ")
    print("  o   |  ")
    print("  |   |  ")
    print("      |  ")
    print("      |  ")
    print("      |  ")
    print("=========")
  elif life == 3:
    print("  +---+  ")
    print("  |   |  ")
    print("  o   |  ")
    print(" /|   |  ")
    print("      |  ")
    print("      |  ")
    print("      |  ")
    print("=========")
  elif life == 4:
    print("  +---+  ")
    print("  |   |  ")
    print("  o   |  ")
    print(" /|\  |  ")
    print("      |  ")
    print("      |  ")
    print("      |  ")
    print("=========") 
  elif life == 5:
    print("  +---+  ")
    print("  |   |  ")
    print("  o   |  ")
    print(" /|\  |  ")
    print(" /    |  ")
    print("      |  ")
    print("      |  ")
    print("=========") 
  elif life == 6:
    print("  +---+  ")
    print("  |   |  ")
    print("  o   |  ")
    print(" /|\  |  ")
    print(" / \  |  ")
    print("      |  ")
    print("      |  ")
    print("=========") 



spelling = ["dhvip", "heril", "kenil", "fenil", "meet"]
for _ in range(len(spelling)):
  index = randint(0, len(spelling) - 1)
  spell = [i for i in spelling[index] ]
  print(spell)

