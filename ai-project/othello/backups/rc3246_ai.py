#!/usr/bin/env python3
# -*- coding: utf-8 -*

"""
COMS W4701 Artificial Intelligence - Programming Homework 2

An AI player for Othello. This is the template file that you need to
complete and submit.

@author: YOUR NAME AND UNI
"""

import random
import sys
import time

# You can use the functions in othello_shared to write your AI
from othello_shared import find_lines, get_possible_moves, get_score, play_move

max_depth = 2

def compute_utility(board, color, current_depth=0):
    heuristics_first_half = [ (corner_heuristic,1.0),(sweet_sixteen_heuristic,1.5)] #
    heuristics_second_half = [(edge_heuristic, 2.5), (corner_heuristic,7.5),(sweet_sixteen_heuristic, 1.0)] #(invincible_edge_heuristic,4.5)],(sweet_sixteen_heuristic, 1.0)
    heuristic_value = 0

    if not switch_phases(board):
        for (heuristic_function, multiplier) in heuristics_first_half:
            heuristic_value += int(heuristic_function(board,color) * multiplier)
    else:
        for (heuristic_function, multiplier) in heuristics_second_half:
            heuristic_value += int(heuristic_function(board,color) * multiplier)
    #sys.stderr.write('Utility: {}\n'.format(heuristic_value))
    return heuristic_value

def move_mobility_heuristic(board,color):
    '''
    A secondary heuristic to maximize the number of plays the AI can do. Intended to synergize with sweet 16.
    '''
    if color == 1:
        opposing_color = 2
    else:
        opposing_color = 1

    opposing_possible_moves = 0
    moves = get_possible_moves(board,color)
    for (column,row) in moves:
        new_board = play_move(board,color,column,row)
        if len(get_possible_moves(new_board,opposing_color)) > opposing_possible_moves:
            opposing_possible_moves = len(get_possible_moves(new_board,opposing_color))
    #sys.stderr.write('Move mobility: {}\n'.format(len(moves) - opposing_possible_moves))
    return len(moves) - opposing_possible_moves + random.randint(0,9)

def sweet_sixteen_heuristic(board,color):
    '''
    Attempts to use the sweet 16 strategy heurisitic when starting out.
    Sweet 16: Play passively and around the center, forcing the opponent to seek edge plays.
    '''
    median = (len(board) - 4) // 2
    bad_positions = [
        (median,median),
        (median,len(board)-median),
        (len(board)-median,median),
        (len(board)-median,len(board)-median)
    ]
    heuristic_value = 0
    for row in range(len(board)):
        for column in range(len(board)):
            #sys.stderr.write(str(median <= board[row][column] <= len(board) - median))
            if (median <= column <= len(board) - median or median <= row <= len(board) - median): #and not (column,row) in bad_positions:
                heuristic_value += 1
    return heuristic_value

def switch_phases(board):
    '''
    Determines when the sweet 16 is near-full — approxiamately some fraction of the board.
    '''
    median = (len(board) - 4) // 2
    tiles_filled = 0
    for row in range(len(board)):
        for column in range(len(board)):
            #sys.stderr.write(str(median <= board[row][column] <= len(board) - median))
            if (median <= column <= len(board) - median or median <= row <= len(board) - median) and board[row][column] != 0:
                tiles_filled += 1
    return tiles_filled >= int(16 * (5/6))

def edge_heuristic(board,color):
    '''
    Switches to an edge capture strategy after sweet 16.
    '''
    heuristic_value = 0
    median = len(board) // 2
    second_median = len(board) // 2 - 1
    adjacent_corners = {
        (0,0) : [(0,1),(1,0),(1,1)],
        (0,len(board)-1): [(0,len(board)-2), (1,len(board)-1), (1,len(board)-2)],
        (len(board)-1,0): [(len(board)-2,0), (len(board)-2,1), (len(board)-1,1)],
        (len(board)-1,len(board)-1): [(len(board)-2,len(board)-2), (len(board)-1,len(board)-2), (len(board)-2,len(board)-1)]
    }
    for row in range(len(board)):
        for column in range(len(board)):
            if board[row][column] == 0:
                if (row == 0 or row == len(board) - 1) and (column == median or column == second_median):
                    heuristic_value += 1
                elif (column == 0 or column == len(board) - 1) and (row == median or row == second_median):
                    heuristic_value += 1
            #if board[row][column] == 0 and row in edge_positions and column in edge_positions:
            #    heurisitic_value += -2
    #sys.stderr.write('edge_heuristic: {}\n'.format(heuristic_value))
    return heuristic_value

def invincible_edge_heuristic(board,color):
    heuristic_value = 0
    # corners and their adjacent tiles
    adjacent_corners = {
        (0,0) : [(0,1),(1,0),(1,1)],
        (0,len(board)-1): [(0,len(board)-2), (1,len(board)-1), (1,len(board)-2)],
        (len(board)-1,0): [(len(board)-2,0), (len(board)-2,1), (len(board)-1,1)],
        (len(board)-1,len(board)-1): [(len(board)-2,len(board)-2), (len(board)-1,len(board)-2), (len(board)-2,len(board)-1)]
    }

    if color == 1:
        opposing_color = 2
    else:
        opposing_color = 1

    corner_advantage = 0
    opposing_corner_advantage = 0
    for (row,column) in adjacent_corners.keys():
        if board[row][column] == opposing_color:
            heuristic_value -= 10000
    #sys.stderr.write('Me: {} Enemy: {} Difference: {}\n'.format(corner_advantage,opposing_corner_advantage, corner_advantage - opposing_corner_advantage))
    # corner_advantage - opposing_corner_advantage
    #sys.stderr.write('invincible_edge_heuristic value: {}\n'.format(heuristic_value))
    return heuristic_value


def corner_heuristic(board,color):
    corners = [(0,0),(0,len(board)-1),(len(board)-1,0),(len(board)-1,len(board)-1)]
    adjacent_corners = {
        (0,0) : [(0,1),(1,0),(1,1)],
        (0,len(board)-1): [(0,len(board)-2), (1,len(board)-1), (1,len(board)-2)],
        (len(board)-1,0): [(len(board)-2,0), (len(board)-2,1), (len(board)-1,1)],
        (len(board)-1,len(board)-1): [(len(board)-2,len(board)-2), (len(board)-1,len(board)-2), (len(board)-2,len(board)-1)]
    }
    heuristic_value = 0
    #moves = get_possible_moves(board,color)

    for (row, column) in corners:
        if board[row][column] == color:
            heuristic_value += 10
        else: #if you don't own the corner, don't bother with it
            for (adjacent_row,adjacent_column) in adjacent_corners[(row,column)]:
                if board[adjacent_row][adjacent_column] == color:
                    heuristic_value -= 100

    '''
    for row in range(len(board)):
        for column in range(len(board)):
            current_tile_coords = (row,column)
            current_tile = board[row][column]
            if current_tile_coords in adjacent_corners.keys() and board[row][column] == 0:
                #sys.stderr.write('TILE: {} Coords: {}\n'.format(current_tile,current_tile_coords) )
                heuristic_value += 1
                for (adjacent_row,adjacent_column) in adjacent_corners[current_tile_coords]:
                    if board[adjacent_row][adjacent_column] == 0:
                        heuristic_value += -2
    '''
        #if move in bad_positions
        #elif move in bad_positions:
        #    heuristic_value -= len(moves)
    #sys.stderr.write('Corner heuristic: {}\n'.format(heuristic_value))
    return heuristic_value


############ MINIMAX ###############################

def minimax_min_node(board, color, depth, temp_max_depth=max_depth):
    if depth >= max_depth:
        return compute_utility(board,color)
    moves = get_possible_moves(board,color)
    move_utility = {}

    if len(moves) != 0:
        for (column,row) in moves:
            new_board = play_move(board,color,column,row)
            #sys.stderr.write(str(new_board) + '\n')
            if not new_board in move_utility.values():
                utility = minimax_max_node(new_board,color, depth + 1)
                move_utility[utility] = new_board
            else:
                return compute_utility(new_board,color)
        return min(move_utility.keys())
    return compute_utility(board,color)


def minimax_max_node(board, color, depth, temp_max_depth=max_depth):
    if depth >= max_depth:
        return compute_utility(board,color)
    moves = get_possible_moves(board,color)
    #sys.stderr.write('\n\n' + str(moves) + '\n\n' + str(color) + '\n\n')
    move_utility = {}

    if len(moves) != 0:
        for (column,row) in moves:
            #sys.stderr.write('\n\nMove played:' + str(row) + str(column))
            new_board = play_move(board,color,column,row)

            #sys.stderr.write('Max:\n\nNew board:' + str(new_board) + '\n\nOld board:' + str(board) )

            if not new_board in move_utility.values():
                utility = minimax_min_node(new_board,color, depth + 1)
                move_utility[utility] = new_board
            else:
                return compute_utility(new_board,color)
        return max(move_utility.keys())
    return compute_utility(board,color)

def select_move_minimax(board, color):
    """
    Given a board and a player color, decide on a move.
    The return value is a tuple of integers (i,j), where
    i is the column and j is the row on the board.
    """
    moves = get_possible_moves(board,color)
    #sys.stderr.write('\n\nHERE ' + str(moves) + '\n\n' + str(color) + '\n\n')
    move_utility = {}

    if len(moves) != 0:
        for (column,row) in moves:
            #sys.stderr.write('\nHERE2\nMove played:' + str(row) + str(column))
            #sys.stderr.flush()
            new_board = play_move(board,color,column,row)
            if not (column, row) in move_utility.values():
                utility = minimax_max_node(new_board,color,0)
                move_utility[utility] = (column,row)
                sys.stderr.write('Move {},{} with utility {} input!\n'.format(column,row,utility))
    new_max = max(move_utility.keys())
    selected_move = (move_utility[new_max][0],move_utility[new_max][1])
    sys.stderr.write('Selected move weight: {} of {}\n# Moves Available: {}\n'.format(new_max,move_utility,len(moves)))
    return selected_move

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
    print("rc3246's AI") # First line is the name of this AI
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
            movei, movej = select_move_minimax(board, color)
            #movei, movej = select_move_alphabeta(board, color)
            print("{} {}".format(movei, movej))


if __name__ == "__main__":
    run_ai()
