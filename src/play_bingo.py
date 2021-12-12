"""
Playing bingo with three boards each consisting of 5x5
grid. Each board wins after row or column is has been
filled
"""
import utils
import pandas as pd


def check_if_this_board_has_won(board_table):
    """
    We need to check if a table has won by going
    through the columns and rows trying to find
    which rows or columns have complete stars.
    :param board_table: pandas table [with possible marks
    see preceding function]
    :return dict [keys: row/column number, unmarked sum, score]
    """
    print(board_table)
    for name in board_table.columns:
        col_values = [i for i in board_table[name]]
        if utils.is_all_equal(col_values):
            return True
        else:
            return False
    for row in board_table.index:
        row_values = [i for i in board_table.loc[row]]
        if utils.is_all_equal(row_values):
            return True
        else:
            return False


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
            df_board_dict[index + 1] = pd.DataFrame(board_split)
        return df_board_dict

    def mark_all_tables_per_draw(self, draw, boards_data_dict):
        """
        Once a draw has been drawn,
        we need to update the table
        with a say a * at that point
        :param draw: int [number drawn]
        :param boards_data_dict: dictionary of tables
        """
        for key in boards_data_dict:
            table = boards_data_dict[key]
            for col_index, col in enumerate(table.columns):
                column_data = [i for i in table[col]]
                for row_index, value in enumerate(column_data):
                    # print(f'row: {row_index}  column: {col_index} value: {value}')
                    if value == draw:
                        table.iloc[row_index, col_index] = "*"
            boards_data_dict[key] = table
        return boards_data_dict

    def determine_winning_board(self):
        """
        Here we want to make a single move on all
        boards and inspect the results for a possible
        win
        """
        self.read_draws_data()
        tables_dict_per_draw = None  # to avoid pycharm highlighting it
        for draw_index, draw in enumerate(self.draws_data):
            if draw_index == 0:
                tables_dict_per_draw = self.read_boards_data()  # read the whole data at the beginning to be able to update later
            tables_dict_per_draw = self.mark_all_tables_per_draw(draw, tables_dict_per_draw)
            for key in tables_dict_per_draw:
                board_table = tables_dict_per_draw[key]
                win_flag = check_if_this_board_has_won(board_table)
                if win_flag:
                    print("-----------------------------")
                    print(f'Table {key} has won the game')
                    print("-----------------------------")
                    print(board_table)
                    return f'Table {key} has won the game'


if __name__ == "__main__":
    draws_data_file = "../data/day4_draws_example_data.csv"
    boards_data_file = "../data/day4_boards_example_data.csv"
    #
    # draws_data_file = "../data/day4_draws_data.csv"
    # boards_data_file = "../data/day4_boards_data.csv"
    obj = Bingo(draws_data_file, boards_data_file)
    print(obj.determine_winning_board())
