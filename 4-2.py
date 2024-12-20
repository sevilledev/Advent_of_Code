grid = open("puzzle.txt").read().splitlines()

rows = len(grid)
cols = len(grid[0])

combs = ["MSMS", "MMSS", "SMSM", "SSMM"]

total = 0


def xmas(r, c):
    res = 0
    
    if (1 <= r <= rows - 2 and 1 <= c <= cols - 2):
        values = f"{grid[r - 1][c - 1]}{grid[r - 1][c + 1]}{grid[r + 1][c - 1]}{grid[r + 1][c + 1]}"

        if (values in combs):
            res += 1

    return res


for r in range(rows):
    for c in range(cols):
        if grid[r][c] == "A":
            total += xmas(r, c)
            

print(total)