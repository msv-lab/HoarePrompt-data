#State of the program right berfore the function call: The function `func` is expected to process multiple test cases. Each test case includes an integer `n` (3 ≤ n ≤ 3·10^5) representing the number of houses, and a string `a` of length `n` consisting only of '0' and '1', where '0' indicates a resident's preference to live on the left side and '1' indicates a preference to live on the right side. The total sum of `n` across all test cases does not exceed 3·10^5.
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
        
    #State: After all iterations of the loop, `pos` is equal to the length of `arr` for each test case, `z_l` is the count of zeros in `arr`, `o_l` is the count of ones in `arr`, `z_r` is 0, `o_r` is 0, `ans` is the position where the conditions `o_r >= (z_r + o_r) / 2` and `z_l >= (z_l + o_l) / 2` and `b_d > abs(n / 2 - pos)` were last met for each test case, `b_d` is the absolute difference between `n / 2` and the position where the conditions were last met for each test case, and `t` is 0.
#Overall this is what the function does:The function `func` processes multiple test cases, each consisting of an integer `n` and a string `a` of length `n` containing '0' and '1'. For each test case, it calculates and prints the position `pos` that minimizes the absolute difference between the number of houses on the left and right sides while ensuring that the number of residents preferring the right side is at least half of the remaining houses and the number of residents preferring the left side is at least half of the houses already processed. The function does not return any value; it only prints the result for each test case. After processing all test cases, the function completes and `t` is 0.

