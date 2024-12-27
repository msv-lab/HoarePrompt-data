#State of the program right berfore the function call: The input consists of two integers h and n, where h is the height of a perfect binary tree and n is a leaf node, such that 1 ≤ h ≤ 50 and 1 ≤ n ≤ 2^h.
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
        
    #State of the program after the  for loop has been executed: `h` is an integer between 1 and 50, `n` is an integer between 1 and 2^`h`, `total_leaves` is 2^`h`, `visited_count` is `h`, `path` is a string of length `h` derived from `bin(n - 1)[2:].zfill(h)`, `current_level` is 0, and `current_node` is determined by the binary path in `path`, starting from 0 and updating based on '0' or '1' directions.
    print(visited_count)
#Overall this is what the function does:The function calculates and prints the number of nodes visited from the root to a given leaf node in a perfect binary tree of height `h`. It takes two integers `h` and `n` as input, where `h` is the height of the perfect binary tree and `n` is a leaf node, such that `1 ≤ h ≤ 50` and `1 ≤ n ≤ 2^h`. The function returns the total number of nodes visited, which is equivalent to the height of the tree, and this count is printed as output. The function assumes that the tree is a perfect binary tree, meaning every level is fully filled, except possibly the last level, which is filled from left to right. The state of the program after execution includes the input variables `h` and `n`, and the calculated `visited_count` which is the height of the tree `h`. The function does not perform any error checking or handling for invalid inputs, edge cases such as `h` or `n` being outside the specified range, or handling for non-perfect binary trees.

