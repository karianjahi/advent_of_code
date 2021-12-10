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


if __name__ == "__main__":
    kalist = [1, 1, 1, 0, 0, 1, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0]
    # new_list = [None,  None,   0,   1,  None,  None,  None,  None,  None,  None,  None,  None]
    print(concatenate_list_into_string(kalist))
