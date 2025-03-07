#State of the program right berfore the function call: t is an integer such that 1 <= t <= 5000. For each test case, n is an integer such that 2 <= n <= 50, and p is a list of n distinct integers where each p_i is an integer such that 1 <= p_i <= n, p_i != i for all i in [1, n].
def func_1():
    n = int(input())
    v = [0] * (n + 1)
    v = [0] + list(map(int, input().split()))
    for i in range(1, n + 1):
        if v[v[i]] == i:
            print(2)
            return
        
    #State: `t` is an integer such that 1 <= t <= 5000; `n` is the input integer; `p` is a list of n distinct integers where each `p_i` is an integer such that 1 <= `p_i` <= n, `p_i` != i for all i in [1, n]; `v` is a list of integers where `v[0]` is 0 and `v[1]` to `v[n]` are the integers read from the input.
    print(3)
    #This is printed: 3
#Overall this is what the function does:The function reads an integer `n` and a list `p` of `n` distinct integers. It checks if there exists an index `i` such that `p[p[i]] == i`. If such an index exists, it prints `2` and terminates. Otherwise, it prints `3`.

