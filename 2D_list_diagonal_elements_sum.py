def diagonal_sum(matrix):
    sum =0
    for diagonal_element in range(len(matrix)):
        sum += matrix[diagonal_element][diagonal_element]
    return sum