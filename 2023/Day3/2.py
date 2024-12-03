#file_name = "i2"
file_name = "input.txt"

with open(file_name, 'r') as f:
    input = f.readlines()

sum = 0

for i_line in range(len(input)):
    for j_column in range(len(input[i_line])):
        if input[i_line][j_column] == "*" :
            nums = []
            for i in range(-1, 2):
                j = -1
                while j < 2:
                    if i != 0 or j != 0:
                        if i_line+i >= 0 and j_column+j >= 0 and i_line+i < len(input) and j_column+j < len(input[i_line]):
                            if input[i_line+i][j_column + j].isnumeric():
                                # We need to find the full number
                                n = input[i_line+i][j_column + j]
                                p = j_column + j
                                p_back = j_column + j - 1
                                p_front = j_column + j + 1
                                while p_back >= 0 and input[i_line+i][p_back].isnumeric():
                                    n = input[i_line+i][p_back] + n
                                    p_back -= 1
                                while p_front < len(input[i_line]) and input[i_line+i][p_front].isnumeric():
                                    n = n + input[i_line+i][p_front]
                                    p_front += 1
                                    j += 1
                                nums.append(int(n))
                    j += 1
            if len(nums) == 2:
                sum += nums[0] * nums[1]

print("sum :", sum)