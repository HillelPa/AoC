instructions = "R1, L3, R5, R5, R5, L4, R5, R1, R2, L1, L1, R5, R1, L3, L5, L2, R4, L1, R4, R5, L3, R5, L1, R3, L5, R1, L2, R1, L5, L1, R1, R4, R1, L1, L3, R3, R5, L3, R4, L4, R5, L5, L1, L2, R4, R3, R3, L185, R3, R4, L5, L4, R48, R1, R2, L1, R1, L4, L4, R77, R5, L2, R192, R2, R5, L4, L5, L3, R2, L4, R1, L5, R5, R4, R1, R2, L3, R4, R4, L2, L4, L3, R5, R4, L2, L1, L3, R1, R5, R5, R2, L5, L2, L3, L4, R2, R1, L4, L1, R1, R5, R3, R3, R4, L1, L4, R1, L2, R3, L3, L2, L1, L2, L2, L1, L2, R3, R1, L4, R1, L1, L4, R1, L2, L5, R3, L5, L2, L2, L3, R1, L4, R1, R1, R2, L1, L4, L4, R2, R2, R2, R2, R5, R1, L1, L4, L5, R2, R4, L3, L5, R2, R3, L4, L1, R2, R3, R5, L2, L3, R3, R1, R3"
directions = instructions.split(", ")

pos = (0,0)
facing = "N"

for d in directions:
    direction, value = d[0], int(d[1:])
    if facing == "N":
        if direction == "R":
            facing = "E"
            pos = (pos[0], pos[1] + value)
        if direction == "L":
            facing = "W"
            pos = (pos[0], pos[1] - value)
        continue
    
    if facing == "E":
        if direction == "R":
            facing = "S"
            pos = (pos[0] + value, pos[1])
        if direction == "L":
            facing = "N"
            pos = (pos[0] - value, pos[1])
        continue
    
    if facing == "S":
        if direction == "R":
            facing = "W"
            pos = (pos[0], pos[1] - value)
        if direction == "L":
            facing = "E"
            pos = (pos[0], pos[1] + value)
        continue
        
    if facing == "W":
        if direction == "R":
            facing = "N"
            pos = (pos[0] - value, pos[1])
        if direction == "L":
            facing = "S"
            pos = (pos[0] + value, pos[1])
        continue
    

distance = abs(pos[0]) + abs(pos[1])

print("distance_finale", distance)

