#State of the program right berfore the function call: h is a positive integer such that 1 ≤ h ≤ 50, and n is an integer such that 1 ≤ n ≤ 2^h.
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
        
    #State of the program after the  for loop has been executed: `h` is an input integer such that 1 ≤ h ≤ 50, `n` is an input integer such that 1 ≤ n ≤ 2^h, `total_leaves` is 2, `visited_count` is `h`, `path` is a binary representation of `n - 1` padded to a length of `h`, `current_level` is `h - 1`, `current_node` is determined by navigating a binary tree according to `path`.
    print(visited_count)
#Overall this is what the function does:The function accepts no parameters, reads two integers from input, and prints the count of visited nodes in a binary tree based on the binary representation of `n - 1`, where the tree has a height of `h`.

