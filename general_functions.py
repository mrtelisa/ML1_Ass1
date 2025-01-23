import numpy as np 

def divide_by_position(array_list):
    # Converts the array list in a numpy array to make the manipulation easier
        #print(array_list, "\n\n")
    np_array = np.array(array_list, dtype = object)
    
    # Uses the transposition to divide the array based on the position of the elements
    divided_arrays = np_array.T  # Transposition
        #print(divided_arrays, "\n")

    # Returns tehe transpose matrix in a numpy array list
    return [divided_arrays]

def create_dict(training_set, likelihood, unique_list):
        #print(likelihood)     
    dict = {}
    for i in range(len(unique_list)):
        dict[unique_list[i]] = likelihood[i]
        #print(dict)

    return dict

def creating_unique_array(array):
    #print(array)
    
    unique_array = []
    unique_row = []
    
    for row in range(len(array)):
        unique_row = list(set(array[row]))
            #print(unique_row)
        unique_array.append(unique_row)
    
    return unique_array

def flatten_list(set):
    flat_list = []
    for item in set:
        if isinstance(item, list):
            flat_list.extend(flatten_list(item))
        else:
            flat_list.append(item)
    return flat_list
