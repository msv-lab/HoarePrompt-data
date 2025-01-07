#State of the program right berfore the function call: n is an integer between 2 and 100, k is an integer between 1 and n-1, and the second input is a string of length n consisting of exactly one 'G' (grasshopper start position), one 'T' (insect position), empty cells represented by '.' and obstacles represented by '#'.
def func():
    n, k = map(int, input().split())
    line = input()
    G_pos = line.index('G')
    T_pos = line.index('T')
    if (G_pos > T_pos) :
        G_pos, T_pos = T_pos, G_pos
    #State of the program after the if block has been executed: *`n` is a user-defined integer between 2 and 100, `k` is a user-defined integer between 1 and `n-1`, `line` is a user-defined string input. If `G_pos` is greater than `T_pos`, then `G_pos` is updated to the previous value of `T_pos`, and `T_pos` is updated to the previous value of `G_pos`, resulting in the current value of `G_pos` being less than the current value of `T_pos`.
    reachable = False
    for pos in range(G_pos, T_pos + 1, k):
        if line[pos] == '#':
            break
        
        if pos == T_pos:
            reachable = True
            break
        
    #State of the program after the  for loop has been executed: `n` is a user-defined integer between 2 and 100, `k` is a user-defined integer between 1 and `n-1`, `line` is a user-defined string input, `G_pos` is less than or equal to `T_pos`, `reachable` is True if there was a path from `G_pos` to `T_pos` without encountering '#', and `pos` is equal to the last position checked in the range from `G_pos` to `T_pos` at the last step before the loop ended. If the loop did not execute, `pos` would remain equal to `G_pos` and `reachable` would remain False.
    if reachable :
        print('YES')
    else :
        print('NO')
    #State of the program after the if-else block has been executed: *`n` is a user-defined integer between 2 and 100, `k` is a user-defined integer between 1 and `n-1`, `line` is a user-defined string input, `G_pos` is less than or equal to `T_pos`. If `reachable` is True, then there exists a path from `G_pos` to `T_pos` without encountering '#', `pos` is equal to the last position checked in the range from `G_pos` to `T_pos` at the last step before the loop ended, and 'YES' has been printed. Otherwise, if `reachable` is False, `pos` is equal to `G_pos` and 'NO' has been printed.
#Overall this is what the function does:The function accepts two integers `n` (between 2 and 100) and `k` (between 1 and `n-1`), along with a string of length `n` that contains exactly one 'G' (the grasshopper's starting position), one 'T' (the insect's position), empty cells represented by '.', and obstacles represented by '#'. It checks if the grasshopper can reach the insect by jumping `k` positions at a time without encountering any obstacles ('#'). If a path exists, it prints 'YES'; otherwise, it prints 'NO'. The function does not handle cases where `G` and `T` are not present in the input string, as it assumes valid input based on the problem description.

