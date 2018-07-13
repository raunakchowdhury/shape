#!/usr/bin/env python3
# -*- coding: utf-8 -*

"""
COMS W4701 Artificial Intelligence - Programming Homework 2

An AI player for Othello. This is the template file that you need to  
complete and submit. 

@author: Beyer White
"""

import random
import sys
import time

# You can use the functions in othello_shared to write your AI 
from othello_shared import find_lines, get_possible_moves, get_score, play_move

def compute_utility(board, color):

    p1_score, p2_score = get_score(board)
    return p1_score - p2_score if color == 1 else p2_score - p1_score

def terminal(counter, board, color):

    if counter >= 4:
        return True
    elif len(get_possible_moves(board, color)) <= 0:
        return True
    else:
        return False

############ MINIMAX ###############################

def minimax_min_node(board, color, counter, worth_dict):

    if color == 1:
        opposite_color = 2
    else:
        opposite_color = 1

    if terminal(counter, board, opposite_color):
        return compute_utility(board, color)

    else:
        moves_a = get_possible_moves(board, opposite_color)
        utility_list_a = []

        counter += 1

        for x in range(len(moves_a)):
            new_board_a = play_move(board, opposite_color, moves_a[x][0], moves_a[x][1])
            
            if new_board_a in worth_dict:
                return worth_dict[new_board_a]
            
            utility_a = minimax_max_node(new_board_a, color, counter, worth_dict)
            worth_dict[new_board_a] = utility_a
            utility_list_a.append((utility_a, new_board_a))

        best_utility_and_board_a = min(utility_list_a, key=lambda item: item[0])

        return best_utility_and_board_a[0]

def minimax_max_node(board, color, counter, worth_dict):

    if terminal(counter, board, color):
        return compute_utility(board, color)

    else:
        moves_b = get_possible_moves(board, color)
        utility_list_b = []

        counter += 1

        for x in range(len(moves_b)):
            new_board_b = play_move(board, color, moves_b[x][0], moves_b[x][1])
            
            if new_board_b in worth_dict:
                return worth_dict[new_board_b]
            
            utility_b = minimax_min_node(new_board_b, color, counter, worth_dict)
            worth_dict[new_board_b] = utility_b
            utility_list_b.append((utility_b, new_board_b))

        best_utility_and_board_b = max(utility_list_b, key=lambda item: item[0])

        return best_utility_and_board_b[0]

def evaluate(utility, move):

    if utility > 0:
        utility *= 10

    if utility > 0 and ((move == (0, 0)) or (move == (7, 0)) or (move == (0, 7)) or (move == (7, 7))):
        utility += 20000

    if (move == (1, 1)) or (move == (1, 0)) or (move == (0, 1)) or (move == (7, 1)) or (move == (6, 0)) or (move == (6, 1)) or (move == (0, 6)) or (move == (1, 6)) or (move == (1, 7)) or (move == (6, 7)) or (move == (7, 6)) or (move == (6, 6)):
        utility -= 1000

    return utility

def select_move_minimax(board, color):
    """
    Given a board and a player color, decide on a move. 
    The return value is a tuple of integers (i,j), where
    i is the column and j is the row on the board.  
    """

    #To make it work, one would need to account for the opposite player's moves, too! Also, make an elif in the 
    #functions for if you have seen a state before (because you can compute utility right from that)!

    moves = get_possible_moves(board, color)
    worth_dict = {}
    utility_list = []
    moves_dict = {}
    counter = 0

    for x in range(len(moves)):
        new_board = play_move(board, color, moves[x][0], moves[x][1])
        utility = minimax_min_node(new_board, color, counter, worth_dict)
        new_utility = evaluate(utility, moves[x])
        worth_dict[new_board] = new_utility
        moves_dict[new_board] = moves[x]
        utility_list.append((new_utility, new_board))

    best_utility_and_board = max(utility_list, key=lambda item: item[0])
    best_move = moves_dict[best_utility_and_board[1]]
    movei = best_move[0]
    movej = best_move[1]

    return movei, movej
    
############ ALPHA-BETA PRUNING #####################

#alphabeta_min_node(board, color, alpha, beta, level, limit)
def alphabeta_min_node(board, color, alpha, beta): 
    return None


#alphabeta_max_node(board, color, alpha, beta, level, limit)
def alphabeta_max_node(board, color, alpha, beta):
    return None


def select_move_alphabeta(board, color): 
    return 0,0 


####################################################
def run_ai():
    """
    This function establishes communication with the game manager. 
    It first introduces itself and receives its color. 
    Then it repeatedly receives the current score and current board state
    until the game is over. 
    """
    print("Minimax AI") # First line is the name of this AI  
    color = int(input()) # Then we read the color: 1 for dark (goes first), 
                         # 2 for light. 

    while True: # This is the main loop 
        # Read in the current game status, for example:
        # "SCORE 2 2" or "FINAL 33 31" if the game is over.
        # The first number is the score for player 1 (dark), the second for player 2 (light)
        next_input = input() 
        status, dark_score_s, light_score_s = next_input.strip().split()
        dark_score = int(dark_score_s)
        light_score = int(light_score_s)

        if status == "FINAL": # Game is over. 
            print 
        else: 
            board = eval(input()) # Read in the input and turn it into a Python
                                  # object. The format is a list of rows. The 
                                  # squares in each row are represented by 
                                  # 0 : empty square
                                  # 1 : dark disk (player 1)
                                  # 2 : light disk (player 2)
                    
            # Select the move and send it to the manager 
            (movei, movej) = select_move_minimax(board, color)
            #movei, movej = select_move_alphabeta(board, color)
            print("{} {}".format(movei, movej))

if __name__ == "__main__":
    run_ai()

"""Heuristics to Implement:
At the selectmove level, increase utility if the move is to capture a corner as long as the utility was already positive by a certain level.
Add in a mobility and stability heuristic.
Add a coin parity heuristic."""