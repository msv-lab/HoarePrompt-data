#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, each test case consists of n and m where 1 ≤ n ≤ 2·10^5 and 1 ≤ m ≤ 10^4, a is a list of n integers where 1 ≤ a_i ≤ 10^4, and s is a string of n characters, each being either 'L' or 'R'. The sum of n over all test cases does not exceed 2·10^5.
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
        
    #State: The loop iterates through each test case, and for each test case, it calculates and prints a list `y` of length `n`. The list `y` contains the results of a series of modular multiplications based on the values in the list `a`, the string `s`, and the integer `m`. After the loop finishes, the variables `t`, `n`, `m`, `a`, and `s` retain their initial values, as they are not modified within the loop. The list `y` is printed for each test case, and the loop moves on to the next test case if any remain.
#Overall this is what the function does:The function `func` processes multiple test cases. For each test case, it reads the number of elements `n` and a modulus value `m`, followed by a list of `n` integers `a` and a string `s` of `n` characters ('L' or 'R'). It then calculates a list `y` of length `n`, where each element is the result of a series of modular multiplications based on the values in `a`, the characters in `s`, and the modulus `m`. The final list `y` is printed for each test case. After processing all test cases, the function completes without modifying the input variables `n`, `m`, `a`, or `s`.

