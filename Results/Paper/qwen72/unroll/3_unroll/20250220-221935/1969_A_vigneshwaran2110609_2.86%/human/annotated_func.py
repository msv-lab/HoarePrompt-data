#State of the program right berfore the function call: The function `func` is intended to solve a problem with multiple test cases, where each test case includes an integer `n` representing the number of friends (2 ≤ n ≤ 50) and a list of integers `p` of length `n` (1 ≤ p_i ≤ n, p_i ≠ i, all p_i are distinct). The function should calculate and return the minimum number of invitations required to ensure at least 2 friends attend the party.
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
        
    #State: The loop iterates `n` times, and for each iteration, it reads an integer `x` and a list `l` of integers. If there is any index `i` in the list `l` such that `l[l[i] - 1] == l[i] - 1`, it prints `2` and sets `flag` to `True`. Otherwise, it prints `3`. The variables `n`, `x`, and `l` are updated in each iteration, but the final state of `n` remains the same as the initial state, and `flag` is set to `True` if the condition was met in any iteration.
#Overall this is what the function does:The function `func` reads an integer `n` from the input, representing the number of test cases. For each test case, it reads an integer `x` and a list `l` of integers. If there is any index `i` in the list `l` such that `l[l[i] - 1] == l[i] - 1`, it prints `2`. Otherwise, it prints `3`. The function does not return any value; it only prints the results for each test case. The final state of the program includes the variables `n`, `x`, and `l` being updated for each iteration, but `n` retains its initial value after the function concludes.

