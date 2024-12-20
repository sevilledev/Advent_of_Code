import re

text = open("puzzle.txt", "r").read()
list_m = re.findall(r"mul\(\d+,\d+\)", text)

total = 0

for pair in list_m:
    list_num = [int(n) for n in re.findall(r"\d+,\d+", pair)[0].split(',')]
    total += list_num[0] * list_num[1]

print(total)