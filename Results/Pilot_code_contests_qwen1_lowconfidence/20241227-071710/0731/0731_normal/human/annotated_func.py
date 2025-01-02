#State of the program right berfore the function call: H and W are integers such that 2 ≤ H, W ≤ 2 × 10^5, s_r and s_c are integers such that 1 ≤ s_r ≤ H and 1 ≤ s_c ≤ W, N is an integer such that 2 ≤ N ≤ 2 × 10^5, S and T are strings consisting of the four kinds of letters 'L', 'R', 'U', and 'D' such that |S| = |T| = N.
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
        
    #State of the program after the  for loop has been executed: 
    if (AO[0] > sc or AO[1] < sc or AO[2] > sr or AO[3] < sr) :
        flag = 1
    #State of the program after the if block has been executed: *`AO` is a list of four integers, where either the first element is greater than `sc` or the second element is less than `sc` or the third element is greater than `sr` or the fourth element is less than `sr`. In this case, `flag` is 1. There is no else part in the code, so if none of these conditions are met, `flag` remains unchanged.
    if (flag == 0) :
        print('YES')
    else :
        print('NO')
    #State of the program after the if-else block has been executed: *`AO` is a list of four integers, `sc` and `sr` are constants, and `flag` is an integer. If the list `AO` satisfies at least one of the following conditions: the first element is greater than `sc`, the second element is less than `sc`, the third element is greater than `sr`, or the fourth element is less than `sr`, then `flag` is 0 and the function prints 'YES'. Otherwise, `flag` is 1 and the function prints 'NO'.
#Overall this is what the function does:The function accepts parameters H, W, s_r, s_c, and N, along with two strings S and T. It calculates the final bounds defined by AO based on the movements specified in S and T. The function checks if these bounds can contain the starting point (s_r, s_c). If at any point during the calculation, the bounds become invalid (i.e., AO[0] > AO[1] or AO[2] > AO[3]), it sets flag to 1. After the loop, it checks if the starting point (s_r, s_c) lies outside the final bounds defined by AO. If the starting point is within the bounds, it prints 'YES'; otherwise, it prints 'NO'. This function essentially determines if the starting point can remain within the bounds defined by the movements in S and T without becoming invalid.

