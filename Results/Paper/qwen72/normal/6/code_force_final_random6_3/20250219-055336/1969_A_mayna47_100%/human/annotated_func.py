#State of the program right berfore the function call: t is an integer such that 1 <= t <= 5000, each test case consists of n (2 <= n <= 50) and a list p of n integers where 1 <= p_i <= n, p_i ≠ i, and all p_i are distinct.
def func_1():
    n = int(input())
    v = [0] * (n + 1)
    v = [0] + list(map(int, input().split()))
    for i in range(1, n + 1):
        if v[v[i]] == i:
            print(2)
            return
        
    #State: `t` is an integer such that 1 <= t <= 5000, `n` is an integer such that 2 <= n <= 50, `p` is a list of `n` integers where 1 <= p_i <= n, p_i ≠ i, and all p_i are distinct, `v` is a list of length `n + 1` with elements initialized to the input values, `i` is `n`. If `v[v[i]]` is equal to `i` for any `i` in the range 1 to `n`, the program prints 2 and returns. Otherwise, the program returns nothing.
    print(3)
    #This is printed: - The code will execute the `else` block and print `3`.
    #
    #Output:
#Overall this is what the function does:The function `func_1` implicitly processes a set of test cases. For each test case, it reads an integer `n` (2 <= n <= 50) and a list `p` of `n` integers where each `p_i` is between 1 and `n`, `p_i` ≠ i, and all `p_i` are distinct. It checks if there exists any index `i` in the range 1 to `n` such that `p[p[i]]` is equal to `i`. If such an index is found, the function prints `2` and returns. If no such index is found, the function prints `3` and returns. The function does not return any value.

