file_name = "input.txt"

fuel = 0
with open(file_name, 'r') as f:
    for line in f:
        fuel += int(line)//3 - 2

print("fuel needed :", fuel)