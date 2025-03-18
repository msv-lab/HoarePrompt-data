#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 5000; for each test case, n is an integer such that 2 ≤ n ≤ 50; p is a list of n integers where 1 ≤ p_i ≤ n, p_i ≠ i, and all p_i are distinct.
def func_1():
    n = int(input())
    v = [0] * (n + 1)
    v = [0] + list(map(int, input().split()))
    for i in range(1, n + 1):
        if v[v[i]] == i:
            print(2)
            return
        
    #State: Output State: `t` is an integer such that 1 ≤ t ≤ 5000, `n` is an input integer such that 2 ≤ n ≤ 50, `p` is a list of n integers where 1 ≤ p_i ≤ n, p_i ≠ i, and all p_i are distinct; `v` is a list of length n+1 where each element is 0 except for the first element which is 0 and the rest are converted from the input split and mapped to integers; the loop prints 2 and returns if there exists an index `i` (1 ≤ i ≤ n) such that `v[v[i]] == i`, otherwise it does nothing.
    print(3)
    #This is printed: 3
#Overall this is what the function does:The function processes a list `p` of integers for each test case, where `n` (the length of the list) ranges from 2 to 50, and each integer in the list is unique and between 1 and `n`, exclusive. It constructs a list `v` based on the input and checks if there exists an index `i` such that `v[v[i]] == i`. If such an index is found, it prints `2` and returns immediately. Otherwise, it prints `3`. The function does not return any value explicitly but prints either `2` or `3` based on the condition check.

