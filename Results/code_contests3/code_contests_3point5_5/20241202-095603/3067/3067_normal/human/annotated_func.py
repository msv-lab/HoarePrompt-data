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
        
    #State of the program after the  for loop has been executed: After all iterations of the loop, P will be a list of size N+1 where each element P[i] will contain the number of occurrences of the substring 'AC' in S up to index i-1. If 'AC' is not found in the substring of S at index i-1 to i, P[i] will be equal to P[i-1].
    for _ in range(Q):
        l, r = map(int, raw_input().split())
        
        print(P[r - 1] - P[l - 1])
        
    #State of the program after the  for loop has been executed: After all iterations of the loop, P[r - 1] - P[l - 1] will be printed for each input value of l and r
#Overall this is what the function does:The function `func` reads input values N and Q, followed by a string S. It then calculates the occurrences of the substring 'AC' in S up to each index i-1 and stores these counts in the list P. After this calculation, it reads Q pairs of integers l and r, and prints the difference between P[r - 1] and P[l - 1] for each pair.

