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
        
    #State of the program after the  for loop has been executed: `N` is greater than 0, `Q` is an integer based on user input, `S` is a string input, `P` is a list where each element `P[i]` is the count of consecutive 'AC' substrings in `S` up to index `i`, `i` is `N-1`
    for _ in range(Q):
        l, r = map(int, raw_input().split())
        
        print(P[r - 1] - P[l - 1])
        
    #State of the program after the  for loop has been executed: `N` is greater than 0, `Q` is greater than 0, `S` is a string input, `P` is a list where each element `P[i]` is the count of consecutive 'AC' substrings in `S` up to index `i`, `i` is `N-1, `l` and `r` are assigned the values from the input after splitting. The output is the difference between the count of consecutive 'AC' substrings in `S` up to index `r-1` and `l-1` after all iterations of the loop have finished.
#Overall this is what the function does:The function `func` reads two integer inputs `N` and `Q`, and a string input `S`. It then calculates the count of consecutive 'AC' substrings in `S` up to each index `i` and stores these counts in a list `P`. After that, for each pair of integers `l` and `r` provided as input, it prints the difference between the count of consecutive 'AC' substrings up to index `r-1` and `l-1`. The function does not have a specific return value.

