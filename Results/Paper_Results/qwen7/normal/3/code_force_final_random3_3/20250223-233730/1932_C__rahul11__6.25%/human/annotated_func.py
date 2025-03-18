#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4; for each test case, n and m are positive integers such that 1 ≤ n ≤ 2⋅10^5 and 1 ≤ m ≤ 10^4; a is a list of n integers such that 1 ≤ a_i ≤ 10^4 for all 1 ≤ i ≤ n; s is a string of length n consisting only of the characters 'L' and 'R'.
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
        
    #State: After the loop executes all the iterations, `c` will be equal to `n`, `ans` will be the final value obtained by successively dividing it by elements in `arr` based on the direction indicated by characters in `s`, and `res` will be a list of length `n` where each element is the result of `ans` after each iteration, modulo `m` and `MOD`.
#Overall this is what the function does:The function processes multiple test cases, each defined by a positive integer \( t \), two positive integers \( n \) and \( m \), a list of \( n \) integers \( a \), and a string \( s \) of length \( n \) containing only 'L' and 'R'. For each test case, it calculates a sequence of results based on the division of a product of elements in the list \( a \) according to the directions specified in \( s \). The final state of the program includes printing a list of length \( n \) where each element represents the intermediate result of the product modulo \( m \) and a large prime number \( MOD \).

