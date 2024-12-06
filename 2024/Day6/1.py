file_name = 'input'
#file_name = 'i2'

input = []
with open(file_name, 'r') as f:
    for line in f:
        line = line.strip()
        input.append([l for l in line])


def find_init_pos():
    for i in range(len(input)):
        for j in range(len(input[i])):
            if input[i][j] == '^':
                return i, j

pos_x, pos_y = find_init_pos()

movements = [(-1, 0), (0, 1), (1, 0), (0, -1)]

move = 0

seen = set()

local_sum = 0
while pos_x in range(0, len(input)-1) and pos_y in range(0, len(input[0])-1):
    seen.add((pos_x, pos_y))
    front = input[pos_x + movements[move][0]][pos_y + movements[move][1]]
    if front == '#':
        print("obstacle")
        print("we moved for ", local_sum)
        local_sum = 0
        move = (move + 1) % 4
    
    local_sum +=1
    pos_x += movements[move][0]
    pos_y += movements[move][1]

print("sum :", len(seen)+1)