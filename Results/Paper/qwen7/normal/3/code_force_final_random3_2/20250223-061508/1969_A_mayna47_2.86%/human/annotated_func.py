#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 5000, and for each test case, n is an integer such that 2 ≤ n ≤ 50, and p is a list of n integers where each p_i satisfies 1 ≤ p_i ≤ n, p_i ≠ i, and all p_i are distinct.
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
            
        #State: Postcondition: `i` is 50, `n` is an integer such that 2 < n ≤ 50, and `v[v[v[i]]]` is not equal to `i`.
        print(3)
        #This is printed: 3
    #State: Postcondition: `t` is an integer such that 1 ≤ t ≤ 5000, `n` is either 2 or an integer such that 2 < n ≤ 50, `p` is a list of `n` integers where each `p_i` satisfies 1 ≤ `p_i` ≤ n, `p_i` ≠ i, and all `p_i` are distinct; `v` is a list of length `n+1` where the first element is 0, and the other elements are integer inputs split from the input string. If `n` is 2, `p` is a list of 2 integers where each `p_i` satisfies 1 ≤ `p_i` ≤ 2, `p_i` ≠ i, and all `p_i` are distinct; `v` is a list of length 3 where the first element is 0, and the other two elements are integer inputs split from the input string. If `n` is greater than 2, `i` is 50, and `v[v[v[i]]]` is not equal to `i`.
#Overall this is what the function does:The function reads an integer `n` and a list of `n` integers `p`, then checks if there exists an index `i` such that `v[v[v[i]]] == i`. If such an index is found, it prints `2` and returns. If no such index exists, it prints `3` and returns. The function does not accept any parameters and always returns `None`.

