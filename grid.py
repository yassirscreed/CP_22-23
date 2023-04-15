# grid.py
def create_grid(N):
    return [[{'food': 1, 'bacteria': []} for _ in range(N)] for _ in range(N)]

def add_food_to_cell(grid, x, y, amount):
    grid[x][y]['food'] += amount

def consume_food_in_cell(grid, x, y, amount):
    grid[x][y]['food'] -= amount
    if grid[x][y]['food'] < 0:
        grid[x][y]['food'] = 0

def remove_food_from_cell(grid, x, y, amount):
    grid[x][y]['food'] -= amount

def add_bacteria_to_cell(grid, x, y, bacteria):
    grid[x][y]['bacteria'].append(bacteria)

def remove_bacteria_from_cell(grid, x, y, bacteria):
    grid[x][y]['bacteria'].remove(bacteria)

def replenish_food(grid):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            cell = grid[i][j]   
            if cell['food'] < 1:
                cell['food'] = 1