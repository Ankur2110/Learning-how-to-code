def rotate_anticlock(matrix):
    for row in matrix:
        row.reverse()
    for row in range(len(matrix)):
        for column in range(row,len(matrix)):
            matrix[row][column], matrix[column][row] = matrix[column][row], matrix[row][column]
    return matrix



print (rotate_anticlock([[1,2,3],[4,5,6],[7,8,9]]))