#State of the program right berfore the function call: t is an integer such that 1 <= t <= 5000, and for each test case, n is an integer such that 2 <= n <= 50, and p is a list of n integers where each p_i satisfies 1 <= p_i <= n and p_i ≠ i, and all p_i are distinct.
def func():
    n = int(input())
    for i in range(n):
        x = int(input())
        
        l = list(map(int, input().strip().split()))
        
        for i in range(0, x):
            if l[l[i] - 1] == i + 1:
                flag = True
                print(2)
                break
        else:
            print(3)
        
    #State: The loop iterates through each integer from 0 to n-1. For each iteration, it reads an integer `x` and a list `l` of integers. It then checks if for any index `i` in the range 0 to `x-1`, the condition `l[l[i] - 1] == i + 1` holds true. If the condition is met, it prints 2 and sets a flag to True, breaking out of the inner loop. If the condition is never met, it prints 3. The variables `t`, `n`, and `p` remain unchanged.
#Overall this is what the function does:The function `func` reads an integer `n` representing the number of test cases. For each test case, it reads an integer `x` and a list `l` of `x` integers. It then checks if for any index `i` in the range 0 to `x-1`, the condition `l[l[i] - 1] == i + 1` holds true. If the condition is met, it prints 2 and breaks out of the inner loop. If the condition is never met, it prints 3. The function does not return any value and does not modify any input parameters or global variables.

