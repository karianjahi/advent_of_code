"""
Hydrothermal venture
"""
import numpy as np
import pandas as pd
import utils


def identify_frequency_of_overlaps(df, minimum=2):
    df2list = utils.table2list(df, True)
    return len([i for i in df2list if i >= minimum])


class HydrothermalVenture:
    """
    Hydrothermal vents on ocean floor
    """

    def __init__(self, data_file):
        self.data_file = data_file

    def read_data_file(self):
        with open(self.data_file, "r") as afile:
            text_data = afile.read()
        return text_data

    def convert_data2list(self):
        text = self.read_data_file()
        return text.split("\n")

    def determine_data_range(self):
        alist = self.convert_data2list()
        list_values = []
        for index, item in enumerate(alist):
            values = item.split("->")
            values = [[int(k) for k in j.split(",")] for j in [i.strip() for i in values]]
            for new_list in values:
                for new_value in new_list:
                    list_values.append(new_value)
        return max(list_values)

    def create_table_of_horizontal_and_vertical(self):
        max_value = self.determine_data_range()
        working_dataframe = pd.DataFrame(np.zeros((max_value + 1, max_value + 1)))
        working_dataframe = working_dataframe.astype(int)
        alist = self.convert_data2list()
        for index, item in enumerate(alist):
            values = item.split("->")
            values = [[int(k) for k in j.split(",")] for j in [i.strip() for i in values]]
            x1 = values[0][0]
            x2 = values[1][0]
            y1 = values[0][1]
            y2 = values[1][1]
            if y1 == y2:
                "we are dealing with a movement along the x-axis"
                y = y1
                if x1 <= x2:
                    start_x = x1
                    end_x = x2
                else:
                    start_x = x2
                    end_x = x1
                xs = [i for i in range(start_x, end_x + 1)]
                for ix in xs:
                    current_df_value = working_dataframe.loc[y, ix]
                    working_dataframe.loc[y, ix] = int(current_df_value + 1)

            if x1 == x2:
                "we are dealing with a movement along y-axis"
                x = x1
                if y1 <= y2:
                    start_y = y1
                    end_y = y2
                else:
                    start_y = y2
                    end_y = y1

                ys = [i for i in range(start_y, end_y + 1)]
                for iy in ys:
                    current_df_value = working_dataframe.loc[iy, x]
                    working_dataframe.loc[iy, x] = int(current_df_value + 1)
        working_dataframe.replace(0, ".", inplace=True)
        return working_dataframe

    def create_table_but_consider_diagonals_too(self):
        """
        Creating table by populating it with the mappings 
        given in the data e.g. An entry 
        like 1,1 -> 3,3 covers points 1,1, 2,2, and 3,3.
        An entry like 9,7 -> 7,9 covers points 9,7, 8,8, and 7,9.
        """
        max_value = self.determine_data_range()
        working_dataframe = pd.DataFrame(np.zeros((max_value + 1, max_value + 1)))
        working_dataframe = working_dataframe.astype(int)
        alist = self.convert_data2list()
        print("")
        print("original list:", alist)
        print("")
        print("")
        for index, item in enumerate(alist):
            print("")
            print(f'Dismantling and populating coordinates mapping for {item} at index {index}/{len(alist)}')
            print("")
            values = item.split("->")
            values = [[int(k) for k in j.split(",")] for j in [i.strip() for i in values]]
            x1 = values[0][0]
            x2 = values[1][0]
            y1 = values[0][1]
            y2 = values[1][1]
            if y1 == y2:
                if x1 < x2:
                    x_values = [i for i in range(x1, x2+1, 1)]
                    for x_value in x_values:
                        working_dataframe.loc[y1, x_value] += 1
                if x1 > x2:
                    x_values = [i for i in range(x1, x2-1, -1)]
                    for x_value in x_values:
                        working_dataframe.loc[y1, x_value] += 1
            if x1 == x2:
                if y1 < y2:
                    y_values = [i for i in range(y1, y2+1, 1)]
                    for y_value in y_values:
                        working_dataframe.loc[y_value, x1] += 1
                if y1 > y2:
                    y_values = [i for i in range(y1, y2-1, -1)]
                    for y_value in y_values:
                        working_dataframe.loc[y_value, x1] += 1
            if x1 < x2 and y1 < y2:
                x_values = [i for i in range(x1, x2+1, 1)]
                y_values = [i for i in range(y1, y2+1, 1)]
                for x_value, y_value in zip(x_values, y_values):
                    working_dataframe.loc[y_value, x_value] += 1
            if x1 > x2 and y1 > y2:
                x_values = [i for i in range(x1, x2-1, -1)]
                y_values = [i for i in range(y1, y2-1, -1)]
                for x_value, y_value in zip(x_values, y_values):
                    working_dataframe.loc[y_value, x_value] += 1
            if x1 > x2 and y1 < y2:
                x_values = [i for i in range(x1, x2-1, -1)]
                y_values = [i for i in range(y1, y2+1, 1)]
                for x_value, y_value in zip(x_values, y_values):
                    working_dataframe.loc[y_value, x_value] += 1
            if x1 < x2 and y1 > y2:
                x_values = [i for i in range(x1, x2+1, 1)]
                y_values = [i for i in range(y1, y2-1, -1)]
                for x_value, y_value in zip(x_values, y_values):
                    working_dataframe.loc[y_value, x_value] += 1
        working_dataframe.replace(0, ".", inplace=True)
        return working_dataframe


if __name__ == "__main__":
    data_file = "../data/data5_data.csv"
    #data_file = "../data/data5_example_data.csv"
    obj = HydrothermalVenture(data_file)
    mutilated_table = obj.create_table_but_consider_diagonals_too()
    print(identify_frequency_of_overlaps(mutilated_table))
