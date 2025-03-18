#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^3, and for each test case, n and k are integers satisfying 1 ≤ n ≤ 100 and 0 ≤ k ≤ n * (n - 1) / 2.
def func():
    t = int(input())
    for i in range(0, t, 1):
        n, k = map(int, input().split())
        
        if k >= n - 1:
            print(1)
        else:
            print(n)
        
    #State: The loop has completed all its iterations, with `t` remaining as the initial value since it is not modified within the loop. The variable `i` will be equal to `t` (the initial value of `t`) plus the number of iterations minus one, which is `t`. Therefore, `i` will be `2 * t - 1`. The variables `n` and `k` will each hold the values of the last `n` and `k` entered by the user during any of the iterations, as they are re-assigned in each iteration.
#Overall this is what the function does:The function processes multiple test cases, each consisting of integers \( t \), \( n \), and \( k \). For each test case, it reads \( t \) and then iterates \( t \) times, reading \( n \) and \( k \) in each iteration. Based on the value of \( k \) relative to \( n-1 \), it prints either 1 or \( n \). After processing all test cases, the function does not return any value but prints the results for each test case.

