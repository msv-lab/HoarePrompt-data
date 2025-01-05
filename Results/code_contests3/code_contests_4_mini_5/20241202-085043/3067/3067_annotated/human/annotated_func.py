#State of the program right berfore the function call: S is a string of length N consisting of characters 'A', 'C', 'G', and 'T', where 2 <= N <= 10^5. Each query consists of integers l_i and r_i such that 1 <= l_i < r_i <= N, and there are Q queries with 1 <= Q <= 10^5.
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
        
    #State of the program after the  for loop has been executed: `P` is a list of length `N` where each element `P[i]` represents the count of occurrences of the substring 'AC' in `S` up to index `i-1`. `N` is a positive integer, `Q` is the second integer input, `S` is the input string, and `P[0]` is 0.
    for _ in range(Q):
        l, r = map(int, raw_input().split())
        
        print(P[r - 1] - P[l - 1])
        
    #State of the program after the  for loop has been executed: `P` is a list of length `N`, `P[0]` is 0; `l` and `r` are the last values assigned from user input; the output has been printed a total of `Q` times as `P[r - 1] - P[l - 1]` for each pair of `(l, r)` provided.
#Overall this is what the function does:The function accepts a string `S` consisting of characters 'A', 'C', 'G', and 'T', and processes multiple queries defined by integer ranges `(l, r)`. It counts the occurrences of the substring 'AC' in the specified segments of the string `S`, returning the count for each query. The function assumes valid input for `l` and `r`, where `1 <= l < r <= N`. If the input does not conform to these constraints (e.g., if `l` equals or exceeds `r`), the behavior is unspecified.

