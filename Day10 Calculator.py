def logo():
	print("""
 .----------------.   .----------------.   .----------------.   .----------------. 
| .--------------. | | .--------------. | | .--------------. | | .--------------. |
| |     ______   | | | |      __      | | | |   _____      | | | |     ______   | |
| |   .' ___  |  | | | |     /  \     | | | |  |_   _|     | | | |   .' ___  |  | |
| |  / .'   \_|  | | | |    / /\ \    | | | |    | |       | | | |  / .'   \_|  | |
| |  | |         | | | |   / ____ \   | | | |    | |   _   | | | |  | |         | |
| |  \ `.___.'\  | | | | _/ /    \ \_ | | | |   _| |__/ |  | | | |  \ `.___.'\  | |
| |   `._____.'  | | | ||____|  |____|| | | |  |________|  | | | |   `._____.'  | |
| |              | | | |              | | | |              | | | |              | |
| '--------------' | | '--------------' | | '--------------' | | '--------------' |
 '----------------'   '----------------'   '----------------'   '----------------' 

	      """)
def add(num_1, num_2):
	"""Return Addition of Two Number"""
	return num_1 + num_2

def sub(num_1, num_2):
	"""Return subtraction of Two Number"""
	return num_1 - num_2
	
def multi(num_1, num_2):
	"""Return Multiplication of Two Number"""
	return num_1 * num_2	

def div(num_1, num_2):
	"""Return Division of Two Number"""
	return num_1 / num_2

opt = {
	"+": add,
	"-": sub,
	"*": multi,
	"/": div
}

def Answer(value_1, operation, value_2):
	"""Return Answer"""	
	operator = opt[operation]
	return operator(value_1,value_2)

		
def Calcu():
	ans = 0
	first_num = float(input("| Enter First Number |\n>> "))
	
	old_ans = True		
	while old_ans:
		print("[ '+', '-', '*', '/' ]")
		operator = input("Pick an Operation\n>> ")
		sec_num = float(input("| Enter Second Number |\n>> "))		
		ans = Answer(first_num, operator, sec_num)
		print(f"<[ {first_num} {operator} {sec_num} = {ans} ]>\n")

		option= input(f"[ Type |y| Continue Calculating with {ans} ]\n[ Type |n| Start New Calculation ]\n[ Type |e| For Exit ]\n>> ").lower()
		if option == 'y':
			first_num = ans
		elif option == 'n':
			Calcu()
		elif option == 'e':
			break	
		else:
			print("Enter Valid Option")
			break
      

logo()
Calcu()	  
