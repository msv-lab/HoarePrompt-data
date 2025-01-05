#State of the program right berfore the function call: **Precondition**: **n and m are integers such that 1 ≤ n, m ≤ 12. Each pair communicated is a set of two distinct integers between 1 and 9. Each set of pairs does not contain the same number twice, and there is exactly one number that is present in both sets.**
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
        
    #State of the program after the  for loop has been executed: All variables `x1`, `y1`, `a`, `i`, `n`, and `m` remain unchanged. The matrix `A` has been updated according to the conditions specified in the loop code for all elements. `B` remains unchanged throughout the loop.
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
        
    #State of the program after the  for loop has been executed: After the loop finishes executing, the values of variables `x1`, `y1`, `a`, `i`, `n`, `j`, `x2`, `y2`, `B[i][0]`, `B[i][1]` will be determined based on the conditions inside the loop. If the loop executes, the values will be updated accordingly. If the loop does not execute, all variables will remain the same as in the initial state.
    if (sum(A[i][0] for i in range(n)) == 1 or sum(B[i][0] for i in range(m)) == 1) :
        for Ai in A:
            if Ai[0] == 1:
                ans = Ai[1]
            
        #State of the program after the  for loop has been executed: If the sum of elements in A at index 0 for all i in the range of n is equal to 1, then `ans` will be assigned the value of the last element `A[i][1]` where `A` is a list of n elements. Otherwise, `ans` will remain unchanged. All other variables will remain the same as in the initial state.
        for Bi in B:
            if Bi[0] == 1:
                ans = Bi[1]
            
        #State of the program after the  for loop has been executed: `ans` may be assigned the value of the second element of the last list in `B` if the sum of elements in `A` at index 0 for all `i` in the range of `n` is equal to 1. Otherwise, `ans` will remain unchanged.
        print(ans)
    else :
        print(0)
    #State of the program after the if-else block has been executed: *After the execution of the if-else block, the values of variables `x1`, `y1`, `a`, `i`, `n`, `j`, `x2`, `y2`, `B[i][0]`, `B[i][1]`, and `ans` will be determined based on the conditions inside the loop. If either the sum of elements in column A is 1 or the sum of elements in column B is 1, `ans` remains unchanged. Otherwise, all variables will retain their initial values, and the program will print 0.
#Overall this is what the function does:Functionality: The function `func` reads input from the standard input and processes pairs of sets of two distinct integers between 1 and 9. Each pair has exactly one number that is common between them. The function then updates matrices A and B based on specific conditions. It checks if the sum of elements in column A or column B is 1, and assigns the common number to the variable `ans`. If the sum condition is met, it prints `ans`; otherwise, it prints 0. The function does not return any value, and it handles input processing and output based on the given constraints.

