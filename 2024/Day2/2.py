file_name = "input"

def check_nums_Dampener(nums):

    num_n1 = int(nums[0])
    num_n = int(nums[1])

    dir = "up" if (num_n1 - num_n < 0) else "down"

    for index, num_n in enumerate(nums[1:]):

        num_n = int(num_n)

        if num_n == num_n1:
            return 0, index

        if abs(num_n - num_n1) > 3:
            return 0, index
    
        this_dir =  "up" if (num_n1 - num_n < 0) else "down"
        if this_dir != dir:
            return 0, index
        
        num_n1 = num_n
    return 1, None


nb_safe = 0

with open(file_name, 'r') as f:

    for line in f:
        damp = False
        nums = line.split(" ")
        result, index = check_nums_Dampener(nums)
        if result == 0 and damp == False:
            damp = True

            if index == 1:
                result, _ = check_nums_Dampener(nums[:index-1]+nums[index:])
                if result == 1 :
                    nb_safe += result
                    continue
            
            result, _ = check_nums_Dampener(nums[:index]+nums[index+1:])
            if result == 0 :
                result, _ = check_nums_Dampener(nums[:index+1]+nums[index+2:])
        nb_safe += result

print("nb_safe final:", nb_safe)