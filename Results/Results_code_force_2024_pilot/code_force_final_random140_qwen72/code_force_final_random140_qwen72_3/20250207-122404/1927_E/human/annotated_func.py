#State of the program right berfore the function call: n and k are integers such that 2 <= k <= n <= 2 * 10^5 and k is even.
def func_1():
    n, k = map(int, input().split(' '))
    permutation = [0] * n
    bottom_v = 1
    top_v = n
    idx = 0
    while idx < k:
        multiples_of_k_plus_idx = idx
        
        while multiples_of_k_plus_idx < len(permutation):
            if idx % 2 == 0:
                permutation[multiples_of_k_plus_idx] = bottom_v
                bottom_v += 1
            else:
                permutation[multiples_of_k_plus_idx] = top_v
                top_v -= 1
            multiples_of_k_plus_idx += k
        
        idx += 1
        
    #State: After all iterations of the loop, `n` and `k` remain integers such that 2 <= k <= n <= 2 * 10^5 and k is even. The `permutation` list is fully populated with values according to the rules specified in the loop. Specifically, elements at indices that are multiples of `k` starting from 0 are filled alternately with increasing values from `1` to `n//2 + 1` (for even indices) and decreasing values from `n` to `n//2 + 1` (for odd indices). The variable `bottom_v` will be `n // 2 + 1 + (total number of even-indexed assignments)`, and `top_v` will be `n - (n // 2) - (total number of odd-indexed assignments)`. The variable `idx` is now `k`, and `multiples_of_k_plus_idx` will be equal to the next multiple of `k` beyond the last index of `permutation`.
    result = ' '.join([str(v) for v in permutation])
    print(result)
    #This is printed: - The `result` is a string containing the space-separated values of the `permutation` list.
    #   - For our example, the `result` will be: `"1 10 2 9 3 8 4 7 5 6"`.
    #
    #### Final Output:
    #Output:
#Overall this is what the function does:The function `func_1` reads two integers `n` and `k` from the user input, where `2 <= k <= n <= 2 * 10^5` and `k` is even. It generates a permutation of numbers from 1 to `n` and prints this permutation as a space-separated string. The permutation is constructed such that for each index `i` that is a multiple of `k`, the value at that index is filled alternately with increasing values from 1 (for even `i`) and decreasing values from `n` (for odd `i`). After the function completes, the original values of `n` and `k` remain unchanged, and the permutation is printed to the console.

#State of the program right berfore the function call: No variables are passed to the function `func_2`.
def func_2():
    t = int(input())
    while t > 0:
        func_1()
        
        t -= 1
        
    #State: No variables are passed to the function `func_2`, `t` is now `0` (where `t` was originally greater than 0), and `func_1()` has been called `t` times.
#Overall this is what the function does:The function `func_2` does not accept any parameters and does not return any value. It reads an integer `t` from the user input and calls the function `func_1` exactly `t` times. After the function concludes, `t` is reduced to 0.

