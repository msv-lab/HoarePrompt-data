#State of the program right berfore the function call: Each test case consists of an integer n (3 ≤ n ≤ 3·10^5) representing the number of houses, followed by a string a of length n consisting only of 0s and 1s, where a_j = 0 if the resident of the j-th house wants to live on the left side of the street, and a_j = 1 if the resident wants to live on the right side. The sum of n over all test cases does not exceed 3·10^5.
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
        
    #State: t is 0.
#Overall this is what the function does:The function processes multiple test cases, each consisting of an integer `n` and a string `a` of length `n` composed of 0s and 1s. It calculates and prints the optimal position to split the residents into two groups such that the number of residents preferring the left side is balanced with those preferring the right side around that position.

