import numpy as np

def create_matrix(file_path):   # This function reads a file and puts its data into a matrix

    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Diving each row in a list of values
    data = [line.strip().split() for line in lines]

    # Convert the list into a matrix and eliminating the first row
    matrix = np.array(data, dtype = object)
    matrix = matrix[1:]
    
    return matrix
