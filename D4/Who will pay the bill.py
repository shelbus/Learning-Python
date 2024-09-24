print("Shelby asks, 'Who's paying the bill for dinner?")
import random
friends = ["Shelby" , "Hailie", "Chris", "Megan"]
who_pays_the_bill = random.choice (friends)
print(who_pays_the_bill)
if (who_pays_the_bill == "Shelby"):
    print("Me!")
else:
    print("Shelby says, 'Haha, suckers!")

#also could be print(random.choice(friends))
#OR random_index = random.randit(0 , 4) then print(friends[random_index])