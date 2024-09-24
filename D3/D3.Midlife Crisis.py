print("Hello! Welcome to the rollercoaster!")
height = int(input("How tall are you in cm?\n"))
bill = 0
if height >= 120:
    print("Great! You can ride the rollercoaster.")
    age = int(input("How old are you?\n"))
    if age <= 12:
        bill = 5
        print("Child tickets are $5.")
    elif age <= 18:
        bill = 7
        print("Youth tickets are $7.")
    elif age >= 45 and age <= 55:
    #elif >= 45 and age <= 55: is ALSO correct and less wordy.
        print("Everything is going to be okay. Have a free ride on us.")
    else:
        bill = 12
        print("Adult tickets are $12.")

    wants_photo = input("Would you like a photo with your ride?\n")
    if wants_photo == "Yes":
        bill += 3

    print(f"Your final bill is ${bill}.")
else:
    print("Sorry, you aren't quite tall enough yet to ride.")