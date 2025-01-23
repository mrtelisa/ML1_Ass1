def error_rate(training, result):
    #print(training)
    n = 0
    last = len(training[0]) - 1
    for row in range(len(training)-1):
            #print(result[i])
            #print(training[i][last])
        if result[row] != training[row][last]:
            #print("ciao")
            n += 1
    
    error = n / (len(result))
        #print(error, len(training))

    return error