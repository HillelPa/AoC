file_name = "input"

nums = []

with open(file_name, 'r') as f:
    for line in f:
        nums.append(int(line))

# for each num in nums, we assign as the target for a sum of a pair : 2020 - num
# So for the first one (1935), we check if there is a pair that sums as 85
# We use the first algorithm to check if there is any pair like that

def find_pair(target, nums):
    seen = set()
    for num in nums:
        target_2 = target - num
        if target_2 in seen:
            return target_2 * num
        seen.add(num)
    return None

for num in nums:
    target = 2020 - num
    pair_product = find_pair(target, nums)
    if pair_product:
        print("Solution :", pair_product * num)
        break
