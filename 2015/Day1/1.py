floor = 0

file_name = "input.txt"

with open(file_name, 'r') as f:
    for c in f.read():
        if c == "(":
            floor += 1
        else:
            floor -= 1

print("floor", floor)