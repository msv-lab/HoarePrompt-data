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
        
    #State of the program after the  for loop has been executed: N is greater than 0, Q is assigned based on input, S is assigned the input string, P is a list where P[i] is the number of occurrences of 'AC' in the substrings S[0:i+1].
    for _ in range(Q):
        l, r = map(int, raw_input().split())
        
        print(P[r - 1] - P[l - 1])
        
    #State of the program after the  for loop has been executed: N is greater than 0, Q is at least 1, S is assigned the input string, P is a list where P[i] is the number of occurrences of 'AC' in the substrings S[0:i+1]
#Overall this is what the function does:The function reads input values for N and Q, then reads a string S and calculates the occurrences of 'AC' in each substring S[0:i+1] using a list P. It then processes Q queries by printing the difference between P[r - 1] and P[l - 1]. The function does not accept any parameters and handles the predetermined input/output process.

