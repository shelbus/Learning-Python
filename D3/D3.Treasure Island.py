print("Welcome to your adventure!")
print("Your mission, should you choose to accept, is to find escape the island, and, perhaps, find some treasure.")
name = input("What is your name?\n")
print(f"Let's begin, {name} !")
print("Imagine you are on a boat in the ocean. The boat's motor broke so you drifted to a nearby island. ")
choice_1 = input("After arriving at the island, you take a look around and figure you'll walk around the island. "
                 "Which direction would you like to go?\n").lower()
if choice_1 == "right":
    choice_2 = input("After walking along the beach for some time, "
                     "you are blocked by a line of turtles wielding swords. "
                     "Would you like to swim around them or ask them for help?\n").lower()
    if choice_1 == "right" and choice_2 == "ask for help":
        print("They seem friendly enough. Besides, how fast can turtles with swords move??")
        print("You ask the turtles for directions. They tell you they carry swords because they "
              "idolize the Teenage Mutant Ninja Turtles, but they don't actually know how to use them, "
              "nor do they want to.")
        choice_3 = input("The turtles offer you three options to escape the island. They can repair your boat, "
                     "build you a dingy, or call the National Guard. "
                     "Which option would you choose?\n").lower()
        if choice_3 == "repair my boat".lower():
            print("Fantastic! They repaired your boat's motor and you are on your way off Turtle with Swords Island.")
            print("They also gave one of their sweet samurai swords as a token of appreciation for not eating them.")
        elif choice_3 == "build a dingy".lower():
            print("Turtles can't build a dingy, silly. You wait forever for them to build you a dingy "
                  "They do not. You die.")
        elif choice_3 == "call the National Guard".lower():
            print("The National Guard does not accept long distance phone calls. You die.")
        else:
            print("A sharknado erupts and sweeps you into oblivion. You die.")
    else:
        print("There was a shark waiting in the water. You die.")
else:
    print("You fall into a hole. You die.")