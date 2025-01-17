#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4. Each test case consists of n, m, and k, where 2 <= n, m <= 10^9 and 2 <= k <= 2 * 10^5. There are k pairs of integers r_i and c_i, where 1 <= r_i <= n and 1 <= c_i <= m, representing the coordinates of fountains. All fountains have distinct positions, and no fountain is at (n, 1).
def func():
    t = int(input())
    for z in range(t):
        n, m, k = map(int, input().split())
        
        c = []
        
        for i in range(k):
            x, y = map(int, input().split())
            c.append((y, x, i))
        
        c.sort()
        
        f = [(1, 0, 0)]
        
        s = 0
        
        answer = [0] * k
        
        for i in range(k):
            if c[i][1] > f[-1][1]:
                s += (c[i][0] - 1) * (c[i][1] - f[-1][1])
                f.append((c[i][0], c[i][1], c[i][2]))
        
        answer[f[-1][2]] = 1
        
        for i in range(1, len(f) - 1):
            if f[i][0] < f[i + 1][0]:
                answer[f[i][2]] = 1
        
        print(s + (n - f[-1][1]) * m)
        
        print(*answer)
        
    #State of the program after the  for loop has been executed: `total` is 0, `i` is `len(f) - 1`, `c` is a list of `k` tuples sorted by the first element, `n` is the last new input integer, `m` is the last new input integer, `k` is the last new input integer, `x` is the last first integer input, `y` is the last second integer input, `s` is the accumulated sum of \((c[i][0] - 1) * (c[i][1] - f[-1][1])\) for all `i` where \(c[i][1] > f[-1][1]\), `f` is a list of tuples from `c` that satisfy the condition \(c[i][1] > f[-1][1]\), and `answer` is a list of `k` zeros with multiple elements set to 1 based on the indices `f[i][2]` where the condition `f[i][0] < f[i + 1][0]` is true; the output of the program is `s + (n - f[-1][1]) * m`.
#Overall this is what the function does:The function processes `t` test cases, where `t` is an integer such that \(1 \leq t \leq 10^4\). For each test case, it accepts three integers `n`, `m`, and `k` with specified ranges, and `k` pairs of integers representing fountain coordinates. The function then calculates and prints two outputs for each test case:
1. A sum `s` which is the result of the expression \((c[i][0] - 1) * (c[i][1] - f[-1][1])\) for all `i` where \(c[i][1] > f[-1][1]\).
2. A list `answer` of length `k` where each element is 1 if the corresponding fountain index satisfies certain conditions, and 0 otherwise.
Specifically, the function sorts the fountain coordinates by the first element, iterates through them to calculate `s`, and updates the `answer` list based on the relative positions of the fountains. After processing all test cases, the function prints the total sum `s` plus the product of `n - f[-1][1]` and `m`, followed by the `answer` list.

