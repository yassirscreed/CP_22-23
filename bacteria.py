# bacteria.py
class Bacteria:
    def __init__(self, id , species , food, x, y):
        self.id = id
        self.species = species
        self.food = food
        self.x = x
        self.y = y


def create_bacteria(id, species, food, x, y):
    return Bacteria(id, species, food, x, y)

def move_bacteria(grid, bacteria, x, y, Q):
    new_x = (x + bacteria.x) % len(grid)
    new_y = (y + bacteria.y) % len(grid[0])

    if len(grid[new_x][new_y]['bacteria']) >= Q: # se tiver mais que Q bactérias na célula, não se move
        return
    
    grid[bacteria.x][bacteria.y]['bacteria'].remove(bacteria)
    grid[new_x][new_y]['bacteria'].append(bacteria)
    bacteria.x, bacteria.y = new_x, new_y

def reproduce(grid, bacteria, Q):
    if len(grid[bacteria.x][bacteria.y]['bacteria']) < Q:
        new_bacteria = create_bacteria(bacteria.id ,bacteria.species, bacteria.food, bacteria.x, bacteria.y)
        grid[bacteria.x][bacteria.y]['bacteria'].append(new_bacteria)

def consume_food(bacteria, amount):
    if bacteria.food >= 1:
        bacteria.food -= amount

def die(grid, bacteria):
    grid[bacteria.x][bacteria.y]['bacteria'].remove(bacteria)