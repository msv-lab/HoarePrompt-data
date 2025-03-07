#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n is an integer such that 1 ≤ n ≤ 2 \cdot 10^5, and a is a list of n integers where 0 ≤ a_i < n. The sum of n over all test cases does not exceed 2 \cdot 10^5. It is guaranteed that for each test case, there exists a valid string s that corresponds to the given trace.
def func():
    a = 'abcdefghijklmnopqrstuvwxyz'
    b = [0] * 26
    for t in range(int(input())):
        n = int(input())
        
        s = list(map(int, input().split()))
        
        r = ''
        
        for i in s:
            x = b.index(i)
            r += a[x]
            b[x] += 1
        
        print(r)
        
    #State: The loop has processed all `t` test cases. For each test case, a string `r` is printed, which is a concatenation of characters from `a` based on the indices in `s`. The list `b` has cumulative counts of characters used across all test cases, and variables `t`, `n`, `s`, and `a` reflect their states based on the last test case processed.
#Overall this is what the function does:The function reads multiple test cases, each consisting of an integer `n` and a list `s` of `n` integers. For each test case, it generates and prints a string `r` by mapping each integer in `s` to a character in the alphabet based on the cumulative count of characters used so far.

