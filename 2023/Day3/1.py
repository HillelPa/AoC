file_name = "input.txt"

with open(file_name, 'r') as f:
    input = f.readlines()


symbols = set()
nums = []
coords_num = []

for index_line, line in enumerate(input):
    line = line.replace("\n", "")
    i = 0
    while i < len(line):
        if line[i] != "." and not line[i].isnumeric():
            symbols.add((index_line, i))
            i += 1
            continue
        if line[i].isnumeric():
            # We have a digit, let's get the full number
            num = line[i]
            j = i + 1
            coord = [(index_line, i)]
            while j < len(line) and line[j].isnumeric():
                coord.append((index_line, j))
                num += line[j]
                j += 1
            i = j
            nums.append(int(num))
            coords_num.append(coord)
            continue
        i += 1

part_coord = set()
for symbol in symbols:
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i != 0 or j != 0:
                if symbol[0]+i >= 0 and symbol[1]+j >= 0 and symbol[0]+i < len(input) and symbol[1]+j < len(input[0]):
                    part_coord.add((symbol[0]+i, symbol[1]+j))


def check_num(num, coords):
    for coord in coords:
        if coord in part_coord:  
            return 1
    return 0

sum = 0

for i in range(len(nums)):
    sum += check_num(nums[i], coords_num[i]) * nums[i]

print("sum", sum)
