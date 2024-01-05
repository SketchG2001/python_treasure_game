# if the bill was Rs 150 split between 5 people, with 12% tip.
# Each person should pay (150/5)*1.20 = 33.6
# Round the result to 2 decimal places = 33.60

print("Welcome to the tip calculator")
bill = float(input("what was the total bill?: "))
tip = int(input("How much tip would you like to give? 10, 12, or 15?"))
people = int(input("How many people to split the bill?"))
bill_with_tip = tip/100*bill+bill
bill_per_person = bill_with_tip/people
final_amoun = "{:.2f}".format(bill_per_person)
print(f"each person should pay: {final_amoun}")
