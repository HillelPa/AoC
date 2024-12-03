# RegEx : mul(X,Y) where X and Y are 3 digits max 
# mul\((\d{1,3}),(\d{1,3})\)

import re 

file_name = "input"

with open(file_name, 'r') as file:
    content = file.read()

matches = re.findall(r'mul\((\d{1,3}),(\d{1,3})\)', content)

sum = 0

for matche in matches:
    sum += int(matche[0]) * int(matche[1])

print("sum :", sum)