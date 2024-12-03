# Still regEx, let's also find "do" et "don't"
# patern : r"mul\((\d{1,3}),(\d{1,3})\)|don't|do"

import re 

file_name = "input"

with open(file_name, 'r') as file:
    content = file.read()

pattern = r"mul\((\d{1,3}),(\d{1,3})\)|don't|do"

matches = re.finditer(pattern, content)


sum = 0
do = True

for match in matches:
    m = match.group(0)
    if m == "do":
        do = True
    elif m == "don't":
        do = False
    elif do:
        nums = re.findall(r'mul\((\d{1,3}),(\d{1,3})\)', m)
        sum += int(nums[0][0]) * int(nums[0][1])


print("sum :", sum)