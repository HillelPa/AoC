file_name = "input.txt"

floor = 0
pos = 1

with open(file_name, 'r') as f:
    for c in f.read():
        if c == "(":
            floor += 1
        elif c == ")":
            floor -= 1
        if floor == -1:
            break
        pos += 1

print("position", pos)