#State of the program right berfore the function call: Each test case contains two positive integers n and m (1 ≤ n, m ≤ 2 · 10^6). The first line of the input contains the number of test cases t (1 ≤ t ≤ 10^4). The sum of n and the sum of m over all test cases do not exceed 2 · 10^6.
def func_1():
    n, k = map(int, input().split())
    ans = n
    root = int(math.sqrt(n)) + 1
    for i in range(2, root + 1):
        cnt = i * i
        
        ans += (n + i) // cnt
        
    #State: `n + sum((n + i) // (i * i) for i in range(2, int(math.sqrt(n)) + 1))`
    print(ans)
    #This is printed: ans (where ans is calculated as n + sum((n + i) // (i * i) for i in range(2, int(math.sqrt(n)) + 1)))
#Overall this is what the function does:The function reads multiple test cases, each consisting of a single positive integer `n`. For each test case, it calculates a value based on `n` and prints the result. The calculation involves summing `n` and the integer division of `(n + i)` by `(i * i)` for each `i` from 2 up to the square root of `n` plus one.

