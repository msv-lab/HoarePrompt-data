#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. Each test case consists of an integer n such that 1 ≤ n ≤ 10^5, a string s of length n consisting of '0's and '1's, and a string f of length n consisting of '0's and '1's. The sum of n over all test cases does not exceed 10^5.
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
        
    #State: The results of each test case printed one by one. The variables `t`, `n`, `s1`, `s2`, `a1`, `a2`, `hd`, and `res` will be in the state corresponding to the last test case processed.
#Overall this is what the function does:The function processes multiple test cases, each consisting of two binary strings of equal length. For each test case, it calculates and prints a result based on the number of '1's in the strings and the positions where one string has '1' and the other has '0'.

