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
        self.data = data

    def count_depth_increases(self):
        """
        count the number times the depth increases
        :return: int
        """
        depths = [int(value) for value in self.data.split("\n")]
        count_increments = []
        for index, depth in enumerate(depths):
            if index != 0:
                if depth > depths[index-1]:
                    count_increments.append(True)
                else:
                    count_increments.append(False)
            else:
                count_increments.append(False)
        # sl = pd.DataFrame({"dat": self.data.split("\n"), "inc": count_increments})
        # print(sl)
        return sum(count_increments)






if __name__ == "__main__":
    text_data = utils.read_text_file("../../data/day_1_example_data.csv")
    obj = SleightKeys(text_data)
    print(obj.count_depth_increases())

