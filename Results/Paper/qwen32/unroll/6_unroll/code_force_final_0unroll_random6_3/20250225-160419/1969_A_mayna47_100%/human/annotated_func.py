#State of the program right berfore the function call: t is an integer such that 1 <= t <= 5000, for each test case, n is an integer such that 2 <= n <= 50, and p is a list of n integers where each p_i is an integer such that 1 <= p_i <= n, p_i != i, and all p_i are distinct.
def func_1():
    n = int(input())
    v = [0] * (n + 1)
    v = [0] + list(map(int, input().split()))
    for i in range(1, n + 1):
        if v[v[i]] == i:
            print(2)
            return
        
    #State: the loop completes all iterations without printing `2` and returning, leaving `t`, `n`, `p`, and `v` unchanged.
    print(3)
    #This is printed: 3
#Overall this is what the function does:The function reads an integer `n` and a list `p` of `n` integers, where each integer `p_i` is distinct, satisfies 1 <= p_i <= n, and p_i is not equal to i. It checks if there exists any index `i` such that `p[p[i]]` equals `i`. If such an index exists, it prints `2` and terminates. If no such index exists after checking all possibilities, it prints `3`.

