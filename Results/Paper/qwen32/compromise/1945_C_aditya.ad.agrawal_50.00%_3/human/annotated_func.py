#State of the program right berfore the function call: The input consists of multiple test cases. Each test case starts with an integer n (3 ≤ n ≤ 3·10^5) representing the number of houses in the village. The next line contains a string a of length n, consisting only of the characters '0' and '1', where '0' indicates a resident wants to live on the left side and '1' indicates a resident wants to live on the right side. The sum of n over all test cases does not exceed 3·10^5.
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
        
    #State: t is 0, n is the input integer from the last test case, a remains unchanged, input_string is the string input by the user for the last test case, arr is the list of integers derived from input_string for the last test case, z is the count of 0s in arr for the last test case, o is the count of 1s in arr for the last test case, z_l is the total count of 0s in arr for the last test case, o_l is the total count of 1s in arr for the last test case, z_r is 0, o_r is 0, dist is abs(n / 2) for the last test case, ans is the position where conditions were met or 0 for the last test case, pos is len(arr) for the last test case, b_d is the minimum abs(n / 2 - pos) where conditions were met or 30001 for the last test case.
#Overall this is what the function does:The function processes multiple test cases, where each test case consists of an integer `n` representing the number of houses in a village and a string `a` of length `n` consisting of '0's and '1's. Each '0' indicates a resident wants to live on the left side, and each '1' indicates a resident wants to live on the right side. The function determines and prints the position in the string where the number of residents wanting to live on the left side and the number of residents wanting to live on the right side are as balanced as possible around the midpoint of the string.

