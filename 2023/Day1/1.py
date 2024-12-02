file_name = "input"

sum = 0
with open(file_name, 'r') as f:
    for line in f:
        only_num = "".join([char for char in line if char.isdigit()])
        sum += int(only_num[0] + only_num[-1])
print("sum :", sum)

