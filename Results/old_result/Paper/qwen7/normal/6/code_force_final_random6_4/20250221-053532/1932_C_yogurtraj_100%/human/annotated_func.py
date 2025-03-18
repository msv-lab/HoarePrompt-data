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
        
    #State: The loop has executed all its iterations. Therefore, `i` is -1; `k` is the final value of `k` after the loop completes, which is determined by the sequence of operations inside the loop based on the characters in `t` and the values in `a`. `q1` and `q2` are adjusted accordingly throughout the iterations. The list `y` is a list of `n` elements, where each element from index `0` to `n-2` (inclusive) is updated to the current value of `k` after the corresponding iteration of the loop, and the last element `y[-1]` is set to the final value of `k`.
#Overall this is what the function does:The function processes a series of test cases, each defined by a positive integer \( t \), followed by \( n \) and \( m \) (both positive integers), an array \( a \) of \( n \) integers, and a string \( s \) of length \( n \) consisting only of 'L' and 'R'. For each test case, it calculates a sequence of values based on the given string \( s \) and array \( a \), and outputs this sequence as a list of integers. The final output for each test case is a list \( y \) of \( n \) elements, where each element is derived through a series of multiplications and modulo operations based on the characters in \( s \) and the values in \( a \).

