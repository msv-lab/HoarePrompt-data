#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. For each test case, n is a positive integer such that 1 ≤ n ≤ 10^5, and both s and f are strings of length n consisting of '0' and '1' characters. The sum of n over all test cases does not exceed 10^5.
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
        
    #State: Output State: The value of `res` after all iterations of the loop have completed for each input pair `(s1, s2)`.
    #
    #To explain in more detail:
    #- For each input integer `t`, the loop processes `t` pairs of binary strings `s1` and `s2`.
    #- For each pair, it calculates the difference `hd` between the number of '1's in `s1` and `s2`.
    #- It then iterates over the length `n` of the strings, adjusting `res` based on certain conditions.
    #- After processing all pairs, `res` will hold the sum of adjustments made during the loop iterations for each pair `(s1, s2)`.
#Overall this is what the function does:The function processes multiple test cases, where for each test case, it reads an integer `t` representing the number of binary string pairs to process, followed by `t` pairs of binary strings `s1` and `s2`. For each pair, it calculates the difference in the number of '1's between `s1` and `s2`, and adjusts a result variable `res` based on specific conditions involving the characters at corresponding positions in the strings. After processing all pairs, it prints the final value of `res`, which represents the total number of positions where `s1` has a '1' and `s2` has a '0'.

