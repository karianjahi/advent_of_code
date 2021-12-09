"""
Day 1: Sonar Sweep
"""
from advent_of_code import utils
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


if __name__ == "__main__":
    # Day 1: First part solution
    text_data = utils.read_text_file("../../data/day1_data.csv")
    obj = SleightKeys(text_data)
    print(f'Day 1 part 1 answer: {obj.count_increasing_depths_by_window(moving_window=1)}')

    # Day 1: Second part solution
    # text_data = utils.read_text_file("../../data/day1_example_data.csv")
    obj = SleightKeys(text_data)
    print(f'Day 1 part 2 answer: {obj.count_increasing_depths_by_window(moving_window=3)}')
