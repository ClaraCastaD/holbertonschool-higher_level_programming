#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
        for i in (matrix):
            k = 0
            for j in i:
                k = k + 1
                if (k == len(i)):
                    print("{:d}".format(j), end="")
                else:
                    print("{:d}".format(j), end=" ")
            print()
