#State of the program right berfore the function call: S is a string of length N consisting of the characters 'A', 'C', 'G', and 'T', where 2 <= N <= 10^5. Q is a positive integer such that 1 <= Q <= 10^5. Each query consists of integers l_i and r_i (1 <= l_i < r_i <= N).
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
        
    #State of the program after the  for loop has been executed: `N` is a positive integer, `P` is a list where each `P[i]` (for `1 <= i < N`) contains the count of 'AC' substrings found in `S` up to index `i-1`, and `P[N]` is 0.
    for _ in range(Q):
        l, r = map(int, raw_input().split())
        
        print(P[r - 1] - P[l - 1])
        
    #State of the program after the  for loop has been executed: `N` is a positive integer; `P` is a list where each `P[i]` (for `1 <= i < N`) contains the count of 'AC' substrings found in `S` up to index `i-1`; `P[N]` is 0; `l` and `r` are integers corresponding to the last input received; the results of `P[r - 1] - P[l - 1]` for all executed queries have been printed.
#Overall this is what the function does:The function accepts a string `S` consisting of the characters 'A', 'C', 'G', and 'T', and an integer `Q` representing the number of queries. For each query defined by the indices `l` and `r`, it calculates and prints the count of 'AC' substrings in the substring `S[l-1:r-1]`. The function does not return any value but prints the results directly for each query. It also assumes valid input as per the specified constraints.

