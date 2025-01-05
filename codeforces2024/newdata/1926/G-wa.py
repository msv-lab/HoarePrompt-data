def min_thick_walls(n, edges, student_types):
    # Create an adjacency list to represent the tree
    tree = [[] for _ in range(n)]
    for i, a in enumerate(edges, start=2):
        tree[i-1].append(a-1)
        tree[a-1].append(i-1)
    
    # Function to traverse the tree and count the minimum number of thick walls
    def traverse(node, parent):
        partying_neighbors = 0
        for neighbor in tree[node]:
            if neighbor != parent:
                partying_neighbors += traverse(neighbor, node)
        if student_types[node] == 'P':
            return partying_neighbors + 1
        elif student_types[node] == 'S':
            return max(0, partying_neighbors - 1)
        else:
            return partying_neighbors
    
    # Start the traversal from the root (assuming node 0 is the root)
    return traverse(0, -1)

# Main function to handle multiple test cases
def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        edges = list(map(int, input().split()))
        student_types = input().strip()
        result = min_thick_walls(n, edges, student_types)
        print(result)

if __name__ == "__main__":
    main()