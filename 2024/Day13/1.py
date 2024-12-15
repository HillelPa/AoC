import re

file_name = 'input'
#file_name = 'i2'

data = []
with open(file_name, 'r') as f:
    for line in f:
        line = line.strip()
        if line != '':
            data.append(line)


def from_nb_tokens_to_nA_nB(nb_T):
    solutions = []
    n_A, n_B = 0, 0
    while n_A <= nb_T//3:
        n_B = nb_T - 3*n_A
        solutions.append((n_A, n_B))
        n_A += 1
    return solutions

from_nb_tokens_to_nA_nB(10)

# Brute force a little smart
def get_nb_tokens(x_A, x_B, y_A, y_B, x_P, y_P):
    tokens = 0
    if not (x_P <= (100*x_A + 100*x_B) and y_P <= (100*y_A + 100*y_B)):
        return 0
    while tokens <= 400:
        #print("tokens :", tokens)
        solutions = from_nb_tokens_to_nA_nB(tokens)
        for solution in solutions:
            #print("(n_A, n_B)", solution)
            n_A = solution[0]
            n_B = solution[1]
            if n_A > 100 or n_B > 100:
                #print("One too many")
                continue
            #print("cxp :", (n_A*x_A + n_B*x_B))
            #print("cyp :", (n_A*y_A + n_B*y_B))
            if x_P == (n_A*x_A + n_B*x_B) and y_P == (n_A*y_A + n_B*y_B):
                print("Best : nA, nB :", n_A, n_B)
                #print("We return :", 3*n_A + n_B)
                return 3*n_A + n_B
        tokens += 1
    print("No solution found")
    #print("We return 0")
    return 0
    
                

total_tokens = 0
    
for i in range(0, len(data), 3):
    print("--------------------------------")
    button_A = data[i]
    x_A = int(button_A[12:14])
    y_A = int(button_A[18:])

    button_B = data[i+1]
    x_B = int(button_B[12:14])
    y_B = int(button_B[18:])

    prize = data[i+2]
    match = re.search(r"X=(\d+), Y=(\d+)", prize)
    x_P = int(match.group(1))
    y_P = int(match.group(2))

    print("Machine", i//3)
    print("Button A:", x_A, y_A, "Button B:", x_B, y_B, "Prize", x_P, y_P)

    total_tokens += get_nb_tokens(x_A, x_B, y_A, y_B, x_P, y_P)

print("--------------------------------")

print("total tokens", total_tokens)
