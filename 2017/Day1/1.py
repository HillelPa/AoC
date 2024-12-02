file_name = "input.txt"

list = []
with open(file_name, "r") as f:
    for c in f.read():
        if c.isnumeric():
            list.append(int(c))

i = 0
j = 1
sum = 0
while i < len(list):
    if list[i] == list[j%len(list)]:
        sum += list[i]
    i+=1
    j+=1

print("sum: ", sum)