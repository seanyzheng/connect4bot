#!/usr/bin/env python3

"""
connect4.py
This is the simulation runner of the project
"""

__author__ = "Sean Zheng"
__version__ = "2019-05-23"

from board import Board
import numpy as np
import random
import math
import sys
import copy


def terminal_node(board):
    """
    board_full = True
    for i in range(board.rows):
        for j in range(board.columns):
            if board.board[i][j * 2] == ".":
                board_full = False
    """
            
    if board.checkWin("X") or board.checkWin("O") or len(get_valid_locations(board)) == 0:
        return True
    else:
        return False

def minimax(board, depth, alpha, beta, maximizingPlayer):
    valid_locations = get_valid_locations(board)
    is_terminal = terminal_node(board)   
    if depth == 0 or is_terminal:
        if is_terminal:
            #if the computer wins return really high value
            if board.checkWin("O") == True:
                return (None, 999)
            #if scenario where player wins return really low value
            elif board.checkWin("X") == True:
                return (None, -999)
            # if board is completely filled up it is a draw so it's ok
            else:
                return (None, 0)  
        elif depth == 0:
            return (None, score_position(board,"O"))
    if maximizingPlayer:
        value = -math.inf
        column = random.choice(valid_locations)
        for col in valid_locations:
            temp_board = copy.deepcopy(board)
            temp_board.move_piece(col, "O")
            new_score =  minimax(temp_board, depth - 1, alpha, beta, False)[1]
            if new_score > value:
                value = new_score
                column = col
            alpha = max(alpha, value)
            if alpha >= beta:
                break
        return column, value
    else:
        value = math.inf
        column = random.choice(valid_locations)
        for col in valid_locations:
            temp_board = copy.deepcopy(board)
            temp_board.move_piece(col, "X")
            new_score = minimax(temp_board, depth - 1, alpha, beta, True)[1]
            if new_score < value:
                value = new_score
                column = col
                beta = min(beta, value)
                if alpha >= beta:
                    break
        return column, value
        
def score_position(board, piece):
    score = 0
    
    center_list = []
    for i in range(board.rows):
        center_list.append(board.board[i][board.rows // 2])
    center_count = center_list.count(piece)
    score += center_count * 3
    
    for i in range(board.rows):
        row = board.board[i]
        for j in range(board.columns - 3):
            window = row[2 * j:2 * j + 8:2]
            if window.count(piece) == 4:
                score += 1000
            elif window.count(piece) == 3 and window.count(".") == 1:
                score += 5
            elif window.count(piece) == 2 and window.count(".") == 2:
                score += 2
            elif window.count("X") == 3 and window.count(".") == 1:
                score -= 4
    
    for j in range(board.columns):
        col = []
        for i in range(board.rows):
            col.append(board.board[i][j * 2])
        for r in range(board.rows - 3):
            window = col[r:r + 4]
  
            if window.count(piece) == 4:
                score += 1000
            elif window.count(piece) == 3 and window.count(".") == 1:
                score += 5

            elif window.count(piece) == 2 and window.count(".") == 2:
                score += 2

            elif window.count("X") == 3 and window.count(".") == 1:
                score -= 4
    
    for row in range(board.rows - 3):
        for col in range(board.columns):
            for i in range(4):
                window = [board.board[row + i][col + 2 * i]]
            if window.count(piece) == 4:
                score += 1000
            elif window.count(piece) == 3 and window.count(".") == 1:
                score += 5
            elif window.count(piece) == 2 and window.count(".") == 2:
                score += 2
            elif window.count("X") == 3 and window.count(".") == 1:
                score -= 4
                
    for row in range(board.rows - 3):
        for col in range(board.columns - 3):
            for i in range(4):
                window = [board.board[row + 3 - i][col + 2 * i]]
            if window.count(piece) == 4:
                score += 1000
            elif window.count(piece) == 3 and window.count(".") == 1:
                score += 5
            elif window.count(piece) == 2 and window.count(".") == 2:
                score += 2
            elif window.count("X") == 3 and window.count(".") == 1:
                score -= 4
        
    return score
    
def get_valid_locations(board):
    valid_locations = []
    for col in range(board.columns):
        if board.board[0][col * 2] == ".":
            valid_locations.append(col)
    return valid_locations

def main():
    game = Board()
    print(game)
    while 1 == 1:
        o_col = minimax(game, 6, -math.inf, math.inf, True)[0]
        game.move_piece(o_col, "O")
        print(game)
        if game.checkWin("O") == True:
            print("Connectatron Wins. ")
            break
        x_col = eval(input("Player Move: "))
        game.move_piece(x_col, "X")
        print(game)
        if game.checkWin("X") == True:
            print("You win. ")
            break
            
if __name__ == "__main__":
    main()