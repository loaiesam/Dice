import random
one = 0
two = 0
three = 0
four = 0
five = 0
six = 0
while True:
    start_game = input("Do want to throw the Dice?: ").lower()
    if start_game == "yes":
        while True:
            random_number = random.randint(0, 5)
            if random_number == 0:
                print("One")
                one += 1
            elif random_number == 1:
                print("Two")
                two += 1
            elif random_number == 2:
                print("Three")
                three += 1
            elif random_number == 3:
                print("Four")
                four += 1
            elif random_number == 4:
                print("Five")
                five += 1
            else:
                print("Six")
                six += 1
            break;
    elif start_game == "no":
        print("You got One", one,"times.")
        print("You got Two", two,"times.")
        print("You got Three", three,"times.")
        print("You got Four", four,"times.")
        print("You got Five", five,"times.")
        print("You got Six", six,"times.")
        break
    else:
        print("Invalid Mode")
        pass
print("Thank you for playing")
