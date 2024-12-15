file_name = "input"
#file_name = 'i2'

with open(file_name, 'r') as f:
    input = f.readlines()

# Find start

for i, line in enumerate(input):
    line = line.strip()
    for j, char in enumerate(line):
        if char == 'S':
            start = (i, j)

print("Start", start)

# change hash table:
movements = {
    '|_from_up': (1, 0),
    '|_from_down': (-1, 0),
    '-_from_right': (0, -1),
    '-_from_left': (0, 1),
    'L_from_right': (-1, 0),
    'L_from_up': (0, 1),
    'J_from_up': (0, -1),
    'J_from_left': (-1, 0),
    '7_from_left': (1, 0),
    '7_from_down': (0, -1),
    'F_from_right': (1, 0),
    'F_from_down': (0, 1),
}
# Make the loop 
loop = []

pos_x, pos_y = start[0], start[1]

loop.append((pos_x, pos_y))

# _ 1 _
# 2 S 4
# _ 3 _

# first movement :

# check pipe 1
if pos_x - 1 > 0 and input[pos_x - 1][pos_y] in '|7F':
    pipe = input[pos_x - 1][pos_y]
    fr = '_from_down'
    pos_x = pos_x - 1
# Check pipe 2
elif pos_y - 1 > 0 and input[pos_x][pos_y - 1] in '-LF':
    pipe = input[pos_x][pos_y - 1]
    fr = '_from_left'
    pos_y = pos_y - 1
# Check pipe 3
elif pos_x + 1 < len(input) and input[pos_x + 1][pos_y] in '|LJ':
    pipe = input[pos_x + 1][pos_y]
    fr = '_from_up'
    pos_x = pos_x + 1
# Check pipe 4
elif pos_y + 1 < len(input[0]) and input[pos_x][pos_y + 1] in '-7J':
    pipe = input[pos_x][pos_y + 1]
    fr = '_from_right'
    pos_y = pos_y + 1

pipe = pipe + fr

print("new pose :", pos_x, pos_y)
loop.append((pos_x, pos_y))
print("Pipe:", pipe)

while (pos_x, pos_y) != start:
    new_pos_x = pos_x + movements[pipe][0]
    new_pos_y = pos_y + movements[pipe][1]

    if new_pos_x > pos_x:
        fr = '_from_up'
    elif new_pos_x < pos_x:
        fr = '_from_down'
    elif new_pos_y > pos_y:
        fr = '_from_left'
    elif new_pos_y < pos_y:
        fr = '_from_right'

    pos_x = new_pos_x
    pos_y = new_pos_y

    print("pos :", pos_x, pos_y)

    pipe = input[pos_x][pos_y]

    pipe = pipe + fr
    
    print("pipe :", pipe)
    loop.append((pos_x, pos_y))

loop.pop()
print("Loop size :", len(loop))
print("loop :", loop)

print("farest :", len(loop)//2)




