file_name = "input.txt"

list = []
with open(file_name, "r") as f:
    for c in f.read():
        if c.isnumeric():
            list.append(int(c))

len_list = len(list)
i = 0
step = len_list//2
j = step
sum = 0


while i < len_list/2:
    if list[i] == list[int(j%len_list)]:
        sum += 2*list[i]
    i+=1
    j+=1

print("sum: ", sum)