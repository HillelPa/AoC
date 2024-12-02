file_name = "input"

seen = set()
output = 0
with open(file_name, 'r') as f:
    for line in f:
        target = 2020 - int(line)
        if target in seen:
            output = target * int(line)
            break
        seen.add(int(line))

print("output :", output)