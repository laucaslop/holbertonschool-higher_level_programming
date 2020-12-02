#!/usr/bin/python3
""" matrix_divide a new matrix divided by div """

general_error = "matrix must be a matrix (list of lists) of integers/floats"


def matrix_divided(matrix, div):
    """ This divides all elements of a matrix by a number div """
    new_list = []

    validate_matrix(matrix)
    validate_div(div)

    for idx in matrix:
        new_list.append(list(map(lambda x: round(x / div, 2), idx)))

    return new_list


def validate_matrix(matrix):
    """ Validate tests matrix """
    if type(matrix) != list or len(matrix) == 0 or matrix[0] is None:
        raise TypeError(general_error)

    for idx in matrix:
        if len(idx) == 0:
            raise TypeError(general_error)
        elif len(matrix[0]) != len(idx):
            raise TypeError("Each row of the matrix must have the same size")
        elif not isinstance(idx, list):
            raise TypeError(general_error)
        else:
            for jdx in idx:
                if not isinstance(jdx, (int, float)):
                    raise TypeError(general_error)


def validate_div(div):
    """ Validate cases div """

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    elif div == 0:
        raise ZeroDivisionError("division by zero")
