# get commands
with open("commands.csv", "r") as file:
    rules = file.read()

# flatten commands
rules = rules.split("\n")
rules_list = []
for rule in rules:
    rule_splits = rule.split()
    rule_splits[1] = float(rule_splits[1])
    rules_list.append(rule_splits)

if __name__ == "__main__":
    print(rules_list)

