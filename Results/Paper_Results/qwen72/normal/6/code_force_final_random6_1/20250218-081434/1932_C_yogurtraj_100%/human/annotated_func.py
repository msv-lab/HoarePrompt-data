#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, n and m are integers such that 1 ≤ n ≤ 2·10^5 and 1 ≤ m ≤ 10^4, a is a list of n integers such that 1 ≤ a_i ≤ 10^4, and s is a string of length n consisting of characters 'L' and 'R'. The sum of n over all test cases does not exceed 2·10^5.
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
        
    #State: `ii` is `t - 1`, `n` is an input integer greater than or equal to 1, `m` is an input integer greater than 0, `a` is a list of integers input by the user, `t` is the input string, `l` is the number of times 'L' appears in `t`, `y` is a list of `n` integers where each element is updated to `k` based on the loop, and `k` is the final value after all iterations, `i` is -1, `q1` is either -1 or `l - n` depending on the last character of `t`, and `q2` is either `l + n - 1` or `l + n` depending on the last character of `t`.
#Overall this is what the function does:The function reads multiple test cases from the input. For each test case, it takes an integer `n`, an integer `m`, a list of `n` integers `a`, and a string `t` of length `n` consisting of characters 'L' and 'R'. It then processes the list `a` and the string `t` to compute a new list `y` of `n` integers. Each element in `y` is calculated based on the values in `a`, the string `t`, and the modulus `m`. The function prints the list `y` for each test case. The final state of the program after the function concludes is that the list `y` has been computed and printed for each test case, and the input variables `n`, `m`, `a`, and `t` are no longer needed for further processing.

