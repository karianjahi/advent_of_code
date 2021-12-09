def read_file(filename):
    with open(filename, "r") as afile:
        return afile.read()


rules = read_file("data/commands.csv").split("\n")
example_bits = read_file("data/example_bits.txt").split("\n")
diagnostic_bits = read_file("data/diagnostic_bits.txt").split("\n")
# flatten commands

rules_list = []
for rule in rules:
    rule_splits = rule.split()
    rule_splits[1] = float(rule_splits[1])
    rules_list.append(rule_splits)

if __name__ == "__main__":
    print(rules_list)
    print(diagnostic_bits)
