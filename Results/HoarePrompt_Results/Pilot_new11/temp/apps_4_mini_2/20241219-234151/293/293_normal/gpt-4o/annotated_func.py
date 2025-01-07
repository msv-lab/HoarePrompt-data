#State of the program right berfore the function call: h is an integer between 1 and 50 inclusive, and n is an integer between 1 and 2^h inclusive.
def func_1():
    input = sys.stdin.read
    h, n = map(int, input().split())
    total_leaves = 2 ** h
    visited_count = 0
    path = bin(n - 1)[2:].zfill(h)
    current_level = 0
    current_node = 0
    for direction in path:
        visited_count += 1
        
        if direction == '0':
            current_node = 2 * current_node + 1
        else:
            current_node = 2 * current_node + 2
        
    #State of the program after the  for loop has been executed: `h` is between 1 and 50 inclusive; `n` is between 1 and `2^h`; `total_leaves` is 2; `visited_count` is equal to the length of `path`; `path` is a binary string of length `h` representing `n - 1`; `current_level` is 0; `current_node` is determined by the binary interpretation of `path` as a sequence of left (0) and right (1) moves from the root node, where `current_node` is within the range of 1 to `2^h - 1.
    print(visited_count)
#Overall this is what the function does:The function reads two integers, `h` and `n`, from standard input, where `h` represents the height of a binary tree (between 1 and 50) and `n` specifies a node within that tree (between 1 and `2^h`). It computes the binary path from the root to the `n-th` node in the tree, tracking how many nodes have been visited to reach that node. The function counts the number of visited nodes and prints this count. The final state includes `h` and `n` remaining unchanged, `total_leaves` set to `2^h`, `visited_count` reflecting the number of nodes traversed (equal to the length of the binary representation of `n-1`), and `current_node` representing the position of the node in the tree based on the provided path. However, the function does not return any values; it merely prints the visited count without handling any potential invalid inputs or edge cases that might arise from the input values.

