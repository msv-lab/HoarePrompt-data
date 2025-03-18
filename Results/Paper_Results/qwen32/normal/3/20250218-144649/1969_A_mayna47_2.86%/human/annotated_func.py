#State of the program right berfore the function call: t is an integer such that 1 <= t <= 5000. For each test case, n is an integer such that 2 <= n <= 50, and p is a list of n distinct integers where 1 <= p_i <= n, p_i != i for all i in [1, n].
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
            
        #State: `t` is an integer such that 1 <= t <= 5000; `n` is an integer input by the user such that 2 <= n <= 50 and `n` is not equal to 2; `p` is a list of `n` distinct integers where 1 <= `p_i` <= `n`, `p_i` != `i` for all `i` in [1, `n`]; `v` is a list starting with 0 followed by the integers provided by the user input. The loop has completed all `n` iterations without printing anything.
        print(3)
        #This is printed: 3
    #State: `t` is an integer such that 1 <= t <= 5000; `n` is an integer input by the user such that 2 <= n <= 50; `p` is a list of `n` distinct integers where 1 <= `p_i` <= `n`, `p_i` != `i` for all `i` in [1, `n`]; `v` is a list starting with 0 followed by the integers provided by the user input. If `n` equals 2, the program does not perform any additional actions beyond maintaining the initial conditions. Otherwise, the loop has completed all `n` iterations without printing anything.
#Overall this is what the function does:The function `func_1` reads an integer `n` and a list of `n` distinct integers from the input. It then checks if `n` is 2, in which case it prints `2`. If `n` is greater than 2, it checks a specific condition involving the list. If the condition is met for any element during the iteration, it prints `2` and exits. If the loop completes without meeting the condition, it prints `3`. The function does not return any value.

