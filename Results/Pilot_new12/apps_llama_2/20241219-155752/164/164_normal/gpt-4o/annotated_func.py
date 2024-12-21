#State of the program right berfore the function call: n is an integer between 2 and 100 (inclusive), k is an integer between 1 and n - 1 (inclusive), the input string has a length of n and consists only of the characters '.', '#', 'G', and 'T', and the characters 'G' and 'T' each appear exactly once in the string.
def func():
    n, k = map(int, input().split())
    line = input()
    G_pos = line.index('G')
    T_pos = line.index('T')
    if (G_pos > T_pos) :
        G_pos, T_pos = T_pos, G_pos
    #State of the program after the if block has been executed: `n` is `input_n`, `k` is `input_k`, `line` is the input string of length `n` consisting only of '.', '#', 'G', and 'T' with 'G' and 'T' each appearing exactly once. If initially `G_pos` is greater than `T_pos`, then `G_pos` is updated to the initial value of `T_pos` and `T_pos` is updated to the initial value of `G_pos`, resulting in `G_pos` being less than `T_pos`. If initially `G_pos` is not greater than `T_pos`, then `G_pos` and `T_pos` remain unchanged, with `G_pos` being less than or equal to `T_pos`.
    reachable = False
    for pos in range(G_pos, T_pos + 1, k):
        if line[pos] == '#':
            break
        
        if pos == T_pos:
            reachable = True
            break
        
    #State of the program after the  for loop has been executed: `n` is `input_n`, `k` is `input_k` and is greater than 0, `line` is the input string of length `n` consisting only of '.', '#', 'G', and 'T' with 'G' and 'T' each appearing exactly once, `G_pos` is less than or equal to `T_pos`, `reachable` is `True` if there is a path from `G_pos` to `T_pos` with a step of `k` without encountering a '#', and `False` otherwise.
    if reachable :
        print('YES')
    else :
        print('NO')
    #State of the program after the if-else block has been executed: *`n` is `input_n`, `k` is `input_k` and is greater than 0, `line` is the input string of length `n` consisting only of '.', '#', 'G', and 'T' with 'G' and 'T' each appearing exactly once, `G_pos` is less than or equal to `T_pos`. If there is a path from `G_pos` to `T_pos` with a step of `k` without encountering a '#', then 'YES' has been printed. Otherwise, 'NO' has been printed.
#Overall this is what the function does:The function determines whether a path exists from the character 'G' to the character 'T' in the input string, moving in steps of `k`, without encountering a '#'. It takes an integer `n` between 2 and 100 (inclusive), an integer `k` between 1 and `n-1` (inclusive), and an input string of length `n` consisting only of the characters '.', '#', 'G', and 'T', with 'G' and 'T' each appearing exactly once. The function returns 'YES' if such a path exists and 'NO' otherwise, after checking all possible positions in the range from the index of 'G' to the index of 'T' with a step of `k`. The function handles cases where the initial position of 'G' is greater than the position of 'T' by swapping their indices, ensuring that 'G' is always to the left of 'T' before the path search. The function correctly handles edge cases, including when 'G' and 'T' are at adjacent positions or when there are '#' characters blocking the path.

