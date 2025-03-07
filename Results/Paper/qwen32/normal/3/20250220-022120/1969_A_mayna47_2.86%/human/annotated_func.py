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
            
        #State: The loop completes all iterations without printing anything.
        print(3)
        #This is printed: 3
    #State: `t` is an integer such that 1 <= t <= 5000; `n` is the input integer such that 2 <= n <= 50; `p` is a list of `n` distinct integers where each `p_i` satisfies 1 <= `p_i` <= `n` and `p_i` != `i`; `v` is a list of `n` + 1 integers, where the first integer is 0 and the remaining integers are the values provided in the input. If `n` equals 2, the program does not perform any additional operations within the if block. Otherwise, the loop completes all iterations without printing anything.
#Overall this is what the function does:The function `func_1` reads an integer `n` and a list of `n` distinct integers `p` from the input, then prints either `2` or `3` based on a specific condition. If `n` is `2`, it prints `2`. Otherwise, it checks if there exists an index `i` such that `v[v[v[i]]] == i`; if such an index exists, it prints `2` and exits. If no such index is found after checking all possible indices, it prints `3`. The function does not return any value.

