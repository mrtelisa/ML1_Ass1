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

""" This programm computes the likelihood probability with the Laplace smoothing approach"""

# Creating a matrix containing the data in the file
weather_matrix = create_matrix('weather_data.txt')
    #print(weather_matrix, "\n")
    #print(weather_matrix[7][4])

error_l = []
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
        print("Error found! The test set is not suitable! Passing on the next iteration")
        continue

    prior_tr_y, prior_tr_n = calculate_prior(training_set)
        #print(prior_tr_y, "\n\n", prior_tr_n, "\n")

    unique_list, training_yl, training_nl = laplace_likelihood(training_set)
        #print(training_yl, "\n\n", training_nl, "\n\n")

    dict_yl = create_dict(training_set, training_yl, unique_list)
    dict_nl = create_dict(training_set, training_nl, unique_list)
        #print(dict_yl, dict_yl)

    #posterior_yl = calculate_posterior(training_set, training_yl, prior_tr_y, dict_yl)
    #posterior_nl = calculate_posterior(training_set, training_nl, prior_tr_n, dict_nl)
        #print(posterior_yl, "\n\n")
        #print(posterior_nl, "\n\n")

    posterior_test_yl = calculate_posterior(test_set, training_yl, prior_tr_y, dict_yl)
    posterior_test_nl = calculate_posterior(test_set, training_nl, prior_tr_n, dict_nl)
        #print(posterior_test_yl)
        #print(posterior_test_nl)

    results_l = compute_result(posterior_test_yl, posterior_test_nl)
        #print(posterior_test_yl, "\n\n", posterior_test_nl, "\n\n", results_l)
    
    last_pos = 0
    for i in range(len(test_set)):
        if test_set[i][len(test_set[i])-1] == 'yes' or test_set[i][len(test_set[i])-1] == 'no':
            last_pos += 1
        if last_pos == (len(test_set) - 1):
            it += 1
            error_l.append(error_rate(test_set, results_l))
            if error_rate(test_set, results_l) == 1:
                print(results_l)

if it == (iterations - n):
    #print(results_l)
    plot_histogram(error_l, iterations, 'Laplace')
else:
    print(results_l)
    


