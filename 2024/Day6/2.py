# I have no idea so i m going to try brute force

file_name = 'input'
#file_name = 'i2'

input = []
with open(file_name, 'r') as f:
    for line in f:
        line = line.strip()
        input.append([l for l in line])


def print_input(input):
    for row in input:
        print(''.join(row))
    print()

def find_init_pos(input):
    for i in range(len(input)):
        for j in range(len(input[i])):
            if input[i][j] == '^':
                return i, j
            
movements = [(-1, 0), (0, 1), (1, 0), (0, -1)]

pos_x, pos_y = find_init_pos(input)

def loop(input):
    move = 0
    pos_x, pos_y = find_init_pos(input)
    #print("we start at", pos_x, pos_y)
    visited_obstacles = set()
    while True:

        if move == 0 and pos_x == 0:
            return 0
        elif move == 1 and pos_y == len(input[0]) - 1:
            return 0
        elif move == 2 and pos_x == len(input) - 1:
            return 0
        elif move == 3 and pos_y == 0:
            return 0
        
        try:
            front = input[pos_x + movements[move][0]][pos_y + movements[move][1]]
            #print("front: ", front)
            if front == '#':

                state = (pos_x, pos_y, move)
                #print("state: ", state)
                #print("visited: ", visited_obstacles)
                if state in visited_obstacles:
                    #print("loop")
                    return 1
                visited_obstacles.add(state)

                # Tourner à droite
                move = (move + 1) % 4
            else:
                # Avancer
                pos_x += movements[move][0]
                pos_y += movements[move][1]
                #print("we moved to", pos_x, pos_y)

        except IndexError:
            # Sortie de la grille
            #print("LEFT")
            return 0


possibilities = 0

for i in range(len(input)):
    for j in range(len(input[i])):
        if input[i][j] != '.':
            continue
        modified_input = [row[:] for row in input]
        modified_input[i][j] = '#'
        #print_input(modified_input)
        #print("--")
        #print_input(input)

        if loop(modified_input):
            print("(",i,",",j,")")
            possibilities += 1
        
        # possibilities += loop(modified_input)

print("possibilities", possibilities)




