#State of the program right berfore the function call: n and m are integers such that 1 ≤ n, m ≤ 12, the first participant communicates n distinct pairs of integers between 1 and 9, and the second participant communicates m distinct pairs of integers between 1 and 9, with each pair containing two different integers.
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
        
    #State of the program after the  for loop has been executed: `n` is an integer between 1 and 12, `m` is an integer greater than or equal to 0, `A` is a list of length `n` where each element is a tuple containing two integers; the first integer is the count of successful matches found for each corresponding tuple in `a`, and the second integer is the last value assigned from either `x1` or `y1` based on the conditions met during the loop execution. If no conditions were met for any iteration for an index `i`, the first integer remains 0 and the second integer remains 0.
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
        
    #State of the program after the  for loop has been executed: `n` is an integer between 1 and 12, `m` is greater than or equal to 0, `B` is a list of length `m` where each element is a tuple containing two integers; the first integer is the count of successful matches found for each corresponding tuple in `b`, and the second integer is the last value assigned from either `x1` or `y1` based on the conditions met during the loop execution.
    if (sum(A[i][0] for i in range(n)) == 1 or sum(B[i][0] for i in range(m)) == 1) :
        for Ai in A:
            if Ai[0] == 1:
                ans = Ai[1]
            
        #State of the program after the  for loop has been executed: `n` is an integer between 1 and 12, `m` is greater than or equal to 0, `A` is a list with at least one element, and `ans` is either the second element of the first tuple in `A` where the first element is 1, or remains undefined if no such tuple exists.
        for Bi in B:
            if Bi[0] == 1:
                ans = Bi[1]
            
        #State of the program after the  for loop has been executed: `n` is an integer between 1 and 12, `m` is greater than or equal to 0, `A` is a list with at least one element, `ans` is the second element of `Bi` for the last `Bi` in `B` where the first element is 1; otherwise, `ans` remains undefined. `B` is a list with at least 1 element.
        print(ans)
    else :
        print(0)
    #State of the program after the if-else block has been executed: *`n` is an integer between 1 and 12, `m` is greater than or equal to 0, and `B` is a list of length `m` where each element is a tuple containing two integers. If the sum of the first elements of all tuples in `A` or `B` equals 1, the value of `ans` is the second element of the last tuple in `B` where the first element is 1 is printed. Otherwise, the sum of the first elements of all tuples in `A` and `B` is not equal to 1, and the value 0 is printed.
#Overall this is what the function does:The function reads two integers `n` and `m`, which represent the number of distinct pairs of integers communicated by two participants. It processes these pairs to count successful matches based on specific conditions, returning the second integer of the last matched pair from the second participant if exactly one successful match is found in either participant's pairs; otherwise, it returns 0. If a conflict in matching occurs, it outputs -1 and exits the program. The function does not accept any parameters and operates solely based on input read from standard input.

