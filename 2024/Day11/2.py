import math
import functools

file_name = 'input'
#file_name = 'i2'

with open(file_name, 'r') as f:
    line = f.readline()
    ss = line.split(" ")

stones = {}

def add_to_dict(dict, stone):
    if int(stone) in dict.keys():
        dict[int(stone)] += 1
    else:
        dict[int(stone)] = 1

for s in ss:
    add_to_dict(stones, s)

def splitting_num(length, num):
    midpoint = length // 2
    tens = 10 ** midpoint
    left_stones = num // tens
    right_stones = num % tens
    return (left_stones, right_stones)

@functools.lru_cache(maxsize=None)
def single_blink_stone(value):
    # Rule 1:
    if value == 0:
        return (1, None)
    # Rule 2:
    length = math.floor(math.log10(value)) + 1
    if length%2 == 0:
        # Split the stone into two halves and removing inutiles 0
         return splitting_num(length, value)
    # Rule 3:
    return (2024*value, None)

@functools.lru_cache(maxsize=None)
def count_stone_blinks(stone, depth):

    left_stone, right_stone = single_blink_stone(stone)

    # Base case
    if depth == 1:
        if right_stone is None:
            return 1
        return 2
    
    output = count_stone_blinks(left_stone, depth - 1)
    if right_stone is not None:
        output += count_stone_blinks(right_stone, depth - 1)
    
    return output


def run(count):
    output = 0
    for stone in stones:
        output += count_stone_blinks(stone, count)
    return output

print()
print("Part 1")
print(run(25))

print()
print("Part 2")
print(run(75))