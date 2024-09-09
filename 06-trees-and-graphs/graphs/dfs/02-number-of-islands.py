# Number of Islands

# Given an m x n 2D binary grid 
# which represents 
#   a map of 
#       1 (land) and 
#       0 (water), 
# return the number of islands. 

# An island is surrounded by water 
# and is formed by connecting 
# adjacent land cells 
# horizontally or vertically.

def num_of_island(grid: list[list[int]]) -> int:
    if not grid:
        return 0

    def dfs(row, col):
        # Check if the cell is out of bounds first
        out_of_bounds = row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0])
        if out_of_bounds:
            return
        
        # Now it's safe to access grid[row][col]
        is_water_or_visited = grid[row][col] == 0
        if is_water_or_visited:
            return

        # Mark the cell as visited by turning it into 0 (water)
        grid[row][col] = 0

        # Explore all adjacent cells (vertically and horizontally)
        dfs(row + 1, col)  # down
        dfs(row - 1, col)  # up
        dfs(row, col + 1)  # right
        dfs(row, col - 1)  # left

    island_count = 0
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == 1:  # Found an unvisited land cell
                dfs(row, col)  # Explore the island
                island_count += 1 

    return island_count

# Test example
grid = [
    [1, 1, 0, 0, 0],
    [1, 1, 0, 0, 1],
    [0, 0, 0, 1, 1],
    [0, 0, 0, 0, 0],
    [1, 0, 1, 0, 1]
]

print("Number of islands:", num_of_island(grid))  
# Expected output: 6
