# Brennon York  |  Maze Solver  |  10/22/2026


# Sample Maze
maze = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0, 1, 1, 1, 1, 0],
    [0, 0, 0, 1, 0, 1, 0, 0, 1, 0],
    [0, 1, 1, 1, 1, 1, 0, 1, 1, 0],
    [0, 1, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 1, 1, 1, 1, 1, 0, 1, 1, 0],
    [0, 0, 0, 0, 0, 1, 0, 0, 1, 0],
    [0, 1, 1, 1, 0, 1, 1, 1, 1, 0],
    [0, 1, 0, 1, 1, 1, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
]
start = (1, 1)
end = (8, 8)

def print_maze(grid,start,end):
    for r in range(len(grid)):
        row = []
        for c in range(len(grid[r])):
            if (r,c) == start:
                row.append('S ')
            elif (r,c) == end:
                row.append('E ')
            elif grid[r][c] == 0:
                row.append('# ')
            else:
                row.append(". ")
        print("".join(row))

def get_neighbors(grid, r, c):
    neighbors = []
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]   # up, down, left, right
    for dr, dc in moves:
        nr = r + dr
        nc = c + dc
        if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and grid[nr][nc] == 1:
            neighbors.append((nr,nc))

    return neighbors

print_maze(maze,start,end)
print(get_neighbors(maze,3,3))