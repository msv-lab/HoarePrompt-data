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
        
    #State of the program after the  for loop has been executed: `N` is a positive integer, `Q` is assigned values obtained from splitting the raw input, `S` is a string input from the user with at least `N+1` characters, `P` is a list where `P[0] = 0` and is updated based on the condition `S[i - 1:i + 1] == 'AC'` where if true `P[i] = P[i - 1] + 1`, else `P` remains initialized with `(N+1)` zeros. The loop executes for all `i` less than `N` and is incremented by 1. If `S[i - 1:i + 1] == 'AC'`, then `P[i] = P[i - 1] + 1`. Otherwise, `P[i]` remains the same as `P[i - 1` for all `i` less than `N`.
    for _ in range(Q):
        l, r = map(int, raw_input().split())
        
        print(P[r - 1] - P[l - 1])
        
    #State of the program after the  for loop has been executed: `N` is a positive integer, `Q` is greater than 0, `S` is a string input with at least `N+1` characters, `P` is a list updated with the condition `S[i - 1:i + 1] == 'AC'`, `l` and `r` are assigned values based on input split, the difference between `P[r - 1]` and `P[l - 1]` is printed for all values of `l` and `r` provided by the user.
#Overall this is what the function does:The function `func` reads input values for N, Q, S, and calculates the list P based on the conditions specified. It then processes Q sets of input values for l and r and prints the difference between P[r - 1] and P[l - 1]. The function does not accept any parameters and solely relies on user input for its execution.

