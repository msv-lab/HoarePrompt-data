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
        
    #State of the program after the  for loop has been executed: `total_leaves` is 2, `visited_count` is `h`, `path` is the empty string, `current_level` is `h-1`, `current_node` is `2
    print(visited_count)
#Overall this is what the function does:The function reads two integers \( h \) and \( n \) from standard input, where \( 1 \leq h \leq 50 \) and \( 1 \leq n \leq 2^h \). It then converts \( n \) into its binary representation (excluding the leading '1') and traverses a binary tree of height \( h \) according to the binary digits of \( n \). For each binary digit, it simulates moving left (if the digit is '0') or right (if the digit is '1') in the tree. The function counts the number of nodes visited during this traversal. After completing the traversal, it prints the count of visited nodes.

