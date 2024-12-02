import timeit

## Making the list

file_name = "input.txt"

list_1 = []
list_2 = []

with open(file_name, "r") as f:
    for l in f:
        elements = l.split("  ")
        list_1.append(int(elements[0]))
        list_2.append(int(elements[1]))

list_1_copy = list_1[:]
list_2_copy = list_2[:]

def algo1(list_1, list_2):
    similarity = 0
    for i in range(len(list_1)):
        for j in range(len(list_2)):
            if list_1[i] == list_2[j]:
                similarity += list_1[i]
    return similarity

def algo2(list_1, list_2):
    ## Sorting the list

    list_1.sort()
    list_2.sort()

    # Calculating the similarity

    similarity = 0

    p1 = 0
    p2 = 0

    while p1 < len(list_1) and p2 < len(list_2) :

        if list_1[p1] == list_2[p2] :
            p22 = p2
            while list_2[p22] == list_1[p1]:
                similarity += list_1[p1]
                p22 += 1
            p1 += 1
        elif list_1[p1] < list_2[p2] :
            p1 += 1
        elif list_1[p1] > list_2[p2] :
            p2 += 1
    return similarity


# Mesure the time of the 2 algorithms
time_1 = timeit.timeit(lambda : algo1(list_1, list_2), number=1)
time_2 = timeit.timeit(lambda : algo2(list_1_copy, list_2_copy), number=1)

print("Time for algo1: ", time_1)
print("Time for algo2: ", time_2)

print("Similarity_2 =", algo2(list_1_copy, list_2_copy))
