import numpy as np 
from general_functions import *

def calculate_prob_cond(array, target):
    # Here I transpose the array and create an unique array conaining for each row each element once
    base = [list(row) for row in zip(*array)]
        #print(base)
    unique_array = creating_unique_array(base)
        #print(unique_array, "\n")
    #Here I transform the array into a list (1 row with all the different elements) and implementate a counter to know how many element of that kind there are in the array if the target is reached
    unique_list = [item for row in unique_array for item in row]
    unique_list = unique_list[:-2]
        #print(unique_list, "\n")
    counter = [0] * (len(unique_list))
        #print(counter)
    num = 0

    #Filling the counter and counting also the number of 'yes'/'no' 
    for row in range(len(array)):
        for col in range(len(array[row])):
            if array[row][len(array[row])-1] == target:
                for k in range(len(unique_list)):
                    if array[row][col] == unique_list[k]:
                        counter[k] += 1
        
    for i in range(len(base[len(base)-1])):
        if base[len(base)-1][i] == target:
            num += 1
    
        #print(counter, num)

    #Computing the real probabilities
    for i in range(len(counter)):
        counter[i] = counter[i]/num
    
    return unique_list, counter


def calculate_likelihood(training_set):
    unique, prob_y = calculate_prob_cond(training_set, 'yes')
    unique, prob_n = calculate_prob_cond(training_set, 'no')
    return unique, prob_y, prob_n

