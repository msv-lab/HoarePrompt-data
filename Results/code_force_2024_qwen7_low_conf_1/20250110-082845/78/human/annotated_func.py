#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4. Each test case consists of n, m, and k, where 2 <= n, m <= 10^9 and 2 <= k <= 2 * 10^5. For each test case, there are k pairs of integers r_i and c_i, where 1 <= r_i <= n and 1 <= c_i <= m, representing the coordinates of the fountains. It is guaranteed that all fountains are in different cells and none of them is at (n, 1). Additionally, the sum of k over all test cases does not exceed 2 * 10^5.
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
        
    #State of the program after the  for loop has been executed: `t` is the number of test cases, `answer` is a list of length `k` where for each `i`, `answer[i]` is 1 if there exists a pair `(j, i)` in `f` such that `f[j][0] < f[j + 1][0]`, otherwise `answer[i]` is 0; `f` is a list of lists where each sublist has at least one element, `s` is the sum of \((c[i][0] - 1) * (c[i][1] - f[-1][1])\) for all `i` where `c[i][1] > f[-1][1]\), `n`, `m`, and `k` are the last `n`, `m`, and `k` read from input, `c` is the last `c` list read from input, and `i` is the last `i` in the loop.
#Overall this is what the function does:The function processes multiple test cases, each consisting of integers \(n\), \(m\), and \(k\), along with \(k\) pairs of integers \((r_i, c_i)\) representing the coordinates of fountains. It calculates a sum \(s\) based on certain conditions involving the fountain coordinates and then prints this sum along with a list of binary values indicating whether certain conditions are met for each fountain coordinate. After processing all test cases, the function outputs the total sum \(s\) plus an additional term related to the last fountain row and the column width \(m\), followed by the binary list.

