file_name = "input"
#file_name = "i2"


with open(file_name, 'r') as f:
    input = f.readlines()

#print("size of input:", len(input), len(input[1]))
pattern = 'MAS'
#print(input)

def check_word_horizontal_f(input, i, j):
    k = j+1
    for letter in pattern:
        if k >= len(input[i]): return 0
        if input[i][k]!= letter:
            return 0
        k += 1
    #print("HF :", i, j)
    return 1

def check_word_vertical_f(input, i, j):
    k = i+1
    for letter in pattern:
        if k >= len(input): return 0
        if input[k][j]!= letter:
            return 0
        k += 1
    #print("VF :", i, j)
    return 1

def check_word_diag_down_f(input, i, j):
    k = i+1
    l = j+1
    for letter in pattern:
        if k >= len(input) or l >= len(input[i]): return 0
        if input[k][l]!= letter:
            return 0
        k += 1
        l += 1
    #print("DDF :", i, j)
    return 1

def check_word_diag_up_f(input, i, j):
    k = i-1
    l = j+1
    for letter in pattern:
        if k < 0 or l >= len(input[i]): return 0
        if input[k][l]!= letter:
            return 0
        k -= 1
        l += 1
    #print("DUF :", i, j)
    return 1

def check_word_horizontal_b(input, i, j):
    k = j-1
    for letter in pattern:
        if k < 0: return 0
        if input[i][k]!= letter:
            return 0
        k -= 1
    #print("HB :", i, j)
    return 1

def check_word_vertical_b(input, i, j):
    k = i-1
    for letter in pattern:
        if k < 0: return 0
        if input[k][j]!= letter:
            return 0
        k -= 1
    #print("VB :", i, j)
    return 1

def check_word_diag_down_b(input, i, j):
    k = i+1
    l = j-1
    for letter in pattern:
        if k >= len(input) or l < 0: return 0
        if input[k][l]!= letter:
            return 0
        k += 1
        l -= 1
    #print("DDB :", i, j)
    return 1

def check_word_diag_up_b(input, i, j):
    k = i-1
    l = j-1
    for letter in pattern:
        if k < 0 or l < 0: return 0
        if input[k][l]!= letter:
            return 0
        k -= 1
        l -= 1
    #print("DUB :", i, j)
    return 1



sum = 0

for i in range(len(input)):
    for j in range(len(input[i])):   
        # We could be at a begining of XMAS
        if input[i][j] == 'X':
            # Frontward
            # Horizontal
            sum += check_word_horizontal_f(input, i, j)
            # Vertical
            sum += check_word_vertical_f(input, i, j)
            # Diagonal down
            sum += check_word_diag_down_f(input, i, j)
            # Diagonal up
            sum += check_word_diag_up_f(input, i, j)
            # backwards
            # Horizontal
            sum += check_word_horizontal_b(input, i, j)
            # Vertical
            sum += check_word_vertical_b(input, i, j)
            # Diagonal down
            sum += check_word_diag_down_b(input, i, j)
            # Diagonal up
            sum += check_word_diag_up_b(input, i, j)

print("sum :", sum)

            

