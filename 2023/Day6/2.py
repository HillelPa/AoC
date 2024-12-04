# I try brut force first

file_name = 'input'

with open(file_name, 'r') as f:
    lines = f.readlines()
    times_line = lines[0].strip().split(':')[1]
    time = int(times_line.replace(' ', ''))

    distance_line = lines[1].strip().split(':')[1]
    distance = int(distance_line.replace(' ', ''))


def algo1(time, distance):
    sum = 0
    for time_pressed in range(time):
        dist = (time_pressed)*(time - time_pressed)
        if dist > distance:
            sum += 1
    print(sum)
    return sum

# With some math
# f(time_pressed) = time_pressed*(time - time_pressed) - distance 
# if f > 0, we win
# let's find the roots
# We check edge cases where roots are int
# With the derivatif of f, we know that f(x)>0 for x in range(x1, x2)
# So we just have to do abs(x2-x1)

# Polynom : -1*time_pressed^2 + time_pressed*time - distance

import math

def quadratic_roots(a, b, c):
    
    delta = b**2 - 4*a*c  # Le discriminant est supposé positif
    sqrt_delta = math.sqrt(delta)
    
    root1 = (-b + sqrt_delta) / (2 * a)
    root2 = (-b - sqrt_delta) / (2 * a)
    
    return (root1, root2)

def algo2(time, distance):
    coefficients = [-1, time, -1*distance]
    roots = sorted(quadratic_roots(*coefficients))
    x1 = int(roots[0]) + 1
    x2 = int(roots[1])
    print(x2 - x1 + 1)
    return x2 - x1 + 1

# Let's time the 2 algos

import timeit

time_copy = time
distance_copy = distance

time1 = timeit.timeit(lambda: algo1(time, distance), number = 10)
time2 = timeit.timeit(lambda: algo2(time_copy, distance_copy), number = 10)

print("Time for algo1: ", time1)
print("Time for algo2: ", time2)

