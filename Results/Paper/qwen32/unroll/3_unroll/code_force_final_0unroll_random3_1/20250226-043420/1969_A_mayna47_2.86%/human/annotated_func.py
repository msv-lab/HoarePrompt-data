#State of the program right berfore the function call: t is an integer such that 1 <= t <= 5000. For each test case, n is an integer such that 2 <= n <= 50, and p is a list of n distinct integers where each p_i satisfies 1 <= p_i <= n and p_i != i.
def func_1():
    n = int(input())
    v = [0] * (n + 1)
    v = [0] + list(map(int, input().split()))
    if (n == 2) :
        print(2)
        #This is printed: 2
    else :
        for i in range(1, n + 1):
            if v[v[v[i]]] == i:
                print(2)
                return
            
        #State: t is an integer such that 1 <= t <= 5000; n is the input integer such that 2 <= n <= 50 and n is not equal to 2; p is a list of n distinct integers where each p_i satisfies 1 <= p_i <= n and p_i != i; v is a list where the first element is 0 and the next n elements are the integers read from the input. The loop has completed all iterations without printing 2.
        print(3)
        #This is printed: 3
    #State: `t` is an integer such that 1 <= t <= 5000; `n` is the input integer such that 2 <= n <= 50; `p` is a list of `n` distinct integers where each `p_i` satisfies 1 <= `p_i` <= `n` and `p_i` != `i`; `v` is a list where the first element is 0 and the next `n` elements are the integers read from the input. If `n` is 2, the specific conditions for `n` being 2 are met. Otherwise, the loop has completed all iterations without printing 2.
#Overall this is what the function does:The function reads an integer `n` and a list of `n` distinct integers `p` where each integer `p_i` satisfies 1 <= `p_i` <= `n` and `p_i` != `i`. It then determines and prints either `2` or `3` based on whether there exists an index `i` such that `v[v[v[i]]] == i`. If `n` is `2`, it directly prints `2`. Otherwise, it checks the condition for all `i` from `1` to `n` and prints `2` if the condition is met for any `i`; otherwise, it prints `3`.

