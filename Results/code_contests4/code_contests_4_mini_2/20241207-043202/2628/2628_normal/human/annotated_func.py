#State of the program right berfore the function call: n and m are integers such that 1 ≤ n, m ≤ 12; the first participant communicates n distinct pairs of integers from 1 to 9, and the second participant communicates m distinct pairs of integers from 1 to 9, with each pair containing two different numbers.
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
        
    #State of the program after the  for loop has been executed: `n` is greater than or equal to 0, `i` is `n`, `m` is greater than or equal to 0, `A[i][0]` is the count of how many times the conditions were satisfied for each `i` from 0 to `n-1`, `A[i][1]` reflects the last assigned value based on the conditions met during the loop for each corresponding `i`, and if no conditions are met for any `i`, `A[i][0]` remains 0 and `A[i][1]` retains its initial value of 0.
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
        
    #State of the program after the  for loop has been executed: `n` is greater than or equal to 0, `i` is equal to `m`, `m` is greater than or equal to 0, `B[i][0]` is the count of valid matches found for each `i` from 0 to `m-1`, `B[i][1]` is the last valid value assigned from `x1` or `y1` for each `i`, or remains unchanged if no valid matches were found. If `m` is 0, then `B[i][0]` remains 0 and `B[i][1]` retains its initial value of 0 for all `i`.
    if (sum(A[i][0] for i in range(n)) == 1 or sum(B[i][0] for i in range(m)) == 1) :
        for Ai in A:
            if Ai[0] == 1:
                ans = Ai[1]
            
        #State of the program after the  for loop has been executed: `n` is greater than or equal to 0, `i` is equal to `m + len(A)`, `m` is greater than or equal to 0, `A` is a list with at least 0 elements, and `ans` is the second element of the last `Ai` in `A` where `Ai[0]` equals 1, or remains unchanged if no `Ai` satisfies the condition.
        for Bi in B:
            if Bi[0] == 1:
                ans = Bi[1]
            
        #State of the program after the  for loop has been executed: `n` is greater than or equal to 0, `i` is equal to `m + len(A)`, `m` is greater than or equal to 0, `A` is a list with at least 0 elements, `ans` is the second element of the last `Bi` in `B` where `Bi[0]` equals 1, or remains unchanged if no `Bi` satisfies the condition, and `B` is a list with at least 0 elements.
        print(ans)
    else :
        print(0)
    #State of the program after the if-else block has been executed: *`n` is greater than or equal to 0, `i` is equal to `m + len(A)` if the sum of the first elements of `A` over the range `n` equals 1 or the sum of the first elements of `B` over the range `m` equals 1, in which case `ans` becomes the second element of the last `Bi` in `B` where `Bi[0]` equals 1, or remains unchanged if no such `Bi` satisfies the condition. If neither sum equals 1, then `n` is greater than or equal to 0, `i` is equal to `m`, `B[i][0]` remains the count of valid matches found for each `i` from 0 to `m-1`, `B[i][1]` is the last valid value assigned from `x1` or `y1`, or remains unchanged if no valid matches were found, and the value `0` has been printed.
#Overall this is what the function does:The function accepts two integers, `n` and `m`, representing the number of distinct pairs communicated by two participants. It processes these pairs and counts matches based on specific conditions. If exactly one match is found among the pairs, it prints the corresponding number from the match; otherwise, it prints 0. If any conflicting conditions are detected during the matching process, the function exits with -1. The function does not handle cases where `n` or `m` is zero, which could potentially lead to unhandled edge cases.

