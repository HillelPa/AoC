import re

file_name = 'input'

instructions = []
graph = {}

with open(file_name, 'r') as f:
    lines = f.readlines()
    instructions = lines[0]
    len_instructions = len(instructions)

    pattern = r'(\w+)\s*=\s*\((\w+),\s*(\w+)\)'
    for l in lines[2:]:
        key, left, right = re.match(pattern, l).groups()
        graph[key] = (left, right)


pos = 'AAA'
step = 0
nb_total_steps = 0
while pos != 'ZZZ':
    instruction = 0 if instructions[step] == 'L' else 1
    pos = graph[pos][instruction]
    nb_total_steps += 1
    step = (step + 1) % (len_instructions -1)

print("nb_total_steps :", nb_total_steps)

print("len of instructions :", len(instructions))