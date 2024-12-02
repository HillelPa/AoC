file_name = "input"

nb_increases = 0
with open(file_name, 'r') as f:
    prev = 99999
    for line in f:
        if int(line) > prev:
            nb_increases += 1
        prev = int(line)

print("nb_increases", nb_increases)
