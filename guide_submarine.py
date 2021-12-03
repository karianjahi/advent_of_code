from submarine import Submarine
from utils import rules_list

submarine_inst = Submarine()

# guide submarine
for rule_list in rules_list:
    command = rule_list[0]
    steps = rule_list[1]
    if command == "forward":
        submarine_inst.move_submarine_horizontally(steps)
    if command == "up" or command == "down":
        submarine_inst.move_submarine_vertically(command, steps)

horizontal_position = submarine_inst.range
vertical_position = submarine_inst.depth

# --------------------- Results --------------------------------------
print("=======================================================================")
print(f'The final horizontal position of submarine: {horizontal_position}. \n'
      f'The final vertical position of submarine: {vertical_position}. \n'
      f'Product: {horizontal_position * vertical_position}')
print("=======================================================================")

print(int("0100111011", 2))
