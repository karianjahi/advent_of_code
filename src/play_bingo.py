"""
Playing bingo with three boards each consisting of 5x5
grid. Each board wins after row or column is has been
filled
"""
import utils
import pandas as pd


class Bingo:
    """
    3 boards each with a grid of 5x5. Won
    when a board has numbers across a row
    or column
    """

    def __init__(self, draws_data_file, boards_data_file):
        """
        Constructor class
        :param draws_data: list [where to draw from]
        :param boards_data: list of tables [boards]
        """
        self.draws_data_file = draws_data_file
        self.boards_data_file = boards_data_file
        self.draws_data = None
        self.boards_data = None

    def read_draws_data(self):
        """
        Read the file containing draws
        :return: None
        """
        df = pd.read_csv(self.draws_data_file)
        self.draws_data = [int(i) for i in df.columns]

    def read_boards_data(self):
        """
        Reads the boards data
        :return: dictionary of pandas dataframes
        """
        with open(self.boards_data_file, "r") as file:
            data = file.read()
        board_lists = utils.divide_list_into_equal_chunks([i.strip() for i in data.split("\n") if i != ""], 5)
        df_board_dict = {}
        for index, board_list in enumerate(board_lists):
            board_split = [[int(j) for j in i.split()] for i in board_list]
            df_board_dict[index+1] = pd.DataFrame(board_split)
        return df_board_dict



if __name__ == "__main__":
    draws_data_file = "../data/day4_draws_example_data.csv"
    boards_data_file = "../data/day4_boards_example_data.csv"
    obj = Bingo(draws_data_file, boards_data_file)
    print(obj.read_boards_data())
