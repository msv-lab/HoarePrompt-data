#State of the program right berfore the function call: The function `func` is expected to be called within a context that provides the necessary inputs as described in the problem statement. Specifically, the inputs should be provided through standard input or a similar mechanism, and they should consist of multiple test cases. Each test case includes two integers n and m, a list of n integers a, and a string s of length n consisting of characters 'L' and 'R'. The constraints are 1 ≤ t ≤ 10^4, 1 ≤ n ≤ 2·10^5, 1 ≤ m ≤ 10^4, 1 ≤ a_i ≤ 10^4, and the sum of n across all test cases does not exceed 2·10^5.
def func():
    for ii in range(int(input())):
        n, m = map(int, input().split())
        
        a = list(map(int, input().split()))
        
        t = input()
        
        l = t.count('L')
        
        k = 0
        
        q1 = 0
        
        q2 = 0
        
        if t[-1] == 'L':
            k = a[l - 1] % m
            q1 = l - 2
            q2 = l
        else:
            k = a[l] % m
            q1 = l - 1
            q2 = l + 1
        
        y = [0] * n
        
        y[-1] = k
        
        for i in range(n - 2, -1, -1):
            if t[i] == 'R':
                k = k * a[q2] % m
                q2 += 1
            else:
                k = k * a[q1] % m
                q1 -= 1
            y[i] = k
        
        print(*y)
        
    #State: The loop has processed all the test cases and printed the results. The variables `ii`, `n`, `m`, `a`, `t`, `l`, `k`, `q1`, `q2`, and `y` have been updated and used during the execution of the loop, but their final values are not retained for the next iteration. The loop completes its execution, and the program ends.
#Overall this is what the function does:The function `func` processes multiple test cases. For each test case, it takes two integers `n` and `m`, a list of `n` integers `a`, and a string `s` of length `n` containing characters 'L' and 'R'. It computes a list `y` of `n` integers where each element is derived based on the characters in `s` and the values in `a`, modulo `m`. The function prints the list `y` for each test case. After processing all test cases, the function completes its execution, and the program ends.

