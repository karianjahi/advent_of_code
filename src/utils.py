"""
Some utility functions
"""

import pandas as pd
import numpy as np


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


def populate_table_with_random_values(table, start, end, ncol=5):
    all_values = table2list(table, False)
    random_values = np.random.randint(start, end, len(all_values))
    return pd.DataFrame(divide_list_into_equal_chunks(random_values, ncol))


if __name__ == "__main__":
    table = pd.read_csv("../data/table2list_tester_table.csv")
    # print(populate_table_with_random_values(table, 5000, 10000, ncol=5))
    import sys
    #ls = [None] * 10000000000
    #print(f'{sys.getsizeof(ls)/1000000000} gigs')
    #print(f'{np.format_float_positional(sys.getsizeof(ls) / 1000000000, trim="-")} gigs')
    gh = np.array([3.5, 1.5, 9.1])
    for g in gh:
        print(g)