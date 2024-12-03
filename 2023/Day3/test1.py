file_name = "i2"
#file_name = "input"

with open(file_name, 'r') as f:
    input = f.readlines()


symbols = set()
nums = {}

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
            nums[int(num)] = coord
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
            print("C'est bon : ", num, "@ :", coord)
            return 1
    return 0

sum = 0
for num, coords in nums.items():
    sum += check_num(num, coords)*num

print("sum", sum)

print("len(symbols)", len(symbols))
print("symbols", symbols)

print("len part coord", len(part_coord))
print("part_coord", part_coord)

print("len nums", len(nums))
print("nums", nums)

def visualize_part_coord(part_coord):
    for i in range(8):
        for j in range(25):
            if (i, j) in part_coord:
                print("*", end="")
            else:
                print(input[i][j], end="")
        print()

#visualize_part_coord(part_coord)