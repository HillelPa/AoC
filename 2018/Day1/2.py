file_name = "input.txt"

freq_seen = set()
freq = 0
run = True
while run:
    with open(file_name, 'r') as f:
        for line in f:
            freq += int(line)
            if freq in freq_seen:
                run = False
                break
            freq_seen.add(freq)

print("1st freq reached twice :", freq)
