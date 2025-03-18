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
        
    #State: `n` and `k` are integers read from the input such that 2 <= k <= n, and k is even; `permutation` is a list of length `n` where each index `j` is filled with the value `floor(j/k) * k + (j % k) + 1`; `idx` is 0; `idx_v` is 1; `curr_v` is n + 1.
    result = ' '.join([str(v) for v in permutation])
    print(result)
    #This is printed: result (where result is the space-separated concatenation of the elements of the permutation list constructed based on the formula `floor(j/k) * k + (j % k) + 1` for j in range(n))
#Overall this is what the function does:The function constructs and prints a permutation of length `n` based on the value of `k`. Each position `j` in the permutation is filled with a value calculated such that elements are grouped in steps of `k`, incrementing the value within each group. The final output is a space-separated string of the permutation list.

#State of the program right berfore the function call: No variables in the function signature. The function `func_2` does not take any parameters and operates based on input read within its body.
def func_2():
    t = int(input())
    while t > 0:
        func_1()
        
        t -= 1
        
    #State: t is 0.
#Overall this is what the function does:The function `func_2` reads an integer input `t` and calls `func_1` a total of `t` times. It does not accept any parameters and does not return any value. After execution, `t` is decremented to 0, and `func_1` is executed the number of times specified by the initial value of `t`.

