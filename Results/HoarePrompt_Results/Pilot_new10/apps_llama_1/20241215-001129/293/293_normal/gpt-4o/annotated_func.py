#State of the program right berfore the function call: the input consists of two integers h and n, where 1 ≤ h ≤ 50 and 1 ≤ n ≤ 2^h.
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
        
    #State of the program after the  for loop has been executed: `h` is an input integer, `n` is an input integer, `total_leaves` is equal to 2 raised to the power of `h`, if `h` is greater than 0, then `visited_count` equals `h`, `path` is a binary string representation of `n-1` with leading zeros to make its length `h`, `current_level` is 0, and `current_node` equals `2 * n - 1`, otherwise if `h` is 0, then `visited_count` equals 0, `current_node` equals 0 and the rest of the variables remain at their initial state.
    print(visited_count)
#Overall this is what the function does:The function reads two integers `h` and `n` from the standard input, traverses a binary tree of height `h` based on the binary representation of `n-1`, and prints the number of nodes visited, which is equal to `h`, assuming `h` and `n` satisfy the conditions `1 ≤ h ≤ 50` and `1 ≤ n ≤ 2^h`.

