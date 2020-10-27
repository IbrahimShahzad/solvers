# This program solves a NxN maze
import numpy as np
import time
from os import system

class MazeSolver:
    def __init__(self,array2D,startx,starty,endx,endy):
        self.grid = array2D
        self.grid_length = len(self.grid)
        self.startx = startx
        self.starty = starty
        self.endx = endx
        self.endy = endy
        if self.grid_length != len(self.grid[0]):
            raise Exception("The grid must be NxN")
    
    def go_right(self,x,y):
        if x == self.grid_length-1:
            return False

        if self.grid[x][y+1] == ' ':
            return True
        return False
    
    def go_left(self,x,y):
        if y == 0:
            return False

        if self.grid[x][y-1] == ' ':
            return True
        return False

    def go_down(self,x,y):
        if x == self.grid_length-1:
            return False
        if self.grid[x+1][y] == ' ':
            return True
        return False

    def go_up(self,x,y):
        if x == 0:
            return False
        if self.grid[x-1][y] == ' ':
            return True
        return False

    def is_safe(self,x,y):
        if self.go_right(x,y):
            return True
        if self.go_left(x,y):
            return True
        if self.go_down(x,y):
            return True
        if self.go_up(x,y):
            return True
        return False

    def solvePath2(self):
        """ This function solves sudoku board (backtracking) """
        system('cls')
        print(np.matrix(self.grid))
        # print(f"sx {self.startx} sy {self.starty} ex {self.endx} ey {self.endy}")
        time.sleep(0.5)
        if (self.startx == self.endx) and (self.starty == self.endy):
            self.grid[self.startx][self.endx] = 'x'
            system('cls')
            print("solved")
            print(np.matrix(self.grid))
            exit()

        if self.grid[self.startx][self.starty] == ' ':
            if self.go_down(self.startx,self.starty):
                self.grid[self.startx][self.starty] = 'x'
                self.startx = self.startx + 1
                self.solvePath2()
                self.startx = self.startx - 1
                self.grid[self.startx][self.starty] = ' '
            if self.go_up(self.startx,self.starty):
                self.grid[self.startx][self.starty] = 'x'
                self.startx = self.startx - 1
                self.solvePath2()
                self.startx = self.startx + 1
                self.grid[self.startx][self.starty] = ' '
            if self.go_right(self.startx,self.starty):
                self.grid[self.startx][self.starty] = 'x'
                self.starty = self.starty + 1
                self.solvePath2()
                self.starty = self.starty - 1
                self.grid[self.startx][self.starty] = ' '
            if self.go_left(self.startx,self.starty):
                self.grid[self.startx][self.starty] = 'x'
                self.starty = self.starty - 1
                self.solvePath2()
                self.starty = self.starty + 1
                self.grid[self.startx][self.starty] = ' '
        return

def run():
    grid = [
        ['#','#','#','#','#','#',' ','#','#','#','#','#','#'],
        ['#',' ',' ',' ','#',' ',' ',' ',' ',' ',' ',' ','#'],
        ['#',' ','#',' ',' ',' ','#','#','#','#','#',' ','#'],
        ['#',' ','#',' ','#',' ','#',' ',' ',' ','#',' ','#'],
        ['#',' ','#','#','#','#','#','#','#',' ',' ',' ','#'],
        ['#',' ','#',' ','#',' ',' ',' ','#','#','#',' ','#'],
        ['#','#','#',' ','#',' ','#',' ','#',' ',' ',' ','#'],
        ['#',' ',' ',' ','#','#','#',' ',' ',' ','#','#','#'],
        ['#',' ','#','#','#',' ','#',' ','#','#','#',' ','#'],
        ['#',' ','#',' ',' ',' ','#',' ',' ',' ','#',' ','#'],
        ['#',' ','#',' ','#',' ','#','#','#',' ','#',' ','#'],
        ['#',' ',' ',' ','#',' ',' ',' ',' ',' ',' ',' ','#'],
        ['#','#','#','#','#','#',' ','#','#','#','#','#','#']]
    mz = MazeSolver(grid,12,6,0,6)
    print("Solving")
    mz.solvePath2()

if __name__ == "__main__":
    run()
