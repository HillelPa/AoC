with open('input', 'r') as f:
    hands = set()
    i = 0
    for l in f:
        hands.add(l.split(' ')[0])
        i+= 1
    
print(len(hands))
print(i)