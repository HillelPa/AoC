file_name = 'input'
#file_name = 'i2'

SCORE = 0
VISITED = set()
VISITED_TAILS = set()

data = []
trail_heads = set()
trail_tails = set()
x, y = 0,0
with open(file_name, 'r') as f:
    for l in f:
        data_local = []
        y = 0
        line = l.strip()
        for c in line:
            c = int(c)
            data_local.append(c)

            if c == 0:
                trail_heads.add((x,y))
            elif c == 9:
                trail_tails.add((x,y))
            y += 1
        data.append(data_local)
        x += 1

#print(data)
#print('-')
#print(trail_heads)
#print("-")
#print(trail_tails)

def check_neighbours(data, coords):
    value = data[coords[0]][coords[1]]
    VISITED.add(coords)
    next_moves = []

    # UP : 
    if coords[0]-1 in range(0, len(data)):
        if data[coords[0]-1][coords[1]] == value+1:
            if (coords[0]-1, coords[1]) not in VISITED:
                next_moves.append((coords[0]-1, coords[1]))
    
    # LEFT : 
    if coords[1]-1 in range(0, len(data[0])):
        if data[coords[0]][coords[1]-1] == value+1:
            if (coords[0], coords[1]-1) not in VISITED:
                next_moves.append((coords[0], coords[1]-1))
    
    # RIGHT : 
    if coords[1]+1 in range(0, len(data[0])):
        if data[coords[0]][coords[1]+1] == value+1:
            if (coords[0], coords[1]+1) not in VISITED:
                next_moves.append((coords[0], coords[1]+1))
    
    # DOWN : 
    if coords[0]+1 in range(0, len(data)):
        if data[coords[0]+1][coords[1]] == value+1:
            if (coords[0]+1, coords[1]) not in VISITED:
                next_moves.append((coords[0]+1, coords[1]))
        
    return next_moves


def recursive_search(data, coords):
    global SCORE
    local_sum = 0
    value = data[coords[0]][coords[1]]
    #print("We recursive check", coords, " value :", value)
    if value == 9:
        #print('tail')
        if coords not in VISITED_TAILS:
            SCORE += 1
            VISITED_TAILS.add(coords)
        return 0
    nexts = check_neighbours(data, coords)
    #print(coords, "NEXTS ARE ", nexts)
    for next in nexts:
        recursive_search(data, next)
    return local_sum



for head in trail_heads:
    VISITED = set()
    VISITED_TAILS = set()
    #print("-- head in :", head)
    recursive_search(data, head)

print("score :", SCORE)