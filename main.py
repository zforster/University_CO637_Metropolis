import random

# Run the model from task 2 for 3 time steps. Based on 10000 repetitions report the probability and
# standard deviation that at time step three (that is after three updates) the turtle is at cell 1,3,9.

if __name__ == '__main__':
    chain = {'1': {'1': 0.5, '2': 0.25, '4': 0.25},
             '2': {'1': 0.25, '2': 0.25, '3': 0.25, '5': 0.25},
             '3': {'2': 0.25, '3': 0.5, '6': 0.25},
             '4': {'1': 0.125, '5': 0.25, '4': 0.375, '7': 0.25},
             '5': {'4': 1/4, '2': 1/8, '6': 1/4, '8': 1/4, '5': 1/8},
             '6': {'9': 1/4, '3': 1/8, '5': 1/4, '6': 3/8},
             '7': {'4': 1/6, '8': 1/4, '7': 7/12},
             '8': {'9': 1/4, '7': 1/4, '5': 1/6, '8': 1/3},
             '9': {'9': 7/12, '6': 1/6, '8': 1/4}
             }

    for state in chain:
        a = 0
        probs = chain[state]
        for i in probs:
            a = a + (probs[i])
        print(a)