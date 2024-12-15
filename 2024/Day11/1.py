file_name = 'input'
#file_name = 'i2'

with open(file_name, 'r') as f:
    line = f.readline()
    stones = line.split(" ")


def blinking(stones):
    new_stones = []
    for s in stones:
        # Rule 1:
        if s == '0':
            new_stones.append('1')
        # Rule 2:
        elif len(s)%2 == 0:
            # Split the stone into two halves and removing inutiles 0
            new_stones.append(str(int(s[:len(s)//2])))
            new_stones.append(str(int(s[len(s)//2:])))
        # Rule 3:
        else:
            num = int(s)
            new_stones.append(str(2024*num))
    return new_stones

for i in range(25):
    print("blinking", i)
    stones = blinking(stones)

print("final len =", len(stones))