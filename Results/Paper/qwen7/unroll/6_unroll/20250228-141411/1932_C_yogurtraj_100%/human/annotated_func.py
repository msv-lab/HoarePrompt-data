#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. For each test case, n and m are positive integers such that 1 ≤ n ≤ 2⋅10^5 and 1 ≤ m ≤ 10^4. The array a is a list of n integers such that 1 ≤ a_i ≤ 10^4 for all i. The string s is a string of length n consisting only of the characters 'L' and 'R'.
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
        
    #State: Output State: t is a positive integer such that 1 ≤ t ≤ 10^4. For each test case, n and m are positive integers such that 1 ≤ n ≤ 2⋅10^5 and 1 ≤ m ≤ 10^4. The array a is a list of n integers such that 1 ≤ a_i ≤ 10^4 for all i. The string s is a string of length n consisting only of the characters 'L' and 'R'. After executing the loop, the variable y is a list of n integers where each element y[i] (0 ≤ i < n) is calculated based on the operations inside the loop using the initial values of n, m, a, and s.
#Overall this is what the function does:The function processes `t` test cases. For each test case, it takes two positive integers `n` and `m`, an array `a` of `n` integers, and a string `s` of length `n` consisting of 'L' and 'R'. It then calculates a list `y` of `n` integers based on the values in `a`, the modulo `m`, and the direction indicated by `s`. Specifically, it computes each element `y[i]` by traversing the array `a` according to the directions specified in `s` and performing modular multiplications. Finally, it prints the list `y` for each test case.

