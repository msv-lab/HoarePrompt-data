#State of the program right berfore the function call: S is a string of length N consisting only of the characters 'A', 'C', 'G', and 'T', N is an integer such that 2 <= N <= 100000, and Q is an integer such that 1 <= Q <= 100000. For each query, l_i and r_i are integers such that 1 <= l_i < r_i <= N.
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
        
    #State of the program after the  for loop has been executed: `N` is a non-negative integer, `P` is a list where `P[i]` contains the count of 'AC' substrings from the start of `S` up to index `i`, and `P[0]` is 0.
    for _ in range(Q):
        l, r = map(int, raw_input().split())
        
        print(P[r - 1] - P[l - 1])
        
    #State of the program after the  for loop has been executed: `N` is a non-negative integer; `P` is a list where `P[0]` is 0; after executing the loop `Q` times, the output will consist of the differences `P[r - 1] - P[l - 1]` for each pair of integers `l` and `r` read from input, where each output represents the count of 'AC' substrings in the specified range.
#Overall this is what the function does:The function accepts a string `S` consisting of the characters 'A', 'C', 'G', and 'T', and two integers `N` (the length of the string) and `Q` (the number of queries). It counts the occurrences of the substring 'AC' in `S` from the start up to each index and allows for multiple queries to return the count of 'AC' substrings within specific ranges defined by pairs of integers `l` and `r`. The output for each query is the difference in counts between indices `r-1` and `l-1`, effectively providing the count of 'AC' substrings in the substring `S[l-1:r]`. This function handles substring queries efficiently but does not validate the input constraints or handle cases where `l` or `r` are outside the valid range.

