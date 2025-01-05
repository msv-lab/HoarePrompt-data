#State of the program right berfore the function call: **Precondition**: **N and Q are positive integers. S is a string of length N consisting of only `A`, `C`, `G`, and `T` characters. Each query i consists of integers l_i and r_i such that 1 <= l_i < r_i <= N.**
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
        
    #State of the program after the  for loop has been executed: `S` is assigned the value of the user input, `P` is a list of size N+1 where each element is the number of consecutive occurrences of the substring 'AC' in `S` up to that index. `N` is greater than or equal to 0.
    for _ in range(Q):
        l, r = map(int, raw_input().split())
        
        print(P[r - 1] - P[l - 1])
        
    #State of the program after the  for loop has been executed: `S` is assigned the value of the user input, `P` is a list of size N+1 where each element is the number of consecutive occurrences of the substring 'AC' in `S` up to that index, N is greater than or equal to 0, `Q` is 0, `l` and `r` are not assigned any values
#Overall this is what the function does:The function `func` reads input values N, Q, and string S. It then calculates the number of consecutive occurrences of the substring 'AC' in S up to each index and stores this information in the list P. After that, it processes Q queries where each query consists of integers l and r. For each query, it prints the count of 'AC' occurrences between positions l and r in the string S. The function does not accept any parameters but operates on the preconditions provided.

