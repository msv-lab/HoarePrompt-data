#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, and for each test case, n and m are integers such that 1 ≤ n, m ≤ 2⋅10^6. It is also guaranteed that the sum of n and the sum of m over all test cases does not exceed 2⋅10^6.
def func_1():
    n, k = map(int, input().split())
    ans = n
    root = int(math.sqrt(n)) + 1
    for i in range(2, root + 1):
        cnt = i * i
        
        ans += (n + i) // cnt
        
    #State: Output State: `t` is an integer such that 1 ≤ t ≤ 10^4, `n` is an integer such that 1 ≤ n ≤ 2⋅10^6, `k` is an integer such that 1 ≤ k ≤ 2⋅10^6, `ans` is equal to `n + sum((n + i) // (i * i) for i in range(2, int(math.sqrt(n)) + 1))`, `root` is equal to `int(math.sqrt(n)) + 1`.
    print(ans)
    #This is printed: n + sum((n + i) // (i * i) for i in range(2, int(math.sqrt(n)) + 1)) (where n is an integer between 1 and 2 * 10^6)
#Overall this is what the function does:The function processes multiple test cases, where for each test case, it takes two integers `n` and `m` (with constraints 1 ≤ n, m ≤ 2⋅10^6). It calculates the value of `ans` as `n + sum((n + i) // (i * i) for i in range(2, int(math.sqrt(n)) + 1))`, where `i` ranges from 2 to the square root of `n`. Finally, it prints the calculated value of `ans` for each test case.

