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
        
    #State: Output State: The output state will be a list of integers, where each integer represents the position `pos` that minimizes the distance to the center of the array while satisfying the conditions on the counts of '0's and '1's in the left and right parts of the array.
    #
    #Explanation: For each test case, the loop calculates the position `pos` in the binary string `arr` that meets the criteria of having at least half of the '1's on the right side and at least half of the '0's on the left side, with the additional condition that this position is closest to the center of the array. The loop then prints this position for each test case.
#Overall this is what the function does:The function processes multiple test cases, each containing an integer \( t \) (number of test cases), an integer \( n \) (length of a binary string), and a binary string \( a \). For each test case, it finds and prints the position \( pos \) in the binary string that minimizes the distance to the center of the array while ensuring that the number of '1's on the right side is at least half of the total '1's and the number of '0's on the left side is at least half of the total '0's. If no such position exists, it prints the position that minimizes the distance to the center without the count constraints.

