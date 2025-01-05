#State of the program right berfore the function call: S is a string of length N consisting of characters 'A', 'C', 'G', and 'T', N is an integer such that 2 <= N <= 100000, Q is an integer such that 1 <= Q <= 100000, and each query consists of integers l_i and r_i such that 1 <= l_i < r_i <= N.
def func():
    N, Q = map(int, raw_input().split())
    S = raw_input()
    P = [0] * (N + 1)
    for i in range(N):
        if i == 0:
            P[0] = 0
            continue
        
        if S[i - 1:i + 1] == 'AC':
            P[i] = P[i - 1] + 1
        else:
            P[i] = P[i - 1]
        
    #State of the program after the  for loop has been executed: `N` is an integer, `P` is a list of length `N + 1` where `P[0]` is 0 and for each `i` from 1 to `N-1`, `P[i]` is the count of contiguous occurrences of 'AC' in the substring `S[0:i]`.
    for _ in range(Q):
        l, r = map(int, raw_input().split())
        
        print(P[r - 1] - P[l - 1])
        
    #State of the program after the  for loop has been executed: `N` is an integer, `P` is a list of length `N + 1`, `l` and `r` hold the last input values, and the result of `P[r - 1] - P[l - 1]` has been printed for each of the `Q` queries.
#Overall this is what the function does:The function accepts a string `S` of length `N`, an integer `N`, and an integer `Q`. It calculates the number of contiguous occurrences of the substring 'AC' in the string `S` and processes `Q` queries, where each query specifies a range defined by indices `l` and `r`. For each query, it returns the count of occurrences of 'AC' in the substring `S[l-1:r-1]`. The function assumes valid input for ranges defined by `l` and `r` according to the constraints provided.

