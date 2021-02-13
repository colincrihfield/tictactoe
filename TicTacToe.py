#! python3

import pprint
import random

# Create blank board tracker
board = {'top-l': ' ', 'top-m': ' ', 'top-r': ' ',
         'mid-l': ' ', 'mid-m': ' ', 'mid-r': ' ',
         'bot-l': ' ', 'bot-m': ' ', 'bot-r': ' ',}


# Print board function
def printBoard(b):
    print(b['top-l'], '|', b['top-m'], '|', b['top-r'])
    print('--+---+--')
    print(b['mid-l'], '|', b['mid-m'], '|', b['mid-r'])
    print('--+---+--')
    print(b['bot-l'], '|', b['bot-m'], '|', b['bot-r'])


# Player name and marker selection
def name_and_mark_select(mode):
    if mode == 'multiplayer':
        print('Player 1, what is your name?')
        p1 = input()
        print(p1, 'please select your marker. It must be a single character.')
        while True:
            p1m = str(input())
            p1m = p1m.upper()
            if len(p1m) == 1:
                break
            else:
                print('Sigh....', p1 + '.', 'I said a SINGLE character. Try again.')
        print('Player 2, it\'s your turn. What should I call you?')
        p2 = input()
        print(p2, 'please select your marker. It must be a single character.')
        while True:
            p2m = str(input())
            p2m = p2m.upper()
            if len(p2m) == 1:
                break
            else:
                print(p2 + '.', 'You watched', p1, 'do this and still messed it up? Try again.')
        playerbook = {1: {'name': p1, 'mark': p1m}, 2: {'name': p2, 'mark': p2m}}
    else:
        print('Under construction')
    return playerbook


# Player turn handling
def turn(player, playerbook):
    # Make sure their move input format is correct
    while True:
        move = str(input())
        if move in board and board[move] == ' ':
            break
        elif move not in board:
            print('''Please enter your move in the following format.
                  top-, mid-, bot- for "row"
                  -l, -m, -r for "column"\nExample: "top-r" for top right space.''')
        else:
            print('That space is already taken. Please enter an open space.')
    # Execute move in board
    board[move] = playerbook[player]['mark']

        
# Win condition checking
def wincheck(playerbook):
    # Create list of board values
    listboard = []
    for x in board.values():
        listboard.append(x)
    # Horizontal check
    for h in range(0,7,3):
        if listboard[h] == listboard[h+1] == listboard[h+2] and listboard[h] != ' ':
            return True
    # Vertical check
    for v in range(3):
        if listboard[v] == listboard[v+3] == listboard[v+6] and listboard[v] != ' ':
            return True
    # Diagonal check
    if listboard[0] == listboard[4] == listboard[8] and listboard[0] != ' ':
        return True
    if listboard[2] == listboard[4] == listboard[6] and listboard[2] != ' ':
        return True
    return False


# Tie (board full) check
def tiecheck():
    listboard = []
    for x in board.values():
        listboard.append(x)
    for i in listboard:
        if i == ' ':
            return False
    return True


# Multiplayer mode code
def multiplayer():
    print('...\n...\n...')
    playerbook = name_and_mark_select('multiplayer')
    print('Starting the game with the following players:')
    print('      ', playerbook[1]['name'], 'as', playerbook[1]['mark'])
    print('      ', playerbook[2]['name'], 'as', playerbook[2]['mark'])
    print('Let\'s get ready to rumblllleeeeeeeeeee')
    currentplayer = random.randint(1,2)
    print('Looks like', playerbook[currentplayer]['name'], 'will be going first today.')
    printBoard(board)
    print(playerbook[currentplayer]['name'], '''please enter your move by typing row-column, using the format of
          top-, mid-, bot- for "row"
          -l, -m, -r for "column"\nExample: "top-r" for top right space.''')
    # Main multiplayer game loop
    # Take a turn, print the board, check for wins/ties
    while True:
        turn(currentplayer, playerbook)
        printBoard(board)
        if wincheck(playerbook):
            print(playerbook[currentplayer]['name'], 'is the winner!! Thanks for playing.')
            break
        if tiecheck():
            print('That\'s a tie folks, thanks for playing.')
            break
        # Swap currentplayer following turn completion and win check
        if currentplayer == 1:
            currentplayer = 2
        else:
            currentplayer = 1
        print(playerbook[currentplayer]['name'], 'it\'s your turn.')


# Soloplay mode code
def soloplay():
    print('Mode under construction. Please try again later.')


###### Gameplay loop ########
print('Good morning, afternoon, or evening and welcome to TicTacToe with Colinho!')
print('Would you like to enter multiplayer mode or test yourself against Colinho\'s ~~robot brain~~?')
while True:
    print('Enter 1 for multiplayer or 2 for solo play.')
    mode = int(input())
    if mode == 1:
        multiplayer()
        break
    elif mode == 2:
        soloplay()
        break
    else:
        print('Please try mode selection again.')
print('\n\n\n\nthe end')



