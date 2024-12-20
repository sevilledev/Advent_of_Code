grid = open("puzzle.txt").read().splitlines()

rows = len(grid)
cols = len(grid[0])

guard = (0, 0)
marked = set()

steps = [(-1, 0), (0, 1), (1, 0), (0, -1)]
step_index = 0


for r in range(rows):
    for c in range(cols):
        if grid[r][c] == "^":
            guard = (r, c)
            marked.add(guard)


while True:
    s_r, s_c = steps[step_index]
    g_r, g_c = guard[0] + s_r, guard[1] + s_c
    
    
    if not (0 <= g_r <= rows - 1 and 0 <= g_c <= cols - 1):
        break
    
    elif (grid[g_r][g_c] == "#"):
        step_index = (step_index + 1) % 4
        
    else:
        guard = (g_r, g_c)
        marked.add(guard)


print(len(marked))