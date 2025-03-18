#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, and for each test case, n and m are integers such that 1 ≤ n, m ≤ 2 · 10^6. The sum of all n and the sum of all m across all test cases do not exceed 2 · 10^6.
def func_1():
    n, k = map(int, input().split())
    ans = n
    root = int(math.sqrt(n)) + 1
    for i in range(2, root + 1):
        cnt = i * i
        
        ans += (n + i) // cnt
        
    #State: `t` is an integer such that 1 ≤ t ≤ 10^4; `n` and `k` are integers read from input where 1 ≤ n, k ≤ 2 · 10^6; `ans` is the result of `n + sum((n + i) // (i * i) for i in range(2, int(math.sqrt(n)) + 2)); `root` is `int(math.sqrt(n)) + 1`.
    print(ans)
    #This is printed: ans (where ans is n plus the sum of (n + i) // (i * i) for i in range(2, int(math.sqrt(n)) + 2))
#Overall this is what the function does:The function `func_1` reads two integers `n` and `k` from the input, computes a value `ans` based on `n`, and prints the result. The computation involves adding to `n` the sum of `(n + i) // (i * i)` for each `i` from 2 up to the square root of `n` plus one. The function does not return any value explicitly but outputs the computed `ans`.

