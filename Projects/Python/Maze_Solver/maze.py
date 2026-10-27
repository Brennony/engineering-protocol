# Brennon York  |  Maze Solver V1.0 Alpha |  10/23/2026


# This program will eventually be able to solve maze's imported online through artiifical intelligence to identify the maze jpg/png/etc
# And mark each open spot as a 1 and closed as 0, then it will solve the maze through whatever means necesary.


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

def solve_dfs(grid, start, end):
    stack = [start]
    came_from = {start: None}

    while stack:
        cell = stack.pop()
        if cell == end:
            path = []
            while cell is not None:
                path.append(cell)
                cell = came_from[cell]
            path.reverse()
            return path

        r, c = cell

        for neighbor in get_neighbors(grid, r, c):
            if neighbor not in came_from:
                came_from[neighbor] = cell
                stack.append(neighbor)

    return None

path = solve_dfs(maze, start, end)
print(path)
print(len(path) - 1)                      # number of moves
print(solve_dfs(maze, start, (4, 2)))     # wall cell: expect None
print(solve_dfs(maze, start, start))      # expect [(1, 1)]
