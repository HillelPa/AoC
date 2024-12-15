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

#print("data", data)

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


def get_perimeter(region):
    perimeter = 0
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    for x, y in region:
        for dx, dy in directions:
            neighbor = (x + dx, y + dy)
            if neighbor not in region:
                perimeter += 1
    
    return perimeter


price = 0
#print("--------------------------------------------------------")
for seed_type, seed_sets in data.items():
    #print("type :", seed_type)
    #print("seed_sets :", seed_sets)
    regions = find_regions(seed_sets)
    #print("regions :", regions)
    #print("nb_regions :", len(regions))

    # Now for each region let's calculate the area and the perimeter
    for nb_r, region in enumerate(regions):
        #print("region :", nb_r)
        area = len(region)
        #print("area :", area)
        perimeter = get_perimeter(region)
        #print("perimeter :", perimeter)
        price += area * perimeter
    #print("----------------------------------------------------------------")

print("price :", price)