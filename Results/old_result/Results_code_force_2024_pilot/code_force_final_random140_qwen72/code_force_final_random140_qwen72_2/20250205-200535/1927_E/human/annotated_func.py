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
        
    #State: `idx` is `k`, `multiples_of_k_plus_idx` is `k-1 + n*k` where `n` is the number of iterations, and `len(permutation)` is greater than or equal to `k-1 + n*k`. The elements in `permutation` at positions `i + j*k` (for `i` from 0 to `k-1` and `j` from 0 to `n-1`) are set to either `bottom_v + j` if `i % 2 == 0` or `top_v - j` if `i % 2 != 0`. `bottom_v` is `1 + n*(k//2)` and `top_v` is `n - n*(k//2)`.
    result = ' '.join([str(v) for v in permutation])
    print(result)
    #This is printed: "5 0 5 6 -1 6 7 -2 7 8 -3 8" (where the elements are determined by the given conditions and the values of `bottom_v` and `top_v`)
#Overall this is what the function does:The function `func_1` reads two integers `n` and `k` from the input, where `2 <= k <= n <= 2 * 10^5` and `k` is even. It generates a permutation of length `n` such that for each index `i` from 0 to `k-1`, the elements at positions `i + j*k` (for `j` from 0 to `n-1`) are filled with increasing values starting from 1 if `i` is even, and decreasing values starting from `n` if `i` is odd. The function then prints the generated permutation as a space-separated string. After the function concludes, the input integers `n` and `k` remain unchanged, and the permutation is printed to the console.

#State of the program right berfore the function call: No variables are passed to the function `func_2`. The function reads an integer `t` from standard input, which represents the number of test cases, and `t` satisfies 1 ≤ t ≤ 10^4.
def func_2():
    t = int(input())
    while t > 0:
        func_1()
        
        t -= 1
        
    #State: `t` is 0, and `func_1` has been called `t` times where `t` was initially an integer between 1 and 10^4 (inclusive).
#Overall this is what the function does:The function `func_2` does not accept any parameters. It reads an integer `t` from standard input, where `t` represents the number of test cases and must satisfy 1 ≤ t ≤ 10^4. The function calls `func_1` exactly `t` times. After the function concludes, `t` is 0, and `func_1` has been called `t` times, where `t` was initially an integer between 1 and 10^4 (inclusive). The function does not return any value.

