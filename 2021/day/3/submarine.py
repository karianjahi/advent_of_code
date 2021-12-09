import pandas as pd


class Submarine:
    def __init__(self):
        self.depth = 0
        self.range = 0

    def move_submarine_vertically(self, command, steps):
        if command == "down":
            self.depth += steps
        if command == "up":
            self.depth -= steps

    def move_submarine_horizontally(self, steps):
        self.range += steps


class SubmarineAim:
    def __init__(self):
        self.aim = 0
        self.depth = 0
        self.range = 0
        self.gamma_rate = None
        self.epsilon_rate = None
        self.gamma_decimal = None
        self.epsilon_decimal = None
        self.power_consumption = None

    def move_submarine(self, command, steps):
        if command == "down":
            self.aim += steps
        if command == "up":
            self.aim -= steps
        if command == "forward":
            self.range += steps
            self.depth += self.aim * steps

    @staticmethod
    def get_diagnostic_code(bits, gamma=True):
        length_of_each_binary = len(bits[0])
        diagnostic_code = ""
        for bit_position in range(length_of_each_binary):
            nth_digits = []
            for bit in bits:
                nth_digits.append(bit[bit_position])
            if gamma:
                diagnostic_code += max(set(nth_digits), key=nth_digits.count)
            else:
                diagnostic_code += min(set(nth_digits), key=nth_digits.count)
        return diagnostic_code

    def get_gamma_decimal(self, bits):
        self.gamma_rate = self.get_diagnostic_code(bits, True)
        self.gamma_decimal = int(self.gamma_rate, 2)

    def get_epsilon_decimal(self, bits):
        self.epsilon_rate = self.get_diagnostic_code(bits, False)
        self.epsilon_decimal = int(self.epsilon_rate, 2)

    def calculate_power_consumption(self, bits):
        self.power_consumption = self.gamma_decimal * self.epsilon_decimal


if __name__ == "__main__":
    submarine_instance = SubmarineAim()
    submarine_instance.move_submarine("forward", 5)
    submarine_instance.move_submarine("down", 5)
    submarine_instance.move_submarine("forward", 8)
    submarine_instance.move_submarine("up", 3)
    submarine_instance.move_submarine("down", 8)
    submarine_instance.move_submarine("forward", 2)
    # print("depth: ", submarine_instance.depth)
    # print("range: ", submarine_instance.range)
    # print("aim: ", submarine_instance.aim)
    # print("product: ", submarine_instance.depth * submarine_instance.range)
    # print("")
    # print("")

    from utils import example_bits

    list_of_bits = example_bits
    submarine_instance.get_gamma_decimal(list_of_bits)
    submarine_instance.get_epsilon_decimal(list_of_bits)
    submarine_instance.calculate_power_consumption(list_of_bits)
    print(submarine_instance.gamma_decimal)
    print(submarine_instance.epsilon_decimal)
    print(f'Power consumption: {submarine_instance.power_consumption}')


