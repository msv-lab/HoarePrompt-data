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
        
    #State of the program after the  for loop has been executed: `total_leaves` is \(2^h\), `visited_count` is `h`, `path` is an empty list, `current_level` is \(h-1\), and `current_node` is the node reached by traversing the path represented by `path`.
    print(visited_count)
#Overall this is what the function does:The function reads two integers `h` and `n` from standard input, constructs a binary path from `n-1`, traverses this path to determine the number of nodes visited, and prints the count of visited nodes. The function assumes valid inputs within the specified ranges (1 ≤ h ≤ 50 and 1 ≤ n ≤ 2^h) and does not handle out-of-range or invalid inputs.

