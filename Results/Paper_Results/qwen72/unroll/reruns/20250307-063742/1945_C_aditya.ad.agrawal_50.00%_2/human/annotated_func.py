#State of the program right berfore the function call: The function should be called with a list of test cases, where each test case is a tuple containing an integer n (3 ≤ n ≤ 3·10^5) and a string a of length n consisting only of '0' and '1'. The list of test cases should be passed as an argument to the function. The number of test cases t should be an integer such that 1 ≤ t ≤ 2·10^4, and the sum of n over all test cases should not exceed 3·10^5.
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
        
    #State: The loop has finished executing all test cases, and the variable `t` is 0. The function has printed the optimal position `ans` for each test case, which is the position where the number of '1's to the right and the number of '0's to the left are as balanced as possible, closest to the middle of the string.
#Overall this is what the function does:The function reads an integer `t` indicating the number of test cases. For each test case, it reads an integer `n` and a string `a` of length `n` consisting of '0's and '1's. It then calculates and prints the optimal position `ans` for each test case, which is the position where the number of '1's to the right and the number of '0's to the left are as balanced as possible, closest to the middle of the string. After processing all test cases, the function terminates with `t` set to 0. The function does not return any value.

