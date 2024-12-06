file_name = "input"

def all_zeros(nums):
    for n in nums:
        if n != 0:
            return False
    return True

total_sum = 0

with open(file_name, 'r') as f:
    for line in f:
        step = 0
        vals = []
        line = line.rstrip()

        vals.append([int(x) for x in line.split(' ')])
        
        while not all_zeros(vals[step]):
            vals.append([vals[step][i+1] - vals[step][i] for i in range(len(vals[step]) - 1)])
            step += 1
        
        compl = 0
        for val in reversed(vals[:-1]):
            new = val[0] - compl
            compl = new
        total_sum += new

print("sum: ", total_sum)


