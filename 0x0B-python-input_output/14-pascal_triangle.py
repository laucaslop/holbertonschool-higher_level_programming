#!/usr/bin/python3
""" Module """


def pascal_triangle(n):
    """ Args:
        n ([int]): [size of tringle]
    Returns:
        [list]: [pascal triangle] """
    lt = [1, 1]
    new = []
    fin = [[1], [1, 1]]
    if n <= 0:
        return new
    if n == 1:
        return [[1]]
    elif n == 2:
        return [[1], [1, 1]]
    else:
        for i in range(3, n + 1):
            new.append(1)
            for j in range(len(lt) - 1):
                new.append(lt[j] + lt[j + 1])
            new.append(1)
            fin.append(new)
            lt = new.copy()
            new = []
        return(fin)
