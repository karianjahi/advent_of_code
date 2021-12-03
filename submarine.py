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

    def move_submarine(self, command, steps):
        if command == "down":
            self.aim += steps
        if command == "up":
            self.aim -= steps
        if command == "forward":
            self.range += steps
            self.depth += self.aim * steps

if __name__ == "__main__":
    submarine_instance = SubmarineAim()
    submarine_instance.move_submarine("forward", 5)
    submarine_instance.move_submarine("down", 5)
    submarine_instance.move_submarine("forward", 8)
    submarine_instance.move_submarine("up", 3)
    submarine_instance.move_submarine("down", 8)
    submarine_instance.move_submarine("forward", 2)
    print("depth: ", submarine_instance.depth)
    print("range: ", submarine_instance.range)
    print("aim: ", submarine_instance.aim)
    print("product: ", submarine_instance.depth * submarine_instance.range)


