#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4; for each test case, n and m are positive integers such that 1 ≤ n ≤ 2⋅10^5 and 1 ≤ m ≤ 10^4; a is a list of n integers such that 1 ≤ a_i ≤ 10^4 for each a_i in a; s is a string of length n consisting only of the characters 'L' and 'R'.
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
        
    #State: i is -1, n is the original n, q1 is l - n + 1, q2 is l - 1, y is a list of length n with the last element equal to k and all other elements equal to 0, k is the final value after all multiplications and mod operations have been performed.
#Overall this is what the function does:The function processes a series of test cases. For each test case, it reads two integers \( n \) and \( m \), a list of \( n \) integers \( a \), and a string \( t \) of length \( n \) consisting of 'L' and 'R'. It then calculates a sequence of values based on the string \( t \) and the list \( a \), performing modular multiplications and updates. Finally, it prints a list of these calculated values.

