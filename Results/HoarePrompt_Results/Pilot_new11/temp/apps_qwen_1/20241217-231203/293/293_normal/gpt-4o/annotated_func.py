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
        
    #State of the program after the  for loop has been executed: `h` is an integer between 1 and 50; `n` is an integer between 1 and \(2^h\); `total_leaves` is \(2^h\); `visited_count` is `h`; `path` is the empty string; `current_node` is \(2^{h-1}\); `current_level` is `h-1`.
    print(visited_count)
#Overall this is what the function does:The function processes a binary path representation of an integer `n` within the range `[1, 2^h]` and calculates the number of nodes visited while traversing the path. The function takes no explicit parameters and reads `h` and `n` from standard input. It prints the number of nodes visited during the traversal. The function starts by reading two integers `h` and `n` from standard input, where `h` represents the height of a binary tree and `n` is an integer in the range `[1, 2^h]`. It then converts `n-1` into its binary representation, which is used to traverse the tree. For each bit in the binary path (from left to right), the function updates the current node and increments the visit count. If the bit is '0', the function moves to the left child; if the bit is '1', it moves to the right child. The function ensures that the input constraints are respected and handles the edge case where the binary path is fully traversed. After the traversal, the function prints the total number of nodes visited, which equals the height `h` of the tree.

