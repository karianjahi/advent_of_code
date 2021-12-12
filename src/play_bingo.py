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

    :return logic
    """
    for name in board_table.columns:
        col_values = [i for i in board_table[name]]
        if utils.is_all_equal(col_values):
            return True
    for row in board_table.index:
        row_values = [i for i in board_table.loc[row]]
        if utils.is_all_equal(row_values):
            return True


def mark_all_tables_per_draw(draw, boards_data_dict):
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


class Bingo:
    """
    n boards each with a grid of 5x5. Won
    when a board has equal numbers across a row
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
        self.boards_data = df_board_dict

    def determine_winning_board(self):
        """
        Here we want to make a single move on all
        boards and inspect the results for a possible
        win
        """
        self.read_draws_data()
        self.read_boards_data()
        tables_dict_per_draw = None  # to avoid pycharm highlighting it
        for draw_index, draw in enumerate(self.draws_data):
            print(f'Draw number: {draw_index + 1}/{len(self.draws_data)}')
            if draw_index == 0:
                tables_dict_per_draw = self.boards_data  # read the whole data at the beginning to be able to update later
            tables_dict_per_draw = mark_all_tables_per_draw(draw, tables_dict_per_draw)
            for key in tables_dict_per_draw:
                board_table = tables_dict_per_draw[key]
                if check_if_this_board_has_won(board_table):
                    print("")
                    print("")
                    print(f'Winning board: {key}')
                    print("-----------------------")
                    unmarked_sum = sum(utils.table2list(board_table, consider_floats_only=True))
                    print("Unplayed Board")
                    print("-----------------------")
                    print(self.boards_data[key])
                    print("")
                    print("-----------------------")
                    print("Current Board")
                    print("-----------------------")
                    print(board_table)
                    print("")
                    print("-----------------------")
                    print("Additional results")
                    print("-----------------------")
                    return f'unmarked sum : {unmarked_sum}\n' \
                           f'last drawn: {draw}\n' \
                           f'score: {unmarked_sum * draw}'

    def get_last_board_to_win(self):
        """
        Get the last board to win
        """
        winning_boards = []
        self.read_draws_data()
        self.read_boards_data()
        boards_data_dict = self.boards_data
        for draw_index, draw in enumerate(self.draws_data):
            boards_data_dict = mark_all_tables_per_draw(draw, boards_data_dict)
            dict_keys = [i for i in boards_data_dict.keys()]
            key = 1
            while key in dict_keys:
                if check_if_this_board_has_won(boards_data_dict[key]):
                    unmarked_sum = sum(utils.table2list(boards_data_dict[key], True))
                    winning_boards.append({"winning_board": key,
                                           "current_board": boards_data_dict[key],
                                           "last_draw": draw,
                                           "unmarked_sum": unmarked_sum,
                                           "score": unmarked_sum * draw})
                    # print("")
                    # print("-------------------------------")
                    # print(f'Board {key} has won the game')
                    # print("--------------------------------")
                    # print("")
                    ncolumns = len(boards_data_dict[key].columns)
                    boards_data_dict[key] = utils.populate_table_with_random_values(boards_data_dict[key], 5000, 10000, ncolumns)
                key += 1
        return winning_boards


if __name__ == "__main__":
    # draws_data_file = "../data/day4_draws_example_data.csv"
    # boards_data_file = "../data/day4_boards_example_data.csv"
    #
    draws_data_file = "../data/day4_draws_data.csv"
    boards_data_file = "../data/day4_boards_data.csv"
    obj = Bingo(draws_data_file, boards_data_file)
    winners = obj.get_last_board_to_win()
    for winner in winners:
        print("---------------------------")
        print(f'Board number: {winner["winning_board"]}')
        print("Current board status")
        print("------------------------------")
        print(winner["current_board"])
        print(f'Current draw: {winner["last_draw"]}')
        print(f'Unmarked sum: {winner["unmarked_sum"]}')
        print(f'Score: {winner["score"]}')
        print("----------------------------")
        print("")
        print("")
        print("")
