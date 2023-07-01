print("Welcome to the tip calculator.")
total_bill = input("What was the total bill? $")
f_total_bill = float(total_bill)
percentage_tip = input("What percentage tip would you like to give? ")
int_percentage_tip = int(percentage_tip)
split_bill = input("How many people to split the bill? ")
int_split_bill = int(split_bill)
each_person_pay = (f_total_bill + (f_total_bill*(12/100)))/int_split_bill
rounding_bill = round(each_person_pay,2)
final_amount = "{:.2f}".format(rounding_bill)
print(f"Each person should play: ${final_amount}")


