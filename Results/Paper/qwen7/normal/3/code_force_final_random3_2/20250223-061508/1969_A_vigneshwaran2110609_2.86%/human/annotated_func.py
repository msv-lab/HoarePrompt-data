#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 5000; for each test case, n is an integer such that 2 ≤ n ≤ 50; p is a list of n integers where each integer p_i satisfies 1 ≤ p_i ≤ n, p_i ≠ i, and all p_i are distinct.
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
        
    #State: Output State: The loop has completed all its iterations without breaking out of the inner if statement. This means that for every iteration of the outer loop, the condition `l[l[i] - 1] == l[i] - 1` was never met for any `i` in the range of `x`. Therefore, the value printed for each iteration was 3, indicating that the condition was not satisfied. After all iterations, the final values of `i` will be 49, `x` will be 50, and `n` will still be within the range of 2 to 50 (inclusive). The variable `flag` will remain unchanged from its initial state or will be False since it was never set to True during the loop's execution.
    #
    #The output state after the loop executes all iterations can be described as follows:
    #- `i` is 49
    #- `x` is 50
    #- `n` is between 2 and 50 (inclusive)
    #- `flag` is False
#Overall this is what the function does:The function processes multiple test cases, each consisting of an integer `n` (2 ≤ n ≤ 50), and a list `p` of `n` integers (each `p_i` satisfies 1 ≤ `p_i` ≤ `n`, `p_i` ≠ `i`, and all `p_i` are distinct). For each test case, it reads `n` integers and checks if the condition `l[l[i] - 1] == l[i] - 1` holds for any `i` in the range of `x`. If the condition is met for any `i`, it prints `2` and breaks out of the loop. If the condition is never met for any `i`, it prints `3`. After processing all test cases, the function outputs the final values of `i` (which will be 49), `x` (which will be 50), and `n` (which remains within the range 2 to 50), and sets `flag` to `False` if it was never set to `True` during the loop's execution.

