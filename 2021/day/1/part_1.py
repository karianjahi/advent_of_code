"""
Day 1: Sonar Sweep
"""
from advent_of_code import utils
from advent_of_code.utils import use_tuples
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
        if command == "down":
            self.submarine_depth += steps
        if command == "up":
            self.submarine_depth -= steps

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

    def move_submarine(self):
        """
        move submarine
        :return: None
        """
        for my_tuple in self.get_commands_and_steps():
            self.move_submarine_once(my_tuple[0], my_tuple[1])


if __name__ == "__main__":
    # Day 1: First part solution
    text_data = utils.read_text_file("../../data/day1_data.csv")
    obj = SleightKeys(text_data)
    print(f'Day 1 part 1 answer: {obj.count_increasing_depths_by_window(moving_window=1)}')

    # Day 1: Second part solution
    # text_data = utils.read_text_file("../../data/day1_example_data.csv")
    obj = SleightKeys(text_data)
    print(f'Day 1 part 2 answer: {obj.count_increasing_depths_by_window(moving_window=3)}')

    # Day 2: First part solution:
    text_data = utils.read_text_file("../../data/day2_example_data.csv")
    obj = SleightKeys(text_data)
    obj.move_submarine()
    final_range = obj.submarine_range
    final_depth = obj.submarine_depth
    final_product = final_range * final_depth
    print("")
    print("Day 2 part 1 results")
    print("------------------------------")
    print(f'Final range: {final_range}\n'
          f'Final depth: {final_depth}\n'
          f'Final product: {final_product}')

