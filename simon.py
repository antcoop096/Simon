from os import system
from time import sleep
from random import randint
from keyboard import read_key

menu_text = """
🟩 🟥
SIMON
🟨 🟦

Start - 1
How To Play - 2
Quit - 3
"""

instructions_text = """
HOW TO PLAY:

The game will start after the countdown.

At first, a single color will be flashed to
the screen, either red, blue, green, or yellow.

After the color is flashed you must press
the correct button on your keyboard that
represents the flashed color:
🔴 = R
🔵 = B
🟢 = G
🟡 = Y

If you guess the color correcly, the color
will be breifly flashed to the screen, a thumbs-up emoji
will be shown, and the next round will begin.

Each round will add a new color to the sequence.

You must press the buttons in the correct order 
of the sequence to advance to the next round.

For Example:
Round 1 sequence: 🔴 
Correct guess: r
Round 2 sequence: 🔴🔵
Correct guess: rb
Round 3 sequence: 🔴🔵🔵
Correct guess: rbb
...

Guessing a color in the sequence incorrectly will
end the game, and your score will be the number of rounds 
you have previously and successfully completed.

PLEASE NOTE: before entering the guess for the next color in
the sequence, wait until the color of the previous guess is
no longer breifly flashed to the screen.

Start - 1
Quit - 2
"""

selection = '' #stores user selection

def menu(): #prints menu
    global selection
    print(menu_text)
    selection = read_key()
    system('cls')

def not_an_option(): #prints if user inputs invalid selection
    system('cls')
    print('That is not an option. Please try again.')
    sleep(2)
    system('cls')

def instructions(): #prints game instructions
    global selection, instructions_text
    selection = '' 
    while True:         
        print(instructions_text)
        sleep(0.47)
        selection = read_key()
        if selection in ['1','2']: #runs if user selection is valid
            system('cls')
            break
        not_an_option() #if user selection is not valid, prints message telling user to try again, and continues the loop
    if selection == '2': #switch selection from '2' to '3' for line 168
        selection = '3'

def countdown(): #counts down to the first round of a game
    for number in [3,2,1]:
        print(number)
        sleep(0.87)
        system('cls')
    sleep(0.87)

colors_dic = {'r': '🔴', #colors representing keyboard buttons
              'b': '🔵',
              'g': '🟢',
              'y': '🟡'}
colors_list = [color for color in colors_dic] #list of keyboard buttons [r,b,g,y]
sequence = [] #stores the current sequence of a game
is_game_over = False #True if game is still going, False otherwise

def show_sequence(): #shows sequence to player before they guess
    for color in sequence:
        print(colors_dic[color])
        sleep(1)
        system('cls')
        print('')
        sleep(0.05)
        system('cls')

def game_round(): #runs through a single round of a game
    next_color = colors_list[randint(0,3)]
    sequence.append(next_color) #adds a new color to the end of the sequence

    show_sequence() #shows sequence to player

    global is_game_over
    for color in sequence: #the user guesses each color of the sequence in order
        while True:
            guess = read_key() #guess for a single color
            if guess.lower() == color: #correct guess
                system('cls')
                print(colors_dic[color]) #flashes color represented by pressed button
                sleep(0.13)
                system('cls')
                break
            elif guess in colors_list:
                is_game_over = True #ends the game if guess is incorrect
                break
        if is_game_over: 
            break

    if not is_game_over: #user guesses the entire sequence, advancing to the next round
        print('👍')
        sleep(2)
        system('cls')                  

def game_over(): #runs if game ends
    global sequence, is_game_over, selection
    game_over_message = f'GAME OVER\nScore: {len(sequence) - 1}\n\nPlay Again - 1\nHow To Play - 2\nQuit - 3\n'
    sequence = [] #resets the sequence and sets is_game_over to False for next game
    is_game_over = False

    while True: 
        print(game_over_message) #prints game over menu
        sleep(0.5)
        selection = read_key() #user selects if they want to play again, read the game instructions, or quit
        if selection in ['1','2','3']: #runs if selection is valid
            system('cls')
            break
        else: #if the user inputs an invalid selection, a message is printed telling the user to try again
            not_an_option()
            continue

#Structure of game
menu()
while True:
    if selection == '1': #plays game
        countdown()
        while not is_game_over:
            game_round()

        game_over() 
        continue

    elif selection == '2': #displays instructions
        instructions() 

    elif selection == '3': #quits the game
        break 

    else: #if user selection is invalid, a message is printed telling the user to try again
        not_an_option()
        menu() 
        continue
