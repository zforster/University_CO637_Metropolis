import random
import operator

# turtle start = 1
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
    time_steps = 3
    repetitions = 1000

    chosen_state = None
    for time_step in range(0, time_steps):
        for repetition in range(0, repetitions):
            # print("we are in state: {}".format(state_choice))
            # tower sample: algorithm below
            k_possible_transitions_from_current_state = len(chain[current_state].keys())
            # print("there are {} possible transitions".format(k_possible_transitions_from_current_state))

            ordered_probabilities = sorted(chain[current_state].items(), key=operator.itemgetter(1), reverse=True)

            t = [0] * (k_possible_transitions_from_current_state + 1)  # array of size k + 1 with all elements set to 0
            for i in range(0, k_possible_transitions_from_current_state):  # add ordered probabilities into this array
                t[i + 1] = ordered_probabilities[i]

            r = get_random_num()

            sum_of_t_elements = 0
            chosen_state = None
            for i in range(0, len(t)):
                if i == 0:
                    sum_of_t_elements = t[i] + sum_of_t_elements
                else:
                    sum_of_t_elements = t[i][1] + sum_of_t_elements
                if not (r > sum_of_t_elements):
                    chosen_state = t[i]
                    break
            chosen_state = int(chosen_state[0])

             # tower sample end
            state_choice = str(chosen_state)
            chosen_state = state_choice
        # print("we have finished in state {}".format(chosen_state))
        times_in_each_state_count[int(chosen_state)] = times_in_each_state_count[int(chosen_state)] + 1
    print(times_in_each_state_count)
    probability = times_in_each_state_count[3] / time_steps
    print(probability)