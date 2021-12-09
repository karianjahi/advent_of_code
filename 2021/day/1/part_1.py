"""
Day 1: Sonar Sweep
"""

class SleightKeys:
    """
    we need to find slight keys:
    day one: count the number of times
    there is an increase in the depth
    """
    def __init__(self, textfile):
        """
        Constructor class
        :param depth_file: a file containing depth measurements
        """
        self.depth_increase_count = None
        self.textfile = textfile



    def count_depth_increases(self):
        """
        count the number times the depth increases
        :return: int
        """
        pass

if __name__ == "__main__":
    afile = "../../../data/day_1_example_data.csv"
    obj = SleightKeys(afile)
    print(obj.read_text_file())



