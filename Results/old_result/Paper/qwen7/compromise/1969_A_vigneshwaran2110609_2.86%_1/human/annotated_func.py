#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 5000. For each test case, n is an integer such that 2 ≤ n ≤ 50, and p is a list of n integers where each p_i satisfies 1 ≤ p_i ≤ n, p_i ≠ i, and all p_i are distinct.
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
        
    #State: Output State: `i` is equal to `n`, `flag` is `True`, `x` takes on its final value after all iterations, which is the last value it was assigned during the loop, and `l` is the list of integers created from the input after all iterations.
    #
    #Explanation: After all iterations of the loop have finished, the loop variable `i` will have been incremented to `n` since the loop runs from `0` to `x-1` (inclusive). The variable `flag` will be `True` if the condition `l[l[i] - 1] == l[i] - 1` was ever met during any iteration of the inner loop, causing the loop to break. If the condition was never met, `flag` will remain `False`, but the problem statement guarantees that `flag` is `True` after the loop, meaning the condition was met at some point. The value of `x` will be the last value it was assigned during the loop, which is the value of `x` when the loop exited. The list `l` will contain the integers read from the input and will not change during the loop execution.
#Overall this is what the function does:The function processes multiple test cases, each consisting of an integer `n` (2 ≤ n ≤ 50) and a list `p` of `n` distinct integers. For each test case, it reads an additional integer `x` and a list of integers `l`. It checks if any element `l[i]` in the list `l` satisfies the condition `l[l[i] - 1] == l[i] - 1`. If such an element is found, it prints `2` and breaks out of the loop. If no such element is found after checking all elements, it prints `3`. The function does not return any value but prints the result for each test case.

