#State of the program right berfore the function call: S is a string of length N (where 2 <= N <= 100000) consisting of characters 'A', 'C', 'G', and 'T'; Q is an integer (where 1 <= Q <= 100000); and each query consists of two integers l_i and r_i (where 1 <= l_i < r_i <= N).
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
        
    #State of the program after the  for loop has been executed: `N` is the length of string `S`, `P` is a list where `P[i]` represents the number of occurrences of the substring 'AC' in the first `i` characters of `S`, and `P[N]` contains the total occurrences of 'AC' in the entire string `S`.
    for _ in range(Q):
        l, r = map(int, raw_input().split())
        
        print(P[r - 1] - P[l - 1])
        
    #State of the program after the  for loop has been executed: `N` is the length of string `S`; `P` is a list where `P[i]` represents the number of occurrences of the substring 'AC' in the first `i` characters of `S`; `l` and `r` are the last assigned integer values from user input; the output of `P[r - 1] - P[l - 1]` has been printed for each query in the range `Q`.
#Overall this is what the function does:The function accepts a string `S` consisting of characters 'A', 'C', 'G', and 'T', and an integer `Q` representing the number of queries. It counts the occurrences of the substring 'AC' in the string `S` and for each query defined by two integers `l` and `r`, it returns the count of 'AC' substrings located between the `l`-th and `r`-th positions (inclusive of `l` and exclusive of `r`). The function does not handle cases where the input values for `l` and `r` might be invalid according to the constraints, as it assumes valid input is provided.

