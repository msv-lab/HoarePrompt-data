#State of the program right berfore the function call: t is an integer such that 1 <= t <= 2 * 10^4. For each test case, n is an integer such that 3 <= n <= 3 * 10^5, and a is a string of length n consisting only of the characters '0' and '1'. The sum of n over all test cases does not exceed 3 * 10^5.
def func():
    t = int(input())
    while t:
        n = int(input())
        
        input_string = input()
        
        arr = [int(ch) for ch in input_string]
        
        z = arr.count(0)
        
        o = arr.count(1)
        
        z_r = z
        
        o_r = o
        
        z_l = 0
        
        o_l = 0
        
        dist, ans, pos = abs(n / 2), 0, 0
        
        if o_r >= (z_r + o_r) / 2:
            b_d = dist
        else:
            b_d = 30001
        
        for i in arr:
            pos += 1
            if i == 0:
                z_l += 1
                z_r -= 1
            else:
                o_l += 1
                o_r -= 1
            if o_r >= (z_r + o_r) / 2 and z_l >= (z_l + o_l) / 2 and b_d > abs(n / 
                2 - pos):
                ans = pos
                b_d = abs(n / 2 - pos)
        
        print(ans)
        
        t -= 1
        
    #State: `t` is 0; `n` is the length of the last input string; `a` is the last input string of '0's and '1's; `input_string` is the same as `a`; `arr` is the list of integers derived from `input_string`; `z` is the count of '0's in `a`; `o` is the count of '1's in `arr`; `z_r` is 0; `o_r` is 0; `z_l` is the count of '0's in `arr`; `o_l` is the count of '1's in `arr`; `dist` is `abs(n / 2)`; `pos` is `n`; `ans` is the last position where the conditions were met; `b_d` is the smallest distance from `n / 2` where the conditions were met.
#Overall this is what the function does:The function processes multiple test cases. For each test case, it takes an integer `n` and a binary string `a` of length `n` consisting of '0's and '1's. It calculates and prints the position in the string where the number of '0's to the left and the number of '1's to the right are balanced, or as close to balanced as possible, relative to the middle of the string.

