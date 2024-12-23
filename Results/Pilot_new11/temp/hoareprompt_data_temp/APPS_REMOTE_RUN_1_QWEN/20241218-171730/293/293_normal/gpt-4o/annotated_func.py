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
        
    #State of the program after the  for loop has been executed: `total_leaves` is 2, `visited_count` is `h`, `path` is the binary representation of `n - 1`, padded with leading zeros to a length of `h`, `current_level` is 0, and `current_node` is the final node reached after processing all bits in `path`.
    print(visited_count)
#Overall this is what the function does:The function reads two integers \( h \) and \( n \) from standard input, where \( 1 \leq h \leq 50 \) and \( 1 \leq n \leq 2^h \). It then calculates the binary representation of \( n-1 \), which is a string of \( h \) bits, and simulates moving through a binary tree of height \( h \) based on these bits. Specifically, for each bit in the binary representation, it moves to either the left child (if the bit is '0') or the right child (if the bit is '1'). The function prints the number of nodes visited during this traversal, which is equal to \( h \). The function does not return any value. There are no explicit edge cases mentioned in the code, but it correctly handles valid inputs within the specified range.

