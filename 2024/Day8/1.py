file_name = 'input'
#file_name = 'i2'

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
    #print('freq', freq)
    for index_a1, loc_a1 in enumerate(locations):
        for index_a2, loc_a2 in enumerate(locations[index_a1+1:]):
            #print(index_a1, loc_a1, index_a2, loc_a2)
            # find the location of each antinodes
            # for antinode 1
            delta_x = loc_a2[0] - loc_a1[0]
            delta_y = loc_a2[1] - loc_a1[1]
            if loc_a1[0] - delta_x in range(0, nb_lines) and loc_a1[1] - delta_y in range(0, nb_columns):
                #print("new end_point in ", loc_a1[0] - delta_x, " and ", loc_a1[1] - delta_y)
                antinodes.add((loc_a1[0] - delta_x, loc_a1[1] - delta_y))
            # for antinode 2
            if loc_a2[0] + delta_x in range(0, nb_lines) and loc_a2[1] + delta_y in range(0, nb_columns):
                #print("new end_point in ", loc_a2[0] + delta_x, " and ", loc_a2[1] + delta_y)
                antinodes.add((loc_a2[0] + delta_x, loc_a2[1] + delta_y))

print(len(antinodes))
                