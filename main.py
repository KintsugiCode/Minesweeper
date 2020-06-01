import random, time, copy, replit
from termcolor import cprint

#Introduction
print()
cprint('Welcome to MineSweeper v.3.0!', 'red')
cprint('=============================', 'red')
print()
print('Excited to declare version 3.0 of MineSweeper as almost fully functional!')


def reset():
    print('''
MAIN MENU
=========

-> For instructions on how to play, type 'I'
-> To play immediately, type 'P')
''')

    choice = input('Type here: ').upper()

    if choice == 'I':

        #Prints Instructions
        print(open('instructions.txt', 'r').read())

        input('Press [enter] when ready to play.')

    elif choice !='P':
        replit.clear()
        reset()

    #The solution grid.
    b = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0, 0, 0, 0, 0]
        ] 

        
    for n in range(0,10):
        placeBomb(b)

    for r in range (0, 9):
        for c in range (0, 9):
            value = l(r, c, b)
            if value == '*':
                updateValues(r, c, b)

    #Sets the variable k to a grid of blank spaces, because nothing is yet known about the grid.
    k = [
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], 
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], 
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], 
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], 
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], 
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], 
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], 
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], 
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    ]
    
    printBoard(k)





def placeBomb(b):
    r = random.randint(0, 8)
    c = random.randint(0, 8)
    #Checks if there's a bomb in the randomly generated location. If not, it puts one there. If there is, it requests a new location to try.
    currentRow = b[r]
    if not currentRow[c] == '*':
        currentRow[c] = '*'
    else:
        placeBomb(b)

#Adds 1 to all of the squares around a bomb.
def updateValues(rn, c, b):

    #Row above.
    if rn-1 > -1:
        r = b[rn-1]
        
        if c-1 > -1:
            if not r[c-1] == '*':
                r[c-1] += 1

        if not r[c] == '*':
            r[c] += 1

        if 9 > c+1:
            if not r[c+1] == '*':
                r[c+1] += 1

    #Same row.    
    r = b[rn]

    if c-1 > -1:
        if not r[c-1] == '*':
            r[c-1] += 1

    if 9 > c+1:
        if not r[c+1] == '*':
            r[c+1] += 1

    #Row below.
    if 9 > rn+1:
        r = b[rn+1]

        if c-1 > -1:
            if not r[c-1] == '*':
                r[c-1] += 1

        if not r[c] == '*':
            r[c] += 1

        if 9 > c+1:
            if not r[c+1] == '*':
                r[c+1] += 1


#Gets the value of a coordinate on the grid.
def l(r, c, b):
    return b[r][c]
  
#Prints the given board.
def printBoard(b):
    replit.clear()
    print('    A   B   C   D   E   F   G   H   I')
    print('  ╔═══╦═══╦═══╦═══╦═══╦═══╦═══╦═══╦═══╗')
    for r in range (0, 9):
        print(r,'║',l(r,0,b),'║',l(r,1,b),'║',l(r,2,b),'║',l(r,3,b),'║',l(r,4,b),'║',l(r,5,b),'║',l(r,6,b),'║',l(r,7,b),'║',l(r,8,b),'║')
        if not r == 8:
            print('  ╠═══╬═══╬═══╬═══╬═══╬═══╬═══╬═══╬═══╣')
    print('  ╚═══╩═══╩═══╩═══╩═══╩═══╩═══╩═══╩═══╝')


reset()