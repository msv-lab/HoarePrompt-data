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
        
    #State of the program after the  for loop has been executed: `h` is between 1 and 50 inclusive, `n` is between 1 and 2^h inclusive, `total_leaves` is 2^h, `visited_count` is equal to the length of `path`, `path` is a binary string of length `h`, `current_node` is the value derived from traversing the binary tree according to the `path` string, which is a result of interpreting `path` as a series of left (0) and right (1) moves starting from the root node (0).
    print(visited_count)
#Overall this is what the function does:The function accepts two integers, `h` (between 1 and 50) and `n` (between 1 and 2^h), computes the binary representation of `n-1` as a path through a binary tree of height `h`, and counts the number of nodes visited along that path. It then prints the total number of visited nodes. The function does not handle any errors that could arise from invalid input, such as `n` being out of the specified range.

