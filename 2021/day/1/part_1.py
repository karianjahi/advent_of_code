"""
Day 1: Sonar Sweep
"""

class sleight_keys:
    """
    we need to find slight keys:
    day one: count the number of times
    there is an increase in the depth
    """
    def __init__(self, depth_file):
        """
        Constructor class
        :param depth_file: a file containing depth measurements
        """
        self.depth_increase_count = None
        self.depth_file = depth_file

    def count_depth_increases(self):
        """
        count the number times the depth increases
        :return: int
        """



