#State of the program right berfore the function call: n and k are integers such that 2 <= k <= n <= 2 * 10^5 and k is even.
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
        
    #State: After the loop executes all its iterations, the final state is as follows: `n` and `k` are integers such that 2 <= k <= n <= 2 * 10^5 and k is even; `permutation` is a list of length `n` where each element at index `j` is set to the value `j // k + 1` if `j % k == 0`, otherwise it is set to the value `(j // k) * k + (j % k) + 1`. The variable `curr_v` is `n + 1`, `i` is `k`, and `multiples_of_k_plus_i` is `k * (n // k) + k - 1`. The variables `idx` and `idx_v` remain unchanged at 0 and 1, respectively.
    result = ' '.join([str(v) for v in permutation])
    print(result)
    #This is printed: [elements of permutation separated by spaces]
#Overall this is what the function does:The function `func_1` reads two integers `n` and `k` from the user input, where `2 <= k <= n <= 2 * 10^5` and `k` is even. It generates a permutation of the first `n` natural numbers, placing them in a specific order based on the value of `k`. The resulting permutation is then printed as a space-separated string. The function does not return any value. After the function concludes, the input variables `n` and `k` remain unchanged, and the permutation list is populated with values according to the described logic.

#State of the program right berfore the function call: t is a positive integer such that 1 <= t <= 10^4.
def func_2():
    t = int(input())
    while t > 0:
        func_1()
        
        t -= 1
        
    #State: `t` is 0, `func_1()` has been called `t` times where `t` is the initial value of `t`.
#Overall this is what the function does:The function `func_2` reads an integer `t` from the user input, where `t` is a positive integer within the range 1 to 10^4. It then calls the function `func_1` exactly `t` times. After the function completes, `t` is 0, and `func_1` has been called `t` times, where `t` is the initial value provided by the user. The function does not return any value.

