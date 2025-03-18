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
        
    #State: The loop will execute `t` times, and for each iteration, it will read two integers `n` and `k` from the input. If `k` is 1, it will print `n` repetitions of the string containing the first `k` lowercase letters of the alphabet. If `k` is greater than 1, it will print `2 - (n == 1)` repetitions of the string containing the first `k` lowercase letters of the alphabet. The values of `n` and `k` will be updated with each iteration, and the variable `s` will be reset to an empty string at the beginning of each iteration.
#Overall this is what the function does:The function `func` reads an integer `t` from the input, indicating the number of test cases. For each test case, it reads two integers `n` and `k` from the input, where `1 <= n <= 26` and `1 <= k <= 26`. It then constructs a string `s` consisting of the first `k` lowercase letters of the alphabet. If `k` is 1, it prints the string `s` repeated `n` times. If `k` is greater than 1, it prints the string `s` repeated `2` times if `n` is greater than 1, and `1` time if `n` is 1. The function does not return any value.

