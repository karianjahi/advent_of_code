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
        self.read_draws_data()
        with open(self.boards_data_file, "r") as file:
            data = file.read()
        board_lists = utils.divide_list_into_equal_chunks([i.strip() for i in data.split("\n") if i != ""], 5)
        df_board_dict = {}
        for index, board_list in enumerate(board_lists):
            board_split = [[int(j) for j in i.split()] for i in board_list]
            df_board_dict[index+1] = pd.DataFrame(board_split)
        return df_board_dict

    def play_one_board(self, board_number):
        """
        :param board_number: int [board number in dict]
        Draws for a single board
        """

        board_table = self.read_boards_data()[board_number]
        board_table.columns = [f'c{i+1}' for i in board_table.columns]
        board_table.index = [f'r{i+1}' for i in board_table.index]
        board_table_original = board_table.copy()
        print("")
        print(board_table)
        print("")
        print(self.draws_data)
        print("")
        print("")
        for draw in self.draws_data:
            for row in board_table.index:
                for col in board_table.columns:
                    row_col_value = board_table.loc[row, col]
                    if row_col_value == draw:
                        board_table.loc[row, col] = "*"
                    print("")
                    print("")
                    print("")
                    print(board_table)
                    # compare row values for equality
                    for irow in board_table.index:
                        if utils.is_all_equal(board_table.loc[irow]):
                            row_values = [i for i in board_table_original.loc[irow]]
                            # Calculate sum of unmarked numbers in the table:
                            unmarked_sum = sum(utils.table2list(board_table, True))
                            score = unmarked_sum * draw

                            return f'Board number {board_number} wins at row {irow}: ' \
                                   f'row values are: {row_values}. unmarked sum = {unmarked_sum}.' \
                                   f' Winning score = {score}'
                    # compare col values for equality
                    for icol in board_table.columns:
                        if utils.is_all_equal(board_table_original.loc[:, icol]):
                            col_values = [i for i in board_table_original.loc[:, icol]]
                            unmarked_sum = sum(utils.table2list(board_table, True))
                            score = unmarked_sum * draw
                            return f'Board number {board_number} wins at column {icol}: ' \
                                   f'column values are: {col_values}. unmarked sum = {unmarked_sum}. ' \
                                   f'Winning score = {score}'




if __name__ == "__main__":
    draws_data_file = "../data/day4_draws_example_data.csv"
    boards_data_file = "../data/day4_boards_example_data.csv"
    obj = Bingo(draws_data_file, boards_data_file)
    print(obj.play_one_board(3))


