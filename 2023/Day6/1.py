file_name = 'input'

with open(file_name, 'r') as f:
    lines = f.readlines()
    time_line = lines[0]
    time_line = time_line.strip()
    times = time_line.split(':')[1].split(' ')
    times = [int(time) for time in times if time.isnumeric()]
    
    distance = lines[1]
    distance = distance.strip()
    distances = distance.split(':')[1].split(' ')
    distances = [int(distance) for distance in distances if distance.isnumeric()]

total = 1
for time, record_dist in zip(times, distances):
    local_sum = 0
    for time_pressed in range(time):
        dist = (time_pressed)*(time - time_pressed)
        if dist > record_dist:
            local_sum += 1
    total *= local_sum

print('Total:', total)