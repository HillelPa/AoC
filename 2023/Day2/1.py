# 12 red, 13 green, 14 blue
# Games :
#{
#    game_id : [red, green, blue]
#}
# [red, green, blue] -> info max for each color
# for example : 
# Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red -> [14, 3, 15]
# ^- a way to represent the data, we won't need to do that for the 1st problem


def check_game(line):

    max_red = 12
    max_green = 13
    max_blue = 14

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
                print("RED")
                value = int(color[:-3])
                print("value :", value)
                if value > max_red:
                    return 0

            elif color[-1] == 'n':
                print("GREEN")
                value = int(color[:-5])
                print("value :", value)
                if value > max_green:
                    return 0
            
            elif color[-1] == 'e':
                print("BLUE")
                value = int(color[:-4])
                print("value :", value)
                if value > max_blue:
                    return 0
    return 1

file_name = "input"
id = 1
sum = 0
with open(file_name, "r") as f:
    for line in f:
        sum += id*check_game(line)
        id += 1

print("sum :", sum)
