#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4; for each test case, n is a positive integer such that 1 ≤ n ≤ 2 ⋅ 10^5; the trace a is a list of n non-negative integers such that 0 ≤ a_i < n for all i, and there exists at least one string s consisting of lowercase Latin letters a-z that matches the given trace.
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
        
    #State: t is a positive integer such that 1 ≤ t ≤ 10^4; n is a positive integer such that 1 ≤ n ≤ 2 ⋅ 10^5; the trace a is a list of n non-negative integers such that 0 ≤ a_i < n for all i; the string a is set to 'abcdefghijklmnopqrstuvwxyz'; b is a list of 26 ones (since each character from 'a' is referenced once per iteration of the inner loop for each input value).
#Overall this is what the function does:The function processes multiple test cases, where each test case consists of a positive integer `t`, a positive integer `n`, and a list `a` of `n` non-negative integers. For each test case, it constructs a string `s` by mapping each integer in the list `a` to a corresponding lowercase letter from the alphabet `a`, and then increments the count of that letter in another list `b`. After processing all test cases, the function prints the constructed string `s` for each case.

