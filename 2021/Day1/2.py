file_name = "input"

with open(file_name, 'r') as f:
    lines = f.readlines()

    depth_n2 = int(lines[0])
    depth_n1 = int(lines[1])

    sum = 99999

    nb_increases = 0

    for line in lines[2:]:
        depth_n = int(line)
        if (depth_n2 + depth_n1 + depth_n) > sum:
            nb_increases += 1
        sum = (depth_n2 + depth_n1 + depth_n)
        depth_n2 = depth_n1
        depth_n1 = depth_n
    
print("nb_increases", nb_increases)

