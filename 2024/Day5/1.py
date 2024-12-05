# rules :
#rules = {
#    key : ([must be before][must be after])
#}

file_name = "input"
#file_name = 'i2'


def check_nums(rules, nums):
    #print("We check")
    for i in range(len(nums)):
        #print("i :", i)
        p1 = 0
        p2 = len(nums)-1
        while p1 < i and p2 >i:
            if nums[p1] in rules[nums[i]][1] or nums[p2] in rules[nums[i]][0]:
                return False
            p1 += 1
            p2 -= 1
    return True
        

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
        #print("nums: ", nums)
        if check_nums(rules, nums):
            #print("line accepted")
            middle = nums[len(nums)//2]
            #print("middle: ", middle)
            sum += middle


print("sum :", sum)