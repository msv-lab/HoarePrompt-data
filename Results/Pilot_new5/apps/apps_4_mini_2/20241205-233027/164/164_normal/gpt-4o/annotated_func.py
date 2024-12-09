#State of the program right berfore the function call: n is an integer (2 ≤ n ≤ 100), k is an integer (1 ≤ k ≤ n - 1), and the input string representing the cells has a length of n, containing exactly one 'G' and one 'T', with '.' for empty cells and '#' for obstacles.
def func():
    n, k = map(int, input().split())
    line = input()
    G_pos = line.index('G')
    T_pos = line.index('T')
    if (G_pos > T_pos) :
        G_pos, T_pos = T_pos, G_pos
    #State of the program after the if block has been executed: *`n` is an integer (2 ≤ n ≤ 100), `k` is an integer (1 ≤ k ≤ n - 1), `line` is an input string representing the cells, `G_pos` is the index of 'G' in `line`, and `T_pos` is the index of 'T' in `line`. If `G_pos` is greater than `T_pos`, then `G_pos` is updated to the previous value of `T_pos`, and `T_pos` is updated to the previous value of `G_pos`.
    reachable = False
    for pos in range(G_pos, T_pos + 1, k):
        if line[pos] == '#':
            break
        
        if pos == T_pos:
            reachable = True
            break
        
    #State of the program after the  for loop has been executed: `n` is an integer (2 ≤ n ≤ 100), `k` is an integer (1 ≤ k ≤ n - 1), `line` is an input string representing the cells, `G_pos` is less than or equal to `T_pos`, `pos` is equal to the position reached by advancing from `G_pos` in increments of `k` until `T_pos` or a '#' is encountered, and `reachable` is True if `pos` is equal to `T_pos`, otherwise `reachable` is False.
    if reachable :
        print('YES')
    else :
        print('NO')
    #State of the program after the if-else block has been executed: *`n` is an integer (2 ≤ n ≤ 100), `k` is an integer (1 ≤ k ≤ n - 1), `line` is an input string representing the cells, `G_pos` is less than or equal to `T_pos`, `pos` is equal to the position reached by advancing from `G_pos` in increments of `k` until `T_pos` or a '#' is encountered. If `reachable` is True, then `pos` is equal to `T_pos`, and 'YES' has been printed. If `reachable` is False, then `pos` is not equal to `T_pos`, and 'NO' has been printed.
#Overall this is what the function does:The function accepts two integers, `n` (the length of the cells string, where 2 ≤ n ≤ 100) and `k` (the maximum jump length, where 1 ≤ k ≤ n - 1), followed by a string representing cells containing one 'G', one 'T', obstacles '#', and empty cells '.'. It checks if it is possible to reach 'T' from 'G' using jumps of length `k`. The function will print "YES" if 'T' is reachable from 'G' without hitting an obstacle, otherwise it prints "NO". The code assumes valid input constraints are met without additional error handling for invalid inputs.

