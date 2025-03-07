#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 5000, and for each test case, n is an integer such that 2 ≤ n ≤ 50, and p is a list of n integers where each p_i satisfies 1 ≤ p_i ≤ n, p_i ≠ i, and all p_i are distinct.
def func_1():
    n = int(input())
    v = [0] * (n + 1)
    v = [0] + list(map(int, input().split()))
    for i in range(1, n + 1):
        if v[v[i]] == i:
            print(2)
            return
        
    #State: Output State: The loop has executed all its iterations without returning any value, meaning that for every `i` from 1 to `n`, the condition `v[v[i]] != i` holds true.
    #
    #In simpler terms, after all iterations of the loop, none of the elements in the list `v` satisfy the condition where `v[v[i]]` equals `i`.
    print(3)
    #This is printed: 3
#Overall this is what the function does:The function reads an integer `n` and a list `p` of length `n`. It then constructs a new list `v` of length `n+1` initialized to zero. The function checks if there exists an index `i` from 1 to `n` such that `v[v[i]]` equals `i`. If such an index is found, the function prints `2` and returns immediately. If no such index exists after checking all elements, the function prints `3` and returns. The function does not accept any parameters and returns either `3` or `None` depending on whether a return statement is encountered.

