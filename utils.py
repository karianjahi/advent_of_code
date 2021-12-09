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
