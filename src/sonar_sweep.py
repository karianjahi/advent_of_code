"""
finding sleight keys
"""
import utils
from utils import use_tuples
import numpy as np
import pandas as pd


class SleightKeys:
    """
    we need to find slight keys:
    day one: count the number of times
    there is an increase in the depth
    """

    def __init__(self, data):
        """
        Constructor class
        :param data: str: > text data
        """
        self.depth_increase_count = None
        self.data = data.split("\n")
        self.submarine_range = 0
        self.submarine_depth = 0
        self.submarine_aim = 0

    def get_running_windows(self, moving_window):
        """
        moving_window: int > how many values per window?
        :param moving_window: int
        :return: list of lists with each containin moving_window values
        """
        running_windows = []
        for index, depth in enumerate(self.data):
            if index < len(self.data) - (moving_window - 1):
                window_indices = range(index, index + moving_window)
                running_windows.append([self.data[i] for i in window_indices])
        return running_windows

    def count_increasing_depths_by_window(self, moving_window):
        """
        moving_window: int > how many values per window?
        Calculating moving depth
        :return: list of moving_window running sums
        """
        moving_window_list_of_list = self.get_running_windows(moving_window)
        moving_window_sum = [sum([float(i) for i in alist]) for alist in moving_window_list_of_list]
        return utils.count_increasing_quantity(moving_window_sum)

    def move_submarine_once(self, command, steps):
        """
        :param command: str. command
        :param steps: int. how many steps
        We need to move the submarine either up, down, or forward
        :return:
        """
        if command == "forward":
            self.submarine_range += steps
            if self.submarine_aim != 0:
                self.submarine_depth += self.submarine_aim * steps
        if command == "down":
            self.submarine_aim += steps
        if command == "up":
            self.submarine_aim -= steps

    def get_commands_and_steps(self):
        """
        Get commands and steps from data
        :return: list of tuples
        """
        commands_and_steps = []
        for line in self.data:
            alist = line.split()
            alist[1] = int(alist[1])
            commands_and_steps.append((alist[0], alist[1]))
        return commands_and_steps

    def move_submarine_the_whole_hog(self):
        """
        move submarine after applying all steps
        :return: None
        """
        for my_tuple in self.get_commands_and_steps():
            self.move_submarine_once(my_tuple[0], my_tuple[1])

    def figure_out_the_rates(self, is_binary=False):
        """
        Figuring out gamma and epsilon rate based on bits
        :param: is_binary - logic if to return binary
        :return: dict
        """
        diagnostic_code_lists = self.get_list_diagnostic_codes()
        gamma_rate = ""
        epsilon_rate = ""
        for diagnostic_code_list in diagnostic_code_lists:
            gamma_rate += f'{utils.get_most_common(diagnostic_code_list, 1)}'
            epsilon_rate += f'{utils.get_least_common(diagnostic_code_list, 1)}'
        if is_binary:
            return {"gamma_rate": gamma_rate,
                    "epsilon_rate": epsilon_rate}
        else:
            return {"gamma_rate": int(gamma_rate, 2),
                    "epsilon_rate": int(epsilon_rate, 2),
                    "power_consumption_rate": int(gamma_rate, 2) * int(epsilon_rate, 2)}

    def get_list_diagnostic_codes(self):
        """
        Get a list of diagnostic codes by putting together
        binary digits of each position across the entire
        array of binary
        :return: list of list
        """
        diagnostic_values_list = []
        for binary_value in self.data:
            diagnostic_values_list.append([int(i) for i in binary_value])
        return np.array(diagnostic_values_list).transpose()

    @staticmethod
    def get_rating(df, is_oxygen, is_binary):
        """
        Get a specific rating
        :param is_oxygen: logical. [should I output oxygen ratings?]
        :param is_binary: logical
        :return: binary or decimal number
        """
        for index in range(len(np.array(df))):
            codes = np.array(df)
            if is_oxygen:
                most_bit = utils.get_most_common(codes[index], 1)
            else:
                most_bit = utils.get_least_common(codes[index], 0)
            # print("")
            # print(f'{index+1}: {[i for i in df.iloc[index]]}, {most_common_bit}')
            for i, value in enumerate(codes[index]):
                if value != most_bit:
                    df[i] = None
        for column in df.columns:
            ratings = [i for i in df[column]]
            if None not in ratings:
                break
        rating = utils.concatenate_list_into_string(ratings)
        if not is_binary:
            return int(rating, 2)
        return rating

    def get_oxygen_rating(self, is_binary):
        """
        :param is_binary: logical [True or False]
        Retaining only the most common bits in a position
        :return:
        """
        df = pd.DataFrame(self.get_list_diagnostic_codes())
        if is_binary:
            return self.get_rating(df, is_oxygen=True, is_binary=True)
        else:
            return self.get_rating(df, is_oxygen=True, is_binary=False)

    def get_co2_rating(self, is_binary):
        """
        :param is_binary: logical [True or False]
        Retaining only the most least bits in a position
        :return:
        """
        df = pd.DataFrame(self.get_list_diagnostic_codes())
        if is_binary:
            return self.get_rating(df, is_oxygen=False, is_binary=True)
        else:
            return self.get_rating(df, is_oxygen=False, is_binary=False)

    def life_support_rating(self):
        """
        This comes from both co2 and oxygen as multiplication
        :return: float
        """
        return self.get_co2_rating(is_binary=False) * self.get_oxygen_rating(is_binary=False)


if __name__ == "__main__":
    # Day 1: First part solution
    text_data = utils.read_text_file("../data/day1_data.csv")
    obj = SleightKeys(text_data)
    print(f'Day 1 part 1 answer: {obj.count_increasing_depths_by_window(moving_window=1)}')

    # Day 1: Second part solution
    # text_data = utils.read_text_file("../data/day1_example_data.csv")
    obj = SleightKeys(text_data)
    print(f'Day 1 part 2 answer: {obj.count_increasing_depths_by_window(moving_window=3)}')

    # Day 2: First part solution:
    text_data = utils.read_text_file("../data/day2_data.csv")
    obj = SleightKeys(text_data)
    obj.move_submarine_the_whole_hog()
    final_range = obj.submarine_range
    final_depth = obj.submarine_depth
    final_product = final_range * final_depth
    print("")
    print("Day 2 part 1 results")
    print("------------------------------")
    print(f'Final range: {final_range}\n'
          f'Final depth: {final_depth}\n'
          f'Final product: {final_product}')

    # Day 2: Second solution
    text_data = utils.read_text_file("../data/day2_data.csv")
    obj = SleightKeys(text_data)
    obj.move_submarine_the_whole_hog()
    final_range = obj.submarine_range
    final_depth = obj.submarine_depth
    final_aim = obj.submarine_aim
    final_product = final_range * final_depth
    print("")
    print("Day 2 part 2 results")
    print("------------------------------")
    print(f'Final range: {final_range}\n'
          f'Final depth: {final_depth}\n'
          f'Final product: {final_product}')

    print("")
    # Day 3: First_solution solution
    text_data = utils.read_text_file("../data/day3_data.csv")
    #text_data = utils.read_text_file("../data/day3_example_data.csv")
    obj = SleightKeys(text_data)
    print("")
    print("Day 3 part 1 results")
    print("------------------------------")
    print(obj.figure_out_the_rates(is_binary=False))
    print("")
    print("Day 3 part 2 results")
    print("------------------------------")
    print(f'Oxygen rating: {obj.get_oxygen_rating(is_binary=False)}')
    print(f'co2 rating: {obj.get_co2_rating(is_binary=False)}')
    print(f'Life support rating: {obj.life_support_rating()}')
