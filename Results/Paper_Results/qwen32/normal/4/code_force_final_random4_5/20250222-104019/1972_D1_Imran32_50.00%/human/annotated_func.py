#State of the program right berfore the function call: Each test case contains two positive integers n and m such that 1 ≤ n, m ≤ 2 · 10^6. The first line of the input contains the number of test cases t (1 ≤ t ≤ 10^4). It is guaranteed that neither the sum of n nor the sum of m over all test cases exceeds 2 · 10^6.
def func_1():
    n, k = map(int, input().split())
    ans = n
    root = int(math.sqrt(n)) + 1
    for i in range(2, root + 1):
        cnt = i * i
        
        ans += (n + i) // cnt
        
    #State: n remains the same, k remains the same, root remains int(math.sqrt(n)) + 1, ans is n plus the sum of (n + i) // (i * i) for i from 2 to root.
    print(ans)
    #This is printed: ans (where ans is n plus the sum of (n + i) // (i * i) for i from 2 to root, and root is int(math.sqrt(n)) + 1)
#Overall this is what the function does:The function `func_1` reads multiple test cases, each consisting of two positive integers `n` and `k`. For each test case, it calculates a value `ans` which is `n` plus the sum of `(n + i) // (i * i)` for `i` ranging from 2 to the integer part of the square root of `n` plus one. It then prints the result `ans` for each test case.

