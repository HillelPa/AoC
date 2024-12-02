# We look for the fewest nb of cube possible
# Games :
#{
#    game_id : [red, green, blue]
#}
# [red, green, blue] -> info max for each color
# for example : 
# Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red -> [14, 3, 15]
# ^- a way to represent the data, we won't need to do that for the 1st problem


def get_power(line):

    red = 0
    green = 0
    blue = 0

    line = line.replace("\n", "")

    #remove the game id and remove the spaces
    subsets = line.split(":")[1][1:].replace(" ", "") # line.split(":")[0] : Game X, line.split(":")[1] : 2 red, 2 green; 6 red, 3 green; 2 red, 1 green, 2 blue; 1 red
    print(subsets)

    # Get each subset
    subsets = subsets.split(";")
    print(subsets)

    for subset in subsets:
        colors = subset.split(",")
        print(colors)

        for color in colors:
            
            # RED
            if color[-1] == 'd':
                value = int(color[:-3])
                if value > red : red = value

            elif color[-1] == 'n':
                value = int(color[:-5])
                if value > green : green = value

            elif color[-1] == 'e':
                value = int(color[:-4])
                if value > blue : blue = value
    return red*green*blue

file_name = "input"
sum = 0
with open(file_name, "r") as f:
    for line in f:
        sum += get_power(line)

print("sum :", sum)
