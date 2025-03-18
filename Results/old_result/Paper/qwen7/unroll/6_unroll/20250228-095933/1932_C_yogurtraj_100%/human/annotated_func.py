#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4; for each test case, n and m are positive integers such that 1 ≤ n ≤ 2⋅10^5 and 1 ≤ m ≤ 10^4; the array a is a list of n integers such that 1 ≤ a_i ≤ 10^4 for all 1 ≤ i ≤ n; the string s is a string of length n consisting only of the characters 'L' and 'R'.
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
        
    #State: Output State: t is a positive integer such that 1 ≤ t ≤ 10^4; for each test case, n and m are positive integers such that 1 ≤ n ≤ 2⋅10^5 and 1 ≤ m ≤ 10^4; the array a is a list of n integers such that 1 ≤ a_i ≤ 10^4 for all 1 ≤ i ≤ n; the string s is a string of length n consisting only of the characters 'L' and 'R'; the variable y is a list of n integers calculated based on the operations inside the loop, with the last element being the value of k after processing the string t from right to left.
#Overall this is what the function does:The function processes a series of test cases. For each test case, it reads two integers \(n\) and \(m\), an array \(a\) of \(n\) integers, and a string \(t\) of length \(n\) containing only 'L' and 'R'. It then calculates a sequence of integers \(y\) based on the values in \(a\) and the direction indicated by \(t\). Specifically, it computes the product of selected elements from \(a\) modulo \(m\), following the directions in \(t\) from right to left, storing the results in \(y\). Finally, it prints the sequence \(y\).

