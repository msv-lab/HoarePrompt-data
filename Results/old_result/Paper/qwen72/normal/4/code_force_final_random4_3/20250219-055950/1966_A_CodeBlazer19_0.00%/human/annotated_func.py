#State of the program right berfore the function call: The function should take two parameters: a list of integers `cards` representing the numbers on the cards, and an integer `k` (2 ≤ k ≤ 100) representing the number of cards to exchange during each operation. The list `cards` should have a length `n` (1 ≤ n ≤ 100) and each element in `cards` should be an integer (1 ≤ c_i ≤ 100).
def func():
    t = int(input())
    for i in range(t):
        n, k = map(int, input().split())
        
        l = list(map(int, input().split()))
        
        print(k - 1)
        
    #State: `t` iterations have completed, `i` is `t-1`, `n` and `k` are the last input integers, `l` is the last list of integers provided by the user.
#Overall this is what the function does:The function reads an integer `t` from the user, indicating the number of test cases. For each test case, it reads two integers `n` and `k` from the user, followed by a list of `n` integers. It then prints `k - 1` for each test case. The function does not return any value or modify the input parameters. After the function concludes, `t` iterations have completed, and the last values of `n`, `k`, and `l` are the ones from the final test case.

