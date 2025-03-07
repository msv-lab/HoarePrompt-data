#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 2⋅10^4. For each test case, n is an integer such that 3 ≤ n ≤ 3⋅10^5, and a is a string of length n consisting only of '0' and '1'. The sum of all n values across all test cases does not exceed 3⋅10^5.
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
        
    #State: Output State: `t` is 0; `pos` is equal to the length of `arr`; `z_r` is equal to the initial value of `z` minus the count of 0s in `arr`; `o_r` is equal to the initial value of `o` minus the count of 1s in `arr`; `o_l` is equal to the count of 1s in `arr`; `z_l` is equal to the count of 0s in `arr`; `b_d` is the minimum value of `abs(n / 2 - pos)` where `pos` is updated in each iteration; `ans` is the position where the conditions `o_r >= (z_r + o_r) / 2` and `z_l >= (z_l + o_l) / 2` are satisfied and `b_d` is minimized, or it remains unchanged if no such position is found.
    #
    #This means that after all iterations of the loop have finished, `t` will be 0 since it is decremented by 1 in each iteration until it reaches 0. The variable `pos` will be equal to the length of `arr` because the loop processes each element of `arr` exactly once. The values of `z_r` and `o_r` will reflect the counts of 0s and 1s remaining in `arr` after processing, while `z_l` and `o_l` will reflect the counts of 0s and 1s encountered so far. The variable `b_d` will hold the minimum distance found where the specified conditions on `o_r`, `z_l`, and `z_r` are met, and `ans` will be the position corresponding to this minimum distance, or it will remain unchanged if no such position exists.
#Overall this is what the function does:The function processes multiple test cases, each consisting of a positive integer \( t \), an integer \( n \), and a binary string \( a \). For each test case, it calculates a specific position \( pos \) based on certain conditions related to the counts of '0's and '1's in the string. The function then prints this position and continues to the next test case until all test cases are processed. After processing all test cases, the function ensures that the counter \( t \) is zero, and the variable \( pos \) reflects the last processed position in the string.

