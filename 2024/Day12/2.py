file_name = 'input'
#file_name = 'i2'

with open(file_name, 'r') as f:
    data = {}
    for i, l in enumerate(f):
        line = l.strip()
        for j, seed in enumerate(line):
            if seed not in data.keys():
                data[seed] = set()
            data[seed].add((i, j))

##print("data", data)

# Split seed_sets into regions
from collections import deque
def find_regions(seed_set):
    visited = set()
    regions = []

    directions = [
        (-1, 0), (1, 0), (0, -1), (0, 1)  # Cardinal only
    ]

    def explore_region(start):
        queue = deque([start])
        region = set()
        while queue:
            point = queue.popleft()
            if point in visited:
                continue
            visited.add(point)
            region.add(point)
            for dx, dy in directions:
                neighbor = (point[0] + dx, point[1] + dy)
                if neighbor in seed_set and neighbor not in visited:
                    queue.append(neighbor)
        return region

    for point in seed_set:
        if point not in visited:
            new_region = explore_region(point)
            regions.append(new_region)
    
    return regions

def get_per_column(sorted_region):
    points_per_column = []
    cur_c = sorted_region[0][1]
    local = []
    for p in sorted_region:
        if p[1]!= cur_c:
            points_per_column.append(local)
            cur_c = p[1]
            local.append(p)
        else:
            local.append(p)


def rm_continuous(sides, type):

    #print("Type :", type)
    #print("Sides :", sides)
    nb_sides = 1
    for side1, side2 in zip(sides, sides[1:]):
        #print("Looking side1, side2 :", side1, side2)
        if type == 'UP':
            if side1[0] != side2[0] or side1[1] != side2[1]-1:
                #print("dis")
                nb_sides += 1
        
        if type == 'RIGHT':
            if side1[1] != side2[1] or side1[0] != side2[0] -1:
                #print("dis")
                nb_sides += 1
        
        if type == 'DOWN':
            if side1[0] != side2[0] or side1[1] != side2[1] + 1 :
                #print("dis")
                nb_sides += 1
        
        if type == 'LEFT':
            if side1[1]!= side2[1] or side1[0] != side2[0] +1:
                #print("dis")
                nb_sides += 1

    #print("FOR", type, " nb_sides", nb_sides)
    return nb_sides



def get_every_sides(region):

    # 4 types of sides 
    # UP RIGHT DOWN LEFT
    up_sides = set()
    right_sides = set()
    down_sides = set()
    left_sides = set()

    sides = set()
    
    for point in region:
        #print("Point : ", point)
        # Check if it's an UP side
        if (point[0]-1, point[1]) not in region:
            #print("up")
            up_sides.add(point)

        # Check if it's a RIGHT side
        if (point[0], point[1]+1) not in region:
            #print("right")
            right_sides.add(point)

        # Check if it's a DOWN side
        if (point[0]+1, point[1]) not in region:
            #print("down")
            down_sides.add(point)

        # Check if it's a LEFT side
        if (point[0], point[1]-1) not in region:
            #print("left")
            left_sides.add(point)
    
    up_sides_sorted = sorted(up_sides, key=lambda x: (x[0], x[1]))
    c_up_s = rm_continuous(up_sides_sorted, 'UP') 

    right_sides_sorted = sorted(right_sides, key=lambda x: (x[1], x[0]))
    c_right_s = rm_continuous(right_sides_sorted, 'RIGHT')

    down_sides_sorted = sorted(down_sides, key=lambda x: (x[0], x[1]), reverse=True)
    c_down_s = rm_continuous(down_sides_sorted, 'DOWN')

    left_sides_sorted = sorted(left_sides, key=lambda x: (x[1], x[0]), reverse=True)
    c_left_s = rm_continuous(left_sides_sorted, 'LEFT')
    

    return c_up_s + c_right_s + c_down_s + c_left_s


#region = {(7, 4), (6, 2), (7, 1), (9, 3), (8, 1), (6, 4), (7, 3), (8, 3), (7, 2), (8, 2), (7, 5), (6, 3), (8, 5), (5, 2)}
##print("sides :", get_every_sides(region))

price = 0
#print("--------------------------------------------------------")
for seed_type, seed_sets in data.items():
    #print("type :", seed_type)
    #print("seed_sets :", seed_sets)
    regions = find_regions(seed_sets)
    #print("regions :", regions)
    #print("nb_regions :", len(regions))

    # Now for each region let's calculate the area and the sides
    for nb_r, region in enumerate(regions):
        #print("region :", nb_r)
        area = len(region)
        #print("area :", area)
        sides = get_every_sides(region)
        #print("sides :", sides)
        price += area * sides
    #print("----------------------------------------------------------------")

print("price :", price)

