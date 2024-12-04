# 1       2      3      4
# M _ M   M _ S  S _ M  S _ S
# _ A _   _ A _  _ A _  _ A _
# S _ S   M _ S  S _ M  M _ M

file_name = "input"

with open(file_name, 'r') as file:
    input = file.readlines()

def check_1(input, i, j):
    if input[i-1][j-1] == 'M' and input[i-1][j+1] == 'M' and input[i+1][j-1] == 'S' and input[i+1][j+1] == 'S' : return 1
    return 0

def check_2(input, i, j):
    if input[i-1][j-1] == 'M' and input[i-1][j+1] == 'S' and input[i+1][j-1] == 'M' and input[i+1][j+1] == 'S' : return 1
    return 0

def check_3(input, i, j):
    if input[i-1][j-1] == 'S' and input[i-1][j+1] == 'M' and input[i+1][j-1] == 'S' and input[i+1][j+1] == 'M' : return 1
    return 0

def check_4(input, i, j):
    if input[i-1][j-1] == 'S' and input[i-1][j+1] == 'S' and input[i+1][j-1] == 'M' and input[i+1][j+1] == 'M' : return 1
    return 0

sum = 0
for i in range(1, len(input) - 1):
    for j in range(1, len(input[i]) - 1):
        if input[i][j] == 'A':
            # We may be in the middle of the X
            if check_1(input, i, j):
                sum += 1
            elif check_2(input, i, j):
                sum += 1
            elif check_3(input, i, j):
                sum += 1
            elif check_4(input, i, j):
                sum += 1
            #sum += check_1(input, i, j) + check_2(input, i, j) + check_2(input, i, j) + check_4(input, i, j)

print("Sum: ", sum)


