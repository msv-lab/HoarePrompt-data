#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4; for each test case, n and m are positive integers such that 1 ≤ n ≤ 2⋅10^5 and 1 ≤ m ≤ 10^4; the array a is a list of n integers such that 1 ≤ a_i ≤ 10^4 for all 1 ≤ i ≤ n; the string s is a string of length n consisting only of the characters 'L' and 'R'.
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
        
    #State: Output State: The output state consists of a list `res` of length `n`, where each element `res[i]` (for 1 ≤ i ≤ n-1) is calculated based on the initial product of elements in the array `arr` and then updated according to the direction specified in the string `s`. Specifically, for each character in `s`:
    #
    #- If the character is 'L', the product is divided by the current leftmost element in `arr` and updated.
    #- If the character is 'R', the product is divided by the current rightmost element in `arr` and updated.
    #
    #Each update is taken modulo `m` and then modulo `1000000006`. The first element of `res` (`res[0]`) is the initial product of all elements in `arr` reduced modulo `m` and then modulo `1000000006`.
#Overall this is what the function does:The function processes multiple test cases, each consisting of a positive integer \( n \), another positive integer \( m \), an array \( a \) of \( n \) integers, and a string \( s \) of length \( n \) containing only 'L' and 'R'. For each test case, it calculates a sequence of values based on the initial product of the array elements and updates this product according to the directions in the string \( s \). Specifically, if a character in \( s \) is 'L', the product is divided by the current leftmost element in \( a \); if 'R', the product is divided by the current rightmost element in \( a \). Each update is taken modulo \( m \) and then modulo \( 1000000006 \). The function outputs a list \( res \) of length \( n \), where each element \( res[i] \) (for \( 1 \leq i < n \)) represents the product after the \( i \)-th update, and the first element \( res[0] \) is the initial product of all elements in \( a \) reduced modulo \( m \) and then modulo \( 1000000006 \).

