def main():
    import sys
    input = sys.stdin.read
    h, n = map(int, input().split())

    # Calculate the total number of leaf nodes
    total_leaves = 2 ** h

    # Track the number of visited nodes
    visited_count = 0

    # Binary representation of the path to the exit node
    path = bin(n - 1)[2:].zfill(h)

    current_level = 0
    current_node = 0  # Represent the root node

    # Simulate the traversal
    for direction in path:
        visited_count += 1
        if direction == '0':
            current_node = 2 * current_node + 1  # Move to the left child
        else:
            current_node = 2 * current_node + 2  # Move to the right child

    # Total nodes visited (excluding the exit node itself)
    print(visited_count)

if __name__ == "__main__":
    main()
