file_name = "input.txt"

freq = 0
with open(file_name, 'r') as f:
    for line in f:
        freq += int(line)

print("Frequency:", freq)