# -*- coding: utf-8 -*-
"""
Created on Tue Apr  5 08:44:06 2022
My simple tic tac toe game in python
@author: Shaunak Mukherjee
"""

        
from IPython.display import clear_output
import random


def display_board(board):
    
    """
    Construct the board for game
    """
    
    clear_output()
    print(board[1] + "|" + board[2] + "|" + board[3])
    print('-'*5)
    print(board[4] + "|" + board[5] + "|" + board[6])
    print('-'*5)
    print(board[7] + "|" + board[8] + "|" + board[9])       
    pass


def player_input():
    
    '''
    Function that can take in a player input and assign their marker as 'X' or 'O'
    '''
    
    choice = ''
    
    while choice != 'x' and choice != 'o':
        
        choice = input("first player, please choose 'x' or 'o': ")
        
        player1 = choice
                
        if player1 == 'x':
            player2 = 'o'
            
        else:
            player2 = 'x'
    
    print(f'first player has chosen {choice}')        
    return(player1, player2)
    
 


def place_marker(board, player_input, position):
    
    '''
    Function that takes in the board list object ('x' or 'o'), and 
    a desired position (number 1-9) and assigns it to the board
    '''
    
    board[position] = player_input
    return position


def win_check(board, mark):
    
    '''
    Function for definition of winning
    '''
      
    return(
    (board[1] == mark and board[2] == mark and board[3] == mark)
    or
    (board[4] == mark and board[5] == mark and board[6] == mark)
    or
    (board[7] == mark and board[8] == mark and board[9] == mark)
    or
    (board[1] == mark and board[4] == mark and board[7] == mark)
    or
    (board[2] == mark and board[5] == mark and board[8] == mark)
    or
    (board[3] == mark and board[6] == mark and board[9] == mark)
    or      
    (board[1] == mark and board[5] == mark and board[9] == mark)
    or
    (board[7] == mark and board[5] == mark and board[3] == mark)) 
    


def choose_first():
    
    '''
    Function that uses the random module to randomly decide which player goes first
    '''
      
    if random.randint(0,1) == 0:
        return 'player1'
    else:
        return 'player2'
    
    
def space_check(board, position):
    
    '''
    Function indicating whether a space on the board is freely available
    '''
    
    if board[position] == ' ': 
        return True
    else:
        return False


def full_board_check(board):
    
    '''
    Function that checks if the board is full and returns a boolean value
    '''
    
    for pos in board:
        
        if pos == ' ':
            return False
        else:
            continue 
         
    return True    

def player_choice(board):
        
    '''
    Function that asks for a player's next position  
    and checks if it's a free position. 
    '''
    
    position = int(input('Choose Position from 1-9: '))
    if space_check(board,position):
        return position 
    
def replay():
    
    '''
    Function that asks the player if they want to play again
    '''
        
    play = input('Do you want to play again? Enter Yes or No: ')
    if play == 'Yes':
        return True
    elif play == 'No':
        return False     