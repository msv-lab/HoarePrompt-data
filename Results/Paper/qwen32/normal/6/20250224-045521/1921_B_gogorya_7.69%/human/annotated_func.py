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
        
    #State: `t` is 0; `n` is the input integer for the last test case; `s1` and `s2` are the input strings for the last test case; `a1` is the count of '1's in `s1` for the last test case; `a2` is the count of '1's in `s2` for the last test case; `hd` is `max(0, a1 - a2 - n)` for the last test case; `res` is `abs(a1 - a2) + count_of('1' in s1 and '0' in s2 over n iterations) for the last test case.`
#Overall this is what the function does:The function processes `t` test cases, where each test case consists of two binary strings `s1` and `s2` of length `n`. For each test case, it calculates and prints the minimum number of changes required to make the number of '1's in `s1` equal to the number of '1's in `s2` by either changing '1's in `s1` to '0's or '0's in `s2` to '1's.

