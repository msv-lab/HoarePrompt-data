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
        
    #State of the program after the  for loop has been executed: N is greater than 0, S is a string input, P is a list of size N+1 with elements calculated based on the condition 'if S[i - 1:i + 1] == 'AC', P[i] = P[i - 1] + 1, else P[i] = P[i - 1]'.
    for _ in range(Q):
        l, r = map(int, raw_input().split())
        
        print(P[r - 1] - P[l - 1])
        
    #State of the program after the  for loop has been executed: N is greater than 0, S is a string input, P is a list of size N+1 based on the condition, Q is greater than 0, l and r are integers obtained from input, and the result of `P[r - 1] - P[l - 1]` is printed for all iterations of the loop
#Overall this is what the function does:The function reads input values N, Q, S, and a list P. It then iterates through the string S to calculate values in the list P based on certain conditions. Afterwards, for each iteration in the range of Q, it reads input values l and r and prints the calculated difference between P[r - 1] and P[l - 1]. The function does not accept any parameters and returns specific output based on the inputs provided.

