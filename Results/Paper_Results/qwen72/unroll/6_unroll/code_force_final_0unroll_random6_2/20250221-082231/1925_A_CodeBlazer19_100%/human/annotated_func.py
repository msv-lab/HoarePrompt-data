#State of the program right berfore the function call: n and k are positive integers such that 1 <= n <= 26 and 1 <= k <= 26.
def func():
    t = int(input())
    for i in range(t):
        n, k = map(int, input().split())
        
        print('abcdefghijklmnopqrstuvwxyz'[:k] * n)
        
    #State: The values of `n` and `k` are updated based on the last input provided during the loop execution, and `t` remains unchanged.
#Overall this is what the function does:The function reads an integer `t` from the input, which represents the number of test cases. For each test case, it reads two positive integers `n` and `k` (where 1 <= n <= 26 and 1 <= k <= 26) from the input. It then prints a string that consists of the first `k` letters of the English alphabet repeated `n` times. After processing all test cases, the function does not return any value, and the state of the program includes the updated values of `n` and `k` based on the last test case, while `t` remains unchanged.

