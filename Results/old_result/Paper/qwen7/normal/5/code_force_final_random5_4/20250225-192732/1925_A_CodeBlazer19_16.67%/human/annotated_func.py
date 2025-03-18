#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 676, and for each test case, n and k are positive integers such that 1 ≤ n ≤ 26 and 1 ≤ k ≤ 26.
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
        
    #State: Output State: `t` must be greater than or equal to 3 and less than or equal to 676, `i` is 3, `k` is an input integer greater than 99, `s` is a string consisting of 95 'û' characters, `j` is 291, `n` is an input integer.
    #
    #Explanation: After the loop has executed all its iterations, `i` will be equal to `t`, which means the loop has run `t` times. Given the constraints, `t` can be any value between 3 and 676 inclusive. The variable `k` must be greater than 99 because the loop starts from 97 and increments by 1 until it reaches `k + 97`. Since the loop runs for each value of `k` up to `t`, `k` must be greater than 99 to ensure the loop completes all iterations. The string `s` will consist of 95 'û' characters because the loop runs from 97 to `k + 97`, and when `k` is greater than 99, the loop runs 95 times. The variable `j` will be 291 at the end of the last iteration. The values of `n` and `t` remain unchanged as they are not affected by the loop body.
#Overall this is what the function does:The function processes multiple test cases defined by the integer `t`. For each test case, it reads two integers `n` and `k`. It then constructs a string `s` containing 95 characters, each being the character corresponding to ASCII values from 97 to `k + 97`. If `k` equals 1, it prints `n` multiplied by the string `s`. Otherwise, it prints `(2 - (n == 1))` multiplied by the string `s`. The function returns nothing but prints the results for each test case.

