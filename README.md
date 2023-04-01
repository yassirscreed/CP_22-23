Documentacao

1. What does zip() do?

    zip() is a built-in Python function that takes iterables (can be zero or more), aggregates them in a tuple, and return it.

    Example: zip(['A', 'B', 'C'], [NA, NB, NC]) returns [('A', NA), ('B', NB), ('C', NC)]

    zip() is useful when you have to manipulate the iterables together.

2.  What does  x, y = random.randint(0, N - 1), random.randint(0, N - 1) do?

    x, y = random.randint(0, N - 1), random.randint(0, N - 1) is a tuple assignment. It assigns the first element of the tuple to x and the second element to y.

    Example: x, y = (1, 2) assigns 1 to x and 2 to y.

3. what does dx, dy = random.randint(-K, K), random.randint(-K, K) do?

    dx, dy = random.randint(-K, K), random.randint(-K, K) is a tuple assignment. It assigns the first element of the tuple to dx and the second element to dy.

    Example: dx, dy = (1, 2) assigns 1 to dx and 2 to dy.

4. Why does when i add every event to events it saves a species_counts.copy()?

    When you add every event to events, it saves a species_counts.copy() because you want to save the state of the simulation at that time.

5. What does this code do other_b for other_b in g[b.x][b.y]['bacteria'] if other_b.species in ['B', 'C'] ?

    This code does other_b for other_b in g[b.x][b.y]['bacteria'] if other_b.species in ['B', 'C'] because you want to iterate through the bacteria in the same location as b and check if the species is B or C.


6. Explain every method of the bacteria class.

    def _init_(self, species, food):
    This is the constructor of the class. It initializes the species and food of the bacteria.

    def create_bacteria(species, food):
    This method creates a bacteria with the given species and food.
    
    def move_bacteria(grid, bacteria, x, y):
    This method moves the bacteria to a new location.

    def reproduce(grid, bacteria, Q):
    This method reproduces the bacteria if the number of bacteria in the same location is less than Q.

    def consume_food(bacteria, amount):
    This method consumes food from the bacteria.

    def die(grid, bacteria):
    This method kills the bacteria.

   
7. Explain every parameter of the simulate function and what happens if its changed.

    N: Grid size (NxN). Increasing N creates a larger environment for the bacteria to move and interact, potentially leading to a more diverse and complex simulation. Decreasing N results in a smaller, more crowded environment that may limit bacterial movement and interactions.

    Q: Maximum number of bacteria that can be produced by a single bacteria during reproduction. Increasing Q allows for a higher potential population growth, while decreasing Q limits the population growth of each bacteria species.

    NA, NB, NC: Initial number of bacteria of each species (A, B, C). Increasing the initial number of bacteria will lead to a more populated grid at the beginning of the simulation, which may affect the interactions between species and competition for resources. Decreasing the initial number of bacteria will result in fewer initial interactions and a less competitive environment.

    F: Initial food level of each bacteria. Increasing F provides more initial resources for bacteria, allowing them to survive and reproduce for a longer period before needing to feed. Decreasing F may cause bacteria to search for food more frequently, potentially leading to quicker depletion of resources and higher competition.

    TS: Total simulation time. Increasing TS allows for a longer simulation period, potentially leading to more complex and diverse outcomes. Decreasing TS results in a shorter simulation with fewer opportunities for bacteria to evolve and interact.

    TR: Reproduction time. Increasing TR results in a slower reproduction rate, leading to slower population growth. Decreasing TR speeds up reproduction, potentially causing rapid population growth and increased competition for resources.

    TF: Fusion time. Increasing TF slows down the fusion rate between bacteria B and C, resulting in fewer BC bacteria formed over time. Decreasing TF increases the fusion rate, potentially leading to a higher number of BC bacteria in the simulation.

    TA: Feeding time. Increasing TA prolongs the time between feeding events, which may result in bacteria dying due to starvation or increased competition for resources. Decreasing TA allows bacteria to feed more frequently, potentially reducing starvation and competition.

    TRP: Food replenishment time. Increasing TRP slows down the rate at which food is added to the grid, potentially leading to scarce resources and increased competition. Decreasing TRP results in faster food replenishment, providing more resources for the bacteria and potentially reducing competition.

    TM: Natural death time. Increasing TM extends the average lifespan of bacteria, allowing them to reproduce and interact for a longer period. Decreasing TM shortens the average lifespan, leading to more frequent natural deaths and potentially affecting population dynamics.

    K: Maximum displacement of a bacteria in a single step. Increasing K allows bacteria to move more significant distances in one step, leading to a more dynamic and dispersed distribution of species on the grid. Decreasing K results in smaller movement steps, potentially leading to a more clustered distribution of species and increased competition for resources within limited areas.

8. Explain how it works in general.
 
    run_simulation: This function takes several parameters to define the initial state and behavior of the simulation, such as grid size, initial bacteria counts, food levels, and time intervals for different events.

    The function begins by creating a grid g with dimensions NxN and initializing dictionaries for species counts and events. It then randomly places bacteria A, B, and C on the grid, adding them to both the grid and the all_bacteria list, and logging the initial events.

    Next, it prints the initial state of the simulation, including species counts, bacteria counts, food counts.

    The main loop of the simulation starts, running until the time t exceeds the total simulation time TS. For each bacteria in the all_bacteria list, the following events may occur:

    a. Bacteria movement: The bacteria move randomly within the range of -K to K in both the x and y directions.

    b. Bacteria reproduction: If the time t is greater than or equal to a random exponential value based on the reproduction time TR, the bacteria will reproduce.

    c. Fusion between bacteria B and C: If the time t is greater than or equal to a random exponential value based on the fusion time TF, bacteria B and C present in the same cell may fuse to form a new species, BC.

    d. Bacteria feeding: If the time t is greater than or equal to a random exponential value based on the feeding time TA, bacteria will feed. Bacteria A feeds on B and C species, while B and C species feed on available food in the grid cell.

    e. Food replenishment: If the time t is greater than or equal to a random exponential value based on the food replenishment time TRP, food will be added to the grid cell.

    f. Natural death: If the time t is greater than or equal to a random exponential value based on the natural death time TM, the bacteria will die.

    All events are logged ( species_counts.copy() ) with their respective times, and the simulation continues until the total simulation time TS is reached.

    plot_evolution: This function takes the logged events from the simulation and generates a graph showing the evolution of the number of bacteria of each species over time. It uses matplotlib to create a line plot for each species (A, B, C, and BC) with a unique color for each species.

9. Explain the grid module.

    The grid is a 2D list of dictionaries, with each dictionary containing two keys: 'food' and 'bacteria'. The 'food' key represents the amount of food available in each cell, while the 'bacteria' key contains a list of bacteria present in that cell.

    1. create_grid(N): This function creates an NxN grid. Each cell in the grid is initialized with a dictionary containing a food value of 1 and an empty list of bacteria. It returns the grid as a 2D list.

    2. add_food_to_cell(grid, x, y, amount): This function takes a grid, x and y coordinates, and an amount of food to add. It increases the food value in the specified cell (x, y) by the given amount.

    3. consume_food_in_cell(grid, x, y, amount): This function takes a grid, x and y coordinates, and an amount of food to consume. It decreases the food value in the specified cell (x, y) by the given amount. If the food value goes below 0, it is set to    0.

    4. remove_food_from_cell(grid, x, y, amount): This function takes a grid, x and y coordinates, and an amount of food to remove. It decreases the food value in the specified cell (x, y) by the given amount. Unlike consume_food_in_cell, it does not have a check for negative food values.

    5. add_bacteria_to_cell(grid, x, y, bacteria): This function takes a grid, x and y coordinates, and a bacteria object. It appends the given bacteria object to the 'bacteria' list in the specified cell (x, y).

    6. remove_bacteria_from_cell(grid, x, y, bacteria): This function takes a grid, x and y coordinates, and a bacteria object. It removes the given bacteria object from the 'bacteria' list in the specified cell (x, y).

    These functions are used in the main simulation to manipulate the grid environment, allowing bacteria to interact with each other and their surroundings, such as moving, feeding, reproducing, and dying.

10. Explain the cap and event modules and how they work together.

    The event and cap modules provide functionality for creating, managing, and manipulating events during the bacteria simulation. Events are used to track the state and actions of the bacteria at different points in time.

    1. event module:
        This module provides simple functions to create and access event properties. An event is represented as a list with three elements: time, kind, and counts.

        1. evt(t, k, counts): This function creates a new event with time t, kind k, and species counts counts. It returns the event as a list.

        2. time(e): This function takes an event e and returns its time value.

        3. kind(e): This function takes an event e and returns its kind.

        4. counts(e): This function takes an event e and returns its species counts.

    2. cap module (Cadeia de Acontecimentos Pendentes):
        This module provides functions for managing a chain of pending events. It uses the event module to create and manipulate individual events.

        1. newc(): This function creates a new empty pending event chain and returns it as an empty list.

        2. addE(c, e): This function takes a pending event chain c and an event e. It adds the event e to the chain in chronological order, based on the event's time value. It returns the updated pending event chain.

        3. delE(c): This function takes a pending event chain c and removes the first event from the chain. If the chain is empty, it prints an error message.

        4. nextE(c): This function takes a pending event chain c and returns the first event in the chain. If the chain is empty, it prints an error message.

        5. showE(c): This function takes a pending event chain c and prints the time and kind of each event in the chain.

    These modules are used in the main simulation to track the state and actions of the bacteria populations, making it easier to monitor and visualize the progression of the simulation.