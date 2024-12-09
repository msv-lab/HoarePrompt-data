#State of the program right berfore the function call: h is an integer satisfying 1 ≤ h ≤ 50, and n is an integer satisfying 1 ≤ n ≤ 2^h.
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
        
    #State of the program after the  for loop has been executed: `h` is an integer satisfying 1 ≤ `h` ≤ 50; `n` is an integer satisfying 1 ≤ `n` ≤ 2^`h`; `total_leaves` is equal to 2^`h`; `visited_count` is equal to `h`; `path` is a binary string of length `h`; `current_level` is `h - 1`; `current_node` is determined by traversing the binary tree according to the `path`.
    print(visited_count)
#Overall this is what the function does:The function reads two integers `h` and `n` from input, where `h` is between 1 and 50, and `n` is between 1 and \(2^h\). It calculates the number of nodes visited in a binary tree traversal based on the binary representation of `n - 1`, which is padded to a length of `h`. It then prints the total count of visited nodes, which will always equal `h` after the traversal.

