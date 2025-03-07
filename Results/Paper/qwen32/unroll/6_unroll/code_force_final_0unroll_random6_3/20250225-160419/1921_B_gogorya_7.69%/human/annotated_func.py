#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4. For each test case, n is an integer such that 1 <= n <= 10^5. s and f are strings of length n, where each character is either '0' or '1'. The sum of n over all test cases does not exceed 10^5.
def func():
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        s1 = input()
        
        s2 = input()
        
        a1 = s1.count('1')
        
        a2 = s2.count('1')
        
        hd = a1 - a2
        
        res = abs(a1 - a2)
        
        for i in range(n):
            if hd > 0:
                hd -= 1
                continue
            if s1[i] == '1' and s2[i] == '0':
                res += 1
        
        print(res)
        
    #State: `t` is an integer such that 1 <= `t` <= 10^4; `n` is an integer such that 1 <= `n` <= 10^5; `s` and `f` are strings of length `n`, where each character is either '0' or '1'. The sum of `n` over all test cases does not exceed 10^5.
#Overall this is what the function does:The function reads an integer `t` representing the number of test cases. For each test case, it reads an integer `n` and two binary strings `s1` and `s2` of length `n`. It calculates and prints the minimum number of changes required to make the number of '1's in `s1` equal to the number of '1's in `s2`, allowing only changes from '0' in `s1` to '1'.

