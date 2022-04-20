import os

display_dictionary = {1:7, 2:8, 3:9, 4:4, 5:5, 6:6, 7:1, 8:2, 9:3} #list_index and keyboard pad mapping
the_list = [display_dictionary[x] for x in range(1, 10)] #Generator list generation something
index_dictionary = {7:0, 8:1, 9:2, 4:3, 5:4, 6:5, 1:6, 2:7, 3:8} #index pad and keyboard pad mapping

def the_board(our_list, message):
    '''This function replicates the TicTacToe board and displays the key/player placeholders on the board.'''
    os.system('cls' if os.name == 'nt' else 'clear') #clears terminal, cross platform
    print('Tic Tac Toe:',message)
    print(f" {our_list[0]} | {our_list[1]} | {our_list[2]} ")
    print(f" {our_list[3]} | {our_list[4]} | {our_list[5]} ")
    print(f" {our_list[6]} | {our_list[7]} | {our_list[8]} ")

def update_position(a_list, index, player): #input index: 0, 1, 2, 3, 4, 5, 6, 7, 8
    '''This functions updates the user input to the respective index in the list with the user placeholder'''
    a_list[index] = player
    return a_list

def game_logic(some_list): #Game logic #returns winner 
    '''This checks for winning conditions for Player X or Player Y by matching three contiguous 'X' or 'Y' placeholders in the horizontal, vertical and diagonal axes.''' 
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

def main(game_list): 
    '''The main method to run all the functions.'''       
    player = 'X'
    winner = None
    message = ''
    while winner == None: #Outer while        
        the_board(game_list, message)
        user_input = input(f"Player {player} enter choose the position: ")
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
                    if game_list[index] == 'X' or game_list[index] == 'Y': #if user placeholder is present, don't allow change!; comparision between int and string                        
                        message = "You cannot alter a preselected position. Please choose again"
                        break
                    else:
                        game_list = update_position(game_list, index, player) #Updating position                                                                   
                        winner = game_logic(game_list) #CHECK FOR WINNER (is None if no winner is preset)                       
                        the_board(game_list, message)

                        if stalemate(game_list): #True                            
                            return 'stale'
                        elif not winner == None:                            
                            return winner #Exits loop
                        else:
                            player = ('Y' if player == 'X' else 'X') #Ternary Operator                            
                            break #All good, break out of inner loop                               
                else:                    
                    message = 'Please enter a number in the range of 1 to 9.'
                    break #break out of inner loop                                               

if __name__ == "__main__": #Executes only if this is the main module
    returned = main(the_list)
    if returned == 'stale':
        print('No win situation. Start Over!')
    else:
        print(f'Player \'{returned}\' won! Game Over.')

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