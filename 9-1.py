disk = open("puzzle.txt").read()

new_format = []
checksum = 0


for i in range(len(disk)):
    for j in range(int(disk[i])):
        if i == 0:
            new_format.append(0)
        elif i % 2 == 1:
            new_format.append(".")
        else:
            new_format.append(i // 2)


last_index = len(new_format) - 1
init_index = 0


while last_index - init_index > 0:
    if new_format[init_index] != ".":
        init_index += 1
        continue
    
    elif new_format[last_index] == ".":
        last_index -= 1
        continue
        
    else:
        new_format[init_index], new_format[last_index] = new_format[last_index], new_format[init_index]
        init_index += 1
        last_index -= 1


j = 0
while new_format[j] != ".":
    checksum += j * int(new_format[j])
    j += 1

print(checksum)