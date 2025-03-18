#State of the program right berfore the function call: Each test case contains two integers n and k where 1 ≤ n ≤ 100 and 0 ≤ k ≤ \frac{n \cdot (n - 1)}{2}. There are multiple test cases, with the number of test cases t satisfying 1 ≤ t ≤ 10^3.
def func():
    t = int(input())
    for i in range(0, t, 1):
        n, k = map(int, input().split())
        
        if k >= n - 1:
            print(1)
        else:
            print(n)
        
    #State: The loop has executed `t` times, and for each iteration, the values of `n` and `k` are read from the input. If `k` is greater than or equal to `n - 1`, the number `1` is printed; otherwise, the number `n` is printed. The variables `n` and `k` are updated with new values from the input in each iteration, but `t` remains unchanged.
#Overall this is what the function does:The function processes multiple test cases, each consisting of two integers `n` and `k`. For each test case, it prints `1` if `k` is greater than or equal to `n - 1`, otherwise it prints `n`. The integer `n` represents the number of elements in a set, and `k` represents a number of pairs that can be formed from the set.

