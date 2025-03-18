#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 5000, and for each test case, n is an integer such that 2 ≤ n ≤ 50, and p is a list of n integers where each p_i is an integer such that 1 ≤ p_i ≤ n, p_i ≠ i, and all p_i are distinct.
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
            
        #State: Output State: The loop will execute for all values of `i` from 1 to `n`. After all iterations, if none of the conditions `v[v[v[i]]] == i` are met for any `i` in the range 1 to `n`, the function will not return anything and will exit the loop. Therefore, the values of `i` will range from 1 to `n`, `n` will remain between 2 and 50 inclusive, and the value of `v[v[v[i]]]` for each `i` from 1 to `n` will not equal `i`.
        print(3)
        #This is printed: 3
    #State: `t` is an integer such that 1 ≤ t ≤ 5000, `n` is an integer such that 2 ≤ n ≤ 50, `p` is a list of `n` integers where each `p_i` is an integer such that 1 ≤ `p_i` ≤ `n`, `p_i` ≠ `i`, and all `p_i` are distinct; `v` is a list of length `n+1` where each element is an integer. If `n` equals 2, `p` is a list of 2 integers where each `p_i` is an integer such that 1 ≤ `p_i` ≤ 2, `p_i` ≠ `i`, and all `p_i` are distinct; `v` is a list of length 3 where each element is an integer. If none of the conditions `v[v[v[i]]] == i` are met for any `i` in the range 1 to `n`, the function will not return anything and will exit the loop.
#Overall this is what the function does:The function reads an integer `n` and a list `p` of length `n` from the input. It then checks if there exists an index `i` such that `v[v[v[i]]] == i` for a constructed list `v`. If such an index is found, it prints `2` and exits. If no such index exists, it prints `3`. The function does not return any value.

