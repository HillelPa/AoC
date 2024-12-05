# Notice that with check.py we checked that no hand appears twice
from collections import Counter

file_name = 'input'

five_ok = {}
four_ok = {}
fh = {}
three_ok = {}
two_p = {}
one_p = {}
high_card = {}

with open(file_name, 'r') as f:
    nb_hands = 0
    for l in f:
        nb_hands += 1
        hand = l.split(' ')[0]
        bid = int(l.split(' ')[1].strip())
        counts = Counter(hand).most_common()
        if counts[0][1] == 5:
            five_ok[hand] = bid
            continue
        if counts[0][1] == 4:
            four_ok[hand] = bid
            continue
        if counts[0][1] == 3:
            # could be full or 3 of a kind
            if counts[1][1] == 2:
                fh[hand] = bid
                continue
            else:
                three_ok[hand] = bid
            continue
        if counts[0][1] == 2:
            # could be 2 pairs or 1 pair
            if counts[1][1] == 2:
                two_p[hand] = bid
                continue
            else:
                one_p[hand] = bid
                continue
        high_card[hand] = bid



# Let's order the hands
order = "AKQJT98765432"

def custom_key(key):
    # Mapper chaque caractère de la clé à sa position dans l'ordre
    return [order.index(char) for char in key]

five_ok = sorted(five_ok.items(), key=lambda item: custom_key(item[0]))
four_ok = sorted(four_ok.items(), key=lambda item: custom_key(item[0]))
fh = sorted(fh.items(), key=lambda item: custom_key(item[0]))
three_ok = sorted(three_ok.items(), key=lambda item: custom_key(item[0]))
two_p = sorted(two_p.items(), key=lambda item: custom_key(item[0]))
one_p = sorted(one_p.items(), key=lambda item: custom_key(item[0]))
high_card = sorted(high_card.items(), key=lambda item: custom_key(item[0]))

total_winnings = 0
rank = nb_hands

for hand, bid in five_ok:
    total_winnings += bid*rank
    rank -= 1

for hand, bid in four_ok:
    total_winnings += bid*rank
    rank -= 1

for hand, bid in fh:
    total_winnings += bid*rank
    rank -= 1

for hand, bid in three_ok:
    total_winnings += bid*rank
    rank -= 1

for hand, bid in two_p:
    total_winnings += bid*rank
    rank -= 1

for hand, bid in one_p:
    total_winnings += bid*rank
    rank -= 1

for hand, bid in high_card:
    total_winnings += bid*rank
    rank -= 1

print(total_winnings)



