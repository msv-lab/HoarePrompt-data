#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4; for each test case, n and m are positive integers such that 1 ≤ n ≤ 2⋅10^5 and 1 ≤ m ≤ 10^4; the array a is a list of n integers such that 1 ≤ a_i ≤ 10^4 for all i; the string s is a string of length n consisting only of the characters 'L' and 'R'.
def func():
    MOD = 10 ** 9 + 6
    for _ in range(int(input())):
        n, m = map(int, input().split())
        
        arr = list(map(int, input().split()))
        
        s = list(input())
        
        res = [0] * n
        
        ans = 1
        
        for i in arr:
            ans *= i
        
        res[0] = ans % m % MOD
        
        c = 1
        
        l = 0
        
        r = n - 1
        
        for k in range(n - 1):
            if s[k] == 'L':
                ans = ans // arr[l] % MOD
                res[c] = ans % m % MOD
                l += 1
            else:
                ans = ans // arr[r] % MOD
                res[c] = ans % m % MOD
                r -= 1
            c += 1
        
        print(*res)
        
    #State: The output state after the loop executes all iterations is as follows:
#Overall this is what the function does:The function processes multiple test cases. For each test case, it takes a positive integer \( n \), another positive integer \( m \), an array \( a \) of \( n \) integers, and a string \( s \) of length \( n \) consisting of 'L' and 'R'. It calculates a result array \( res \) where each element \( res[i] \) is computed based on the product of elements in \( a \) and the direction specified in \( s \). Specifically, for each character in \( s \), if the character is 'L', it divides the current product by the leftmost element in \( a \) and updates the result array; if the character is 'R', it divides the current product by the rightmost element in \( a \) and updates the result array. Finally, it prints the result array for each test case.

