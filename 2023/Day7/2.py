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
        counts = dict(Counter(hand).most_common())

        print("hand", hand)
        print("counts", counts)
        
        # handling the jokers
        if 'J' in counts:
            nb_jokers = counts['J']
            del counts['J']

             # What if we add only Js (we just deleted them from counts)
            if len(counts) == 0:
                five_ok[hand] = bid
                continue

            keys_iterator = iter(counts)
            most_common = next(keys_iterator)
            counts[most_common] += nb_jokers
        
        keys_iterator = iter(counts)
        most_common = next(keys_iterator)
        if counts[most_common] == 5:
            five_ok[hand] = bid
            continue
        if counts[most_common] == 4:
            four_ok[hand] = bid
            continue
        if counts[most_common] == 3:
            # could be full or 3 of a kind
            second_most = next(keys_iterator)
            if counts[second_most] == 2:
                fh[hand] = bid
                continue
            else:
                three_ok[hand] = bid
            continue
        if counts[most_common] == 2:
            second_most = next(keys_iterator)
            # could be 2 pairs or 1 pair
            if counts[second_most] == 2:
                two_p[hand] = bid
                continue
            else:
                one_p[hand] = bid
                continue
        high_card[hand] = bid

# Let's order the hands
order = "AKQT98765432J"

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