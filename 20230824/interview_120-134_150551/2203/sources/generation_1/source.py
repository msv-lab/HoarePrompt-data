def check_exit_node(h, q, questions):
    # Initialize the list to keep track of possible exit nodes
    possible_exit_nodes = list(range(2**h, 2**(h+1)))
    
    # Iterate through the given questions and answers
    for i, L, R, ans in questions:
        # Check if the answer is contradictory
        if ans == 0 and L <= possible_exit_nodes[0] and R >= possible_exit_nodes[-1]:
            return "Game cheated!"
        
        # Update the possible exit nodes based on the answer
        new_possible_exit_nodes = []
        for node in possible_exit_nodes:
            if (node >= L and node <= R and ans == 1) or (node < L or node > R and ans == 0):
                new_possible_exit_nodes.append(node)
        possible_exit_nodes = new_possible_exit_nodes
    
    # Check if the number of questions is sufficient to identify the exit node
    if len(possible_exit_nodes) == 1:
        return possible_exit_nodes[0]
    else:
        return "Data not sufficient!"

# Read inputs
h, q = map(int, input().split())
questions = []
for _ in range(q):
    i, L, R, ans = map(int, input().split())
    questions.append((i, L, R, ans))

# Call the function
result = check_exit_node(h, q, questions)

# Print the result
print(result)