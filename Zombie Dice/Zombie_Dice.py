import random

Cup = ["Green", "Green", "Green", "Green", "Green", "Green", "Yellow", "Yellow", "Yellow", "Yellow", "Red", "Red", "Red"]
random.shuffle(Cup)

Hand = []
Score = 0
Shots = 0

Dice = {
    "Green": ["Brain", "Brain", "Brain", "Run", "Run", "Shot"],
    "Yellow": ["Brain", "Brain", "Run", "Run", "Shot", "Shot"],
    "Red": ["Brain", "Run", "Run", "Shot", "Shot", "Shot"]
    }

Choice = "Y"


# Slightly wrong but I'm just gonna keep it so you can see the dice colors beforehand
while Choice == "Y" and Shots < 3 and len(Cup)+len(Hand) >= 3 :
    while len(Hand) < 3:
        Hand.append(Cup.pop())

    print("Current Hand: " + str(Hand))

    Choice = input("Would you like to roll the dice? Y/N ")
    print("")

    if (Choice == "Y"):
        TempHand = Hand.copy()

        for item in Hand:
            x = Dice[item].copy()
            random.shuffle(x)
            print(x[0] + " (" + item + ")")

            if x[0] == "Brain":
                Score += 1
                TempHand.remove(item)
            elif x[0] == "Shot":
                Shots += 1
                TempHand.remove(item)
        
        Hand = TempHand.copy()

        print("")
        if Shots >= 3:
            print("Sorry! You've been shot too many times and your round is over. You score 0 points.")
        else:
            print("Current brains rolled: " + str(Score) + "\nCurrent shots rolled: " + str(Shots) + "\n\n--------------------------------------------\n")


if (Shots < 3):
    print("Congrats! You have scored " + str(Score) + " Points for the round!")