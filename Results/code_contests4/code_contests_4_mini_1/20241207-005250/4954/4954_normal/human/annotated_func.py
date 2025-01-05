#State of the program right berfore the function call: N is a positive integer (1 <= N <= 20), M is a positive integer (1 <= M <= 20), C is an integer (-100 <= C <= 100), B is a list of M integers (-100 <= B[i] <= 100), and A is a list of N lists, each containing M integers (-100 <= A[i][j] <= 100).
def func():
    N, M, C = map(int, raw_input().split())
    B = map(int, raw_input().split())
    ans = 0
    for i in range(0, N):
        A = map(int, raw_input().split())
        
        tmp = [(A[m] * B[m]) for m in range(M)]
        
        if sum(tmp) + C > 0:
            ans += 1
        
    #State of the program after the  for loop has been executed: `N` is a positive integer (1 <= N <= 20), `i` is `N-1`, `A` is a map object containing integers from user input for the last iteration, `tmp` is a list of products of corresponding elements from `A` and `B` for each index `m` in the range from 0 to `M-1`, and `ans` is the count of how many times the sum of `tmp` plus `C` is greater than 0 after all `N` iterations.
    print(ans)
#Overall this is what the function does:The function reads integers N, M, and C, and a list B of M integers from input. It processes N lists A, each containing M integers, calculating the sum of products of corresponding elements from A and B for each list. If the sum of these products plus C is greater than 0, it increments a counter. Finally, it prints the count of how many times this condition was met across all N lists. The function does not accept parameters directly, and it could handle cases where the sum is exactly zero or negative, but only increments the counter when the sum exceeds zero.

