# -*- coding: utf-8 -*-
"""
Created on Tue Apr  5 08:49:09 2022

@author: Shaunak Mukherjee
"""

from utilities.functions import *
from IPython.display import clear_output

print('Welcome to Tic Tac Toe!')



while True:
    clear_output()
    main_board = [' ']*10
    
    
    player1, player2 = player_input()
    
    
    player_turn = choose_first()
    print(f'Game starts with: {player_turn}')
    
    
    
    play_game = input(('Should we start the game? y or n: '))
    
    if play_game == 'y':
        game_on = True
    elif play_game == 'n':
        game_on = False
        print('Bye')
        break
        
        
    while game_on:
        if player_turn=='player1':
            display_board(main_board)
            position = player_choice(main_board)
            space_check(main_board, position)
            place_marker(main_board, player1, position)
            
            
            if win_check(main_board, player1):
                print(f"Congrats {player_turn} you have won!")
                break
                  
            elif full_board_check(main_board):
                print("Its a draw!")
                break
            else:
                player_turn = 'player2'
        else:
            display_board(main_board)
            position = player_choice(main_board)
            space_check(main_board, position)
            place_marker(main_board, player2, position)
            
            
            if win_check(main_board, player2):
                print(f"Congrats {player_turn} you have won!")
                break
                  
            elif full_board_check(main_board):
                print("Its a draw!")
                break
            else:
                player_turn = 'player1' 
                
    if not replay():
        break
                              

        
        
            

            


        


        
        
 

