alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ','+', '-', '*', '/', '"', ',', 'X', '_', '.', '(', ')', '[', ']', '%', '?', '{', '}', '!', "'", "=", ":", "^", '1', '2', '3', '4', '5', '6', '7', '8', '9', '0' ]
 
len_char = len(alphabet) - 1

def encrypt(plan_text, key):
	index = 0
	raw_index = 0
	encode_text = ""
	for letter in plan_text:
		index = alphabet.index(letter)
		if len_char - index < key:
			raw_index = key - (len_char - index)
			index = raw_index - 2 
			encode_text += alphabet[index]
		else:	
			encode_text += alphabet[index + key]
	print(f"\nEncrypt Text | {encode_text} |") 
	


def decrypt(plan_text, key):
	index = 0
	decode_text = ""
	for letter in plan_text:
		index = alphabet.index(letter)
		if index < key:
			raw_index = (index + len_char) - key
			index = raw_index + 2 
			decode_text += alphabet[index]
		else:			
			decode_text += alphabet[index - key]
	print(f"\nDecrypt Text | {decode_text} |")


print(""" 
    ______      ____            ______          __        
   / ____/___  / __ \___       / ____/___  ____/ /__      
  / __/ / __ \/ / / / _ \     / /   / __ \/ __  / _ \     
 / /___/ / / / /_/ /  __/    / /___/ /_/ / /_/ /  __/     
/_____/_/ /_/_____/\___/     \____/\____/\__,_/\___/      
                                                          
      """)
while True:
	direction = input("Type [encode] to Encrypt, Type [decode] to Decrypt:\nType [exit] to Exit\n>> ").lower()
	
	if direction == "exit":
		print("[ Thank You! ]")
		break
	elif direction == "encode":
		text = input("[ Type Your Message ]\n>> ").lower()
		shift = int(input("[ Type The Key ]\n>> "))
		if shift > len_char -1:
			shift %= len_char
		encrypt(text, shift)
	elif direction == "decode":	
		text = input("[ Type Your Message ]\n>> ").lower()
		shift = int(input("[ Type The Key ]\n>> "))
		if shift > len_char -1:
			shift %= len_char		
		decrypt(text, shift)	
	else:
		print("[ Select Valid Item ] ")
	print()
