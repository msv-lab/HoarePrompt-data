#State of the program right berfore the function call: h and n are integers such that 1 ≤ h ≤ 50 and 1 ≤ n ≤ 2^h.
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
        
    #State of the program after the  for loop has been executed: `h` is an integer such that 1 ≤ `h` ≤ 50, `n` is an integer such that 1 ≤ `n` ≤ 2^`h`, `total_leaves` is 2, `visited_count` is `h`, `path` is a binary string of length `h`, `current_node` is determined by processing all directions in `path`.
    print(visited_count)
#Overall this is what the function does:The function reads two integers, `h` and `n`, from the input, where `h` determines the depth of a binary tree and `n` identifies a specific node within that tree. It calculates the path from the root to this node in the binary tree and counts the number of edges traversed (i.e., the levels visited). The function then prints the number of visited edges, which corresponds to the depth `h`, confirming that the function operates correctly for all valid values of `h` and `n` given the stated constraints.

