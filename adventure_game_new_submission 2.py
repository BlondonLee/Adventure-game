# You can use this workspace to write and submit your adventure game project.
import time
import random


def print_pause(text):
    print(text)
    time.sleep(1)


def intro():
    print_pause("You find yourself standing in an open field,"
                " filled with grass and yellow wildflowers.")
    print_pause("Rumor has it that a wicked fairie is somewhere around here,"
                " and has been terrifying the nearby village.")
    print_pause("......")
    print_pause("In front of you is a house.")
    print_pause("To your right is a dark cave.")
    print_pause("In your hand you hold your trusty"
                " (but not very effective) dagger.")


def house(enemylist, weapon, enemy):
    print_pause("You knock on the door of the house")
    print_pause("You approach the door of the house.")
    print_pause(f"You are about to knock when the door"
                f" opens and out steps a {enemy}.")
    print_pause(f"Eep! This is the {enemy}'s house!")
    print_pause(f"The {enemy} attacks you!")
    print_pause(f"You feel a bit under-prepared for this,"
                " what with only having a tiny dagger.")


def cave(enemylist, weapon, enemy):
    if "Sword of Ogoroth" in weapon:
        print_pause("You peer cautiously into the cave.")
        print_pause("You've been here before, and gotten all the good stuff."
                    " It's just an empty cave now.")
        print_pause("You walk back out to the field.\n")
        adventure(enemylist, weapon, enemy)
    else:
        print_pause("You peer cautiously into the cave.")
        print_pause("It turns out to be only a very small cave.")
        print_pause("Your eye catches a glint of metal behind a rock.")
        print_pause("You have found the magical Sword of Ogoroth!")
        print_pause("You discard your silly old dagger"
                    " and take the sword with you.")
        print_pause("You walk back out to the field.\n")
        weapon[0] = "Sword of Ogoroth"
        adventure(enemylist, weapon, enemy)


def play_again(enemylist, weapon, enemy):
    while True:
        play_again = input("Would you like to play again? (y/n) \n")
        if play_again == "y".lower():
            print_pause("You run back into the field.\n")
            weapon[0] = "dagger"
            adventure(enemylist, weapon, enemy)
        elif play_again == "n".lower():
            print_pause("Goodbye!")
            exit(0)
        else:
            print_pause("Your entry is invalid, please try again.\n")
            adventure(enemylist, weapon, enemy)


def fight(enemylist, weapon, enemy):
    if "Sword of Ogoroth" in weapon:
        print_pause(f"As the {enemy} moves to attack,"
                    " you unsheath your new sword.")
        print_pause(f"The Sword of Ogoroth shines brightly in your hand"
                    "as you brace yourself for the attack.")
        print_pause(f"But the {enemy} takes one look at your"
                    " shiny new toy and runs away!")
        print_pause(f"You have rid the town of the gorgon."
                    " You are victorious!\n")
    else:
        print_pause("You do your best...")
        print_pause(f"but your dagger is no match for the {enemy}")
        print_pause("You have been defeated!")
        play_again(enemylist, weapon, enemy)


def adventure(enemylist, weapon, enemy):
    print_pause("Enter 1 to knock on the door of the house.")
    print_pause("Enter 2 to peer into the cave.")
    choice = input("What would you like to do?"
                   " (Please enter 1 or 2): \n")
    if choice == '1':
        house(enemylist, weapon, enemy)
        while True:
            action = input("Would you like to (1) fight"
                           " or (2) run away?: \n")
            if action == "1":
                fight(enemylist, weapon, enemy)
                play_again(enemylist, weapon, enemy)
            elif action == "2":
                print_pause("You walk back out to the field.\n")
                adventure(enemylist, weapon, enemy)
            else:
                print_pause("Your entry is invalid, please try again.\n")

    elif choice == '2':
        cave(enemylist, weapon, enemy)
    else:
        print_pause("Your entry is invalid, please try again.\n")
        adventure(enemylist, weapon, enemy)


def start_game():
    enemylist = ["pirate", "witch", "frankenstein", "Michael Myers"]
    weapon = ["dagger"]
    enemy = random.choice(enemylist)
    intro()
    adventure(enemylist, weapon, enemy)


start_game()
