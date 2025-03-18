#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^3, each test case consists of two integers n and k such that 1 ≤ n ≤ 100 and 0 ≤ k ≤ (n * (n - 1)) / 2.
def func():
    t = int(input())
    for i in range(0, t, 1):
        n, k = map(int, input().split())
        
        if k >= n - 1:
            print(1)
        else:
            print(n - 1)
        
    #State: The loop has executed all its iterations. The variable `t` retains its initial value, which is a positive integer such that 1 ≤ t ≤ 10^3. The variable `i` is now equal to `t`, indicating that all iterations have been completed. The variables `n` and `k` retain their last input values from the third iteration of the loop.
#Overall this is what the function does:The function processes a series of test cases, each consisting of two integers \( n \) and \( k \). It checks if \( k \) can be formed by choosing \( k \) pairs from \( n \) elements. If \( k \) is greater than or equal to \( n - 1 \), it prints 1, indicating that such a selection is possible. Otherwise, it prints \( n - 1 \), indicating that the input is invalid or such a selection is not possible. After processing all test cases, the function concludes.

