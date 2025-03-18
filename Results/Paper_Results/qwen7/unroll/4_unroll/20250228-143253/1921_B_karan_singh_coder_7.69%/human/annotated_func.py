#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. For each test case, n is a positive integer such that 1 ≤ n ≤ 10^5, and s and f are strings of length n consisting of '0' and '1' characters, representing the initial and desired positions of the cats in the boxes, respectively. The sum of n over all test cases does not exceed 10^5.
def func():
    for _ in range(int(input())):
        n = int(input())
        
        s = input()
        
        t = input()
        
        s1 = s.count('1')
        
        t1 = t.count('1')
        
        cnt = 0
        
        for i in range(n):
            cnt += s[i] != t[i]
        
        if s1 == t1:
            print(s1 if cnt else 0)
        else:
            d = abs(s1 - t1)
            print((cnt - d) // 2 + d)
        
    #State: Output State: t is a positive integer such that 1 ≤ t ≤ 10^4. For each test case, n is a positive integer such that 1 ≤ n ≤ 10^5, and s and f are strings of length n consisting of '0' and '1' characters, representing the initial and desired positions of the cats in the boxes, respectively. After executing the loop for all test cases, the sum of n over all test cases does not exceed 10^5. The output for each test case is either the count of differing positions (cnt) adjusted by the difference in the number of '1's in s and f (d), or the absolute difference in the number of '1's (d) depending on whether the counts of '1's are equal or not, printed for each test case.
#Overall this is what the function does:The function processes multiple test cases, where for each test case, it reads a positive integer `n`, two binary strings `s` and `f` of length `n`, and calculates and prints either the count of differing positions between `s` and `f` adjusted by the difference in the number of '1's in `s` and `f`, or the absolute difference in the number of '1's in `s` and `f`. The function does not return any value but outputs the result for each test case.

