#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 2⋅10^4. For each test case, n is an integer such that 3 ≤ n ≤ 3⋅10^5, and a is a string of length n consisting only of '0' and '1'. The sum of n over all test cases does not exceed 3⋅10^5.
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
        
    #State: All elements in `arr` have been processed, `pos` equals the length of `arr` + 1, `z_l` and `z_r` are both 0, `o_l` equals the total number of 1s in `arr`, `o_r` equals the total number of -1s in `arr`, `b_d` equals `abs(n / 2 - len(arr))`, and `ans` equals the last position where the condition `o_r >= (z_r + o_r) / 2 and z_l >= (z_l + o_l) / 2 and (b_d > abs(n / 2 - pos))` was satisfied, or remains 0 if no such position existed.
#Overall this is what the function does:The function processes multiple test cases, each consisting of an integer `n` and a binary string `a` of length `n`. It calculates and prints the position `pos` in the string `a` where the number of zeros to the left of `pos` is at least half the number of zeros plus the number of ones to the left of `pos`, and the number of ones to the right of `pos` is at least half the number of ones plus the number of zeros to the right of `pos`. If no such position exists, it prints 0.

