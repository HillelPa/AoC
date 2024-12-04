file_name = 'input'

sum = 0
with open(file_name, 'r') as f:
    for line in f:
        line = line.strip()

        nums = line.split(':')[1]
        nums = nums.split('|')

        wining_nums = nums[0]
        wining_nums = wining_nums.split(" ")
        wining_nums = [int(num) for num in wining_nums if num.isnumeric()]

        my_nums = nums[1]
        my_nums = my_nums.split(" ")
        my_nums = [int(num) for num in my_nums if num.isnumeric()]

        local_sum = 0
        for num in wining_nums:
            if num in my_nums:
                local_sum = max(1,2*local_sum)
        sum += local_sum

print("sum :", sum)
        