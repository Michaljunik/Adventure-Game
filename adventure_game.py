# Camping game
import time
import random


def print_pause(story_text):
    print(story_text)
    time.sleep(2)


def print_long_pause(suspense_text):
    print(suspense_text)
    time.sleep(4)


def game_over():
    print_pause("The game has now ended, thank you for playing.")
    print_pause("Would you like to play again?")
    finish = input("Enter'y' to play again\n"
                   "Enter 'n' to close game\n")
    if finish == 'y':
        play_game()
    elif finish == 'n':
        exit()
    else:
        print_pause("Please enter 'y' or 'n'.")
        game_over()


def game_win():
    print_pause("You use the left over embers\n"
                "to build a favorable fire for cooking.")
    print_pause("You prepare the fish and season it to your liking.")
    print_pause("The fillet makes a satisfying sizzle when placed on the pan.")
    print_long_pause("Shortly after you smell the aromas\n"
                     "of a meal that is properly cooked.")
    print_long_pause("You sit back with your meal\n"
                     "and watch the sky blossom with orange as it sets.")
    game_over()


def game_lose():
    print_pause("You prepare your fish and place it on the pan.")
    print_long_pause("You wait as long as you can\n"
                     "before hunger convinces you your meal is ready.")
    print_pause("It wasn't the most satisfying or great tasting\n"
                "but you feel full.")
    print_long_pause("...later that night...")
    print_pause("You wake up in cold sweat, and feeling unwell!")
    print_pause("With your stomach churning,\n"
                "you make a dash out of your tent to the nearest bush!")
    print_long_pause("You have gotten sick from eating uncooked fish,\n"
                     "and you must cut your adventure short.")
    game_over()


def intro():
    print_long_pause("You're out camping in the woods.")
    print_pause("Exiting your tent from your mid-day nap.")
    print_pause("There is a gentle breeze that rustles the trees,\n"
                "and the smell of pine surrounds you.")
    print_pause("In the distance you hear the calming flow of a river.")
    print_pause("You feel yourself getting hungry,\n"
                "you must catch your dinner.")


# Option 1 Head over to river
def river_path(fish):
    print_pause("You head over to the river")
    # Fish has been caught
    if "caught_fish" in fish:
        print_pause("You have already acquired your fish.")
        print_pause("You stay just a little while to take in the view.")
    # Haven't caught fish yet
    else:
        print_pause("You bring your trusty fishing pole to the river,\n"
                    "and you cast your line.")
        print_long_pause("You wait...")
        print_long_pause("And you wait...")
        print_long_pause("Suddenly you feel a strong tug on your line.")
        print_pause("You pull the pole in the opposite direction,\n"
                    "and reel in your catch!")
        print_pause("As it comes closer you reach in and pull out a......")
        river_fish = ['Crappie', 'Trout', 'Bass']
        caught_fish = random.choice(river_fish)
        print_pause(caught_fish)
        fish.append("caught_fish")
    print_pause("You head back to the pathway.")
    story_pathway(fish)


# Option 2 Head over to the fire pit
def firepit_path(fish):
    # Fish has been caught
    if "caught_fish" in fish:
        print_pause("You approach the fire pit.\n"
                    "see that there are a few warm embers.")
        print_pause("Would you like to:\n"
                    "Build a fire to cook with?\n"
                    "Or cook with the few embers already in the fire pit?\n")
        cook = input("Enter '1' to build a fire\n"
                     "Enter '2' to cook with the remaining embers\n")
        if cook == '1':
            game_win()
        elif cook == '2':
            game_lose()
        else:
            print_pause("Please enter '1' or '2'.")
            firepit_path(fish)
    else:
        print_pause("You approach the fire pit,\n"
                    "however you have not caught your dinner yet.")
        print_pause("You leave the fireplace and go back to the pathway.")
        story_pathway(fish)


def story_pathway(fish):
    print_pause("Your pathway splits in two directions")
    print_pause("Enter 1 to go left headed for the river")
    print_pause("Enter 2 to go right towards the fire pit")
    path = input("1. river\n"
                 "2. fire pit\n")
    if path == '1':
        river_path(fish)
    elif path == '2':
        firepit_path(fish)
    else:
        print_pause("Please enter '1' or '2'.")
        story_pathway(fish)


def play_game():
    fish = []
    intro()
    story_pathway(fish)


play_game()
