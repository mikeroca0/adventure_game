import time
import random


# Print pause function.
def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(0)


# Play again feature.
def play_again():
    while True:
        again = input("Do you want to play again? (1) yes or (2) no\n")
        if again == "1":
            print_pause("Great! Restarting the game...")
            main()
        elif again == "2":
            print_pause("Thanks for playing! See you next time.")
            exit(0)
        else:
            play_again()


# Setting the stage with the introduction.
def intro(item, option):
    print_pause("You find yourself standing in an open field, filled with grass and yellow wildflowers.")
    print_pause("Rumor has it that a " + option + " is somewhere around here, and has been terrifying the nearby village.")
    print_pause("In front of you is a house.")
    print_pause("To your right is a dark cave.")
    print_pause("In your hand you hold your trusty (but not very effective) dagger.")


# The cave scene, including the option to find the spear.
def cave(item, option):
    if "spear" in item:
        print_pause("You have already been here. There is nothing left to be found.")
        print_pause("You walk back to the field.")
    else:
        print_pause("You find yourself standing in a dark, wet cave")
        print_pause("In the corner of your eye, you can see something sparkle")
        print_pause("As you approach the sparkling object, you realize that you have found the legendary Spear of Doom!")
        print_pause("You ditch your trusty dagger and take the spear with you.")
        print_pause("You walk back to the field.")
        item.append("spear")
    field(item, option)


# The house scene, including the option to fight or run away.
def house(item, option):
    print_pause("You approach the door of the house.")
    print_pause("You are about to knock when the door opens and out steps a " + option + "!")
    print_pause("Raaaaawr! Oh no! This is the " + option + ("'s house!"))
    print_pause("The " + option + " lunges forward and tries to attack you.")
    while True:
        choice2 = input("Be quick! Would you like to (1) fight or (2) run away?\n")
        if choice2 == "1":
            if "spear" in item:
                print_pause("As the " + option + " moves to attack, you unsheath your new legendary spear.")
                print_pause("The Spear of Doom shines brighty in your hand as you brace yourself for the attack.")
                print_pause("But the " + option + " takes one look at your sparkly new weapon and runs away!")
                print_pause("You have rid the town of the " + option + ". You are victorious!")
                play_again()
            else:
                print_pause("You do your best to fight off the " + option + "...")
                print_pause("but your dagger is no match for the " + option + ".")
                print_pause("You have been defeated!")
                play_again()
        if choice2 == "2":
            print_pause("You run back into the field. Luckily you don't seem to have been followed...for now.")
            field(item, option)


# The beginning field scene, which acts as a start for the game.
def field(item, option):
    print_pause("Enter 1 to knock on the door of the house.")
    print_pause("Enter 2 to peer into the cave.")
    print_pause("What would you like to do?")
    while True:
        choice1 = input("(Please enter 1 or 2)\n")
        if choice1 == "1":
            house(item, option)
            break
        elif choice1 == "2":
            cave(item, option)
            break


# Function to start the game.
def main():
    item = []
    option = random.choice(["wicked fairie", "pirate", "dragon", "ghoul", "ghost", "troll"])
    intro(item, option)
    field(item, option)


main()
