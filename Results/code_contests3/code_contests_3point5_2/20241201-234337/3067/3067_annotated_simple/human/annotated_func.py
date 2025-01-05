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
        
    #State of the program after the  for loop has been executed: After all the iterations of the loop have finished, P will contain the cumulative count of occurrences where the substring 'AC' appears in consecutive positions in the string S.
    for _ in range(Q):
        l, r = map(int, raw_input().split())
        
        print(P[r - 1] - P[l - 1])
        
    #State of the program after the  for loop has been executed: After all the iterations of the loop have finished, P will contain the cumulative count of occurrences where the substring 'AC' appears in consecutive positions in the string S for each query.
#Overall this is what the function does:The function reads input values N, Q, and a string S. It then processes the string S to determine the cumulative count of occurrences where the substring 'AC' appears in consecutive positions. For each query specified by input values l and r, it prints the difference between the cumulative count at position r-1 and the cumulative count at position l-1. The function does not accept any parameters and outputs the results of the queries based on the processed string S.

