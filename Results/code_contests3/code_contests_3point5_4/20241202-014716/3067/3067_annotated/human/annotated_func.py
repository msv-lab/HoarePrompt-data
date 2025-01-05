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
        
    #State of the program after the  for loop has been executed: After all iterations of the loop have finished, `N` and `Q` are assigned values based on user input, `S` is assigned the raw input value, `P` is a list of integers where each element represents the count of occurrences where the substring of `S` from index `i-1` to `i+1` is equal to 'AC' up to index `i`.
    for _ in range(Q):
        l, r = map(int, raw_input().split())
        
        print(P[r - 1] - P[l - 1])
        
    #State of the program after the  for loop has been executed: After all iterations of the loop have finished, `N` and `Q` are assigned values based on user input, `S` is assigned the raw input value, `P` is a list of integers representing the count of occurrences where the substring of `S` from index `i-1` to `i+1` is equal to 'AC' up to index `i`. The loop will print the difference between the values at index `r - 1` and `l - 1` of list `P` for each iteration of the loop.
#Overall this is what the function does:The function reads user input for N and Q, a string S, and calculates occurrences of the substring 'AC' in S up to each index. It then reads pairs of integers l and r, and for each pair, it prints the difference between the count of 'AC' occurrences at index r - 1 and l - 1 in the list P. The function does not accept any parameters and provides specific output based on user input.

