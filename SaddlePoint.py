import numpy as np


def is_saddle(row, column, *args):
    index = 0
    size = row * column
    matrix = np.arange(size).reshape(row, column)
    for i in range(row):
        for j in range(column):
            matrix[i][j] = args[0][index]
            index = index + 1
    print(matrix)
    for item_row in matrix:
        column_number = 0
        min_item = np.amin(item_row)
        for i in range(len(item_row)):
            if min_item == item_row[i]:
                row_number = i
                reversed_matrix = matrix.transpose()
                max_item = np.amax(reversed_matrix[row_number])
                if max_item == min_item:
                    print("saddle point found : {}".format(min_item))

    return matrix


row = input("enter row")
column = input("enter column")
matrix = input("enter the matrix items")
is_saddle(row, column, matrix)
