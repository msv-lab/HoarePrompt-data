#State of the program right berfore the function call: n is an integer (2 ≤ n ≤ 100) representing the number of cells, k is an integer (1 ≤ k ≤ n - 1) representing the length of one grasshopper's jump, and a string of length n contains the characters '.', '#', 'G', and 'T' where 'G' is the grasshopper's starting position, 'T' is the target position, '.' represents empty cells, and '#' represents obstacles. It is guaranteed that 'G' and 'T' appear exactly once in the string.
def func():
    n, k = map(int, input().split())
    line = input()
    G_pos = line.index('G')
    T_pos = line.index('T')
    if (G_pos > T_pos) :
        G_pos, T_pos = T_pos, G_pos
    #State of the program after the if block has been executed: *`n` is an integer (2 ≤ n ≤ 100), `k` is an integer (1 ≤ k ≤ n - 1), `line` is a string obtained from input, `G_pos` and `T_pos` are indices of 'G' and 'T' in `line` respectively. If `G_pos` is greater than `T_pos`, `G_pos` is now assigned the previous value of `T_pos`, and `T_pos` is now assigned the previous value of `G_pos`.
    reachable = False
    for pos in range(G_pos, T_pos + 1, k):
        if line[pos] == '#':
            break
        
        if pos == T_pos:
            reachable = True
            break
        
    #State of the program after the  for loop has been executed: `n` is an integer (2 ≤ n ≤ 100), `k` is an integer (1 ≤ k ≤ n - 1), `line` is a string, `G_pos` is less than or equal to `T_pos`, `reachable` is True if `pos` equals `T_pos` after the loop finishes, `pos` is the last position reached in the loop, which must be between `G_pos` and `T_pos`, inclusive. If the loop does not execute, `reachable` is False and `pos` is not defined.
    if reachable :
        print('YES')
    else :
        print('NO')
    #State of the program after the if-else block has been executed: *`n` is an integer (2 ≤ n ≤ 100), `k` is an integer (1 ≤ k ≤ n - 1), `line` is a string, `G_pos` is less than or equal to `T_pos`. If `reachable` is True, then `pos` is the last position reached in the loop, which is between `G_pos` and `T_pos` inclusive, and 'YES' has been printed. Otherwise, if `reachable` is False, `pos` is not defined, and 'NO' has been printed.
#Overall this is what the function does:The function accepts an integer `n` (the number of cells), an integer `k` (the length of the grasshopper's jump), and a string `line` containing the characters '.', '#', 'G', and 'T'. It checks if the grasshopper can reach the target 'T' from its starting position 'G' by jumping exactly `k` cells at a time without landing on any obstacles (`'#'`). It prints 'YES' if the target is reachable and 'NO' otherwise. The code does not handle cases where the grasshopper might overshoot the target if `k` is larger than the distance to the target, nor does it validate the input parameters beyond guaranteed constraints.

