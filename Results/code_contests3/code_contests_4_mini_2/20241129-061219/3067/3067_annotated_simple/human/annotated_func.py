#State of the program right berfore the function call: S is a string of length N consisting only of the characters 'A', 'C', 'G', and 'T', where 2 <= N <= 100000. Q is a positive integer such that 1 <= Q <= 100000, and each query consists of integers l_i and r_i such that 1 <= l_i < r_i <= N.
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
        
    #State of the program after the  for loop has been executed: `N` is a non-negative integer, `P[0]` is 0, `P` is a list of length `N + 1` where `P[N]` is the count of occurrences of 'AC' in string `S`.
    for _ in range(Q):
        l, r = map(int, raw_input().split())
        
        print(P[r - 1] - P[l - 1])
        
    #State of the program after the  for loop has been executed: `N` is a non-negative integer, `P[0]` is 0, `P` is a list of length `N + 1`, `l` and `r` are integers from input for each of the `Q` iterations; the output is the difference `P[r - 1] - P[l - 1]` for each pair of `l` and `r` provided in the input.
#Overall this is what the function does:The function accepts a string `S` and a number of queries `Q`, and for each query defined by indices `l` and `r`, it returns the count of occurrences of the substring 'AC' in the specified range of `S`.

