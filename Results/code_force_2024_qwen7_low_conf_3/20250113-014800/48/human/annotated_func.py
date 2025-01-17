#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. For each test case, n is a positive integer such that 1 ≤ n ≤ 10^5. s and f are strings of length n consisting of '0' and '1', where the i-th character of s and f represents whether there is a cat in the i-th box initially and finally, respectively. The sum of n over all test cases does not exceed 10^5.
def func():
    for _ in range(int(input())):
        n = int(input())
        
        s = input()
        
        f = input()
        
        c = 0
        
        for i in range(n):
            if s[i] == f[i] and s[i] == '1':
                c += 1
        
        s1 = 0
        
        for i in s:
            if i == '1':
                s1 += 1
        
        f1 = 0
        
        for i in f:
            if i == '1':
                f1 += 1
        
        print(max(s1, f1) - c)
        
    #State of the program after the  for loop has been executed: t is a positive integer such that 1 ≤ t ≤ 10^4, for each test case, n is a positive integer such that 1 ≤ n ≤ 10^5, s and f are strings of length n consisting of '0' and '1', s1 is the total count of '1's in `s`, f1 is the total count of '1's in `f`, c is the number of indices `i` (where `0 <= i < n`) such that `s[i] == f[i]` and `s[i] == '1', the value printed is `max(s1, f1) - c`.
#Overall this is what the function does:The function processes multiple test cases, where for each test case, it reads two binary strings `s` and `f` representing the initial and final states of boxes, respectively, each potentially containing a cat. It calculates and prints the maximum number of boxes that contained cats either initially or finally, minus the number of boxes that contained cats in both the initial and final states. The function handles up to 10,000 test cases, with each test case containing up to 100,000 boxes. The function correctly accounts for all given constraints and potential edge cases, including scenarios where no boxes contained cats, and all boxes contained cats.

