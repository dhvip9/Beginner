import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 
           'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n>> "))
nr_symbols = int(input(f"How many symbols would you like?\n>> "))
nr_numbers = int(input(f"How many numbers would you like?\n>> "))

l_password = ""
password_list = []
for _ in range(nr_letters):
  Ans = random.choice(letters)
  l_password += Ans

  password_list.append(random.choice(letters))

for _ in range(nr_symbols):
  Ans = random.choice(symbols)
  l_password += Ans

  password_list.append(random.choice(symbols))

for _ in range(nr_numbers):
  Ans = random.choice(numbers)
  l_password += Ans 

  password_list.append(random.choice(numbers)) 

random.shuffle(password_list)
s_password = ""
for p in password_list:
  s_password += p
print("-----------------------------------------------")
print("      |    Here is Your Password    |")
print(f"| light [ {l_password} ] | Strong [ {s_password} ] |")
