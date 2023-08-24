# The problem can be solved using Breadth First Search (BFS) algorithm.

def elevator_button_pushes(f, s, g, u, d):
    # Initialize a list to keep track of the visited floors
    visited = [False] * (f + 1)
    # Initialize a list to keep track of the number of button pushes for each floor
    button_pushes = [-1] * (f + 1)

    # Initialize the starting floor with 0 button pushes
    button_pushes[s] = 0

    # Create a queue for BFS
    queue = []
    # Enqueue the starting floor
    queue.append(s)
    visited[s] = True

    # BFS
    while queue:
        # Dequeue a floor from the queue
        current_floor = queue.pop(0)

        # Check if the current floor is the goal floor
        if current_floor == g:
            return button_pushes[current_floor]

        # Calculate the next floors (up and down)
        next_up_floor = current_floor + u
        next_down_floor = current_floor - d

        # Check if the next up floor is within the building and not yet visited
        if next_up_floor <= f and not visited[next_up_floor]:
            # Set the number of button pushes for the next floor
            button_pushes[next_up_floor] = button_pushes[current_floor] + 1
            # Enqueue the next up floor
            queue.append(next_up_floor)
            visited[next_up_floor] = True

        # Check if the next down floor is within the building and not yet visited
        if next_down_floor >= 1 and not visited[next_down_floor]:
            # Set the number of button pushes for the next floor
            button_pushes[next_down_floor] = button_pushes[current_floor] + 1
            # Enqueue the next down floor
            queue.append(next_down_floor)
            visited[next_down_floor] = True

    # If the goal floor is not reachable, return "use the stairs"
    return "use the stairs"

# Read input from standard input
f, s, g, u, d = map(int, input().split())
# Call the function and print the result
print(elevator_button_pushes(f, s, g, u, d))