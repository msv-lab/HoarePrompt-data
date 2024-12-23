#State of the program right berfore the function call: n is an integer such that 2 ≤ n ≤ 100, k is an integer such that 1 ≤ k ≤ n - 1, and the second input line is a string of length n consisting of the characters '.', '#', 'G', and 'T' where 'G' and 'T' appear exactly once.
def func():
    n, k = map(int, input().split())
    line = input()
    G_pos = line.index('G')
    T_pos = line.index('T')
    if (G_pos > T_pos) :
        G_pos, T_pos = T_pos, G_pos
    #State of the program after the if block has been executed: *`n` is an integer such that 2 ≤ `n` ≤ 100; `k` is an integer such that 1 ≤ `k` ≤ `n - 1`; `line` is a string of length `n` containing '.', '#', 'G', and 'T'; if `G_pos` is greater than `T_pos`, then `G_pos` is updated to the previous value of `T_pos`, and `T_pos` is updated to the previous value of `G_pos`, resulting in `G_pos` being less than `T_pos`.
    reachable = False
    for pos in range(G_pos, T_pos + 1, k):
        if line[pos] == '#':
            break
        
        if pos == T_pos:
            reachable = True
            break
        
    #State of the program after the  for loop has been executed: `n` is an integer such that 2 ≤ `n` ≤ 100; `k` is an integer such that 1 ≤ `k` ≤ `n - 1;` `line` is a string of length `n` containing '.', '#', 'G', and 'T'; `G_pos` is the position of 'G'; `T_pos` is the position of 'T'; if `G_pos` can reach `T_pos` without hitting a '#', then `reachable` is True; otherwise, `reachable` is False.
    if reachable :
        print('YES')
    else :
        print('NO')
    #State of the program after the if-else block has been executed: *`n` is an integer such that 2 ≤ `n` ≤ 100; `k` is an integer such that 1 ≤ `k` ≤ `n - 1;` `line` is a string of length `n` containing '.', '#', 'G', and 'T'; `G_pos` is the position of 'G'; `T_pos` is the position of 'T'; if `reachable` is True, then 'YES' is printed, indicating that `G_pos` can reach `T_pos` without hitting a '#'. If `reachable` is False, then 'NO' is printed, indicating that `G_pos` cannot reach `T_pos` without hitting a '#'.
#Overall this is what the function does:The function accepts two integers, `n` (the length of a string) and `k` (the step size), along with a string `line` of length `n` containing the characters '.', '#', 'G', and 'T', where 'G' and 'T' appear exactly once. The function determines whether the character 'G' can reach the character 'T' by making steps of size `k` without encountering the character '#'. If 'G' can reach 'T' without hitting '#', the function prints 'YES'; otherwise, it prints 'NO'. The function handles cases where 'G' and 'T' may be in reversed order, ensuring correct evaluation regardless of their positions. It does not account for input validation beyond the initial assumptions about bounds on `n` and `k`, nor does it check for the presence of exactly one 'G' and one 'T' in the string.

