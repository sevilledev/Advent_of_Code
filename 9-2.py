disk = open("puzzle.txt").read()

files = {}
spaces = []
checksum = 0

# 2333133121414131402

# {0: [0, 2], 1: [5, 3], 2: [11, 1], 3: [15, 3], 4: [19, 2], 5: [22, 4], 6: [27, 4], 7: [32, 3], 8: [36, 4], 9: [40, 2]}
# [[2, 3], [8, 3], [12, 3], [18, 1], [21, 1], [26, 1], [31, 1], [35, 1]]


index = 0
for i in range(len(disk)):
    count = int(disk[i])
    
    if count > 0:
        if i == 0:
            files[0] = [index, count]
        elif i % 2 == 1:
            spaces.append([index, count])
        else:
            files[i // 2] = [index, count]
            
        index += count


for i in range(len(files) - 1, 0, -1):
    for space in spaces:
        if (files[i][1] <= space[1]):
            files[i][0] = space[0]
            space[0] += files[i][1]
            space[1] -= files[i][1]
            break
        
        if space[0] > files[i][0]:
            break
    

for index, (init, count) in files.items():
    for j in range(count):
        checksum += index * (init + j)

print(checksum)