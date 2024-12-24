grid = [[int(num) for num in row] for row in open("puzzle.txt").read().splitlines()]

rows = len(grid)
cols = len(grid[0])

trailheads = []
sum = 0      


def score(r, c):
    trail = [(r, c)]
    count = 0
    
    while trail:
        tr, tc = trail.pop()
        
        if grid[tr][tc] == 9:
            count += 1
        
        for i, j in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
            nr, nc = tr + i, tc + j
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == grid[tr][tc] + 1:
                trail.append((nr, nc))

    return count


for r in range(rows):
    for c in range(cols):
        if grid[r][c] == 0:
            trailheads.append((r, c))


for r, c in trailheads:
    sum += score(r, c)
    
print(sum)