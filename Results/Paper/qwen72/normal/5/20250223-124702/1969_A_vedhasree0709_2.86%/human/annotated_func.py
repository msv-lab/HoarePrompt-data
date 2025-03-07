#State of the program right berfore the function call: t is an integer such that 1 <= t <= 5000, n is an integer such that 2 <= n <= 50, and p is a list of integers where each p_i satisfies 1 <= p_i <= n and p_i ≠ i, and all p_i are distinct.
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
        
    #State: The values of `t`, `n`, and `p` remain unchanged. The loop iterates `t` times, and for each iteration, the list `l` is processed. If the condition `l[i] == i + 2` and `l[i + 1] == i + 1` is met for any `i` in the range `[0, n-1]`, the loop prints `2` and breaks. Otherwise, it prints `3`. The variables `i` and `j` are reset to `0` at the start of each iteration, and their final values after the loop are not relevant to the output state.
#Overall this is what the function does:The function `func` does not accept any parameters and does not return any value. It reads input from the user, iterating `t` times, where `t` is an integer between 1 and 5000. For each iteration, it reads an integer `n` (2 <= n <= 50) and a list `l` of `n` integers. The function checks if there is any index `i` in the range `[0, n-1]` such that `l[i] == i + 2` and `l[i + 1] == i + 1`. If such an index is found, it prints `2` and breaks out of the loop. If no such index is found, it prints `3` after the loop completes. The function does not modify the input values `t`, `n`, or `p` (where `p` is the list of integers read as `l`).

