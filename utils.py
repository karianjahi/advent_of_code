"""
Some utility functions
"""


def read_text_file(self):
    """
    Reading a text file
    :return: str
    """
    with open(self.textfile, "r") as afile:
        return afile.read()
