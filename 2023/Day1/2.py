file_name = "input"
#file_name = "i2"
def translate(line):
    digit_names = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    for num, name in enumerate(digit_names):
        line = line.replace(name, name+str(num)+name)
    return line

sum = 0

with open(file_name, 'r') as f:
    for line in f:
        line = line.strip()
        line = translate(line)
        digits = [char for char in line if char.isnumeric()]
        sum += int(digits[0]) * 10 + int(digits[-1])

print("sum :", sum)