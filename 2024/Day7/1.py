file_name = 'input'
#file_name = 'i2'

result = 0

with open(file_name, 'r') as f:
    for line in f:
        #print("--------------------------------")
        line = line.strip()
        #print(f'Line: {line}')
        line = line.split(': ')
        target = int(line[0])
        nums = [int(x) for x in line[1].split(' ')]
        #print(nums)

        # Let's make a binary tree
        #     A
        #  +/   \*
        #  A+B  A*B

        tree = []
        for i in range(len(nums)):
            if i == 0:
                tree.append([nums[i]])
                continue
            level = []
            for case in tree[i-1]:
                level.append(case + nums[i])
                level.append(case * nums[i])
            tree.append(level)
        
        if target in tree[-1]: result += target

print('result:', result)


