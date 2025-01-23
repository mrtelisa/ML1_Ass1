import pandas as pd 
from create_matrix import *
from split_matrix import split_matrix, split_matrix_random
from control_matrices import *
from calculate_likelihood import *
from general_functions import *
from calculate_prior import *
from calculate_posterior import *
from compute_result import *
from error_rate import *
from plot_hist import *
from laplace_likelihood import *

""" This programm computes the likelihood probability with the normal approach"""

# Creating a matrix containing the data in the file
weather_matrix = create_matrix('weather_data.txt')
    #print(weather_matrix, "\n")
    #print(weather_matrix[7][4])

error = []
n = 0
it = 0

iterations = 1000

for i in range(iterations):
    """This code should be uncommented in case it wants to be tested a specific test_set on the data gained from a specific training_set:
        test_set = create_matrix('test_set.txt')
        training_set = create_matrix('training_set.txt')"""
        
    test_set, training_set = split_matrix_random(weather_matrix)
        #print(test_set, "\n")
        #print(training_set, "\n")
        #print(training_set[1])
    
    ok = control_matrices(training_set, test_set)
    if not ok:
        n += 1
        print("\n", test_set)
        print("\nError found! This test set is not computable! Passing on the next iteration")
        continue

    prior_tr_y, prior_tr_n = calculate_prior(training_set)
        #print(prior_tr_y, prior_tr_n, "\n")

    unique_list, training_y, training_n = calculate_likelihood(training_set)
        #print(training_y, "\n\n", training_n)

    dict_y = create_dict(training_set, training_y, unique_list)
    dict_n = create_dict(training_set, training_n, unique_list)
        #print(dict_y, "\n")
        #print(dict_n, "\n")

    #posterior_y = calculate_posterior(training_set, training_y, prior_tr_y, dict_y)
    #posterior_n = calculate_posterior(training_set, training_n, prior_tr_n, dict_n)
        #print(posterior_y, "\n")
        #print(posterior_n, "\n")

    posterior_test_y = calculate_posterior(test_set, training_y, prior_tr_y, dict_y)
    posterior_test_n = calculate_posterior(test_set, training_n, prior_tr_n, dict_n)
        #print(posterior_test_y, "\n")
        #print(posterior_test_n, "\n")

    results = compute_result(posterior_test_y, posterior_test_n)
        #print(posterior_test_y, "\n")
        #print(posterior_test_n, "\n")
        #print(results, "\n")
    
    last_pos = 0
    for i in range(len(test_set)):
        if test_set[i][len(test_set[i])-1] == 'yes' or test_set[i][len(test_set[i])-1] == 'no':
            last_pos += 1
        if last_pos == (len(test_set) - 1):
            it += 1
            error.append(error_rate(test_set, results))

#print(error)

print("\n\nNumber of iterations skipped:", n)

if it == (iterations - n):
    #print(results)
    plot_histogram(error, iterations, 'normal')
else:
    print(results)



    


