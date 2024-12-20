num_list_str = open("puzzle.txt", "r").read().split()
nums = [int(n) for n in num_list_str]

left_list = nums[0::2]
right_list = nums[1::2]

left_list.sort()
right_list.sort()

total = 0

for n1, n2 in zip(left_list, right_list):
    total += abs(n1-n2)
    

print(total)