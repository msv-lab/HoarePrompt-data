#State of the program right berfore the function call: Each test case contains two positive integers n and m such that 1 ≤ n, m ≤ 2 · 10^6. The first line of the input contains the number of test cases t (1 ≤ t ≤ 10^4). It is guaranteed that neither the sum of n nor the sum of m over all test cases exceeds 2 · 10^6.
def func_1():
    n, k = map(int, input().split())
    ans = n
    root = int(math.sqrt(n)) + 1
    for i in range(2, root + 1):
        cnt = i * i
        
        ans += (n + i) // cnt
        
    #State: ans is the sum of its initial value `n` and the results of the additions `(n + i) // (i * i)` for each `i` from `2` to `root`.
    print(ans)
    #This is printed: ans (where ans is the initial value n plus the sum of (n + i) // (i * i) for each i from 2 to root)
#Overall this is what the function does:The function `func_1` reads input for a single test case consisting of two positive integers `n` and `k`. It calculates a value `ans` starting from `n` and adds to it the sum of `(n + i) // (i * i)` for each `i` from `2` to the square root of `n` rounded up. The result is then printed.

