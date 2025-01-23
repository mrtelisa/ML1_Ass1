import numpy as np 
from general_functions import *

def control_matrices(training_set, test_set):
    c1 = len(training_set[0])
    c2 = len(test_set[0])
        #print(c1, c2)
    if c1 != c2:
        if c1 != (c2 + 1): 
            raise ValueError("Error: the test set is not suitable!")
        #else: n1 == n2-1; case in which I have in the test set a target class -> I'm ok
   
    training_set_flat = flatten_list(training_set)
    test_set_flat = flatten_list(training_set)

    # Check if all the element in the test_set_flat are in the training_set_flat
    all_ok = np.isin(test_set_flat, training_set_flat).all()


    #all_ok = np.isin(test_set, training_set).all()
    return all_ok


