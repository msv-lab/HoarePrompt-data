#State of the program right berfore the function call: The function `func` is expected to be called within a program that handles multiple test cases. Each test case consists of an integer n (1 ≤ n ≤ 2·10^5), an integer m (1 ≤ m ≤ 10^4), a list of n integers a (1 ≤ a_i ≤ 10^4), and a string s of length n consisting only of the characters 'L' and 'R'. The sum of n values across all test cases does not exceed 2·10^5.
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
        
    #State: The loop has executed `int(input())` times. For each execution, `ii` ranges from 0 to `int(input()) - 1`. The variables `n`, `m`, `a`, and `t` are updated with new user input values for each test case. The variable `l` is the count of 'L' characters in the string `t` for each test case. The variable `k` is the final value of the modulo operation `k % m` after all iterations of the inner loop for each test case. The variables `q1` and `q2` are updated based on the characters in `t` and the initial values of `q1` and `q2` for each test case. The list `y` is a list of `n` integers where each element is the result of the loop's computation for each test case.
#Overall this is what the function does:The function `func` processes multiple test cases. For each test case, it reads an integer `n` and an integer `m` from user input, followed by a list of `n` integers `a` and a string `s` of length `n` containing only 'L' and 'R'. It then computes a list `y` of `n` integers, where each element is the result of a series of modulo operations based on the characters in `s` and the values in `a`. The final state of the program after the function concludes is that the list `y` is printed for each test case, and the function is ready to process the next test case if any.

