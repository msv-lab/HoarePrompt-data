#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. For each test case, n is a positive integer such that 1 ≤ n ≤ 2⋅10^5, and the second line contains n non-negative integers a_1, a_2, ..., a_n such that the sum of a_i is divisible by n.
def func_1():
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        a = list(map(int, input().split()))
        
        total_water = sum(a)
        
        target = total_water // n
        
        current_balance = 0
        
        possible = True
        
        for i in range(n):
            current_balance += a[i] - target
            if current_balance < 0:
                possible = False
                break
        
        if possible:
            print('YES')
        else:
            print('NO')
        
    #State: Output State: After the loop executes all the iterations, `i` is `n`, `current_balance` is the sum of `(a[i] - target)` for all `i` from `0` to `n-1`, `possible` is either `True` or `False` depending on whether the condition `current_balance < 0` was ever met during any iteration, `t` is `0` since it starts from the value of the input integer `t` and decreases by `1` with each iteration until it reaches `0`, `a` is a list of integers entered by the user, `total_water` is the sum of all elements in list `a`, and `target` is `total_water // n`.
    #
    #In simpler terms, after the loop completes all its iterations, `i` will be equal to `n`, `current_balance` will hold the final balance calculated after processing all elements in list `a`, `possible` will indicate whether it was possible to distribute the water such that no one has a negative balance, `t` will be `0` as all inputs have been processed, and the other variables (`a`, `total_water`, and `target`) will retain their last computed values.
#Overall this is what the function does:The function processes multiple test cases. For each test case, it reads an integer `t` (number of sub-cases), an integer `n` (number of non-negative integers), and a list of `n` non-negative integers `a`. It calculates whether it is possible to distribute the total amount of water represented by the sum of `a` equally among `n` people without any person having a negative balance. If such a distribution is possible, it prints 'YES'; otherwise, it prints 'NO'. After processing all test cases, the function does not return any value but prints the result for each test case.

