grid = open("puzzle.txt").read().splitlines()

rows = len(grid)
cols = len(grid[0])

guard = (0, 0)
steps = [(-1, 0), (0, 1), (1, 0), (0, -1)]

count = 0


for r in range(rows):
    for c in range(cols):
        if grid[r][c] == "^":
            guard = (r, c)


def is_loop(guard, pos):
    marked = set()
    step_index = 0
    
    new_grid = [list(line) for line in grid]
    new_grid[pos[0]][pos[1]] = "#"
    
    while True:
        if (guard, step_index) in marked:
            return True
        
        marked.add((guard, step_index))
        
        s_r, s_c = steps[step_index]
        g_r, g_c = guard[0] + s_r, guard[1] + s_c
        
        
        if not (0 <= g_r <= rows - 1 and 0 <= g_c <= cols - 1):
           return False
        
        elif (new_grid[g_r][g_c] == "#"):
            step_index = (step_index + 1) % 4
            
        else:
            guard = (g_r, g_c)

        
for r in range(rows):
    for c in range(cols):
        if grid[r][c] == ".":
            if (is_loop(guard, (r, c))):
                count += 1


print(count)