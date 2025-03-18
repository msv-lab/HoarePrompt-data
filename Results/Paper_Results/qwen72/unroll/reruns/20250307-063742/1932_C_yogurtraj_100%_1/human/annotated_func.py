#State of the program right berfore the function call: The function `func` is intended to process multiple test cases. Each test case consists of an integer n (1 ≤ n ≤ 2·10^5), an integer m (1 ≤ m ≤ 10^4), a list of n integers a (1 ≤ a_i ≤ 10^4), and a string s of length n consisting of characters 'L' and 'R'. The total sum of n across all test cases does not exceed 2·10^5.
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
        
    #State: The loop processes each test case and prints the resulting list `y` for each test case. The variables `ii`, `n`, `m`, `a`, `t`, `l`, `k`, `q1`, `q2`, and `y` are updated and used within the loop for each test case, but their values are reset or redefined for the next test case. After all iterations of the loop, the final state of these variables is undefined as they are local to the loop and are not retained between test cases. The only persistent state is the input and the printed output for each test case.
#Overall this is what the function does:The function `func` processes multiple test cases, each consisting of an integer `n`, an integer `m`, a list of `n` integers `a`, and a string `s` of length `n` containing only the characters 'L' and 'R'. For each test case, it computes a list `y` of length `n` where each element is derived from the elements of `a` and the characters in `s` using modulo operations with `m`. The final list `y` is printed for each test case. The function does not return any value; it only prints the results. After processing all test cases, the final state of the function's local variables is undefined, and the only persistent state is the input and the printed output for each test case.

