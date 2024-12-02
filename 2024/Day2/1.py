file_name = "input"
#file_name = "i2"

def check_line(line):
    nums = line.split(" ")

    num_n1 = int(nums[0])
    num_n = int(nums[1])

    dir = "up" if (num_n1 - num_n < 0) else "down"

    for num_n in nums[1:]:

        num_n = int(num_n)

        if num_n == num_n1:
            return 0

        if abs(num_n - num_n1) > 3:
            return 0
    
        this_dir =  "up" if (num_n1 - num_n < 0) else "down"
        if this_dir != dir:
            return 0
        
        num_n1 = num_n
    return 1



nb_safe = 0

with open(file_name, 'r') as f:
    for line in f:
        nb_safe += check_line(line)

print("nb_safe final:", nb_safe)