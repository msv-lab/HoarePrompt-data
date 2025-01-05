#State of the program right berfore the function call: S is a string of length N consisting of characters 'A', 'C', 'G', and 'T', N is an integer such that 2 <= N <= 100000, and Q is an integer such that 1 <= Q <= 100000. Each query consists of two integers l_i and r_i (1 <= l_i < r_i <= N).
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
        
    #State of the program after the  for loop has been executed: `N` is an integer representing the length of the string `S`, `P` is a list where `P[i]` holds the count of 'AC' substrings in `S` up to index `i`, and `P[0]` is 0. If `N` is 0, `P` remains a list with one element, which is 0.
    for _ in range(Q):
        l, r = map(int, raw_input().split())
        
        print(P[r - 1] - P[l - 1])
        
    #State of the program after the  for loop has been executed: `N` is an integer representing the length of the string `S`, `P[0]` is 0, `P` is a list where `P[i]` holds the count of 'AC' substrings in `S` up to index `i`, and the results of `P[r - 1] - P[l - 1]` for each query have been printed, with `l` and `r` being integers from user input for each iteration of the loop.
#Overall this is what the function does:The function accepts a string S consisting of characters 'A', 'C', 'G', and 'T' with a length N, and an integer Q representing the number of queries. It counts the occurrences of the substring 'AC' in S and processes Q queries, where each query specifies a range [l, r]. For each query, it returns the number of 'AC' substrings within that range. Note that the function does not handle cases where the input values for l and r are incorrect or where the string S is empty, although such cases are constrained by the problem statement.

