from general_functions import *

def calculate_posterior(matrix, likelihood, prior, dict):

    minimum = len(matrix[0])
    for i in range(len(matrix)):
        if len(matrix[i]) < minimum:
            minimum = len(matrix[i])
        #print(minimum)

    result =[1 for i in range(len(matrix))]
        #print(result)
    
    for row in range(len(matrix)):
        for col in range(minimum):
            for key, value in dict.items():
                if matrix[row][col] == key:
                    result[row] = result[row] * value
    
        #print(result)
    
    for i in range(len(result)):
        result[i] = result[i] * prior

        #print(result)

    return result