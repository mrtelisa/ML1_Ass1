import numpy as np
import matplotlib.pyplot as plt

def plot_histogram(values_array, iterations, string):
    # Filter the non valid values
    values_array = [v for v in values_array if v in [0, 0.25, 0.5, 0.75, 1]]
    
    # Check if the array is empty after filtering it
    if not values_array:
        print("No valid values in the array")
        return

    # Defining the possible values
    bins = [0, 0.25, 0.5, 0.75, 1]
    
    # Plotting the histogram 
    plt.hist(values_array, bins=[-0.1, 0.1, 0.35, 0.6, 0.85, 1.3], rwidth=0.8, align='mid')

    plt.xticks(bins)
    plt.xlabel('Values')
    plt.ylabel('Count')
    plt.title(f"% of elements of the test_set with a wrong output over {iterations} iterations computed with the {string} method:")

    # Show the graph
    plt.show()
