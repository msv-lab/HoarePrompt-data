#State of the program right berfore the function call: n and m are integers such that 1 ≤ n, m ≤ 12; the first participant communicates n pairs of distinct integers, each between 1 and 9; the second participant communicates m pairs of distinct integers, each between 1 and 9; all pairs within each set are distinct and contain different numbers.
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
        
    #State of the program after the  for loop has been executed: `n` is an integer within 1 to 12, `A` contains counts of successful matches found among the elements of `b` for each pair in `a`, `A[i][0]` represents the number of valid matches for the i-th pair, and `A[i][1]` holds the last assigned value of either `x1` or `y1` for each pair, or remains 0 if no matches were found.
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
        
    #State of the program after the  for loop has been executed: `n` is an integer within 1 to 12; `m` is greater than or equal to 0; `B[i][0]` is the count of valid matches found for each pair in `a`; `B[i][1]` holds the last assigned value of either `x1` or `y1` for each pair, or remains 0 if no matches were found; `i` is equal to `m` after the loop concludes; `x1` and `y1` are the last assigned values from `b[m-1]` if `m` is greater than 0, otherwise they remain undefined if `m` is 0.
    if (sum(A[i][0] for i in range(n)) == 1 or sum(B[i][0] for i in range(m)) == 1) :
        for Ai in A:
            if Ai[0] == 1:
                ans = Ai[1]
            
        #State of the program after the  for loop has been executed: `n` is an integer within 1 to 12, `m` is greater than or equal to 0, `A` is a list with at least `n` elements, `ans` holds the value of the last `A[i][1]` where `A[i][0]` equals 1 or remains undefined if no such element exists, `i` is equal to the length of `A` after the loop concludes.
        for Bi in B:
            if Bi[0] == 1:
                ans = Bi[1]
            
        #State of the program after the  for loop has been executed: `n` is an integer within 1 to 12, `m` is greater than or equal to 0, `A` is a list with at least `n` elements, `ans` holds the value of the last `Bi[1]` where `Bi[0]` equals 1 or remains undefined if no such element exists, `B` is a list with at least 0 elements, and `i` is equal to the length of `A`.
        print(ans)
    else :
        print(0)
    #State of the program after the if-else block has been executed: *`n` is an integer within 1 to 12 and `m` is greater than or equal to 0. If either the sum of the first elements of `A` across the range of `n` or the sum of the first elements of `B` across the range of `m` equals 1, then `ans` holds the value of the last `B[i][1]` where `B[i][0]` equals 1, or remains undefined if no such element exists. Otherwise, the sum of the first elements of `A` across the range of `n` is not equal to 1, the sum of the first elements of `B` across the range of `m` is not equal to 1, and the value 0 has been printed.
#Overall this is what the function does:The function accepts two integers `n` and `m`, representing the number of pairs of distinct integers communicated by two participants, and processes these pairs. It counts valid matches between the pairs while ensuring no duplicates in terms of matching criteria. If exactly one valid match is found among the pairs for either participant, it returns the last integer associated with that match. If there are no valid matches or more than one valid match, it returns 0. The function also prints -1 and exits if any pair violates the matching rules, indicating an inconsistency in the input pairs.

