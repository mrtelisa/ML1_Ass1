def compute_result(post_y, post_n):
    
    result = []
    
    for pos in range(len(post_y)):
        if post_y[pos] > post_n[pos]:
            result.append('yes')
        elif post_y[pos] < post_n[pos]:
            result.append('no')
        else:
            result.append('same probability of yes and no')

    return result