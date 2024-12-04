file_name = 'input'

total_scratch_cards = 0


def scratch_card(my_num, wining_num, index_card, my_nums, wining_nums):
    global total_scratch_cards
    total_scratch_cards += 1
    #print("We scratch card : ", index_card)
    #print(index_card, "wining :", wining_num, "num :", my_num) 

    num_card = index_card
    for num in wining_num:
        if num in my_num:
            #print(num_card, "MATCHING ", num)
            index_card += 1
            if index_card >= len(my_nums):
                break
            scratch_card(my_nums[index_card], wining_nums[index_card], index_card, my_nums, wining_nums)


with open(file_name, 'r') as f:
    input = f.readlines()


wining_nums = []
my_nums = []

for line in input:
    line = line.strip()

    nums = line.split(':')[1]
    nums = nums.split('|')

    wining_num = nums[0]
    wining_num = wining_num.split(" ")
    wining_num = [int(num) for num in wining_num if num.isnumeric()]
    wining_nums.append(wining_num)

    my_num = nums[1]
    my_num = my_num.split(" ")
    my_num = [int(num) for num in my_num if num.isnumeric()]
    my_nums.append(my_num)

print("hello")
for i in range(len(my_nums)):
    scratch_card(my_nums[i], wining_nums[i], i, my_nums, wining_nums)

print("total scratch :", total_scratch_cards)
