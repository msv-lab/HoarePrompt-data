#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4. For each test case, n and m are integers such that 1 <= n <= 2*10^5 and 1 <= m <= 10^4. a is a list of n integers where each integer a_i satisfies 1 <= a_i <= 10^4. s is a string of length n consisting of the characters 'L' and 'R'. The sum of all n across all test cases does not exceed 2*10^5.
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
        
    #State: The loop has executed `t` times, where `t` is the initial integer input. For each test case, the variables `n`, `m`, `a`, and `t` are read from the input. The list `y` is computed for each test case and printed. The final values of `k`, `q1`, and `q2` are determined by the last iteration of the inner loop for each test case. The variables `ii`, `n`, `m`, `a`, and `t` retain their values from the last test case processed.
#Overall this is what the function does:The function processes multiple test cases, each consisting of an integer `n`, an integer `m`, a list of `n` integers `a`, and a string `s` of length `n` containing 'L' and 'R'. For each test case, it computes a list `y` of length `n` based on the values in `a` and the direction indicators in `s`, and prints the list `y`.

