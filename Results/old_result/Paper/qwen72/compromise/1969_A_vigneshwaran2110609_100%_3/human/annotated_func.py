#State of the program right berfore the function call: t is an integer such that 1 <= t <= 5000, n is an integer such that 2 <= n <= 50, and p is a list of integers where each p_i satisfies 1 <= p_i <= n and p_i ≠ i, and all p_i are distinct.
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
        
    #State: The loop has executed `n` times, and for each iteration, `x` is an input integer, `l` is a list of integers provided by the user, and `flag` is True if the condition `l[l[i] - 1] == i + 1` was met for any `i` in the range 0 to `x - 1` during that iteration. If the condition was met, the loop printed 2 and broke early. If the condition was never met, the loop printed 3 after completing all iterations. The values of `t` and `p` remain unchanged.
#Overall this is what the function does:The function `func` reads an integer `n` from the user, where `2 <= n <= 50`. For each of the `n` iterations, it reads another integer `x` and a list `l` of integers from the user. It then checks if there exists any index `i` in the range 0 to `x - 1` such that `l[l[i] - 1] == i + 1`. If such an index is found, the function prints 2 and breaks out of the inner loop. If no such index is found, it prints 3 after completing the inner loop. The function does not return any value and does not modify any external variables. The values of `t` and `p` remain unchanged.

