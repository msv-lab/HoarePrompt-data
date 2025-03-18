#State of the program right berfore the function call: t is an integer where 1 ≤ t ≤ 10^3; for each test case, n and k are integers where 1 ≤ k ≤ n ≤ 10^3.
def func():
    for _ in range(int(input())):
        n, k = list(map(int, input().split(' ')))
        
        if n == k:
            print(('1 ' * n)[:-1])
        elif k == 1:
            print(' '.join([str(x + 1) for x in range(n)]))
        else:
            print(-1)
        
    #State: `t` is an integer where 1 ≤ t ≤ 10^3, and for each test case, `n` and `k` are integers where 1 ≤ k ≤ n ≤ 10^3. The values of `t`, `n`, and `k` remain unchanged for each iteration of the loop.
#Overall this is what the function does:The function `func` processes a series of test cases, each defined by two integers `n` and `k` (where `1 ≤ k ≤ n ≤ 10^3`). For each test case, it prints a specific output based on the values of `n` and `k`:
- If `n` equals `k`, it prints a space-separated string of `n` ones.
- If `k` equals 1, it prints a space-separated string of integers from 1 to `n`.
- For any other values of `n` and `k`, it prints `-1`. The function does not return any value; it only prints the results to the console.

