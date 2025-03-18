#State of the program right berfore the function call: t is an integer such that 1 <= t <= 5000, n is an integer such that 2 <= n <= 50, and p is a list of integers of length n where 1 <= p_i <= n, p_i ≠ i, and all p_i are distinct.
def func():
    for _ in range(int(input())):
        n = int(input())
        
        l = list(map(int, input().split()))
        
        i = 0
        
        j = 0
        
        while i <= n - 1:
            if l[i] == i + 2 and l[i + 1] == i + 1:
                print(2)
                j = 1
                break
            i += 1
        
        if j == 0:
            print(3)
        
    #State: The values of `t`, `n`, and `p` remain unchanged. The loop iterates `t` times, and for each iteration, it checks the list `l` of length `n`. If it finds an index `i` such that `l[i] == i + 2` and `l[i + 1] == i + 1`, it prints `2` and breaks out of the loop. Otherwise, it prints `3`. The variables `i` and `j` are reset to `0` at the beginning of each iteration.
#Overall this is what the function does:The function `func` reads an integer `t` from the input, which represents the number of test cases. For each test case, it reads an integer `n` and a list `l` of `n` integers from the input. It then checks if there exists an index `i` in the list `l` such that `l[i] == i + 2` and `l[i + 1] == i + 1`. If such an index is found, it prints `2` and moves to the next test case. If no such index is found, it prints `3`. The function does not return any value; it only prints the results for each test case. The values of `t`, `n`, and the input list `l` remain unchanged after the function execution.

