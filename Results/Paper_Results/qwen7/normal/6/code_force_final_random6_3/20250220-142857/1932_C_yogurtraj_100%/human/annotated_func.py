#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. For each test case, n and m are positive integers satisfying 1 ≤ n ≤ 2⋅10^5 and 1 ≤ m ≤ 10^4. The array a is a list of n integers where 1 ≤ a_i ≤ 10^4 for all 1 ≤ i ≤ n. The string s is a sequence of n characters, each being either 'L' or 'R'.
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
        
    #State: After the loop executes all its iterations, `i` will be -1, indicating that the loop has completed all its iterations. The variable `k` will hold the final value after all the multiplications and mod operations as per the conditions inside the loop. The list `y` will contain the values of `k` for each iteration starting from the last index down to the second index (since `y[-1]` is set to `k` in the last iteration). The values of `n`, `m`, `a`, `t`, `l`, `q1`, and `q2` will remain unchanged from their last known state before the loop started.
#Overall this is what the function does:The function processes a series of test cases. For each test case, it reads the number of elements \( n \), the modulus \( m \), an array \( a \) of \( n \) integers, and a string \( t \) of length \( n \) consisting of 'L' and 'R'. It then calculates a sequence of values based on the direction indicated by 'L' and 'R' in \( t \) and stores these values in a list \( y \). The final list \( y \) is printed, where each element \( y[i] \) represents the product of certain elements in \( a \) modulo \( m \), depending on the direction specified by \( t \).

