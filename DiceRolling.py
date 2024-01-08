import random

DiceRolling = True;

while DiceRolling:
    answer = input("Do You Want To Rolling [Y/n] :").lower();
    if answer == "y" or answer == "yes":
        DiceNumber = random.randint(1, 6);

        print(f"Your Dice Number is {DiceNumber}");
        continue;

    else:
        print("Game Over");
        break;