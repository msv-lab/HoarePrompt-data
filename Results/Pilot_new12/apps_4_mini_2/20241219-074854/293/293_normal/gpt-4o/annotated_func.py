#State of the program right berfore the function call: h is an integer such that 1 ≤ h ≤ 50, and n is an integer such that 1 ≤ n ≤ 2^{h}.
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
        
    #State of the program after the  for loop has been executed: `h` is an integer in the range from 1 to 50; `n` is an integer in the range from 1 to 2^h; `total_leaves` is equal to 2^h; `visited_count` is equal to `h`; `path` remains unchanged; `current_level` will be `h-1`; `current_node` is the node corresponding to the binary path derived from `n-1`.
    print(visited_count)
#Overall this is what the function does:The function reads two integers, `h` and `n`, from the standard input, where `h` is constrained between 1 and 50 and `n` between 1 and 2 raised to the power of `h`. It calculates the total number of leaves in a binary tree represented by `h`. The function then constructs a binary path corresponding to `n-1` and traverses this path in the binary tree, incrementing a count of visited nodes. Finally, it prints the total number of visited nodes, which equals `h`, indicating how many levels were traversed in the process. The function does not return a value nor use explicit parameters but relies on standard input for its operation.

