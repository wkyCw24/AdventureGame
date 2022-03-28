import time
import random
name = random.choice(["Dragon", "Gorgon", "Wicked fairie", "Troll", "Pirate"])
items = []


def print_pause(messages):
    print(messages)
    time.sleep(2)


def valid_input(prompt, option1, option2):
    while True:
        response = input(prompt).lower()
        if response == option1:
            return response
        elif response == option2:
            return response
    print_pause(prompt)


def main():
    print_pause("You find yourself standing in an open field, "
                "filled with grass and yellow wildflowers.")
    print_pause(f"Rumor has it that {name} is somewhere around here, "
                "and has been terrifying the nearby village.")
    print_pause("In front of you is a house.")
    print_pause("To your right is a dark cave.")
    print_pause("In your hand you hold your trusty "
                "(but not very effective) dagger.\n")
    field()


def battle():
    response = valid_input("Would you like to (1) fight or (2) run away?",
                           "1", "2")
    if response == "1":
        fight()
    if response == "2":
        print_pause("You run back into the field."
                    "Luckily, you don't seem to have been followed.")
        field()


def play_again():
    choice = valid_input("Would you like to play again?(y/n)\n",
                         "y", "n").lower()
    if choice == "y":
        print_pause("Excellent! Restarting the game ...")
        main()
    if choice == "n":
        print_pause("Thanks for playing! See you next time.")


def fight():
    if "sword" in items:
        print_pause(f"As the {name} moves to attack,"
                    "you unsheath your new sword.")
        print_pause("The Sword of Ogoroth shines brightly in your hand"
                    "as you brace yourself for the attack.")
        print_pause(f"But the {name} takes one look at your"
                    "shiny new toy and runs away!")
        print_pause(f"You have rid the town of the {name}."
                    "You are victorious!")
    else:
        print_pause("You do your best...")
        print_pause(f"but your dagger is no match for the {name}.")
        print_pause("You have been defeated!")
        print_pause("GAME OVER")
    play_again()


def cave():
    if "sword" in items:
        print_pause("You peer cautiously into the cave.")
        print_pause("You've been here before, and gotten all the good stuff.")
        print_pause("It's just an empty cave now.")
        print_pause("You walk back out to the field.")
        field()
    else:
        print_pause("You peer cautiously into the cave.")
        print_pause("It turns out to be only a very small cave.")
        print_pause("Your eye catches "
                    "a glint of metal behind a rock.")
        print_pause("You have found the magical Sword of Ogoroth!")
        print_pause("You discard your silly old dagger "
                    "and take the sword with you.")
        items.append("sword")
        print_pause("You walk back out to the field.")
    field()


def field():
    print_pause("Enter 1 to knock on the door of the house.")
    print_pause("Enter 2 to peer into the cave.")
    print("What would you like to do?")
    response = valid_input("(Please enter 1 or 2.)\n", "1", "2")
    if response == "1":
        house()
    elif response == "2":
        cave()


def house():
    print_pause("You approach the door of the house.")
    print_pause("You are about to knock "
                f"when the door opens and out steps a {name}.")
    print_pause(f"Eep! This is {name}'s house!")
    print_pause(f"The {name} attacks you!")
    if "dagger" in items:
        print_pause("You feel a bit under-prepared for this,"
                    "what with only having a tiny dagger.")
        battle()
    else:
        battle()


main()
