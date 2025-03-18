#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4. For each test case, n and m are integers such that 1 <= n <= 2*10^5 and 1 <= m <= 10^4. a is a list of n integers where each integer a_i satisfies 1 <= a_i <= 10^4. s is a string of length n consisting of the characters 'L' and 'R'. The sum of all n values across all test cases does not exceed 2*10^5.
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
        
    #State: For each test case, a list `y` of length `n` where each element is computed based on the rules described above.
#Overall this is what the function does:For each test case, the function computes a list `y` of length `n` based on the given integers `n` and `m`, a list `a` of `n` integers, and a string `s` of length `n` consisting of 'L' and 'R'. The list `y` is computed such that each element is derived from the rules involving the characters in `s` and the corresponding values in `a`, modulo `m`. The function prints the list `y` for each test case.

