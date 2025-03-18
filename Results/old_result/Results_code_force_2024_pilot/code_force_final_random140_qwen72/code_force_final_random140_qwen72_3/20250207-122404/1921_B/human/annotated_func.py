#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, representing the number of test cases. For each test case, n is an integer such that 1 ≤ n ≤ 10^5, representing the number of boxes. s and f are strings of length n, consisting of '0's and '1's, representing the initial and final positions of the cats in the boxes, respectively. The sum of n over all test cases does not exceed 10^5.
def func():
    for _ in range(int(input())):
        n = int(input())
        
        s = input()
        
        t = input()
        
        a = b = 0
        
        for i in range(n):
            a += s[i] > t[i]
            b += s[i] < t[i]
        
        print(max(a, b))
        
    #State: After the loop executes all the iterations, `n` remains unchanged, `i` is `n-1`, `a` is the count of indices where `s[i]` is greater than `t[i]` for all `i` in the range `[0, n-1]`, and `b` is the count of indices where `s[i]` is less than `t[i]` for all `i` in the range `[0, n-1]`.
#Overall this is what the function does:The function reads multiple test cases from the standard input. For each test case, it reads the number of boxes `n`, the initial state of the boxes `s`, and the final state of the boxes `t`. It then calculates and prints the maximum number of positions where the characters in `s` are greater than those in `t` or less than those in `t`. The function does not return any value; instead, it directly prints the result for each test case.

