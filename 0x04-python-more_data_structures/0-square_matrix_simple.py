#!/usr/bin/bash
def square_matrix_simple(miatrix=[]):
    new_matrix = matrix.copy()
    for row in range(len(new_matrix)):
        new_matrix[row] = list(map(lambda x: x ** 2, new_matrix[row]))
    return new_matrix
