# The main path planning function. Additional functions, classes,
# variables, libraries, etc. can be added to the file, but this
# function must always be defined with these arguments and must
# return an array ('list') of coordinates (col,row).
#DO NOT EDIT THIS FUNCTION DECLARATION
def do_a_star(grid, start, end, display_message):
    #EDIT ANYTHING BELOW HERE

    # Get the size of grid
    COL = len(grid)  # Number of columns (height of the grid)
    ROW = len(grid[0])  # Number of rows (width of the grid)

    # Define movement directions: Up, Down, Left, Right
    # (row_offset, col_offset) represents the movement in the grid
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    # A* uses a priority queue, but instead of heapq, we use a sorted list
    open_set = [(0, start)]  # (f(n), (col, row))

    # Dictionary to store the cost from the start node to each explored node
    g_cost = {start: 0}

    # Dictionary to track the path by storing the previous node for each node
    came_from = {}

    # Heuristic function (h(n)) using Euclidean distance
    def heuristic(a, b):
        return ((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2) ** 0.5

    # Start the A* search
    while open_set:
        # Sort the open_set manually based on f(n) value and get the lowest one
        open_set.sort()
        _, current = open_set.pop(0)  # Extract the node with the lowest f(n) value

        # If we reach the goal, reconstruct and return the path
        if current == end:
            path = []
            while current in came_from:
                path.append(current)  # Add the current node to the path
                current = came_from[current]  # Move to the previous node
            path.append(start)  # Add the start node
            path.reverse()  # Reverse the path to get it in the correct order
            display_message("Path found successfully!")  # Display success message
            display_message("Start location is " + str(start))
            return path  # Return the computed path

        # Explore the neighboring nodes
        for d in directions:
            # Compute the new neighbor's coordinates
            neighbor = (current[0] + d[0], current[1] + d[1])

            # Check if the neighbor is within the grid and is a valid walkable cell (grid[neighbor] == 1)
            if 0 <= neighbor[0] < COL and 0 <= neighbor[1] < ROW and grid[neighbor[0]][neighbor[1]] == 1:
                # Compute the tentative g(n) cost (assuming each move has a cost of 1)
                tentative_g_cost = g_cost[current] + 1

                # If the neighbor is not yet explored or a better path is found, update values
                if neighbor not in g_cost or tentative_g_cost < g_cost[neighbor]:
                    g_cost[neighbor] = tentative_g_cost  # Update g(n) value
                    f_cost = tentative_g_cost + heuristic(neighbor, end)  # Compute f(n) = g(n) + h(n)
                    open_set.append((f_cost, neighbor))  # Add the neighbor to the priority queue
                    came_from[neighbor] = current  # Record the previous node for path reconstruction

    # If no path is found, return an empty list
    display_message("No valid path found!")  # Display failure message
    return []  # Return an empty list indicating no path is available


#end of file