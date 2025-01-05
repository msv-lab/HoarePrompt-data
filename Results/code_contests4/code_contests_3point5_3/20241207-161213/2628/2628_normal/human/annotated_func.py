#State of the program right berfore the function call: **Precondition**: **n and m are integers such that 1 <= n, m <= 12. The pairs of numbers communicated from each participant are distinct and each pair consists of two different numbers. The two sets of pairs do not contradict the statements, and there is a pair from the first set and a pair from the second set that share exactly one number.**
def func():
    n, m = list(map(int, sys.stdin.readline().strip().split(' ')))
    a = list(map(int, sys.stdin.readline().strip().split(' ')))
    b = list(map(int, sys.stdin.readline().strip().split(' ')))
    a = [(a[i * 2], a[i * 2 + 1]) for i in range(n)]
    b = [(b[i * 2], b[i * 2 + 1]) for i in range(m)]
    A = [[0, 0] for i in range(n)]
    B = [[0, 0] for i in range(m)]
    for i in range(n):
        x1, y1 = a[i]
        
        for j in range(m):
            x2, y2 = b[j]
            if set(a[i]) != set(b[j]):
                if x1 == x2 or x1 == y2:
                    if A[i][1] != 0 and A[i][1] != x1:
                        print(-1)
                        exit()
                    else:
                        A[i][0] += 1
                        A[i][1] = x1
                elif y1 == x2 or y1 == y2:
                    if A[i][1] != 0 and A[i][1] != y1:
                        print(-1)
                        exit()
                    else:
                        A[i][0] += 1
                        A[i][1] = y1
        
    #State of the program after the  for loop has been executed: At the end of the loop, the variables `i`, `j`, `x1`, `y1`, `m`, `A[i][0]`, `A[i][1]`, `x2`, `y2` will have been adjusted based on the loop execution. The final values will depend on the specific conditions met during the loop iterations, such as the comparison of sets `a[i]` and `b[j]`, and the relationships between `x1`, `x2`, `y1`, and `y2` in each iteration. If certain conditions are met, `A[i][0]` will be incremented by 1 and `A[i][1]` will be assigned specific values. If the program exits prematurely due to specific conditions, then the final values of the variables will reflect that. If the loop does not execute at all, all variables retain their initial values.
    for i in range(m):
        x1, y1 = b[i]
        
        for j in range(n):
            x2, y2 = a[j]
            if set(b[i]) != set(a[j]):
                if x1 == x2 or x1 == y2:
                    if B[i][1] != 0 and B[i][1] != x1:
                        print(-1)
                        exit()
                    else:
                        B[i][0] += 1
                        B[i][1] = x1
                elif y1 == x2 or y1 == y2:
                    if B[i][1] != 0 and B[i][1] != y1:
                        print(-1)
                        exit()
                    else:
                        B[i][0] += 1
                        B[i][1] = y1
        
    #State of the program after the  for loop has been executed: At the end of the loop, the variables `i`, `j`, `x1`, `y1`, `m`, `A[i][0]`, `A[i][1]`, `x2`, `y2`, and `B[i]` will be adjusted based on the loop execution. If the loop does not execute, the variables will remain the same as the initial state.
    if (sum(A[i][0] for i in range(n)) == 1 or sum(B[i][0] for i in range(m)) == 1) :
        for Ai in A:
            if Ai[0] == 1:
                ans = Ai[1]
            
        #State of the program after the  for loop has been executed: If A is not empty and the sum of the first elements of all A arrays is equal to 1, then `ans` will be assigned the value of the last Ai[1] where Ai[0] is equal to 1. If the loop does not execute, the variables will remain the same as the initial state.
        for Bi in B:
            if Bi[0] == 1:
                ans = Bi[1]
            
        #State of the program after the  for loop has been executed: If A is not empty and the sum of the first elements of all A arrays is equal to 1, then `ans` is assigned the value of the last Ai[1] where Ai[0] is equal to 1. If the loop does not execute, `ans` remains the same as the initial state.
        print(ans)
    else :
        print(0)
    #State of the program after the if-else block has been executed: *At the end of the loop, the variables `i`, `j`, `x1`, `y1`, `m`, `A[i][0]`, `A[i][1]`, `x2`, `y2`, and `B[i]` will be adjusted based on the loop execution. If the loop does not execute, the variables will remain the same as the initial state. If sum((A[i][0] for i in range(n))) == 1 or sum((B[i][0] for i in range(m))) == 1, then `ans` value will be the last `A[i][1]` where `A[i][0]` is equal to 1. Otherwise, `ans` will remain the same as the initial state. If the condition is not met, the sum of `A[i][0]` for all `i` in range `n` will still not be equal to 1 and the sum of `B[i][0]` for all `i` in range `m` will still not be equal to 1.
#Overall this is what the function does:The function reads pairs of numbers from two sets of pairs communicated by participants. It then processes these pairs according to given constraints to determine if there is a pair from the first set and a pair from the second set that share exactly one number. The function prints the shared number if such a pair exists, otherwise, it prints 0.

