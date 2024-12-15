file_name = 'input'

antennas = {}
with open(file_name, 'r') as f:
    for x, line in enumerate(f):
        line = line.strip()
        for y, point in enumerate(line):
            if point.isdigit() or point.isalpha():
                if point in antennas:
                    antennas[point].append((x, y))
                else:
                    antennas[point] = [(x, y)]

nb_lines = x+1
nb_columns = y+1

antinodes = set()

for freq, locations in antennas.items():
    for index_a1, loc_a1 in enumerate(locations):
        antinodes.add(loc_a1)
        for index_a2, loc_a2 in enumerate(locations[index_a1+1:]):
            # find the location of each antinodes
            # find the number of antinodes for each couple
            delta_x = loc_a2[0] - loc_a1[0]
            delta_y = loc_a2[1] - loc_a1[1]
            # before a1
            new_x = loc_a1[0] - delta_x
            new_y = loc_a1[1] - delta_y
            while new_x in range(0, nb_lines) and new_y in range(0, nb_columns):
                antinodes.add((new_x, new_y))
                new_x -= delta_x
                new_y -= delta_y
            
            # after a2
            new_x = loc_a2[0] + delta_x
            new_y = loc_a2[1] + delta_y
            while new_x in range(0, nb_lines) and new_y in range(0, nb_columns):
                antinodes.add((new_x, new_y))
                new_x += delta_x
                new_y += delta_y
    
print(len(antinodes))


                