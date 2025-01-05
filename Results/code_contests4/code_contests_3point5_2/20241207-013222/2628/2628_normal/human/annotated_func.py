#State of the program right berfore the function call: n and m are integers such that 1 ≤ n, m ≤ 12. The pairs of numbers communicated from participants are distinct and each pair consists of two different numbers from 1 to 9.**
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
        
    #State of the program after the  for loop has been executed: At the end of the loop, the values of the variables A, i, n, x1, y1, m, j, x2, and y2 will remain the same as their initial values. The loop does not execute, and the variables retain their initial values.
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
        
    #State of the program after the  for loop has been executed: At the end of the loop, the values of the variables A, i, n, x1, y1, m, j, x2, and y2 will remain unchanged. The values of B[i][0] and B[i][1] are modified based on the conditions within the loop. The loop will either print -1 and exit or increment B[i][0] and assign a new value to B[i][1].
    if (sum(A[i][0] for i in range(n)) == 1 or sum(B[i][0] for i in range(m)) == 1) :
        for Ai in A:
            if Ai[0] == 1:
                ans = Ai[1]
            
        #State of the program after the  for loop has been executed: At the end of the loop, the values of the variables A, i, n, x1, y1, m, j, x2, and y2 remain unchanged. The values of B[i][0] and B[i][1] are modified based on the conditions within the loop. If Ai[0] equals 1 for any Ai in A, then `ans` will be assigned the value of the first Ai[1] where Ai[0] is 1.
        for Bi in B:
            if Bi[0] == 1:
                ans = Bi[1]
            
        #State of the program after the  for loop has been executed: At the end of the loop, the values of A, i, n, x1, y1, m, j, x2, and y2 remain unchanged. If B is not empty and there exists an element in B where the first element is equal to 1, then `ans` will be assigned the value of the first element's second value where the first element is 1. If no such element exists in B, then `ans` will not be assigned a value.
        print(ans)
    else :
        print(0)
    #State of the program after the if-else block has been executed: *At the end of the loop, the values of the variables A, i, n, x1, y1, m, j, x2, and y2 remain unchanged. The values of B[i][0] and B[i][1] are modified based on the conditions within the loop. If the sum of A[i][0] for i in range(n) is equal to 1 or the sum of B[i][0] for i in range(m) is equal to 1, the value of `ans` will depend on the elements of list B. If neither condition is met, the loop will either print -1 and exit or increment B[i][0] and assign a new value to B[i][1].
#Overall this is what the function does:The function `func` reads pairs of numbers from participants, processes them according to specific constraints, and prints the result. It does not accept any parameters explicitly. The function checks if there is a unique number in each list of pairs. If there is a unique number in either list, it prints that number. If there is no unique number, it prints 0. The function exits with -1 if certain conditions are not met during processing.

