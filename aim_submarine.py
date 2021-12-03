from submarine import SubmarineAim
from utils import rules_list

submarine_aim_inst = SubmarineAim()

for rule_list in rules_list:
    command = rule_list[0]
    steps = rule_list[1]
    submarine_aim_inst.move_submarine(command, steps)

print(f'final depth: {submarine_aim_inst.depth}\n'
      f'final range: {submarine_aim_inst.range}\n'
      f'final aim: {submarine_aim_inst.aim}\n'
      f'product: {submarine_aim_inst.depth * submarine_aim_inst.range}')
