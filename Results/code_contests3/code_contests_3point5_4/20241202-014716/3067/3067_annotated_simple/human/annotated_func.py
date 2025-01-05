#State of the program right berfore the function call: S is a string of length N, where N is a positive integer. Q is a positive integer. l_i and r_i are integers such that 1 <= l_i < r_i <= N. Each character in S is either 'A', 'C', 'G', or 'T'.**
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
        
    #State of the program after the  for loop has been executed: S is a string of unknown length, Q is a positive integer, P is a list where each element represents the number of occurrences of the substring 'AC' up to that index in the string S.
    for _ in range(Q):
        l, r = map(int, raw_input().split())
        
        print(P[r - 1] - P[l - 1])
        
    #State of the program after the  for loop has been executed: S is a string of unknown length, Q is 0, P is a list representing the number of occurrences of 'AC' up to each index in S
#Overall this is what the function does:The function `func` reads input values N, Q, and a string S. It then calculates a list P where each element represents the number of occurrences of the substring 'AC' up to that index in the string S. Afterward, it iterates Q times, taking pairs of integers l and r as input and prints the difference between P[r-1] and P[l-1]. The function does not explicitly return any value.

