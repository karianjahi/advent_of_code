"""
Some utility functions
"""


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