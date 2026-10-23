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

#,start,end

def print_maze(grid,start,end):
    maze_disp = []
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

print_maze(maze,start,end)