#State of the program right berfore the function call: t is an integer such that 1 <= t <= 5000, n is an integer such that 2 <= n <= 50, and p is a list of n integers where 1 <= p_i <= n, p_i ≠ i, and all p_i are distinct.
def func():
    n = int(input())
    for i in range(n):
        x = int(input())
        
        l = list(map(int, input().strip().split()))
        
        for i in range(0, x):
            if l[l[i] - 1] == l[i] - 1:
                flag = True
                print(2)
                break
        else:
            print(3)
        
    #State: The value of `t` remains unchanged. The value of `n` remains unchanged. The list `p` remains unchanged. The loop prints either `2` or `3` for each iteration of the outer loop, depending on the condition inside the inner loop. If the condition `l[l[i] - 1] == l[i] - 1` is met for any `i` in the range `0` to `x-1`, it prints `2` and sets `flag` to `True`. Otherwise, it prints `3`. The final state of the loop does not change the values of `t`, `n`, or `p`.
#Overall this is what the function does:The function `func` reads an integer `n` from the user, and for each of the `n` iterations, it reads another integer `x` and a list `l` of integers from the user. For each `x`, it checks if there is any index `i` in the list `l` such that `l[l[i] - 1] == l[i] - 1`. If such an index is found, it prints `2` and sets a flag to `True`. If no such index is found, it prints `3`. The function does not return any value. The values of `t`, `n`, and `p` (if they exist) remain unchanged after the function execution.

