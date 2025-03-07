#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 5000, and for each test case, n is an integer such that 2 ≤ n ≤ 50, and p is a list of n integers where 1 ≤ p_i ≤ n, p_i ≠ i, and all p_i are distinct.
def func_1():
    n = int(input())
    v = [0] * (n + 1)
    v = [0] + list(map(int, input().split()))
    for i in range(1, n + 1):
        if v[v[i]] == i:
            print(2)
            return
        
    #State: Output State: `v` is a list of length n+1 where the first element is 0 and the next n elements are integers from the input split and converted to integers, and either no "2" is printed or exactly one "2" is printed based on the condition `if v[v[i]] == i`.
    print(3)
    #This is printed: 3
#Overall this is what the function does:The function processes a predefined set of inputs (t, n, p) where t is an integer between 1 and 5000, n is an integer between 2 and 50, and p is a list of n distinct integers each between 1 and n, excluding the index position. It initializes a list `v` of length `n+1` with the first element as 0 and the rest as integers from the input list `p`. If it finds an index `i` such that `v[v[i]] == i`, it prints `2` and returns immediately. Otherwise, it prints `3`.

