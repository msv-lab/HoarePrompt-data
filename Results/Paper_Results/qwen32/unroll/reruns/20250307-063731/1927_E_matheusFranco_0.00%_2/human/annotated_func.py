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
        
    #State: `n` and `k` are integers such that `2 <= k <= n`, and `k` is even; `permutation` is a list of `n` integers from `1` to `n` in a specific order determined by the multiples of `k` plus `i`; `idx` is 0; `idx_v` is 1; `curr_v` is `n+1`.
    result = ' '.join([str(v) for v in permutation])
    print(result)
    #This is printed: result (where result is the space-separated values of the permutation list)
#Overall this is what the function does:The function generates and prints a permutation of `n` integers based on specific multiples of `k`, where `k` is an even integer between 2 and `n`. The permutation is constructed such that certain positions in the list are filled with sequential integers starting from 1, following a pattern determined by the multiples of `k` plus an offset. The final output is a space-separated string of the generated permutation.

#State of the program right berfore the function call: t is a positive integer such that 1 <= t <= 10^4.
def func_2():
    t = int(input())
    while t > 0:
        func_1()
        
        t -= 1
        
    #State: t is 0.
#Overall this is what the function does:The function `func_2` reads a positive integer `t` from the input, then repeatedly calls `func_1` a total of `t` times, decrementing `t` by 1 after each call. After all calls to `func_1` are completed, `t` is 0.

