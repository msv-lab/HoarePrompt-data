#State of the program right berfore the function call: t is an integer such that 1 <= t <= 5000, n is an integer such that 2 <= n <= 50, and p is a list of n integers where each p_i is an integer such that 1 <= p_i <= n and p_i ≠ i, and all p_i are distinct.
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
        
    #State: t remains an integer such that 1 <= t <= 5000, n remains an input integer such that 2 <= n <= 50, p remains a list of n integers where each p_i is an integer such that 1 <= p_i <= n and p_i ≠ i, and all p_i are distinct. The loop prints either 2 or 3 for each iteration of the outer loop, depending on the condition inside the inner loop.
#Overall this is what the function does:The function reads an integer `n` from the user, and for each of the `n` iterations, it reads another integer `x` and a list `l` of `x` integers. It then checks if for any index `i` in the list `l`, the value at the index `l[i] - 1` equals `i + 1`. If such a condition is met, it prints `2` and breaks out of the inner loop; otherwise, it prints `3` after completing the inner loop. The function does not return any value. After the function concludes, `t` remains an integer such that 1 <= t <= 5000, `n` remains an integer such that 2 <= n <= 50, and `p` remains a list of `n` integers where each `p_i` is an integer such that 1 <= p_i <= n and p_i ≠ i, and all `p_i` are distinct. The function affects the state by printing either `2` or `3` for each iteration of the outer loop.

