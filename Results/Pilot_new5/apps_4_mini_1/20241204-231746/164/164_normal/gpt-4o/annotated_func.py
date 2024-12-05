#State of the program right berfore the function call: n is an integer such that 2 ≤ n ≤ 100, k is an integer such that 1 ≤ k ≤ n - 1, and the input string of length n consists of characters '.', '#', 'G', and 'T', where 'G' and 'T' appear exactly once.
def func():
    n, k = map(int, input().split())
    line = input()
    G_pos = line.index('G')
    T_pos = line.index('T')
    if (G_pos > T_pos) :
        G_pos, T_pos = T_pos, G_pos
    #State of the program after the if block has been executed: *`n` is an integer such that 2 ≤ n ≤ 100, `k` is an integer such that 1 ≤ k ≤ n - 1, `line` is an input string. If `G_pos` is greater than `T_pos`, then `G_pos` is now equal to the previous value of `T_pos`, and `T_pos` is now equal to the previous value of `G_pos`.
    reachable = False
    for pos in range(G_pos, T_pos + 1, k):
        if line[pos] == '#':
            break
        
        if pos == T_pos:
            reachable = True
            break
        
    #State of the program after the  for loop has been executed: `n` is an integer such that 2 ≤ `n` ≤ 100, `k` is an integer such that 1 ≤ `k` ≤ `n - 1`, `line` is an input string, `G_pos` is less than or equal to `T_pos`, `reachable` is True if `pos` equals `T_pos` after the last iteration, and `pos` is equal to `T_pos` if the loop completes without encountering '#', otherwise `pos` will be the first index in `line` that contains '#' after `G_pos`. If the loop does not execute, `pos` remains equal to `G_pos`, and `reachable` remains False.
    if reachable :
        print('YES')
    else :
        print('NO')
    #State of the program after the if-else block has been executed: *`n` is an integer such that 2 ≤ `n` ≤ 100, `k` is an integer such that 1 ≤ `k` ≤ `n - 1`, `line` is an input string, and `G_pos` is less than or equal to `T_pos`. If `reachable` is True, then `pos` equals `T_pos` after the last iteration, indicating the loop completed without encountering '#', and 'YES' has been printed. If the loop does not execute, `pos` remains equal to `G_pos`, and `reachable` is False. Conversely, if `reachable` is False, then `pos` is equal to `G_pos` if the loop does not execute, and if it does execute, `pos` will be the first index in `line` that contains '#' after `G_pos`, with the output being 'NO'.
#Overall this is what the function does:The function accepts no parameters and reads an integer `n` (length of the string) and an integer `k` (step size) from input, followed by a string of length `n` containing characters '.', '#', 'G', and 'T'. It determines if the character 'G' can reach 'T' by moving in steps of `k` without encountering a '#' character in between. If 'G' can reach 'T', it prints 'YES'; otherwise, it prints 'NO'. The function assumes that 'G' and 'T' appear exactly once in the string.

