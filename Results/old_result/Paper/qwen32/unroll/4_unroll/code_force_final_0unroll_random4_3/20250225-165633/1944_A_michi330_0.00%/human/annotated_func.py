#State of the program right berfore the function call: The function receives an integer t (1 ≤ t ≤ 10^3) representing the number of test cases. For each test case, the function receives two integers n (1 ≤ n ≤ 100) and k (0 ≤ k ≤ n * (n - 1) / 2) where n is the number of islands and k is the maximum number of bridges Dominater can destroy.
def func():
    t = int(input())
    for i in range(0, t, 1):
        n, k = map(int, input().split())
        
        if k >= n - 1:
            print(1)
        else:
            print(n - 1)
        
    #State: The function has processed all t test cases, printing 1 if k is greater than or equal to n-1, otherwise printing n-1 for each test case. The values of t, n, and k have been updated according to the input for each iteration of the loop.
#Overall this is what the function does:The function processes multiple test cases, each consisting of two integers `n` (number of islands) and `k` (maximum number of bridges Dominater can destroy). For each test case, it prints `1` if `k` is greater than or equal to `n-1`, otherwise it prints `n-1`.

