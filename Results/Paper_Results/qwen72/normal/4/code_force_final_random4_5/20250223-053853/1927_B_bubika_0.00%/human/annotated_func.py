#State of the program right berfore the function call: t is an integer such that 1 \le t \le 10^4, n is an integer such that 1 \le n \le 2 \cdot 10^5, and a is a list of n integers where 0 \le a_i < n. The sum of n over all test cases does not exceed 2 \cdot 10^5, and for each trace a, there exists a valid string s consisting of lowercase Latin letters a-z.
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
        
    #State: `t` is an integer such that 1 ≤ t ≤ 10^4, `n` is an integer such that 1 ≤ n ≤ 2 · 10^5, `a` is the string 'abcdefghijklmnopqrstuvwxyz', `b` is a list of integers where each element is incremented by the number of times its corresponding index in `a` was used in the output strings `r` during the loop iterations.
#Overall this is what the function does:The function `func` processes a series of test cases. Each test case involves reading an integer `n` and a list `s` of `n` integers. For each integer in `s`, the function maps it to a corresponding character in the alphabet string 'abcdefghijklmnopqrstuvwxyz' and constructs a string `r`. The function then prints the string `r` for each test case. After processing all test cases, the list `b` contains the count of how many times each character in the alphabet string was used in the output strings `r`. The function does not return any value.

