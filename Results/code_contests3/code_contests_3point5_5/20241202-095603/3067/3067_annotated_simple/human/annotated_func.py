#State of the program right berfore the function call: **
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
        
    #State of the program after the  for loop has been executed: `N` is greater than 0, `Q` is an input integer, `S` is a string input, `P` is a list of `N + 1` integers where each element represents the number of occurrences of the substring 'AC' up to that index in `S`.
    for _ in range(Q):
        l, r = map(int, raw_input().split())
        
        print(P[r - 1] - P[l - 1])
        
    #State of the program after the  for loop has been executed: `N` is greater than 0, `Q` is greater than 0, `S` is a string input, `P` is a list of `N + 1` integers representing occurrences of 'AC' in `S`, `l` and `r` are integers obtained from splitting the input string, and the differences between `P[r - 1]` and `P[l - 1]` for all `Q` iterations are printed
#Overall this is what the function does:The function reads inputs for N, Q, and a string S. It then calculates the occurrences of the substring 'AC' in the string S up to each index and stores them in a list P. After that, for each pair of integers l and r from the input, it prints the difference between P[r - 1] and P[l - 1]. The function does not accept any parameters and only performs the described operations on the inputs provided.

