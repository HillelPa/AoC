file_name = "input"

with open(file_name, 'r') as f:
    max = 0
    current = 0
    for line in f:
        print(line)
        print("max :", max)
        print("current :", current)
        if line == "\n":
            print("A")
            if current > max:
                max = current
            current = 0
        else:
            print("B")
            current += int(line)

print("max", max)