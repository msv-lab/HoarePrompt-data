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
        
    #State: `r` is printed for each test case as a sequence of characters based on the counts in `b`, and `b` is reset to 26 zeros for each new test case. `a` and `t` remain unchanged.
#Overall this is what the function does:The function processes multiple test cases. For each test case, it reads an integer `n` and a list `s` of `n` integers. It then constructs and prints a string `r` of length `n` where each character corresponds to the position of the integers in `s` in a cyclic order starting from 'a' to 'z'. The function ensures that the string `r` is valid according to the given trace for each test case.

