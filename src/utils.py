"""
Some utility functions
"""

import pandas as pd


def read_text_file(text_file):
    """
    Reading a text file
    :return: str
    """
    with open(text_file, "r") as afile:
        return afile.read()


def count_increasing_quantity(alist):
    """
    count the number times a quantity increases only
    :param alist: list of numbers or characters which
    are float-convertible
    :return: int
    """
    quantity = [float(value) for value in alist]
    count_increments = []
    for index, depth in enumerate(quantity):
        if index != 0:
            if depth > quantity[index - 1]:
                count_increments.append(True)
            else:
                count_increments.append(False)
        else:
            count_increments.append(False)
    # sl = pd.DataFrame({"dat": alist, "inc": count_increments})
    # print(sl)
    return sum(count_increments)


def use_tuples(func):
    """
    This is a decorator meant to change
    a function that takes 2 arguments/attributes
    so that it can take a list of tuples instead
    :param func: A function that takes 2 attributes
    :return:
    """

    def inner(list_of_tuples):
        for my_tuple in list_of_tuples:
            func(my_tuple[0], my_tuple[1])
        return inner


def get_least_common(alist, bit_to_prioritize):
    """
    Identify the least common bit
    :param alist:
    :param bit_to_prioritize: int. Which index to prioritize
    :return: int
    """
    df = pd.DataFrame(alist)
    value_counts = df.value_counts()
    last_row = value_counts.iloc[-1]
    least_common_df = value_counts[value_counts == last_row]
    if len(least_common_df) == 1:
        return least_common_df.index[0][0]  # multi-index
    else:
        if bit_to_prioritize in least_common_df:
            return bit_to_prioritize


def get_most_common(alist, bit_to_prioritize):
    """
    Identify the most common bit
    :param alist:
    :param bit_to_prioritize: int. Which index to prioritize
    :return: int
    """
    df = pd.DataFrame(alist)
    value_counts = df.value_counts()
    first_row = value_counts.iloc[0]
    most_common_df = value_counts[value_counts == first_row]
    if len(most_common_df) == 1:
        return most_common_df.index[0][0]  # multi-index
    else:
        if bit_to_prioritize in most_common_df:
            return bit_to_prioritize


def concatenate_list_into_string(alist):
    """
    Given a list like
    alist = ["ada", "subtract", "divide", "multiply"]
    the aim is to concatentate the to have a
    string of the form: "adasubstractdividemultiply"
    :param alist: list [list of items]
    :return: str
    """
    string = ""
    for item in alist:
        string += f'{item}'
    return string

def divide_list_into_equal_chunks(alist, chunks):
    """
    Divide a list into equal chunks
    :param alist: list
    :param chunks: int
    :return: list
    """
    return [alist[i:i + chunks] for i in range(0, len(alist), chunks)]

def is_all_equal(alist):
    """
    Checking if all members of a list are equal
    :return logical
    """
    first_member = alist[0]
    logic_list = []
    for item in alist:
        if item == first_member:
            logic_list.append(True)
        else:
            logic_list.append(False)
    return all(logic_list)

def table2list(table, consider_floats_only=True):
    """
    Given a pandas table, convert
    it to a list of values
    :param consider_floats_only: should we consider only floats?
    :return list
    """
    my_list = []
    for col in table.columns:
        column_values = table[col]
        for i in column_values:
            try:
                my_list.append(int(i))
            except:
                my_list.append(i)
    if consider_floats_only:
        return [i for i in my_list if isinstance(i, int)]
    return my_list

def list2string(alist, with_space):
    """
    given a list like [2, 5, 6] we
    want to concatenate the numbers into
    this string "2 5 6"
    :param alist: list [a list of  items]
    :param with_space: logical [should we use space or not?]
    :return str [a string]
    """
    string = ""
    for item in alist:
        if with_space:
            string = string + " " + str(item)
        else:
            string += str(item)
    return string

def get_fastest_winner(dict_list, sort_key):
    """
    get fastest winner
    :param dict_list: a list of dictionaries
    :param sort_key: key to sort dictionary
    :return list
    """
    df = pd.DataFrame(dict_list)
    df.sort_values(sort_key, inplace=True)
    return dict_list[df.index[0]]


def print_winning_board(board_number,
                        board_original,
                        board_after,
                        values,
                        unmarked_sum,
                        draw,
                        sub_row = None,
                        sub_column = None):
    """
    Printing out some information about the winning board
    :param board_number: board number
    :subrow: are we dealing with a row or column win
    : values: values of the winning row or column
    : marked sum: sum of remaining values after table has been filled by drawns
    : draw: the no drawn at this point
    : board_original: original board
    : board_after: mutilated board after play
    """
    score = unmarked_sum * draw
    if sub_row is not None:
        print("")
        print("")
        print("")
        print(f'WINNING BOARD NUMBER: {board_number}\n'
              f'WINNING ROW NUMBER: {sub_row} OR ROW INDEX: {int(sub_row.split("r")[1]) - 1}\n'
              f'WINNING ROW VALUES: {list2string(values, True)}\n'
              f'UNMARKED SUM: {unmarked_sum}\n'
              f'WINNING SCORE: {score}')
        print("---------------------------------")
        print("")
        print(f"Original board no. {board_number}")
        print(board_original)
        print("")
        print(f"Updated board no. {board_number}")
        print(board_after)
        print("")
    else:
        print(f'WINNING BOARD NUMBER: {board_number}\n'
              f'WINNING COL NUMBER: {sub_column} OR COL INDEX: {int(sub_column.split("r")[1]) - 1}\n'
              f'WINNING COL VALUES: {list2string(values, True)}\n'
              f'UNMARKED SUM: {unmarked_sum}\n'
              f'WINNING SCORE: {score}')
        print("")
        print("")
        print("")
        print("---------------------------------")
        print("")
        print(f"Original board no. {board_number}")
        print(board_original)
        print("")
        print(f"Updated board no. {board_number}")
        print(board_after)
        print("")



if __name__ == "__main__":
    #kalist = [1, 1, 1, 0, 0, 1, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0]
    # new_list = [None,  None,   0,   1,  None,  None,  None,  None,  None,  None,  None,  None]
    #print(concatenate_list_into_string(kalist))
    #print(divide_list_into_equal_chunks(kalist, 4))
    my_list = ["jal", "jal", "jal", "jal"]
    print(is_all_equal(my_list))

    #df = pd.read_csv("../data/table2list_tester_table.csv")
    #df.index = [f'r{i+1}' for i in range(len(df))]
    #print(table2list(df, True))
    # print(list2string([5, 8, 9], True))
    adict_list = [{'board_number': 1, 'iterations': 3383},
                  {'board_number': 2, 'iterations': 4735},
                  {'board_number': 3, 'iterations': 2781}]
    print(get_fastest_winner(adict_list, sort_key="iterations"))
    print(max(5, 8))
