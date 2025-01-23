import numpy as np

def calculate_prior(training_set):
    training_set = np.array(training_set)
    
    # Creating the col_play in which I store all the values in the column Play of the training set
    last = training_set.shape[1] - 1
    col_play = training_set[:, last]
        #print(col_play, "\n")
    tot = col_play.size     # Here i get the numer of elements in the array
        #print(tot, "\n")

    # Here i calculate the probability of 'yes' and 'no', firstly counting how many yes and no there are in col_play and then computing the probability
    y, n = 0, 0
    for i in range(tot):
        if col_play[i] == 'no':
            n = n+1
                #print(col_play[i], n)
        if col_play[i] == 'yes':
            y = y+1
                #print(col_play[i], y)
    
    p_n = n / tot
    p_y = y / tot

    return p_y, p_n
