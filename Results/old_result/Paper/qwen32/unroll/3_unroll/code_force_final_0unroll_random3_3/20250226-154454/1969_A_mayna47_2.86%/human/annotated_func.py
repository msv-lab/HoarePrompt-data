#State of the program right berfore the function call: t is an integer such that 1 <= t <= 5000. For each test case, n is an integer such that 2 <= n <= 50, and p is a list of n integers where each p_i is an integer such that 1 <= p_i <= n, p_i != i for all i in [1, n], and all p_i are distinct.
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
            
        #State: the loop completes all iterations without printing anything, and the values of `t`, `n`, `p`, and `v` remain unchanged.
        print(3)
        #This is printed: 3
    #State: `t` is an integer such that 1 <= t <= 5000; `n` is an integer such that 2 <= n <= 50; `p` is a list of n integers where each p_i is an integer such that 1 <= p_i <= n, p_i != i for all i in [1, n], and all p_i are distinct; `v` is a list of n + 1 integers where the first element is 0 and the remaining n elements are the integers read from the input. If `n` is 2, the conditions on `t`, `n`, `p`, and `v` remain as specified, and no additional changes occur. Otherwise, the values of `t`, `n`, `p`, and `v` remain unchanged.
#Overall this is what the function does:The function reads an integer `n` and a list `v` of `n` integers from the input, where each integer `v_i` is distinct, satisfies `1 <= v_i <= n`, and `v_i` is not equal to `i` for any `i` in the range [1, n]. It then checks if there exists any `i` such that `v[v[v[i]]] == i`. If such an `i` exists, it prints `2` and exits. If no such `i` exists after checking all possibilities, it prints `3`.

