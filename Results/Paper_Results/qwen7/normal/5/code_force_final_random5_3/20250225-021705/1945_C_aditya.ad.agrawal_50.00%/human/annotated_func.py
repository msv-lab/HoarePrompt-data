#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 2⋅10^4. For each test case, n is an integer such that 3 ≤ n ≤ 3⋅10^5, and a is a string of length n consisting only of '0' and '1'. The sum of n over all test cases does not exceed 3⋅10^5.
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
        
    #State: Output State: After the loop executes all the iterations, `t` will be 0 because it is decremented by 1 in each iteration until it reaches 0. `pos` will be equal to the length of the final `arr`, which is `n`. `o_r` and `o_l` will both be 0 because all ones have been processed. Similarly, `z_r` will be 0, and `z_l` will be the total number of zeros in `arr`. `b_d` will be the minimum absolute difference between `n / 2` and any position that meets the conditions `o_r >= (z_r + o_r) / 2` and `z_l >= (z_l + o_l) / 2`. `ans` will be the position that minimizes this distance.
#Overall this is what the function does:The function processes multiple test cases, each containing a positive integer t, an integer n, and a binary string a. For each test case, it calculates and prints the position pos that minimizes the absolute difference between n/2 and pos, under the condition that the number of ones encountered so far is at least half the total number of ones and the number of zeros to the left is at least half the total number of zeros. After processing all test cases, the function outputs the calculated positions for each case.

