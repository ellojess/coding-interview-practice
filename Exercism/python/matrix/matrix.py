"""
- A list of the rows, reading each row left-to-right 
  while moving top-to-bottom across the rows,
- A list of the columns, reading each column top-to-bottom 
  while moving from left-to-right.

"""

class Matrix:
    def __init__(self, matrix_string):
        self.matrix = [list(map(int, x.split())) for x in matrix_string.split('\n')]

    def row(self, index):
        return self.matrix[index - 1]

    def column(self, index):
        return [x[index - 1] for x in self.matrix]