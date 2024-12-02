import heapq

file_name = "input"

with open(file_name, 'r') as f:
    current = 0
    heap = []
    for line in f:
        if line == "\n":
            heapq.heappush(heap, current)
            if len(heap) > 3:
                heapq.heappop(heap)
            current = 0
        else:
            current += int(line)

print(heap)
print("sum :", sum(heap) )