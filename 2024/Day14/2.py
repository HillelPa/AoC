import re

test = False

file_name = 'input'
if test: file_name = 'i2'


def print_image(final_picture, tall, wide):
    for i in range(tall):
        for j in range(wide):
            if (j, i) in final_picture:
                print('@', end='')
            else:
                print(' ', end='')
        print()


wide = 101
tall = 103
nb_robots = 500
if test: wide = 11
if test: tall = 7
if test: nb_robots = 12

robots = []

with open(file_name, 'r') as f:
    for line in f:
        match = re.search(r"p=(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)", line)
        px, py, vx, vy = map(int, match.groups())
        robots.append([px, py, vx, vy])

i = 1
while True:
    final_picture = set()
    next_robots = []
    for robot in robots:
        px, py, vx, vy = robot[0], robot[1], robot[2], robot[3]
        px = (px + vx) % wide
        py = (py + vy) % tall
        final_picture.add((px, py))
        next_robots.append([px, py, vx, vy])
    robots = next_robots
    if len(final_picture) == nb_robots:
        print_image(final_picture, tall, wide)
        break
    i += 1


