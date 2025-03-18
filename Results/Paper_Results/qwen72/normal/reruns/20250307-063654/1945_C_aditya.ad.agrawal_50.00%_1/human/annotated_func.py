#State of the program right berfore the function call: The function `func` is expected to be called within a context where it processes multiple test cases. Each test case includes an integer `n` (3 ≤ n ≤ 3·10^5) representing the number of houses, and a string `a` of length `n` consisting only of '0' and '1', where '0' indicates a resident's preference to live on the left side and '1' indicates a preference to live on the right side. The function should be able to handle up to 2·10^4 test cases, and the sum of `n` over all test cases does not exceed 3·10^5.
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
        
    #State: `t` is 0, `n` is an input integer where 3 ≤ n ≤ 3·10^5, `input_string` is a string input by the user, `arr` is a list of integers where each integer is the integer representation of each character in `input_string`, `z` is the number of times 0 appears in `arr`, `o` is the number of times 1 appears in `arr`, `dist` is `abs(n / 2)`, `pos` is `n`, `z_l` is the number of 0s in the first `n` elements of `arr`, `o_l` is the number of 1s in the first `n` elements of `arr`, `z_r` is 0, `o_r` is 0, `ans` is the position where the conditions `o_r >= (z_r + o_r) / 2` and `z_l >= (z_l + o_l) / 2` and `b_d > abs(n / 2 - pos)` were last met, or 0 if these conditions were never met, `b_d` is the minimum value of `abs(n / 2 - pos)` where the conditions were met, or 30001 if the conditions were never met.
#Overall this is what the function does:The function `func` processes multiple test cases, each containing an integer `n` (3 ≤ n ≤ 3·10^5) representing the number of houses, and a string `a` of length `n` consisting only of '0' and '1', where '0' indicates a resident's preference to live on the left side and '1' indicates a preference to live on the right side. For each test case, the function computes and prints the position `pos` that minimizes the absolute difference between the number of houses on the left and right sides while ensuring that the number of residents on the left side who prefer to live on the left is at least half of the total residents on the left, and the number of residents on the right side who prefer to live on the right is at least half of the total residents on the right. The function handles up to 2·10^4 test cases, and the sum of `n` over all test cases does not exceed 3·10^5. After processing all test cases, the function terminates with `t` being 0.

