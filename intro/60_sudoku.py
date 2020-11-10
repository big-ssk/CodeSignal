def sudoku(grid):
    
    unique = set(range(1, 10))

    rows = [grid[i] for i in range(9)]
    
    columns = [[grid[i][j] for i in range(9)] for j in range(9)]
    
    cubes = [grid[i][j:j + 3] + grid[i + 1][j:j + 3] + grid[i + 2][j:j + 3] for i in range(0, 9, 3) for j in
             range(0, 9, 3)]
             
    items = [rows, columns, cubes]

    return all(set(subitem) == unique for item in items for subitem in item)
