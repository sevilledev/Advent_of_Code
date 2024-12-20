num_list_str = open("puzzle.txt", "r").read().split()
nums = [int(n) for n in num_list_str]

left_list = nums[0::2]
right_list = nums[1::2]

total = 0

for n1 in left_list:
    total += n1 * right_list.count(n1)
    

print(total)