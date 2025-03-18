#State of the program right berfore the function call: The function `func` is expected to take input parameters, but they are not defined in the provided function definition. Based on the problem description, the function should take a list of integers `c` representing the numbers on the cards, and two integers `n` and `k` where `1 <= n <= 100` and `2 <= k <= 100`. The list `c` should have a length of `n` and each element should be an integer such that `1 <= c_i <= 100`.
def func():
    t = int(input())
    for i in range(t):
        n, k = map(int, input().split())
        
        l = list(map(int, input().split()))
        
        print(k - 1)
        
    #State: `i` is `t-1`, `t` is the total number of iterations, `n` and `k` are the last input integers, `l` is the last list of integers provided by the user.
#Overall this is what the function does:The function `func` reads an integer `t` from the user, indicating the number of test cases. For each test case, it reads two integers `n` and `k`, and a list of `n` integers `l`. It then prints `k - 1` for each test case. The function does not return any value. After the function concludes, `t` is the total number of test cases processed, `i` is `t-1`, `n` and `k` are the last input integers, and `l` is the last list of integers provided by the user.

