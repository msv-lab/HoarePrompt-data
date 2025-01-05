#State of the program right berfore the function call: n and m are integers such that 1 ≤ n, m ≤ 12, the first set contains n pairs of distinct integers between 1 and 9, and the second set contains m pairs of distinct integers between 1 and 9. Each pair contains two different numbers, and there is exactly one number shared between a pair from the first set and a pair from the second set.
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
        
    #State of the program after the  for loop has been executed: `n` is an integer greater than or equal to 1, `m` is the total number of elements in `b`, `A` contains `n` pairs of integers where each pair represents the count of valid matches and the last valid value assigned or remains 0 if no valid matches were found for each respective index.
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
        
    #State of the program after the  for loop has been executed: `n` is an integer greater than or equal to 1, `m` is greater than or equal to 1, `B` holds the count of successful updates and the last assigned values for each index based on the comparisons of elements in `b` and `a`.
    if (sum(A[i][0] for i in range(n)) == 1 or sum(B[i][0] for i in range(m)) == 1) :
        for Ai in A:
            if Ai[0] == 1:
                ans = Ai[1]
            
        #State of the program after the  for loop has been executed: `n` is an integer greater than or equal to 1, `m` is greater than or equal to 1, `B` holds the count of successful updates, `A` is a list of elements, and `ans` is the second element of the last element in `A` with the first element equal to 1, or remains unchanged if no such element exists.
        for Bi in B:
            if Bi[0] == 1:
                ans = Bi[1]
            
        #State of the program after the  for loop has been executed: `n` is greater than or equal to 1, `m` is greater than or equal to 1, `B` is unchanged, `ans` is the second element of the last element in `B` with the first element equal to 1, or remains unchanged if no such element exists.
        print(ans)
    else :
        print(0)
    #State of the program after the if-else block has been executed: *`n` is an integer greater than or equal to 1, `m` is greater than or equal to 1, and `B` holds the count of successful updates and the last assigned values for each index based on the comparisons of elements in `b` and `a`. If the sum of the first elements in `A` equals 1 or the sum of the first elements in `B` equals 1, then `ans` is the second element of the last element in `B` where the first element is equal to 1 (or remains unchanged if no such element exists), and `ans` is printed. Otherwise, the output is 0.
#Overall this is what the function does:The function accepts two integers `n` and `m`, representing the number of pairs of distinct integers from two sets. It processes these pairs to determine if there is exactly one valid match for either set, based on shared numbers between the pairs. If there is exactly one match, it returns the shared number; otherwise, it returns 0. If there is any inconsistency or invalid match during processing, it outputs -1. The function does not handle cases where the input pairs might not adhere to the specified constraints.

