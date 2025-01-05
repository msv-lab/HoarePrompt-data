#State of the program right berfore the function call: S is a string of length N consisting of characters 'A', 'C', 'G', and 'T'. 2 <= N <= 10^5, 1 <= Q <= 10^5, 1 <= l_i < r_i <= N.**
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
        
    #State of the program after the  for loop has been executed: N is the length of string S, Q is the number of queries, P is a list where each element represents the number of occurrences of 'AC' in the substring ending at that index.
    for _ in range(Q):
        l, r = map(int, raw_input().split())
        
        print(P[r - 1] - P[l - 1])
        
    #State of the program after the  for loop has been executed: `N` is the length of string S, `Q` is greater than or equal to 0, `P` is a list representing the number of occurrences of 'AC' in substrings, and the difference between the occurrences of 'AC' in the substrings ending at index `r - 1` and `l - 1` is printed for each query.
#Overall this is what the function does:The function `func` reads an input string `S` of length `N` containing characters 'A', 'C', 'G', and 'T'. It then processes multiple queries `Q`, where each query consists of two integers l and r. The function calculates the number of occurrences of the substring 'AC' in the substrings ending at index r - 1 and l - 1, and prints the difference of these occurrences for each query.

