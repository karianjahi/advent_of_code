"""
Test for possible bugs in find sleight keys
"""
import pytest
from sonar_sweep import SleightKeys


class TestFindSleightKeys:
    """
    Testing SleightKeys class
    """
    TEST_DATA = "2\n5\n3\n1"
    OBJ = SleightKeys(TEST_DATA)

    def test_running_windows(self):
        """
        Test if we can get the values:
        [[2, 5, 3], [5, 3, 1]]
        :return: None
        """
        assert TestFindSleightKeys.OBJ.get_running_windows(3) == [["2", "5", "3"], ["5", "3", "1"]]

    def test_count_increasing_depths_by_window(self):
        """
        Testing increasing depths
        :return: None
        """
        assert TestFindSleightKeys.OBJ.count_increasing_depths_by_window(3) == 0
