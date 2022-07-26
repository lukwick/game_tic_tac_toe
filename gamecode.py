

# IMPORTED MODULES
# ------------------------------------------------------------

import random   # To randomise computer's choice
import time     # To allow to have pauses after printed text and computer's choices




# FUNCTIONS
# ------------------------------------------------------------

def explain_playing_field():
    print("""
    1 | 2 | 3
    ---------
    4 | 5 | 6
    ---------
    7 | 8 | 9
    """)


def show_playing_field():
    print_waiting_text("The field looks now like this:")
    
    print_waiting_text(f"""
    {field_display[0]} | {field_display[1]} | {field_display[2]}
    ---------
    {field_display[3]} | {field_display[4]} | {field_display[5]}
    ---------
    {field_display[6]} | {field_display[7]} | {field_display[8]}
    """,
    3) # 3 Seconds waiting time, otherwise it is too quick


def print_text(text):
    print("\n")
    print(text)
    print("\n")


def print_waiting_text(txt, seconds = 2):
    print("\n")
    print(txt)
    print("\n")
    time.sleep(seconds)


def press_enter():
    input("Press Enter to continue\n")


# Ensure to get an integer as input
def get_int():
    
    # Player can give any input
    choice = input("\nMake your choice, choose a number from 1 to 9:\n \n")
    time.sleep(1)

    # Player can leave the game
    if choice == "q":
        print_waiting_text("You want to leave the game?")
        print_waiting_text("OK. Goodbye! :)")
        quit()
        

    # If possible, input becomes an int
    try:
        choice = int(choice)
        return choice
    
    # If not possible, redo the input
    except ValueError:
        print_waiting_text("Wrong input, you have to choose a number from 1 to 9. Or you can press 'q' to leave the game.")
        return get_int()


def remove_option(field_spot):
    field_options.remove(field_spot)


def player_makes_choice():

    while True:
        # Player gives an input
        player_choice = get_int()

        # If choice is not available, help the player which options are left
        if player_choice not in field_options:
            print_waiting_text("Wrong input, you have to choose a number from 1 to 9, which is still free.")
            print_waiting_text("The following options are still available:")
            for x in field_options:
                print(x)
            continue
        
        # Choice is valid
        else:
            break
             
    print_waiting_text(f"You have choosen the {field_names[player_choice]}.")
    
    # Playing field and display field is updated
    field_invisible[player_choice-1] = 1
    field_display[player_choice-1] = "X"

    # Choice is removed from the left choices
    remove_option(player_choice)

    show_playing_field()


def computer_makes_choice():

    # Print "fake processing time"
    print_waiting_text("The computer is preparing its next move!")
    print_waiting_text("The computer is thinking ...")
    print_waiting_text("...")

    # Computer makes a random choice from the left over options
    computer_choice = int(random.choice(field_options)-1)
    print_waiting_text(f"The computer has choosen the {field_names[computer_choice+1]}.")

    # Update the playing field and display field
    field_invisible[computer_choice] = -1
    field_display[computer_choice] = "O"

    # Remove the option from the option list
    remove_option(computer_choice+1)

    show_playing_field()


def check_if_won(player):
    f = field_invisible
    # Rows / columns / diagonals
    if f[0] + f[1] + f[2] == 3 * player \
        or f[3] + f[4] + f[5] == 3 * player \
        or f[6] + f[7] + f[8] == 3 * player \
        or f[0] + f[3] + f[6] == 3 * player \
        or f[1] + f[4] + f[7] == 3 * player \
        or f[2] + f[5] + f[8] == 3 * player \
        or f[0] + f[4] + f[8] == 3 * player \
        or f[2] + f[4] + f[6] == 3 * player:
        return player




# VARIABLES
# ------------------------------------------------------------

field_invisible = [0 for i in range(9)]     # Field to save the current game situation

field_options = [i for i in range(1, 10)]   # Field options left to choose from
 
field_display = [" " for i in range(9)]     # Field to show the current game in a more presentable matter

field_names = {                             # Give more descriptive names for the field names
    1: "top left (position 1)",
    2: "top middle (position 2)",
    3: "top right (position 3)",
    4: "left middle (position 4)",
    5: "middle (position 5)",
    6: "right middle (position 6)",
    7: "bottom left (position 7)",
    8: "bottom middle (position 8)",
    9: "bottom right (position 9)"
     }




# THE GAME CODE
# ---------------------------------------------------------

## Introduction
## --------------------

print_text("WELCOME to Tic-Tac-Toe (TTT)! :)")
press_enter()

print_text("The game works as a normal TTT-game. You start with setting your 'X' against the computer 'O'.")
press_enter()

print_text("As usual, the field has 9 options. See the options below.\n\nOptions:")
press_enter()

explain_playing_field()
press_enter()

print_text("As you can see, this means if you want to put your 'X' e.g. in the top right corner, you have to select the number 3.")
press_enter()

print_text("The player, who has three in a row, column or diagonal first, wins.")
press_enter()

print_text("If you want to leave the game, type 'q' when it is your turn.")
press_enter()

print_text("Alright? Let's go! :)")
press_enter()



## THE ACTUAL GAME CODE
## --------------------

while True:

    player_makes_choice()    

    if check_if_won(1) == 1:
        print_waiting_text("You won the game! :-)")
        break

    # Check if field has space left
    if len(field_options) == 0:
        print_waiting_text("No space left, it's a draw!")
        break

    computer_makes_choice()

    if check_if_won(-1) == -1:
        print_waiting_text("The computer won the game! :-(")
        break


print_text("Game Ends")
