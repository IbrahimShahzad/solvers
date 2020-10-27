# python code to solve soduku
import pprint
import numpy as np
import logging, sys
logging_level = logging.INFO
logging.basicConfig(stream=sys.stderr, level=logging_level)

class SudokuSolver:
    """Sodoku Solver Class """
    def __init__(self,array):
        """ Takes in 9x9 sudoku array """
        self.arr = array
        # self.result = []
        
    def is_possible_grid(self,row,col,user_value):
        """ This function checks whether the input is valid for 3x3 grid """
        start_row = row - (row % 3)
        start_col = col - (col % 3)
        for x in range(3):
            for y in range(3):
                if self.arr[x+start_row][y+start_col] == user_value:
                    logging.debug(f"is_posssible_grid(): (False) x: {x} y: {y} s_row: {start_row} s_col: {start_col} arr[x+start_row][y+start_col]: {self.arr[x+start_row][y+start_col]} == {user_value}")
                    return False
        logging.debug(f"is_posssible_grid(): (True) x: {x} y: {y} s_row: {start_row} s_col: {start_col} arr[x+start_row][y+start_col]: {self.arr[x+start_row][y+start_col]} != {user_value}")
        return True

    def is_posssible_col(self,col,user_value):
        """ This function checks whether the input is valid for column (len 9) """
        for row in range(9):
            if self.arr[row][col] == user_value:
                logging.debug(f"is_posssible_col row(): (False) row: {row} col: {col} arr{self.arr[row][col]} == {user_value}")
                return False
        logging.debug(f"is_posssible_col row(): (True) row: {row} col: {col} arr{self.arr[row][col]} != {user_value}")
        return True

    def is_posssible_row(self,row,user_value):
        """ This function checks whether the input is valid for row (len 9) """
        for col in range(9):
            if self.arr[row][col] == user_value:
                logging.debug(f"is_posssible_row(): (False) row: {row} col: {col} arr{self.arr[row][col]} == {user_value}")
                return False
        logging.debug(f"is_posssible_row(): (True) row: {row} col: {col} arr{self.arr[row][col]} != {user_value}")
        return True
    
    def is_possible_value(self,row,col,user_value):
        """ This function checks whether the input is for sudoku board """
        if self.is_possible_grid(row,col,user_value):
            if self.is_posssible_row(row,user_value):
                return self.is_posssible_col(col,user_value)
    
    def solve(self):
        """ This function solves sudoku board (backtracking) """
        for x in range(9):
            for y in range(9):
                if self.arr[x][y] == 0:
                    for value in range(1,10):
                        if self.is_possible_value(x,y,value):
                            self.arr[x][y] = value
                            self.solve()
                            self.arr[x][y] = 0            
                    return
        print(np.matrix(self.arr))
                

def run():
    array = [[3, 0, 6, 5, 0, 8, 4, 0, 0], 
        [5, 2, 0, 0, 0, 0, 0, 0, 0], 
        [0, 8, 7, 0, 0, 0, 0, 3, 1], 
        [0, 0, 3, 0, 1, 0, 0, 8, 0], 
        [9, 0, 0, 8, 6, 3, 0, 0, 5], 
        [0, 5, 0, 0, 9, 0, 6, 0, 0], 
        [1, 3, 0, 0, 0, 0, 2, 5, 0], 
        [0, 0, 0, 0, 0, 0, 0, 7, 4], 
        [0, 0, 5, 2, 0, 6, 3, 0, 0] ]
    # array = [[0, 0, 0, 2, 6, 0, 7, 0, 1], 
    #     [6, 8, 0, 0, 7, 0, 0, 9, 0], 
    #     [1, 9, 0, 0, 0, 4, 5, 0, 0], 
    #     [8, 2, 0, 1, 0, 0, 0, 4, 0], 
    #     [0, 0, 4, 6, 0, 2, 9, 0, 0], 
    #     [0, 5, 0, 0, 0, 3, 0, 2, 8], 
    #     [0, 0, 9, 3, 0, 0, 0, 7, 4], 
    #     [0, 4, 0, 0, 5, 0, 0, 3, 6], 
    #     [7, 0, 3, 0, 1, 8, 0, 0, 0] ]
    print("Input:")
    sod = SudokuSolver(array)
    print(np.matrix(sod.arr))
    print("Solution(s):")
    sod.solve()
    #print(np.matrix(sod.solved()))

if __name__ == "__main__":
    run()
