#State of the program right berfore the function call: N and Q are positive integers, S is a string of length N consisting of characters 'A', 'C', 'G', or 'T', and l_i and r_i are integers such that 1 <= l_i < r_i <= N.**
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
        
    #State of the program after the  for loop has been executed: N and Q are positive integers, S is a string of length N consisting of characters 'A', 'C', 'G', or 'T', l_i and r_i are integers such that 1 <= l_i < r_i <= N, S is assigned the input string. If S[i - 1:i + 1] == 'AC', then P is a list of N+1 elements with values from 0 to N where the element at index i is equal to i. If S[i - 1:i + 1] is not equal to 'AC', then P is a list of N+1 elements where all elements are 0.
    for _ in range(Q):
        l, r = map(int, raw_input().split())
        
        print(P[r - 1] - P[l - 1])
        
    #State of the program after the  for loop has been executed: N and Q are positive integers, S is a string of length N, P is a list of N+1 elements where all elements are 0.
#Overall this is what the function does:The function `func` implicitly accepts positive integers N and Q, a string S of length N consisting of characters 'A', 'C', 'G', or 'T', and integers l_i and r_i such that 1 <= l_i < r_i <= N. It reads input values, processes the string S to create a list P where each element represents the count of occurrences of 'AC' substring up to that index. Then, for each query (l, r), it prints the difference P[r-1] - P[l-1]. The function does not explicitly return any value.

