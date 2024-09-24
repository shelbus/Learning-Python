print("Welcome to Python Pizza Deliveries!")
bill = 0
size = input ("What size pizza would you like? Small, Medium or Large:?\n")
if size == "Small":
    bill += 15
    print(f"Got it, a small pizza. That is $ {bill}")
if size == "Medium":
    bill += 20
    print(f"Got it, a medium pizza. That is $ {bill}")
if size == "Large":
    bill += 25
    print(f"Got it, a large pizza. That is ${bill}")
pepperoni = input ("Would you like pepperoni on your pizza? Yes or No:\n")
if pepperoni == "Yes":
    if size == "Small":
            bill += 2
    else:
        bill += 3
extra_cheese = input ("Would you like extra cheese? Yes or No:\n")
if extra_cheese == "Yes":
        bill += 1
tax = (bill * .10)
tip = input("Would you like to tip? If yes, what percent?\n")
if tip == "Yes":
    bill * tip
total_bill = round(bill * tax, 2)
print (f"Your total bill is ${total_bill}.")