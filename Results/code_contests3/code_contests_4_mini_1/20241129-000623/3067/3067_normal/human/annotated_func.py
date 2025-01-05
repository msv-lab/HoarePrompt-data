#State of the program right berfore the function call: S is a string of length N consisting of characters 'A', 'C', 'G', and 'T', N is an integer such that 2 <= N <= 100000, Q is an integer such that 1 <= Q <= 100000, and for each query, l_i and r_i are integers such that 1 <= l_i < r_i <= N.
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
        
    #State of the program after the  for loop has been executed: `P` is a list where `P[i]` contains the count of 'AC' substrings in `S` from the start up to index `i`, with `P[0]` being 0 and `P[N]` being the total count of 'AC' in `S`.
    for _ in range(Q):
        l, r = map(int, raw_input().split())
        
        print(P[r - 1] - P[l - 1])
        
    #State of the program after the  for loop has been executed: `P` is a list where `P[i]` contains the count of 'AC' substrings in `S`; `l` and `r` are integers representing the range for each query, with the final output being the results of `P[r - 1] - P[l - 1]` for each of the `Q` queries.
#Overall this is what the function does:The function accepts a string `S` consisting of characters 'A', 'C', 'G', and 'T', and an integer `Q` representing the number of queries. For each query defined by the indices `(l_i, r_i)`, it returns the count of the substring 'AC' in `S` between the indices `l_i` and `r_i`. However, it does not count occurrences of 'G' and 'T', which is a discrepancy from the annotations. The function also assumes valid input for `l` and `r`, where `1 <= l < r <= N`.

