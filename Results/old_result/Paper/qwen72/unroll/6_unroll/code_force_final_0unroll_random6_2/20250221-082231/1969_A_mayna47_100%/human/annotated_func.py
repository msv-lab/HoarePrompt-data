#State of the program right berfore the function call: t is an integer such that 1 <= t <= 5000, n is an integer such that 2 <= n <= 50, and p is a list of n integers where each p_i satisfies 1 <= p_i <= n and p_i ≠ i, and all p_i are distinct.
def func_1():
    n = int(input())
    v = [0] * (n + 1)
    v = [0] + list(map(int, input().split()))
    for i in range(1, n + 1):
        if v[v[i]] == i:
            print(2)
            return
        
    #State: The loop will either print 2 and return, or it will complete all iterations without printing anything. The values of t, n, p, and v remain unchanged.
    print(3)
    #This is printed: 3
#Overall this is what the function does:The function `func_1` reads an integer `n` from the user and a list of `n` integers from the user. It then checks if for any index `i` in the range `[1, n]`, the value at `v[v[i]]` equals `i`. If such an index is found, the function prints `2` and returns. If no such index is found, the function prints `3` and returns. The function does not return any value, and it does not modify the input parameters `t`, `n`, or `p` (though `p` is not used in the function). The final state of the program is that the function has printed either `2` or `3` and has returned.

