# bacteria.py
class Bacteria:
    def __init__(self, species, food):
        self.species = species
        self.food = food

def create_bacteria(species, food):
    return Bacteria(species, food)

def move_bacteria(grid, bacteria, x, y):
    new_x = (x + bacteria.x) % len(grid)
    new_y = (y + bacteria.y) % len(grid[0])
    grid[bacteria.x][bacteria.y]['bacteria'].remove(bacteria)
    grid[new_x][new_y]['bacteria'].append(bacteria)
    bacteria.x, bacteria.y = new_x, new_y

def reproduce(grid, bacteria, Q):
    if len(grid[bacteria.x][bacteria.y]['bacteria']) < Q:
        new_bacteria = create_bacteria(bacteria.species, bacteria.food)
        grid[bacteria.x][bacteria.y]['bacteria'].append(new_bacteria)

def consume_food(bacteria, amount):
    bacteria.food -= amount

def die(grid, bacteria):
    grid[bacteria.x][bacteria.y]['bacteria'].remove(bacteria)