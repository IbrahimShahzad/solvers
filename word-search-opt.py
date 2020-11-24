class WordSearch:
    def __init__(self, wordss, arrayy):
        self.words = wordss
        self.array = arrayy
        self.count = 0          # count of letters found (in a word)

    def main_loop(self, word): 
        index = 0               # index of word array
        found = False           # word found or not
        word_length = len(word) # total length of the word array
        rows = 10               # total rows in the grid
        cols = 10               # total columns in the grid
        row = 0
        col = 0
        print(f"Length of the given word: {word_length}")
        if(word_length > rows):
            return "Word Length exceeds the grid row size"
        if(rows != cols):
            return "Grid is not a square."
        for row in range (rows):
            index = 0
            self.count = 0
            for col in range (cols):
                self.count = 0
                if(self.array[row][col] == word[index]):
                    self.count = self.count + 1
                    if(word_length <= cols - col):
                        found = self.check_horizontal(row, col, word_length, word, index)
                        if(found):       
                            return f"Word {word} found!"
                        self.count = 1
                    if(word_length <= rows - row):
                        found = self.check_vertical(row, col, word_length, word, index)
                        if (found):
                            return f"Word {word} found!"
                        self.count = 1
                    if(word_length <= (rows - row) and word_length <= (cols - col)):
                        found = self.check_right_diagonal(row, col, word_length, word, index)
                        if (found):
                            return f"Word {word} found!"
                        self.count = 1
                    if(word_length <= col and word_length <= rows - row):
                        found = self.check_left_diagonal(row, col, word_length, word, index)
                        if (found):
                            return f"Word {word} found!"
                        self.count = 1
            if(row + 1 == rows and self.count != word_length):
                return f"WORD '{word}' not found!"

    def check_horizontal(self, row, col, word_length, word, index):
        for i in range(1, word_length):
            if (self.array[row][col+i] == word[index+i]):                   
                self.count = self.count + 1
            else:
                return False
        return self.count == word_length

    def check_vertical(self, row, col, word_length, word, index):
        for i in range(1, word_length):
            if(self.array[row+i][col] == word[index+i]):
                self.count = self.count + 1
            else:
                return False
        return self.count == word_length

    def check_left_diagonal(self, row, col, word_length, word, index):
        for i in range(1, word_length):
            if (self.array[row+i][col-i] == word[index+i]):
                self.count = self.count + 1
            else:
                return False
        return self.count == word_length

    def check_right_diagonal(self, row, col, word_length, word, index): 
        for i in range(1, word_length):
            if(self.array[row+i][col+i] == word[index+i]):
                self.count = self.count + 1
            else:
                return False   
        return self.count == word_length

if __name__ == '__main__':
    array = [['A','R','R','A','N','G','E','S','T','D'],
             ['P','L','F','W','G','U','B','A','K','E'],
             ['P','C','U','R','T','A','I','N','I','M'],
             ['A','U','R','K','U','B','A','L','N','P'],
             ['R','S','U','V','R','I','G','H','T','R'],
             ['E','T','X','O','G','H','T','L','U','E'],
             ['N','O','O','I','E','K','O','V','R','S'],
             ['T','M','O','O','N','S','O','O','N','S'],
             ['Q','E','C','M','T','H','L','G','C','L'],
             ['Z','R','E','F','R','E','S','H','K','P']
            ]
    words={'FRUIT','CUSTOMER','MOONSOON','ROOM','URGENT','LOST','BAKE','TOOL','MOON','SOON','CUSTOM','CURTAIN','EMPRESS','ARRANGE','APPARENT','RIGHT','REFRESH','TURN'}
    w = WordSearch(words,array)   
    print(w.main_loop(list('MOONSOON')))