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
        
    #State: After all iterations of the loop, `n` and `k` remain integers such that 2 <= k <= n <= 2 * 10^5 and k is even, `n` is the first integer from input, `k` is the second integer from input, `permutation` is a list of length `n` where `permutation[i]` is set to `i // k + 1` for every index `i` that is a multiple of `k` (i.e., `i % k == 0`), and for every index `i` that is not a multiple of `k`, `permutation[i]` is set to the next available value of `curr_v` in the sequence. The variable `curr_v` will be equal to `n + 1` after the loop completes, and the loop variable `i` will be equal to `k`.
    result = ' '.join([str(v) for v in permutation])
    print(result)
    #This is printed: "1 4 2 5 3 6" (where the elements of the permutation list are determined based on the given conditions)
#Overall this is what the function does:The function `func_1` reads two integers `n` and `k` from the input, where `2 <= k <= n <= 2 * 10^5` and `k` is even. It generates a permutation of the numbers from 1 to `n` such that each element at an index that is a multiple of `k` is set to a specific value based on the sequence, and the remaining elements are filled with the next available values in the sequence. The function then prints this permutation as a space-separated string. After the function completes, `n` and `k` retain their original values, and the permutation list is fully populated and printed.

#State of the program right berfore the function call: No variables are passed to the function `func_2`. The function reads an integer `t` from standard input, where 1 ≤ t ≤ 10^4, representing the number of test cases.
def func_2():
    t = int(input())
    while t > 0:
        func_1()
        
        t -= 1
        
    #State: `t` is 0, `func_1()` has been called `t` times, where `t` was initially an integer value between 1 and 10^4.
#Overall this is what the function does:The function `func_2` reads an integer `t` from standard input, where `1 ≤ t ≤ 10^4`, representing the number of test cases. It then calls the function `func_1` exactly `t` times. After the function completes, `t` is 0, and `func_1` has been called `t` times, where `t` was initially an integer value between 1 and 10^4. The function does not return any value.

