import random

# Constants
NORTH = 'n'
EAST = 'e'
SOUTH = 's'
WEST = 'w'
YES = 'y'
NO = 'n'

def move(direction, col, row):
    ''' Returns updated col, row given the direction '''
    if direction == NORTH:
        row += 1
    elif direction == SOUTH:
        row -= 1
    elif direction == EAST:
        col += 1
    elif direction == WEST:
        col -= 1
    return(col, row)    

def is_victory(col, row):
    ''' Return true if player is in the victory cell '''
    return col == 3 and row == 1 # (3,1)

def print_directions(directions_str):
    print("You can travel: ", end='')
    first = True
    for ch in directions_str:
        if not first:
            print(" or ", end='')
        if ch == NORTH:
            print("(N)orth", end='')
        elif ch == EAST:
            print("(E)ast", end='')
        elif ch == SOUTH:
            print("(S)outh", end='')
        elif ch == WEST:
            print("(W)est", end='')
        first = False
    print(".")
        
def find_directions(col, row):
    ''' Returns valid directions as a string given the supplied location '''
    if col == 1 and row == 1:   # (1,1)
        valid_directions = NORTH
    elif col == 1 and row == 2: # (1,2)
        valid_directions = NORTH+EAST+SOUTH
    elif col == 1 and row == 3: # (1,3)
        valid_directions = EAST+SOUTH
    elif col == 2 and row == 1: # (2,1)
        valid_directions = NORTH
    elif col == 2 and row == 2: # (2,2)
        valid_directions = SOUTH+WEST
    elif col == 2 and row == 3: # (2,3)
        valid_directions = EAST+WEST
    elif col == 3 and row == 2: # (3,2)
        valid_directions = NORTH+SOUTH
    elif col == 3 and row == 3: # (3,3)
        valid_directions = SOUTH+WEST
    return valid_directions


def play_one_move(col, row, valid_directions, coins_count):
    ''' Plays one move of the game
        Return if victory has been obtained and updated col,row '''
    
    options_list = ["n","s","e","w"]
    victory = False
    #direction = input("Direction: ")
    #direction = direction.lower()
    direction = random.choice(options_list)
    print("Direction: ",direction)
        
    if not direction in valid_directions:
        print("Not a valid direction!")
    else:
        col, row = move(direction, col, row)
        coins_count = pull_coin_lever(col, row, coins_count)
        victory = is_victory(col, row)
    return victory, col, row, coins_count

def pull_coin_lever(col, row, coins_count):
    ''' Checks if there is a coin on user location and give lever...'''
    #pull_lever.lower() = input("Pull a lever (y/n): ")

    if (col == 1 and row == 2): #and (first_coin == 1): # (1,2)
        pull_lever = random.choice([YES,NO])
        print("Pull a lever (y/n): ",pull_lever)
        if pull_lever == "y":
            coins_count += 1
            print(f"You received 1 coin, your total is now {coins_count}.")
            
    elif col == 2 and row == 2: # (2,2)
        pull_lever = random.choice([YES,NO])
        print("Pull a lever (y/n): ",pull_lever)
        if pull_lever == "y":
            coins_count += 1
            print(f"You received 1 coin, your total is now {coins_count}.")

    elif col == 2 and row == 3: # (2,3)
        pull_lever = random.choice([YES,NO])
        print("Pull a lever (y/n): ",pull_lever)
        if pull_lever == "y":
            coins_count += 1
            print(f"You received 1 coin, your total is now {coins_count}.")

    elif col == 3 and row == 2: # (3,2)
        pull_lever = random.choice([YES,NO])
        print("Pull a lever (y/n): ",pull_lever)
        if pull_lever == "y":
            coins_count += 1
            print(f"You received 1 coin, your total is now {coins_count}.")

    return coins_count

# The main program starts here
def play():
    random.seed(int(input("Input seed: ")))
    victory = False
    row = 1
    col = 1
    coins_count = 0
        
    while not victory:
        valid_directions = find_directions(col, row)
        print_directions(valid_directions)

        victory, col, row, coins_count = play_one_move(col, row, valid_directions, coins_count)

        
    print(f"Victory! Total coins {coins_count}.")
    play_again = input("Play again (y/n): ")
    return play_again

play_again = "y"

while play_again == "y":
    play_again = play()
