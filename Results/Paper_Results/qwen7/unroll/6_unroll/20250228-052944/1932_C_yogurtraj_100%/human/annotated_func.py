#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. For each test case, n and m are positive integers satisfying 1 ≤ n ≤ 2⋅10^5 and 1 ≤ m ≤ 10^4. The array a is a list of n integers where 1 ≤ a_i ≤ 10^4 for all 1 ≤ i ≤ n. The string s is a string of length n consisting only of the characters 'L' and 'R'.
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
        
    #State: Output State: t is a positive integer such that 1 ≤ t ≤ 10^4. For each test case, n and m are positive integers satisfying 1 ≤ n ≤ 2⋅10^5 and 1 ≤ m ≤ 10^4. The array a is a list of n integers where 1 ≤ a_i ≤ 10^4 for all 1 ≤ i ≤ n. The string s is a string of length n consisting only of the characters 'L' and 'R'. After executing the loop, the variable y is a list of n integers representing the computed values based on the given rules, with y[-1] being the last computed value and y[i] for 0 ≤ i < n-1 being the intermediate values calculated during the backward iteration through the string s.
#Overall this is what the function does:The function processes a series of test cases. For each test case, it reads two positive integers \( n \) and \( m \), an array \( a \) of \( n \) integers, and a string \( s \) of length \( n \) consisting only of 'L' and 'R'. Based on the string \( s \), it calculates a sequence of integers \( y \) where each element \( y[i] \) (for \( 0 \leq i < n-1 \)) is derived from the previous elements and the array \( a \). The final element \( y[-1] \) is also calculated according to specific rules involving the last character of \( s \) and the array \( a \). The function then prints the sequence \( y \) for each test case.

