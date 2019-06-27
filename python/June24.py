start = "I'm lonely and I need friends. Let's go find some!"

print(start)

keepplaying = "yes"

while keepplaying == "yes":
    location = input("Should I look for friends in the woods or in the river? ")
    if location == "woods":
        print("There are no friends here.")
        keepplaying = input("Try again? ")
    elif location == "river":
        print("There's a snake! Let's try to befriend it.")
        keepplaying = "next"
    else:
        print("That's not an option")
        keepplaying = input("Try again? ")
    if keepplaying == "no":
        quit()

keepplaying = "yes"
while keepplaying == "yes":
    snake = input("The snake wants food, do you want to get the snake food? ")
    if snake == "yes":
        print("You made a friend!")
        print("You now have 1 friend.")
        keepplaying = "next"
    elif snake == "no":
        print("The snake leaves, he isn't your friend.")
        keepplaying = input("Try again? ")
    else:
        print("That's not an option")
        keepplaying = input("Try again? ")
    if keepplaying == "no":
        quit()

keepplaying = "yes"
while keepplaying == "yes":
    morefriends = input("Do you want to make more friends? ")
    if morefriends == "yes":
        print("Let's go to the beach!")
        keepplaying = "next"
    elif morefriends == "no":
        print("Have fun with your 1 friend!")
        keepplaying = "no"
    else:
        print("That's not an option")
        keepplaying = input("Try again? ")
    if keepplaying == "no":
        quit()


    
