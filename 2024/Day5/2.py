# rules :
#rules = {
#    key : ([must be before][must be after])
#}

file_name = "input"


def check_nums(rules, nums):
    for i in range(len(nums)):
        p1 = 0
        p2 = len(nums)-1
        while p1 < i and p2 >i:
            if nums[p1] in rules[nums[i]][1]:
                # False bc p1 is supposed to be after
                return 0, nums[p1], nums[i]
            if nums[p2] in rules[nums[i]][0]:
                # False bc p2 is supposed to be before
                return 0, nums[i], nums[p2]
            p1 += 1
            p2 -= 1
    return 1, None, None
        

sum = 0

with open(file_name, 'r') as f:
    rules = {}
    rule = True
    for line in f:
        if rule:
            if line == '\n':
                rule = False
                continue
            
            line = line.rstrip()
            parts = line.split("|")
            before = int(parts[0])
            after = int(parts[1])

            if before not in rules:
                rules[before] = ([], [after])
            else:
                rules[before][1].append(after)
            
            if after not in rules:
                rules[after] = ([before], [])
            else:
                rules[after][0].append(before)
            continue

        line = line.strip()
        nums = [int(l) for l in line.split(',')]
        case, b, a = check_nums(rules, nums)
        if case == 0:
            while case == 0:
                i_a = nums.index(a)
                i_b = nums.index(b)
                nums[i_a], nums[i_b] = nums[i_b], nums[i_a]
                case, b, a = check_nums(rules, nums)
            sum += nums[len(nums)//2]
            
print("sum :", sum)