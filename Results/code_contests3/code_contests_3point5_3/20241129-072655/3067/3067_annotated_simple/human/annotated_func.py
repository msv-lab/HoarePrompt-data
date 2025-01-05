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
        
    #State of the program after the  for loop has been executed: After all iterations of the loop have executed, P will contain the number of occurrences where the substring 'AC' appears in consecutive positions in the input string S.
    for _ in range(Q):
        l, r = map(int, raw_input().split())
        
        print(P[r - 1] - P[l - 1])
        
    #State of the program after the  for loop has been executed: After all iterations of the loop have executed, `P` contains the number of occurrences where the substring 'AC' appears in consecutive positions in the input string `S`, `Q` is greater than 0, `l` and `r` are assigned values from the input.
#Overall this is what the function does:The function `func` reads an input consisting of integers `N` and `Q`, followed by a string `S`. It then processes the string `S` to count the occurrences where the substring 'AC' appears in consecutive positions and stores the count in a list `P`. After that, it reads pairs of integers `l` and `r` from the input and prints the difference between `P[r - 1]` and `P[l - 1]` for each pair. The function does not accept any parameters and returns the output based on the processed input.

