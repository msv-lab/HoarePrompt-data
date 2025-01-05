#State of the program right berfore the function call: N is an integer such that 2 <= N <= 100000, Q is an integer such that 1 <= Q <= 100000, S is a string of length N consisting of characters 'A', 'C', 'G', and 'T', and for each query, l_i and r_i are integers such that 1 <= l_i < r_i <= N.
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
        
    #State of the program after the  for loop has been executed: `N` is an integer such that 2 <= `N` <= 100000, `P` is a list where `P[N - 1]` is the total count of 'AC' in the substring `S`, and `P[0]` is 0.
    for _ in range(Q):
        l, r = map(int, raw_input().split())
        
        print(P[r - 1] - P[l - 1])
        
    #State of the program after the  for loop has been executed: `P[r - 1] - P[l - 1]` is computed for each query, `l` and `r` are integers derived from user input, and the output reflects the difference of counts of 'AC' in substring `S` for each query.
#Overall this is what the function does:The function accepts an integer `N`, an integer `Q`, and a string `S` of length `N`. It counts the occurrences of the substring 'AC' within `S` and processes `Q` queries, each defined by a pair of integers `(l, r)`, to return the count of 'AC' pairs in the substring `S[l-1:r]`. If `l` and `r` are invalid (not satisfying `1 <= l < r <= N`), the behavior is not defined, as the code does not handle such cases.

