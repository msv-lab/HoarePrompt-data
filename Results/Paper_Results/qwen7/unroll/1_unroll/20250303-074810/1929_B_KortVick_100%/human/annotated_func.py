#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 1000, and for each test case, n and k are integers such that 2 ≤ n ≤ 10^8 and 1 ≤ k ≤ 4n - 2.
def func():
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        
        if 4 * n - 2 == k:
            print(k // 2 + 1)
        else:
            print(ceil(k / 2))
        
    #State: Output State: The output state will consist of a series of lines, each containing either `k // 2 + 1` or `ceil(k / 2)`, depending on whether `4 * n - 2` equals `k` for each iteration. The number of lines will be equal to the value of `t`, which is a positive integer between 1 and 1000 (inclusive). Each line's content depends on the specific values of `n` and `k` provided during the corresponding iteration of the loop.
#Overall this is what the function does:The function processes multiple test cases, where for each test case, it reads two integers \( n \) and \( k \). If \( 4n - 2 \) equals \( k \), it prints \( \frac{k}{2} + 1 \); otherwise, it prints \( \left\lceil \frac{k}{2} \right\rceil \). The function reads \( t \) test cases, where \( t \) is a positive integer between 1 and 1000 (inclusive), and for each test case, it outputs one line based on the conditions specified.

