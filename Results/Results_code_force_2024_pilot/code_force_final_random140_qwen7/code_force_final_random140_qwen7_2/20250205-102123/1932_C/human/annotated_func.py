#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4; for each test case, n and m are positive integers such that 1 ≤ n ≤ 2⋅10^5 and 1 ≤ m ≤ 10^4; the array a is a list of n integers such that 1 ≤ a_i ≤ 10^4 for all i; the string s is a string of length n consisting only of the characters 'L' and 'R'.
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
        
        y = str(k)
        
        for i in range(n - 2, -1, -1):
            if t[i] == 'R':
                k = k * a[q2] % m
                q2 += 1
            else:
                k = k * a[q1] % m
                q1 -= 1
            y += ' ' + str(k)
        
        print(y[::-1])
        
    #State: ii is 0, i is -1, k is the final value of k after all iterations, q1 is l-1, q2 is l, y is a string containing spaces followed by the value of k converted to a string for each iteration, n is the original input integer, m is the original input integer, a is the original list of integers, l is the count of 'L' in the input string t, t is the original input string.
#Overall this is what the function does:The function processes a series of test cases. For each test case, it reads two integers \(n\) and \(m\), a list of \(n\) integers \(a\), and a string \(t\) consisting of 'L' and 'R'. It calculates a value \(k\) based on the last character of \(t\) and the elements of \(a\). Then, it iterates through \(t\) from the second last character to the first, updating \(k\) according to the direction indicated by 'L' or 'R'. Finally, it prints a space-separated string of the intermediate values of \(k\) for each character in \(t\), in reverse order.

