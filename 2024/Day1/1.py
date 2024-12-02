## Making the list

file_name = "input.txt"

list_1 = []
list_2 = []

with open(file_name, "r") as f:
    for l in f:
        elements = l.split("  ")
        list_1.append(int(elements[0]))
        list_2.append(int(elements[1]))

## Sorting the list

list_1.sort()
list_2.sort()

## Calculating the distance

d = 0
for i, j in zip(list_1, list_2):
    d += abs(i - j)

print("distance =", d)