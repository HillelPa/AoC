import re

test = True

file_name = 'input'
if test: file_name = 'i2'

wide = 101
tall = 103
if test: wide = 11
if test: tall = 7

# q1 | q2
# -------
# q3 | q4

#q1, q2, q3, q4 = [], [], [], []
q1, q2, q3, q4 = 0, 0, 0, 0

with open(file_name, 'r') as f:
    for line in f:
        match = re.search(r"p=(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)", line)
        px, py, vx, vy = map(int, match.groups())
        #print("px, py, vx, vy", px, py, vx, vy)
        px100 = (px + 100*vx) % wide
        py100 = (py + 100*vy) % tall

        if px100 < wide // 2:
            if py100 < tall // 2:
                q1 += 1
                #q1.append((px100, py100))
            else:
                if py100!= tall // 2:
                    q3 += 1
                #q3.append((px100, py100))
        else:
            if px100 != wide // 2:
                if py100 < tall // 2:
                    q2 += 1
                    #q2.append((px100, py100))
                else:
                    if py100 != tall // 2:
                        q4 += 1
                        #q4.append((px100, py100))

print("q1", q1)
print("q2", q2)
print("q3", q3)
print("q4", q4)

scaling_factor = q1 * q2 * q3 * q4
print("scaling_factor", scaling_factor)



