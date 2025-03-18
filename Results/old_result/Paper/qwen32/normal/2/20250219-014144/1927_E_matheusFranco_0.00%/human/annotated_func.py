#State of the program right berfore the function call: n and k are integers such that 2 <= k <= n, k is even, and n is the length of the desired permutation.
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
        
    #State: `n` and `k` are integers such that `2 <= k <= n` and `k` is even; `permutation` is a list of length `n` with values 1 through `n` distributed according to the pattern described above; `idx` is 0; `idx_v` is 1; `curr_v` is `n + 1`; `multiples_of_k_plus_i` is the last position updated in the final iteration; `i` is `k-1`.
    result = ' '.join([str(v) for v in permutation])
    print(result)
    #This is printed: result (where result is a space-separated string of the elements in the permutation list)
#Overall this is what the function does:The function generates and prints a permutation of length `n` where elements are filled in a specific pattern determined by the value of `k`. The pattern involves filling every `k`-th position starting from each index from 0 to `k-1`, incrementing the value to be placed each time.

#State of the program right berfore the function call: This function does not have any parameters in its signature, so there are no variables or relationships to describe.
def func_2():
    t = int(input())
    while t > 0:
        func_1()
        
        t -= 1
        
    #State: t is 0.
#Overall this is what the function does:The function `func_2` repeatedly calls `func_1` a number of times specified by the integer input `t`. After `t` calls, the function terminates without returning any value.

