import random




def roll_dice():
    return random.randint(1,6)

def main():
    print("---Yo! Welcome to the Dice Rolling Simulator!----")
    ASK = input("Are you ready?")
    if ASK == "yes":
        print("Let's Start Fun :)")
        while True:
            result = roll_dice()
            print(f"\nResult ---> You roles a {result}! :)")

            while True:
                choice = input("Do you wanna roll again? (y or n)").lower()
                if choice in ["y","n"]:
                    break
                print("Invalid Input. Please enter y or n.")
            if choice == "n":
                print("Thanks you for playing !!! Goodbyee..have a nice day!")
                break
    else:
        print("Okay bye")




if __name__ == "__main__":
    main()

