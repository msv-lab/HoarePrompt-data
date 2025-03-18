#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^3, and for each test case, n and k are integers such that 1 <= k <= n <= 10^3.
def func():
    t = int(input())
    for _ in range(t):
        n, k = (int(i) for i in input().split())
        
        res = [1] * n if k == n else range(n) if k == 1 else [-1]
        
        print(*res)
        
    #State: The loop iterates `t` times, and for each iteration, it reads a pair of integers `n` and `k` from the input. If `k` equals `n`, it prints a list of `n` ones. If `k` equals 1, it prints the range of numbers from 0 to `n-1`. Otherwise, it prints `-1`. The values of `t`, `n`, and `k` are unchanged after the loop completes.
#Overall this is what the function does:The function `func` reads an integer `t` from the input, representing the number of test cases. For each test case, it reads two integers `n` and `k` from the input. If `k` equals `n`, it prints a list of `n` ones. If `k` equals 1, it prints the range of numbers from 0 to `n-1`. If `k` is neither `n` nor 1, it prints `-1`. The function does not return any value and does not modify the input variables `t`, `n`, or `k`.

