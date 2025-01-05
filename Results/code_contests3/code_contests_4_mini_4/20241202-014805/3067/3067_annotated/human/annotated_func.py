#State of the program right berfore the function call: S is a string of length N consisting of the characters 'A', 'C', 'G', and 'T', where 2 <= N <= 100000. Q is a non-negative integer representing the number of queries, with 1 <= Q <= 100000. For each query, l_i and r_i are integers such that 1 <= l_i < r_i <= N.
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
        
    #State of the program after the  for loop has been executed: `N` is a non-negative integer, `P` is a list of length `N + 1` where `P[N]` is the count of 'AC' occurrences in string `S`, and `P[0]` is 0.
    for _ in range(Q):
        l, r = map(int, raw_input().split())
        
        print(P[r - 1] - P[l - 1])
        
    #State of the program after the  for loop has been executed: `N` is a non-negative integer; `P` is a list of length `N + 1`; `l` and `r` are two integers assigned from input during each iteration; the printed output is the difference `P[r - 1] - P[l - 1]` for each pair of `l` and `r` provided in the input.
#Overall this is what the function does:The function accepts a string `S` consisting of the characters 'A', 'C', 'G', and 'T', and a non-negative integer `Q` representing the number of queries. It counts occurrences of the substring 'AC' in `S` and for each query defined by indices `(l, r)`, it returns the total number of 'AC' occurrences in the substring `S[l-1:r-1]` (using 0-based indexing). The output for each query is printed sequentially.

