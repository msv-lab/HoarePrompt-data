#State of the program right berfore the function call: S is a string of length N consisting of the characters 'A', 'C', 'G', and 'T', N is an integer such that 2 <= N <= 100000, and each query consists of two integers l_i and r_i (1 <= l_i < r_i <= N) that define valid substring indices.
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
        
    #State of the program after the  for loop has been executed: `P` is a list where `P[i]` contains the count of 'AC' substrings in `S` from the start up to index `i - 1`, for `0 <= i < N`.
    for _ in range(Q):
        l, r = map(int, raw_input().split())
        
        print(P[r - 1] - P[l - 1])
        
    #State of the program after the  for loop has been executed: `P` is a list where `P[i]` contains the count of 'AC' substrings in `S` for `0 <= i < N`; `l` and `r` are integers representing the ranges input by the user; the output consists of the differences `P[r - 1] - P[l - 1]` for each query executed, indicating the counts of 'AC' substrings in the specified ranges.
#Overall this is what the function does:The function accepts a string `S` of length `N` (where 2 <= N <= 100000) and processes `Q` queries, each defined by a pair of indices `(l, r)`. For each query, it calculates and returns the number of occurrences of the substring 'AC' within the substring of `S` defined by those indices. The function uses a prefix sum array to efficiently count the number of 'AC' substrings from the start of the string up to various points. However, it does not handle cases where the input indices are out of bounds or invalid, which could lead to runtime errors.

