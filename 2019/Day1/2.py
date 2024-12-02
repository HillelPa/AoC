file_name = "input.txt"

fuel = 0
with open(file_name, 'r') as f:
    for line in f:
        print("weight of the module :", line)
        fuel_n = int(line)//3 - 2
        fuel_n1 = 0
        fuel_module = fuel_n
        while fuel_n > 0:
            fuel_n1 = fuel_n//3 - 2
            if fuel_n1 > 0:
                fuel_module += fuel_n1
            fuel_n = fuel_n1
        fuel += fuel_module
        print("fuel needed for the module:", fuel)

print("total fuel needed (including fuel for fuel):", fuel)