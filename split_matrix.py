import random
import numpy as np 

def split_matrix_random(matrix):

    # Selecting 4 casual rows
    ind = random.sample(range(len(matrix)), 4)
    #print(ind)

    selected_rows = []
    remaining_rows = []

    # Creating two new matrices
    for i in ind:
        selected_rows.append(list(map(str, matrix[i]))) 
    
    for i in range(len(matrix)):
        if i not in ind:
            remaining_rows.append(list(map(str, matrix[i])))
    
    return selected_rows, remaining_rows

def split_matrix(matrix):

    # Selecting 4 specific rows
    ind = [10, 11, 12, 13]
    #print(ind)

    selected_rows = []
    remaining_rows = []

    # Creating two new matrices
    for i in ind:
        selected_rows.append(list(map(str, matrix[i]))) 
    
    for i in range(len(matrix)):
        if i not in ind:
            remaining_rows.append(list(map(str, matrix[i])))
    
    return selected_rows, remaining_rows


