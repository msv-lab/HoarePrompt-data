#State of the program right berfore the function call: n and m are integers such that 1 ≤ n, m ≤ 12; the first set consists of n pairs of distinct integers in the range from 1 to 9; the second set consists of m pairs of distinct integers in the range from 1 to 9; all pairs within each set are distinct and no pair contains the same number twice; it is guaranteed that there is a pair from the first set and a pair from the second set that share exactly one number.
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
        
    #State of the program after the  for loop has been executed: `n` is an integer from 1 to 12, `m` is an integer from 1 to 12, `A` is a list of `n` pairs of integers where each pair holds the count of valid matches found and the last assigned value based on the conditions met during iterations; if no valid matches were found for a specific index, the count remains 0 and the last assigned value remains 0.
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
        
    #State of the program after the  for loop has been executed: `n` is an integer from 1 to 12; `m` is an integer from 1 to 12; `B` is a list where each `B[i][0]` holds the count of valid matches found for each `i` from 0 to `m-1`, and `B[i][1]` holds the last value assigned based on the conditions involving elements of `b` and `a`, or remains 0 if no matching conditions were met for that `i`.
    if (sum(A[i][0] for i in range(n)) == 1 or sum(B[i][0] for i in range(m)) == 1) :
        for Ai in A:
            if Ai[0] == 1:
                ans = Ai[1]
            
        #State of the program after the  for loop has been executed: `n` is an integer from 1 to 12, `A` is a list with at least `n` elements, `ans` holds the value of the second element of the last `Ai` for which `Ai[0]` equals 1, or remains unchanged if no such `Ai` exists.
        for Bi in B:
            if Bi[0] == 1:
                ans = Bi[1]
            
        #State of the program after the  for loop has been executed: `n` is an integer from 1 to 12, `A` is a list with at least `n` elements, `ans` holds the value of the second element of the last `Bi` for which `Bi[0]` equals 1, or remains unchanged if no such `Bi` exists; `B` may have any number of elements.
        print(ans)
    else :
        print(0)
    #State of the program after the if-else block has been executed: *`n` is an integer from 1 to 12; if the sum of the first elements of `A` equals 1 or the sum of the first elements of `B` equals 1, `ans` holds the value of the second element of the last `Bi` for which `Bi[0]` equals 1, or remains unchanged if no such `Bi` exists, and `ans` is printed. Otherwise, `n` and `m` remain integers from 1 to 12, the sum of the first elements of `A` is not equal to 1, the sum of the first elements of `B` is not equal to 1, and 0 has been printed.
#Overall this is what the function does:The function reads two sets of pairs of distinct integers and checks for a shared integer between one pair from the first set and one pair from the second set. If exactly one valid match is found in either set, it returns the shared integer; otherwise, it returns 0. If there are conflicting matches that violate the pair conditions, the function exits with -1.

