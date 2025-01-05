#State of the program right berfore the function call: S is a string of length N consisting only of the characters 'A', 'C', 'G', and 'T', N is an integer such that 2 <= N <= 100000, and Q is an integer such that 1 <= Q <= 100000. Each query consists of integers l_i and r_i (1 <= l_i < r_i <= N).
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
        
    #State of the program after the  for loop has been executed: `N` is an integer within the range 2 to 100000, `Q` is an integer within the range 1 to 100000, `S` is a string from raw input, and `P` is a list of length `N + 1` where `P[i]` represents the count of occurrences of the substring 'AC' from the start of the string up to index `i-1`. If 'AC' appears consecutively, `P[i]` will be incremented accordingly, otherwise it will retain the previous count.
    for _ in range(Q):
        l, r = map(int, raw_input().split())
        
        print(P[r - 1] - P[l - 1])
        
    #State of the program after the  for loop has been executed: `N` is an integer within the range 2 to 100000; `Q` is an integer within the range 1 to 100000; `S` is a string from raw input; `P` is a list of length `N + 1`; `l` and `r` are integers from raw input for each of the `Q` queries; the output of the print statements for each query is `P[r - 1] - P[l - 1]` for each respective pair of `l` and `r`.
#Overall this is what the function does:The function accepts a string `S` of length `N` (where 2 <= N <= 100000) and an integer `Q` (where 1 <= Q <= 100000). It counts the occurrences of the substring 'AC' in `S` and allows for `Q` queries, each defined by a pair of integers `(l, r)`. For each query, it returns the number of times 'AC' appears in the substring `S[l-1:r]`. The function does not handle invalid inputs for `l` and `r`, which must be within the valid range of the string length.

