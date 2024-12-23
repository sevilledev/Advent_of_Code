stones = [int(n) for n in open("puzzle.txt").read().split()]
loop = 25


def blink(stones, loop):
    new_stones = []
    
    for stone in stones:
        length = len(str(stone))

        if stone == 0:
            new_stones.append(1)

        elif length % 2 == 0:
            new_stones.append(int(str(stone)[: length // 2]))
            new_stones.append(int(str(stone)[length // 2 :]))
            
        else:
            new_stones.append(stone * 2024)
            
    loop -= 1
    
    if loop == 0:
        return len(new_stones)
            
    return blink(new_stones, loop)
            

print(blink(stones, loop))