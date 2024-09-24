from typing import final

print("Welcome to the tip calculator!")
bill = float(input("What was the total bill?\n $"))
tip = int(input("What percentage tip would you like to give?\n"))
people = int(input("How many people are splitting the bill?\n"))
tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people
round(bill_per_person, 2)
final_amount = round(bill_per_person, 2)
print(f"Each person should pay ${final_amount}")