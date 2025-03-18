#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4. For each test case, n is an integer such that 1 <= n <= 10^5, s and f are strings of length n consisting of '0' and '1' characters only. The sum of n over all test cases does not exceed 10^5.
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
        
    #State: The loop has processed all `t` test cases. For each test case, it has calculated and printed the value of `res`, which represents the minimum number of operations needed to make the number of '1's in `s1` equal to the number of '1's in `s2` by flipping '0's in `s1` to '1's.
#Overall this is what the function does:The function processes multiple test cases, each consisting of two binary strings `s1` and `s2` of the same length `n`. For each test case, it calculates and prints the minimum number of operations required to make the number of '1's in `s1` equal to the number of '1's in `s2` by flipping '0's in `s1` to '1's.

