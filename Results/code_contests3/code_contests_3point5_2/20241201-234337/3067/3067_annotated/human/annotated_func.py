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
        
    #State of the program after the  for loop has been executed: N is a positive integer, S has a valid assigned value based on user input, P is a list of length N+1 where each element represents the number of consecutive 'AC' substrings ending at that index in S.
    for _ in range(Q):
        l, r = map(int, raw_input().split())
        
        print(P[r - 1] - P[l - 1])
        
    #State of the program after the  for loop has been executed: N is a positive integer, S has a valid assigned value, P is a list of length N+1, Q is greater than 0, l and r are assigned values based on user input, the loop has executed Q times, and the difference between the elements at index r - 1 and l - 1 of list P has been printed Q times.
#Overall this is what the function does:The function reads input values N, Q, S, and creates a list P where each element represents the number of consecutive 'AC' substrings ending at that index in S. It then processes Q queries by reading pairs of integers l and r, and prints the difference between the elements at index r - 1 and l - 1 of list P. The function does not accept any parameters and does not have a return value.

