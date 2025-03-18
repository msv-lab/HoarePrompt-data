#State of the program right berfore the function call: n and k are integers such that 2 <= k <= n, and k is even.
def func_1():
    n, k = map(int, input().split(' '))
    permutation = [0] * n
    idx = 0
    idx_v = 1
    curr_v = 1
    for i in range(k):
        multiples_of_k_plus_i = i
        
        while multiples_of_k_plus_i < len(permutation):
            permutation[multiples_of_k_plus_i] = curr_v
            curr_v += 1
            multiples_of_k_plus_i += k
        
    #State: `n` and `k` are integers read from the input, such that \(2 \leq k \leq n\) and \(k\) is even; `permutation` is a list of length `n` with values `1, 2, 3, ..., n` distributed according to the pattern described above; `idx` is 0; `idx_v` is 1; `curr_v` is `n+1`; `multiples_of_k_plus_i` is the last index filled in the final iteration.
    result = ' '.join([str(v) for v in permutation])
    print(result)
    #This is printed: result (where result is the space-separated concatenation of the elements in the permutation list)
#Overall this is what the function does:The function reads two integers `n` and `k` from the input, where `2 <= k <= n` and `k` is even. It constructs a permutation of numbers from 1 to `n` following a specific pattern based on the value of `k`. The constructed permutation is then printed as a space-separated string.

#State of the program right berfore the function call: No variables are present in the function signature of `func_2`. Therefore, no precondition can be derived from the given function signature alone.
def func_2():
    t = int(input())
    while t > 0:
        func_1()
        
        t -= 1
        
    #State: t is 0.
#Overall this is what the function does:The function `func_2` prompts the user to input an integer `t`, then repeatedly calls `func_1` until `t` becomes 0. It does not accept any parameters and does not return a value; instead, it performs actions based on the internal logic within `func_1`.

