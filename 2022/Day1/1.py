file_name = "input"

with open(file_name, 'r') as f:
    max = 0
    current = 0
    for line in f:
        if line == "\n":
            if current > max:
                max = current
            current = 0
        else:
            current += int(line)

print("max", max)