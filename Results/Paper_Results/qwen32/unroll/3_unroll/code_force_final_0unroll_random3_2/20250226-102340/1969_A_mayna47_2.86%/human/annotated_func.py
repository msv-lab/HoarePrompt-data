#State of the program right berfore the function call: t is an integer such that 1 <= t <= 5000. For each test case, n is an integer such that 2 <= n <= 50, and p is a list of n integers where 1 <= p_i <= n, p_i != i, and all p_i are distinct.
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
            
        #State: t is an integer such that 1 <= t <= 5000; n is the input integer and n is not equal to 2; p is a list of n integers where 1 <= p_i <= n, p_i != i, and all p_i are distinct; v is a list starting with 0 followed by the integers from the input.
        print(3)
        #This is printed: 3
    #State: `t` is an integer such that 1 <= t <= 5000; `n` is the input integer; `p` is a list of `n` integers where 1 <= p_i <= n, p_i != i, and all p_i are distinct; `v` is a list starting with 0 followed by the integers from the input. If `n` is equal to 2, the specific conditions on `p` and `v` remain as described in the if part. Otherwise, the conditions on `p` and `v` remain as described in the else part.
#Overall this is what the function does:The function `func_1` reads an integer `n` and a list `p` of `n` integers for each test case. It then determines and prints either `2` or `3` based on whether there exists an index `i` such that `v[v[v[i]]] == i`. If `n` is `2`, it always prints `2`. Otherwise, it prints `2` if such an index exists, otherwise it prints `3`.

