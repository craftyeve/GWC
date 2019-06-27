# --- Define your functions below! ---
def joke():
    input("What kind of androids do you find in the arctic? ")
    print("A snow-bot!")

def valid(answer):
    options = ['yes', 'Yes', 'yeah', 'yea']
    for a in options:
        if answer == a:
            return True

# --- Put your main program below! ---
def main():
    answer = input("(What will you say?) ")
    print("That's cool!")
    
print(valid("no"))


# DON'T TOUCH! Setup code that runs your main() function.
if __name__ == "__main__":
    main()