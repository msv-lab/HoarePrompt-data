#State of the program right berfore the function call: t is an integer where 1 ≤ t ≤ 10^4, for each test case: n and m are integers where 1 ≤ n ≤ 2·10^5 and 1 ≤ m ≤ 10^4, a is a list of n integers where 1 ≤ a_i ≤ 10^4, s is a string of n characters, each character is either 'L' or 'R'. The sum of n over all test cases does not exceed 2·10^5.
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
        
    #State: The loop has completed all iterations. `t` is the input string, `ii` is `t - 1`, `n` and `m` are positive integers, `a` is a list of integers provided by the input, `l` is the number of occurrences of 'L' in the input string `t`, `y` is a list of `n` elements where each element is the result of the loop's computation for that index, `i` is -1, `q1` is `l - n + 1` if the last character of `t` is 'L' or `l - n + 2` otherwise, `q2` is `l + n - 1` if the last character of `t` is not 'L' or `l + n` otherwise, and `k` is the final computed value after all iterations.
#Overall this is what the function does:The function processes multiple test cases, each defined by integers `n` and `m`, a list of integers `a` of length `n`, and a string `t` of length `n` containing characters 'L' or 'R'. For each test case, it computes a new list `y` of length `n`, where each element in `y` is derived from the elements in `a` and the characters in `t`, using modular arithmetic with `m`. The final state of the program after the function concludes is that the list `y` for each test case is printed, and the loop has completed all iterations. The variables `ii`, `n`, `m`, `a`, `l`, `y`, `i`, `q1`, and `q2` are no longer in use.

