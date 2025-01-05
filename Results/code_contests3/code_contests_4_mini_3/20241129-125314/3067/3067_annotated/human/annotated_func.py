#State of the program right berfore the function call: S is a string of length N consisting only of the characters 'A', 'C', 'G', and 'T', where 2 <= N <= 10^5. Q is a positive integer such that 1 <= Q <= 10^5, and for each query, l_i and r_i are integers such that 1 <= l_i < r_i <= N.
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
        
    #State of the program after the  for loop has been executed: `P` is an array of length `N + 1` where `P[i]` is the count of 'AC' occurrences in the substring `S[0:i]`, `i` ranges from 0 to N.
    for _ in range(Q):
        l, r = map(int, raw_input().split())
        
        print(P[r - 1] - P[l - 1])
        
    #State of the program after the  for loop has been executed: `P` is an array of length `N + 1`, `l` and `r` are integers from user input for each query, the output is the result of `P[r - 1] - P[l - 1]` for each query executed a total of `Q` times.
#Overall this is what the function does:The function accepts a string `S` consisting of characters 'A', 'C', 'G', and 'T', and an integer `Q` representing the number of queries. It calculates the cumulative count of occurrences of the substring 'AC' in `S` up to each index and allows `Q` queries that return the number of 'AC' occurrences between the specified indices `l_i` and `r_i`. The function does not handle cases where `l_i` or `r_i` are out of the specified range or where `S` is not properly formatted.

