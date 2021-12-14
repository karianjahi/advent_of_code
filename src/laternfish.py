"""
Day 6 of trying to find the sleight keys
lanternfish
"""


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


class Lanternfish:
    """
    lanternfish swimming across the deep sea
    """
    def __init__(self, data_file):
        self.initial_states = None
        self.initial_state = None
        self.data_file = data_file

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
        return next_states

    def count_total_number_of_fish(self, days):
        return len(self.examine_lanternfish_growth_over_time(days))
            
       



if __name__ == "__main__":
    #datafile = "../data/day6_example_data.csv"
    datafile = "../data/day6_lanternfish_data.csv"
    obj = Lanternfish(datafile)
    days = 256
    print("")
    print("")
    print(f'After {days} days, there shall a total of  {obj.count_total_number_of_fish(days)} fish')





