#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n and m are integers such that 1 ≤ n ≤ 2·10^5 and 1 ≤ m ≤ 10^4. a is a list of n integers where each integer a_i satisfies 1 ≤ a_i ≤ 10^4. s is a string of length n consisting of the characters 'L' and 'R'. The sum of all n values across all test cases does not exceed 2·10^5.
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
        
    #State: `ii` is `t-1`, `n` is the number of elements in the last `a`, `m` is the modulus from the last test case, `a` is the list of integers from the last test case, `t` is the string from the last test case, `l` is the count of 'L' in the last `t`, `y` is the list of results from the last test case, `i` is -1, `q1` and `q2` are the final indices from the last test case, and `k` is the final value of `k` from the last test case.
#Overall this is what the function does:The function processes multiple test cases, each consisting of a list of integers and a corresponding string of 'L' and 'R' characters. For each test case, it computes a new list based on specific rules involving the integers, the string, and a given modulus. The result for each test case is printed as a space-separated string of integers.

