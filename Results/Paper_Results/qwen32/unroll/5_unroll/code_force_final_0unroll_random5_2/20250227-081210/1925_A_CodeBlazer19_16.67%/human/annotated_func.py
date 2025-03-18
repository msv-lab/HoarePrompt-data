#State of the program right berfore the function call: t is an integer such that 1 <= t <= 676, and for each of the t test cases, n and k are integers such that 1 <= n <= 26 and 1 <= k <= 26.
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
        
    #State: The output state consists of `t` printed lines, each corresponding to the result of the loop's print statement for each test case. Each line is either the string `s` repeated `n` times if `k == 1`, an empty string if `k > 1` and `n == 1`, or the string `s` repeated twice if `k > 1` and `n > 1`.
#Overall this is what the function does:The function processes `t` test cases, where each test case consists of two integers `n` and `k`. For each test case, it constructs a string `s` containing the first `k` lowercase letters of the alphabet. It then prints the string `s` repeated `n` times if `k` is 1, or prints `s` repeated twice if `k` is greater than 1 and `n` is greater than 1, or prints an empty string if `k` is greater than 1 and `n` is 1.

