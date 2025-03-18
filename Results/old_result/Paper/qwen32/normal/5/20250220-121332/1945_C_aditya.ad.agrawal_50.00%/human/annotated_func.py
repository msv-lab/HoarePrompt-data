#State of the program right berfore the function call: The input consists of multiple test cases. Each test case starts with an integer n (3 ≤ n ≤ 3·10^5), representing the number of houses. This is followed by a string a of length n, consisting only of the characters '0' and '1', where '0' indicates a resident wants to live on the left side and '1' indicates a resident wants to live on the right side. The sum of n over all test cases does not exceed 3·10^5.
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
        
    #State: t is 0; n is the last input integer; input_string is the last input provided by the user; arr is a list of integers where each integer is a digit from the last input_string; z is the count of the digit 0 in the last arr; o is the count of the digit 1 in the last arr; z_r is 0; o_r is 0; z_l is the count of the digit 0 in the last arr; o_l is the count of the digit 1 in the last arr; dist is abs(n / 2); ans is the position where the condition was last met for the last test case; pos is the length of the last arr; b_d is the minimum distance from n / 2 where the condition was met for the last test case.
#Overall this is what the function does:The function processes multiple test cases, each consisting of an integer `n` and a string `a` of length `n`. The string `a` contains '0's and '1's, where '0' indicates a resident wants to live on the left side and '1' indicates a resident wants to live on the right side. For each test case, the function calculates and prints the position in the string where the difference between the number of '0's and '1's is closest to zero, indicating a balanced distribution of residents on both sides up to that point.

