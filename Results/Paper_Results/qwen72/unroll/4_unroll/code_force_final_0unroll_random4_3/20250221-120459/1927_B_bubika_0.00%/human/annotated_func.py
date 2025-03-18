#State of the program right berfore the function call: t is a positive integer such that 1 <= t <= 10^4, n is a positive integer such that 1 <= n <= 2 \cdot 10^5, and a is a list of n integers where 0 <= a_i < n. The sum of n over all test cases does not exceed 2 \cdot 10^5, and for each trace a, there exists a suitable string s consisting of lowercase Latin letters a-z.
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
        
    #State: `t` is a positive integer such that 1 <= t <= 10^4, `n` is a positive integer such that 1 <= n <= 2 \cdot 10^5, `a` is the string 'abcdefghijklmnopqrstuvwxyz', `b` is a list of 26 integers where each integer is the count of how many times the corresponding character in `a` has been appended to `r` in the loop.
#Overall this is what the function does:The function `func` reads multiple test cases from the standard input. For each test case, it reads an integer `n` and a list of integers `s`. It then constructs a string `r` by mapping each integer in `s` to a corresponding character in the alphabet 'abcdefghijklmnopqrstuvwxyz' and increments a count for each character used. The function prints the constructed string `r` for each test case. The function does not return any value. After the function concludes, `t` remains a positive integer (1 <= t <= 10^4), `n` is the last read positive integer (1 <= n <= 2 \cdot 10^5), `a` is the string 'abcdefghijklmnopqrstuvwxyz', and `b` is a list of 26 integers representing the counts of how many times each character in `a` was appended to `r` in the loop.

