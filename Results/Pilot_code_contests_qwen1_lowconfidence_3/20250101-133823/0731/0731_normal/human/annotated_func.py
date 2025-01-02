#State of the program right berfore the function call: H and W are integers such that 2 ≤ H, W ≤ 2 × 10^5, s_r and s_c are integers such that 1 ≤ s_r ≤ H and 1 ≤ s_c ≤ W, N is an integer such that 2 ≤ N ≤ 2 × 10^5, S and T are strings consisting of the characters 'L', 'R', 'U', and 'D' such that |S| = |T| = N.
def func():
    H, W, N = map(int, raw_input().split())
    sr, sc = map(int, raw_input().split())
    S = raw_input()
    T = raw_input()
    AO = [1, W, 1, H]
    flag = 0
    for i in reversed(range(N)):
        if i != N - 1:
            if T[i] == 'L':
                AO[1] = min(W, AO[1] + 1)
            elif T[i] == 'R':
                AO[0] = max(1, AO[0] - 1)
            elif T[i] == 'U':
                AO[3] = min(H, AO[3] + 1)
            elif T[i] == 'D':
                AO[2] = max(1, AO[2] - 1)
        
        if S[i] == 'L':
            AO[0] += 1
        elif S[i] == 'R':
            AO[1] -= 1
        elif S[i] == 'U':
            AO[2] += 1
        elif S[i] == 'D':
            AO[3] -= 1
        
        if AO[0] > AO[1] or AO[2] > AO[3]:
            flag = 1
            break
        
    #State of the program after the  for loop has been executed: `H` is as per the precondition, `W` is as per the precondition, `N` is as per the precondition, `sr` is as per the precondition, `sc` is as per the precondition, `S` is as per the precondition, `T` is as per the precondition, `flag` is 1 if the loop modifies `AO` such that `AO[0] > AO[1]` or `AO[2] > AO[3]` at any point, otherwise `flag` remains 0, `i` is 0, `AO[0]`, `AO[1]`, `AO[2]`, `AO[3]` are adjusted according to the instructions in the loop based on the characters in `S` and `T`.
    if (AO[0] > sc or AO[1] < sc or AO[2] > sr or AO[3] < sr) :
        flag = 1
    #State of the program after the if block has been executed: *`H` is as per the precondition, `W` is as per the precondition, `N` is as per the precondition, `sr` is as per the precondition, `sc` is as per the precondition, `S` is as per the precondition, `T` is as per the precondition, `flag` is 1, `i` is 0, `AO[0]`, `AO[1]`, `AO[2]`, `AO[3]` are adjusted according to the instructions in the loop based on the characters in `S` and `T`, and the condition `(AO[0] > sc or AO[1] < sc or AO[2] > sr or (AO[3] < sr))` is true.
    if (flag == 0) :
        print('YES')
    else :
        print('NO')
    #State of the program after the if-else block has been executed: *`H` is as per the precondition, `W` is as per the precondition, `N` is as per the precondition, `sr` is as per the precondition, `sc` is as per the precondition, `S` is as per the precondition, `T` is as per the precondition, `flag` is either 0 or 1 depending on the condition `(AO[0] > sc or AO[1] < sc or AO[2] > sr or (AO[3] < sr))`, `i` is 0, `AO[0]`, `AO[1]`, `AO[2]`, `AO[3]` are adjusted according to the instructions in the loop based on the characters in `S` and `T`, and the output is 'YES' if `flag` is 0 and 'NO' if `flag` is 1.
#Overall this is what the function does:The function `func()` accepts parameters `H`, `W`, `s_r`, `s_c`, `N`, `S`, and `T`, which represent the dimensions of a grid, starting coordinates, and two strings of moves. It processes these inputs to determine if a certain set of moves described by `S` and `T` can be performed without violating the grid boundaries. Specifically, the function checks if the sequence of moves in `S` and `T` keeps the player within the grid bounds defined by `H` and `W`. If the player stays within the grid throughout the moves, the function prints 'YES'; otherwise, it prints 'NO'. The function uses an auxiliary array `AO` to track the dynamic bounds of the grid during the process. If at any point the moves violate the grid boundaries, the function sets a flag to 1. The function handles edge cases where the dynamic bounds might become invalid due to overlapping moves in `S` and `T`.

