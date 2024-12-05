import re

file_name = 'input'
#file_name = 'i2'

instructions = []
graph = {}
starts = []
ends = []

with open(file_name, 'r') as f:
    lines = f.readlines()
    instructions = lines[0]
    len_instructions = len(instructions)

    pattern = r'(\w+)\s*=\s*\((\w+),\s*(\w+)\)'
    for l in lines[2:]:
        key, left, right = re.match(pattern, l).groups()
        graph[key] = (left, right)
        if key[-1] == 'A':
            starts.append(key)
        if key[-1] == 'Z':
            ends.append(key)


# Brute force, i think it's too long
def bf():
    step = 0
    nb_total_steps = 0
    starts
    ends_reached = set()

    while len(ends_reached) != len(ends):
        # 1 step : 
        ends_reached = set()
        instruction = 0 if instructions[step] == 'L' else 1
        for i in range(len(starts)):
            starts[i] = graph[starts[i]][instruction]
            if starts[i][-1] == 'Z':
                ends_reached.add(starts[i])

        nb_total_steps += 1
        step = (step + 1) % (len_instructions -1)

    print("nb_total_steps :", nb_total_steps)



# Now let's check if there's a more efficient way to do this
# The intuition is that every start is connected to a particular end
# Let's check that with the code of 1.py
# So, we do have loops
# Let's find the least common multiple of thoses loops

loops = []
for start in starts:
    pos = start
    step = 0
    nb_total_steps = 0
    step_loop = 0
    i = 0
    while pos[-1] != 'Z':
        instruction = 0 if instructions[step] == 'L' else 1
        pos = graph[pos][instruction]
        nb_total_steps += 1
        step_loop += 1
        step = (step + 1) % (len_instructions -1)
    loops.append(nb_total_steps)

from functools import reduce
import math

def lcm_multiple(numbers):
    return reduce(lambda x, y: abs(x * y) // math.gcd(x, y), numbers)

print(lcm_multiple(loops))
