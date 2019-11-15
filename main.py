import random
import operator
import math
# we want to find the steady state probability
# Run the model from task 2 for 3 time steps. Based on 10000 repetitions report the probability and
# standard deviation that at time step three (that is after three updates) the turtle is at cell 1,3,9.


def valid_probabilities(chain: dict):
    """
    :param chain: The markov chain model
    :return: true if all probabilities sum to 1, false if otherwise
    """
    for state in chain:
        a = 0
        probs = chain[state]
        for i in probs:
            a = a + (probs[i])
        if a != 1:
            print('Not all probability values sum to 1')
            exit(1)


def get_random_num():
    return random.uniform(0, 1)


def tower_sample(current_state: str, chain: dict):
    # tower sampling chooses a state to transition to based off of the probabilities of the transitions
    k_possible_transitions_from_current_state = len(chain[current_state].keys())
    # print("current_state: {}".format(current_state))
    # print("possible transitions: {}".format(k_possible_transitions_from_current_state))
    ordered_probabilities = sorted(chain[current_state].items(), key=operator.itemgetter(1), reverse=True)
    t = [0] * (k_possible_transitions_from_current_state + 1)  # array of size k + 1 with all elements set to 0
    for i in range(0, k_possible_transitions_from_current_state):  # add ordered probabilities into this array
        t[i + 1] = ordered_probabilities[i]
    # print("ordered probability t array: {}".format(t))
    r = get_random_num()
    sum_of_t_elements = 0
    state = None
    for probability in range(0, len(t)):
        if probability == 0:
            sum_of_t_elements = t[probability] + sum_of_t_elements
        else:
            sum_of_t_elements = t[probability][1] + sum_of_t_elements  # if not first element then the results will be in a tuple.
            # print("this iteration of sum: {}".format(sum_of_t_elements))
        if not (r > sum_of_t_elements): # if r is not greater than the sum of the elements, then we have found the state to transition to
            # print("stopping sum as r {} which is smaller than the sum: {}".format(r, sum_of_t_elements))
            # print("the state that r is smaller than or equal to is: {}".format(t[probability]))
            state = t[probability][0]
            # print('go to state {}'.format(state))
            break
    return int(state)


def get_mean(listof: list, runs: int):
    i = 0
    for num in listof:
        i = i + num
    return i / runs


def get_standard(listof: list, mean: float):
    mean_minus_probability_squared_values = []
    for probability in listof:
        prob_minus_mean = probability - mean
        squared_val = (prob_minus_mean ** 2)
        mean_minus_probability_squared_values.append(squared_val)
    summed_values = 0
    for num in mean_minus_probability_squared_values:
        summed_values = summed_values + num
    variance = ((1/len(mean_minus_probability_squared_values)) * summed_values)
    return math.sqrt(variance)


if __name__ == '__main__':
    # below we have a markov chain that contains the transition probabilities, so now we do not need the metropolis algorithm
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
    valid_probabilities(chain=chain)

    states = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    times_in_each_state_count = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    current_state = random.choice(states)
    print("STARTING STATE: {}".format(current_state))
    time_steps = 3
    repetitions = 10000
    total_runs = 50

    one = []
    nine = []
    three = []

    for i in range(0, total_runs):
        for repetition in range(1, repetitions + 1):
            for time_step in range(1, time_steps + 1):
                chosen_state = tower_sample(current_state=current_state, chain=chain)
                current_state = str(chosen_state)
            times_in_each_state_count[chosen_state] = times_in_each_state_count[chosen_state] + 1
        print(times_in_each_state_count)
        probability_of_being_in_1 = times_in_each_state_count[1] / repetitions
        probability_of_being_in_2 = times_in_each_state_count[2] / repetitions
        probability_of_being_in_3 = times_in_each_state_count[3] / repetitions
        probability_of_being_in_4 = times_in_each_state_count[4] / repetitions
        probability_of_being_in_5 = times_in_each_state_count[5] / repetitions
        probability_of_being_in_6 = times_in_each_state_count[6] / repetitions
        probability_of_being_in_7 = times_in_each_state_count[7] / repetitions
        probability_of_being_in_8 = times_in_each_state_count[8] / repetitions
        probability_of_being_in_9 = times_in_each_state_count[9] / repetitions
        print('Estimated probability of being in state 1: {}'.format(probability_of_being_in_1))
        print('Estimated probability of being in state 3: {}'.format(probability_of_being_in_3))
        print('Estimated probability of being in state 9: {}'.format(probability_of_being_in_9))
        one.append(probability_of_being_in_1)
        three.append(probability_of_being_in_3)
        nine.append(probability_of_being_in_9)
        times_in_each_state_count = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    print(" ")

    mean_one = get_mean(listof=one, runs=total_runs)
    standard_deviation_one = get_standard(listof=one, mean=mean_one)
    print("probability of state one: {}, standard deviation: {}".format(mean_one, standard_deviation_one))

    mean_three = get_mean(listof=three, runs=total_runs)
    standard_deviation_three = get_standard(listof=three, mean=mean_three)
    print("probability of state three: {}, standard deviation: {}".format(mean_three, standard_deviation_three))

    mean_nine = get_mean(listof=nine, runs=total_runs)
    standard_deviation_nine = get_standard(listof=nine, mean=mean_nine)
    print("probability of state nine: {}, standard deviation: {}".format(mean_nine, standard_deviation_nine))
