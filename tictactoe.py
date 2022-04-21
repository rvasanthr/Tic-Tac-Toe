import os

display_dictionary = {1:7, 2:8, 3:9, 4:4, 5:5, 6:6, 7:1, 8:2, 9:3} #list_index and keyboard pad mapping
index_dictionary = {7:0, 8:1, 9:2, 4:3, 5:4, 6:5, 1:6, 2:7, 3:8} #index pad and keyboard pad mapping
symbols = {'p1':'', 'p2':''} #Symbol choices
players = {'p1': '', 'p2': ''} #Names

def set_board_list():
    return [display_dictionary[x] for x in range(1, 10)] #Board's list generation through list comprehension, returns a list

def the_board(our_list):
    '''This function replicates the TicTacToe board and displays the key/player placeholders on the board.'''
    os.system('cls' if os.name == 'nt' else 'clear') #clears terminal, cross platform
    print('Tic Tac Toe:')
    print(f" {our_list[0]} | {our_list[1]} | {our_list[2]} ")
    print(f" {our_list[3]} | {our_list[4]} | {our_list[5]} ")
    print(f" {our_list[6]} | {our_list[7]} | {our_list[8]} ")

def update_position(a_list, index, player): #input index: 0, 1, 2, 3, 4, 5, 6, 7, 8
    '''This functions updates the user input to the respective index in the list with the user placeholder'''
    a_list[index] = player
    return a_list

def game_logic(some_list): #Game logic #returns winner 
    '''This checks for winning conditions for Player X or Player O by matching three contiguous 'X' or 'O' placeholders in the horizontal, vertical and diagonal axes.''' 
    for i in range(0,9,3): #Horizontal comparision, 3 iterations
        if some_list[i] == some_list[i+1] == some_list[i+2]:
            return some_list[i]    
    for _ in range(3): #Vertical comparisions 3 columns
        if some_list[_] == some_list[_+3] == some_list[_+6]:
            return some_list[_]    
    for j in (0,2): #Diagonal comparisions, 2 diagonals #tuple passed
        if j == 0:
            if some_list[j] == some_list[j+4] == some_list[j+8]:
                return some_list[j]
        else:
            if some_list[j] == some_list[j+2] == some_list[j+4]:
                return some_list[j]
    return None    

def stalemate(game):
    '''This function check for stalemate conditions (No win scenarios)'''
    count = 0
    for each in game:
        if each in (1,2,3,4,5,6,7,8,9):
            count += 1
    state = game_logic(game)
    if state == None and count == 0:
        return True
    else:
        return False

def player_symbol_pairing():    
    global players, symbols
    counter = 1
    name = ''
    symbol = ''
    for each in players: #Setting names 
        while name == '': #Won't allow empty strings
            name = input(f'Enter your name player{counter}: ')
            if len(name) > 0:
                players[each] = name
                name = ''
                break
        counter += 1        
    while not symbol in ('1','2'): #Choosing symbols
        symbol = input(f'Player {players["p1"]}, enter your choice of symbol among "X" and "O". Enter "1" for "X" or enter "2" for "O": ')
        symbols['p1'] = 'X' if symbol == '1' else 'O' #It's either 1 or 2
        symbols['p2'] = 'O' if symbols['p1'] == 'X' else 'X'    
    for each in players: #Output
        print(f'{players[each]} is assigned symbol \'{symbols[each]}\'')
    return f'{players["p1"]}\'s symbol is {symbols["p1"]}.\n{players["p2"]}\'s symbol is {symbols["p2"]}.\nGood luck! Let the game begin.'


def main(game_list, message): 
    '''The main method to run all the functions.'''       
    person = 'p1'
    winner = None    
    while winner == None: #Outer while        
        the_board(game_list)
        print(message)
        user_input = input(f"Player {players[person]} enter the position you wish to mark: ")
        while not user_input == '': #Inner while
            message = '' #reseting message
            if len(user_input) > 1:                
                if user_input[0] in '-+': #Catching the signs
                    message = "Please don't use signs. "                
                message += f'You entered {user_input}. Please enter a number in the range starting from 1 and ending at 9.'
                break
            else: #single digit or character is entered, i.e length == 1                
                if user_input in ('1', '2', '3', '4', '5', '6', '7', '8', '9'):                    
                    index = index_dictionary[int(user_input)]
                    if game_list[index] == 'X' or game_list[index] == 'O': #if user placeholder is present, don't allow change!; comparision between int and string                        
                        message = "You cannot alter a preselected position. Please choose again"
                        break
                    else:
                        game_list = update_position(game_list, index, symbols[person]) #Updating position                                                                   
                        winner = game_logic(game_list) #CHECK FOR WINNER (is None if no winner is preset)                       
                        the_board(game_list)

                        if stalemate(game_list): #True                            
                            return 'stale'
                        elif not winner == None:                            
                            return winner #Exits loop
                        else:
                            person = ('p2' if person == 'p1' else 'p1') #Ternary Operator                            
                            break #All good, break out of inner loop                               
                else:                    
                    message = 'Please enter a number in the range of 1 to 9.'
                    break #break out of inner loop                                               

if __name__ == "__main__": #Executes only if this is the main module
    gaming = 'y'
    message = player_symbol_pairing() #player name and symbol choosing    
    while gaming == 'y':
        the_list = set_board_list()
        returned = main(the_list, message) #Stale or None or X or O
        if returned == 'stale':
            print('No win situation. Start Over!')            
        else:
            if returned == symbols['p1']:
                    champion = players['p1']
            else:
                champion = players['p2']
            #selective code for player who won
            print(f'Player \'{champion}\' won! Game Over.')
        gaming = '' #reset gaming
        while not gaming in ('y', 'n'):
            # the_list = set_board_list() #reset board
            gaming = input("Do you want to continue gaming (press y(yes) / n(no))? ").lower()
    print("Good bye. Have a good day.")


#Visual Aid
#index              #list comprehension             #keyboard value
# 0 | 1 | 2         # 1 | 2 | 3                     #7 | 8 | 9
# 3 | 4 | 5         # 4 | 5 | 6                     #4 | 5 | 6
# 6 | 7 | 8         # 7 | 8 | 9                     #1 | 2 | 3

#Tasks
#setup variables
#Board and display
    #Numeric Keyboard display and mapping
    #Dynamic info update when necessary
        #Get input and display in position ===> DONE
        #Don't allow overwriting of data ===> DONE
    #Clear output
    #Stalemate decleration
#Game logic
#Input update
#User Input and related    
    #Get input alternating between the players ===> DONE
        #X for one player and Y for one player, has to alternate ===> DONE
    
#Add-on tasks: Completed
    #Players get to enter names
    #first player gets to choose symbol, either x or o
    #Allow players to continue game

#Bug Fixes: Completed
    #Wrong symbol assigned to player 1 fixed
	#After tie game, lack of message regarding same and game starts by itself issue fixed
	#Board reset issue because of underlying functionality fixed
