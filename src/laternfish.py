"""
Day 6 of trying to find the sleight keys
lanternfish
"""

from collections import deque
import sys
def create_and_reset_lanternfish_timer(initial_states):
    next_states = [None] * len(initial_states)
    for index, item in enumerate(initial_states):
        if index == len(initial_states) - 1:
            if item == 0:
                next_states.append(8)
            else:
                next_states[index] = initial_states[index] - 1
        else:
            if item == 0:
                next_states[index] = 6
                next_states.append(8)
            else:
                next_states[index] = initial_states[index] - 1
    return next_states


def count_number_of_fish_after_n_days(laternfish_list, no_of_days):
    # init counts
    basket = deque([0] * 9)
    for laternfish in laternfish_list:
        basket[laternfish] += 1

    # run through days
    for each_day in range(no_of_days):
        basket[7] += basket[0]
        basket.rotate(-1)
    return sum(basket)


class Lanternfish:
    """
    lanternfish swimming across the deep sea
    """
    def __init__(self, data_file, days_to_simulate):
        self.initial_states = None
        self.initial_state = None
        self.data_file = data_file
        self.days_to_simulate = days_to_simulate

    def read_data(self):
        with open(self.data_file, "r") as afile:
            data = afile.read()
        self.initial_states = [int(i) for i in data.split(",")]

    def examine_lanternfish_growth_over_time(self, days):
        self.read_data()
        initial_states = self.initial_states
        for day in range(days):
            print(f'day: {day}/{days} days')
            next_states = create_and_reset_lanternfish_timer(initial_states)
            initial_states = next_states
            sys.getsizeof(initial_states)
        return next_states

    def count_total_number_of_fish(self, days):
        return len(self.examine_lanternfish_growth_over_time(days))

    def get_total_number_of_fish_deque(self):
        self.read_data()
        return count_number_of_fish_after_n_days(self.initial_states, self.days_to_simulate)


if __name__ == "__main__":
    # datafile = "../data/day6_example_data.csv"
    datafile = "../data/day6_lanternfish_data.csv"
    obj = Lanternfish(datafile, days_to_simulate=256)
    print("")
    print("")
    print(f'After {obj.days_to_simulate} days, there shall a total of {obj.get_total_number_of_fish_deque()} fish')






