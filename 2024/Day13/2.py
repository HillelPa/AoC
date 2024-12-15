import re
from sympy import symbols, Eq, solve

file_name = 'input'
#file_name = 'i2'

data = []
with open(file_name, 'r') as f:
    for line in f:
        line = line.strip()
        if line != '':
            data.append(line)

def get_nb_tokens(xA, xB, yA, yB, xP, yP):
    # Définir les variables
    nA, nB = symbols('nA nB', integer=True)

    # Définir les deux équations
    eq1 = Eq(xP, nA * xA + nB * xB)  # Équation pour x
    eq2 = Eq(yP, nA * yA + nB * yB)  # Équation pour y

    # Résolution du système d'équations
    solutions = solve((eq1, eq2), (nA, nB), dict=True)
    #print(solutions)

    if len(solutions) == 0: return 0

    lowest_cost = float('inf')
    for sol in solutions:
        nA = sol[nA]
        nB = sol[nB]
        cost = 3 * nA + nB
        if cost < lowest_cost:
            lowest_cost = cost
    
    return lowest_cost


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
    x_P = 10000000000000 + int(match.group(1))
    y_P = 10000000000000 + int(match.group(2))
    #x_P = int(match.group(1))
    #y_P = int(match.group(2))

    print("Machine", i//3)
    print("Button A:", x_A, y_A, "Button B:", x_B, y_B, "Prize", x_P, y_P)

    total_tokens += get_nb_tokens(x_A, x_B, y_A, y_B, x_P, y_P)
    #print("now total tokens", total_tokens)

print("--------------------------------")

print("total tokens", total_tokens)