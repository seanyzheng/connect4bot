#!/usr/bin/env python3

"""
board.py
This program defines the board class.
"""

__author__ = "Sean Zheng"
__version__ =  "2019-05-24"

import time
import os
import numpy as np
import sys

class Board(object):

    def __init__(self): 
        self.board = []
        self.rows = 6
        self.columns = 7
        for i in range(self.rows):
            self.board.append([])
            for j in range(self.columns * 2):
                self.board[i].append(".")
                self.board[i].append(" ")
    
    def move_piece(self, column, piece):
        actual_column = 2 * column
        for i in range(self.rows):
            #if it's at the bottom of the board
            if i + 2 > self.rows:
                self.board[i][actual_column] = piece
            #if it has hit another piece
            elif self.board[i + 1][actual_column] != ".":
                self.board[i][actual_column] = piece
                break
    
    
    def checkWin(self, piece):
        #horizontal wins
        for i in range(self.rows):
            for j in range(self.columns * 2 - 6):
                if self.board[i][j] == piece and self.board[i][j + 2] == piece \
                and self.board[i][j + 4] == piece and self.board[i][j + 6] == piece:
                    return True
        #vertical wins
        for i in range(self.rows - 3):
            for j in range(self.columns * 2):
                if self.board[i][j] == piece and self.board[i + 1][j] == piece \
                and self.board[i + 2][j] == piece and self.board[i + 3][j] == piece:
                    return True
        # left to right top to bottom diagonal wins
        """
        x
          x
            x
              x
        """
        for i in range(self.rows - 3):
            for j in range(self.columns * 2 - 6):
                if self.board[i][j] == piece and self.board[i + 1][j + 2] == piece \
                and self.board[i + 2][j + 4] == piece and self.board[i + 3][j + 6] == piece:
                    return True
        #left to right bottom to top diagonal wins
        """
              x
            x
          x
        x
        """
        for i in range(self.rows - 3):
            for j in range(6, self.columns * 2):
                if self.board[i][j] == piece and self.board[i + 1][j - 2] == piece \
                and self.board[i + 2][j - 4] == piece and self.board[i + 3][j - 6] == piece:
                    return True
                    
                    
        return False
            
        
    def __repr__(self):
        os.system("clear")
        print()
        self.repr = "0 1 2 3 4 5 6"
        for i in range(self.rows):
            self.repr += "\n"
            for j in range(self.columns * 2):
                self.repr = self.repr + self.board[i][j]
        return self.repr