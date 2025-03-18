#State of the program right berfore the function call: The function `func` is expected to take two positive integers `n` and `k` as input, where 1 <= n <= 26 and 1 <= k <= 26.
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
        
    #State: `t` is 0, `i` is `t - 1`, `n` and `k` are input integers where `k` is greater than 0, `s` is the string containing the first `k` letters of the alphabet starting from 'a', `j` is `k + 96`, and `k + 97` is greater than `k + 96`. If `k` is 1, `s` contains the character 'a' and `j` is 97. If `k` is greater than 1, `s` contains the characters from 'a' to the character with ASCII value `k + 96` and `j` is `k + 96`.
#Overall this is what the function does:The function `func` reads an integer `t` from the input, which represents the number of test cases. For each test case, it reads two positive integers `n` and `k` (where 1 <= n <= 26 and 1 <= k <= 26) from the input. It then constructs a string `s` containing the first `k` letters of the alphabet starting from 'a'. If `k` is 1, it prints the string `s` repeated `n` times. If `k` is greater than 1, it prints the string `s` repeated twice if `n` is greater than 1, and once if `n` is 1. After processing all test cases, the function concludes with `t` being 0 and `i` being `t - 1`. The variables `n`, `k`, and `s` are reset for each test case.

