#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, n is an integer such that 1 ≤ n ≤ 2 · 10^5, and a is a list of n integers where 0 ≤ a_i < n. The sum of n over all test cases does not exceed 2 · 10^5, and for each test case, a valid string s exists that corresponds to the given trace.
def func():
    a = 'abcdefghijklmnopqrstuvwxyz'
    for t in range(int(input())):
        b = [0] * 26
        
        n = int(input())
        
        s = list(map(int, input().split()))
        
        r = ''
        
        for i in s:
            x = b.index(i)
            r += a[x]
            b[x] += 1
        
        print(r)
        
    #State: t is an integer such that 0 ≤ t ≤ 10^4 (t has been decremented by 1 for each iteration), n is an integer such that 1 ≤ n ≤ 2 · 10^5 (unchanged), a is the string 'abcdefghijklmnopqrstuvwxyz' (unchanged). The sum of n over all test cases does not exceed 2 · 10^5 (unchanged), and for each test case, a valid string r is generated from the input string s.
#Overall this is what the function does:The function `func` reads input from the user for a specified number of test cases `t`. For each test case, it reads an integer `n` and a list of integers `s`. It then generates a string `r` by mapping each integer in `s` to a corresponding character in the alphabet string `a` and increments a counter for each character used. The function prints the generated string `r` for each test case. After all test cases are processed, `t` is decremented to 0, `n` and `a` remain unchanged, and the sum of `n` over all test cases does not exceed 2 · 10^5.

