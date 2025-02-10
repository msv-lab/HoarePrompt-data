#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. For each test case, n and m are positive integers such that 1 ≤ n ≤ 2⋅10^5 and 1 ≤ m ≤ 10^4. The array a is a list of n integers such that 1 ≤ a_i ≤ 10^4 for all 1 ≤ i ≤ n. The string s is a string of length n consisting only of the characters 'L' and 'R'.
def func():
    for _ in range(int(input())):
        n, m = map(int, input().split())
        
        arr = list(map(int, input().split()))
        
        s = input()
        
        l = 0
        
        r = n - 1
        
        for k in s:
            if k == 'L':
                l += 1
            else:
                r -= 1
        
        p = 1
        
        ans = []
        
        for strr in s[::-1]:
            if strr == 'R':
                r += 1
                p = p * arr[r] % m
            else:
                l -= 1
                p = p * arr[l] % m
            ans.append(p)
        
        print(*ans[::-1])
        
    #State: Output State: After the loop executes all iterations, `p` will be the final cumulative product of elements from the array `arr` based on the directions given by the string `s`, taken modulo `m`. The list `ans` will contain all the intermediate values of `p` calculated during each iteration of the loop. The variable `s` will be an empty string, `l` will be the total count of 'L' characters in the original string `s`, and `r` will be the total count of 'R' characters in the original string `s`. The variables `t`, `n`, `m`, `a`, and `arr` will retain their initial values.
    #
    #In simpler terms, after processing all characters in the string `s` (both forward and backward), `p` will hold the final result of the product operations described in the loop, and `ans` will contain the sequence of intermediate results. The counts `l` and `r` will reflect the total occurrences of 'L' and 'R' in the original string `s`, respectively.
#Overall this is what the function does:The function processes a series of test cases. For each test case, it takes two positive integers \( n \) and \( m \), an array \( a \) of \( n \) integers, and a string \( s \) of length \( n \) consisting only of 'L' and 'R'. It calculates a cumulative product \( p \) of elements from the array \( a \) based on the directions given by the string \( s \), taking the result modulo \( m \). The function computes this product both forward and backward through the string \( s \), storing each intermediate value in a list \( ans \). Finally, it prints the reversed list \( ans \) containing all intermediate results.

