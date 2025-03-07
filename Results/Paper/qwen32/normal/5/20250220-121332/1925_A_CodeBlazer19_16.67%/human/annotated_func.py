#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 676, and for each of the t test cases, n and k are integers such that 1 ≤ n ≤ 26 and 1 ≤ k ≤ 26.
def func():
    t = int(input())
    for i in range(t):
        n, k = map(int, input().split())
        
        s = ''
        
        for j in range(97, k + 97):
            s += chr(j)
        
        if k == 1:
            print(n * s)
        else:
            print((2 - (n == 1)) * s)
        
    #State: `t` is an integer input such that 1 ≤ `t` ≤ 676; `i` is equal to `t`; `n` and `k` are the values from the last iteration; `s` is a string of `k` consecutive lowercase letters starting from 'a'. If `k` is equal to 1, then `s` is "a". Otherwise, `k` is not equal to 1, and `s` is a string of `k` consecutive lowercase letters starting from 'a'.
#Overall this is what the function does:The function reads an integer `t` representing the number of test cases. For each test case, it reads two integers `n` and `k`. It constructs a string `s` of `k` consecutive lowercase letters starting from 'a'. If `k` is 1, it prints the string `s` repeated `n` times. Otherwise, it prints the string `s` repeated twice if `n` is greater than 1, or just once if `n` is 1.

