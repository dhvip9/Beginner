total_amount = float(input("Welcome to the tip Calculator\nWhat was the total bill?\n>> $"))
perc_tip = float(input("What percentage tip would you like to give?\n>> %"))
total_person = float(input("How person should pay?\n>> "))    
payable_amt = ( total_amount + ( total_amount * perc_tip / 100 ) ) / total_person   
print(f"Each person should pay:[ {round(payable_amt,2)} ]")
