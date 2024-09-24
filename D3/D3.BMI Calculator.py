weight = int(input("What is your weight in pounds?\n"))
height = int(input("What is your height in inches?\n"))
bmi = weight * 703 / height ** 2
print(f"Your body mass index is", bmi)
if bmi >= 25:
    print("You are overweight.")
elif bmi >= 18.5:
    print("You are normal weight.")
else:
    print("You are underweight.")