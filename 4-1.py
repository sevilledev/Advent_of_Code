grid = open("puzzle.txt").read().splitlines()

rows = len(grid)
cols = len(grid[0])


def xmas(r, c):
    res = 0
    
    for dr in (-1, 0, 1):
        for dc in (-1, 0, 1):
            if dr == dc == 0:
                continue
            for i in range(len("XMAS")):
                nr = r + dr * i
                nc = c + dc * i
                
                if 0 <= nr < rows and 0 <= nc < cols:
                    if grid[nr][nc] == "XMAS"[i]:
                        if i == 3:
                            res += 1
                    else:
                        break
                    
    return res
                
    
total = 0
for r in range(rows):
    for c in range(cols):
        total += xmas(r, c)
        
print(total)