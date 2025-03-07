#State of the program right berfore the function call: The function should take two parameters, n and k, where n is the length of the array and k is the number of sorted cyclic shifts required. Both n and k are integers such that 1 ≤ k ≤ n ≤ 10^3.
def func():
    for s in [*open(0)][1:]:
        n, k = map(int, s.split())
        
        if k >= 2:
            if n == k:
                print(*[k for j in range(k)])
            else:
                print('-1')
        else:
            print(*[(j + 1) for j in range(n)])
        
    #State: Output State: The loop reads lines from the input, processes each line to extract `n` and `k`, and then prints an array based on the conditions given. If `k` is greater than or equal to 2 and `n` equals `k`, it prints an array of `k` elements, each being `k`. If `k` is greater than or equal to 2 and `n` does not equal `k`, it prints `-1`. If `k` is less than 2, it prints an array of `n` elements, each being the index `j + 1` (where `j` ranges from 0 to `n-1`). After all iterations, the loop finishes and no further changes are made to the variables `n` and `k`. The final state of the variables `n` and `k` will be the values from the last line of input processed. The output state is the sequence of printed arrays or `-1` values based on the input lines. **The output state is the sequence of printed arrays or `-1` values based on the input lines.**
#Overall this is what the function does:The function reads lines from the standard input, where each line contains two integers `n` and `k`. For each line, it processes `n` and `k` and prints an array or a `-1` based on the following conditions: If `k` is greater than or equal to 2 and `n` equals `k`, it prints an array of `k` elements, each being `k`. If `k` is greater than or equal to 2 and `n` does not equal `k`, it prints `-1`. If `k` is less than 2, it prints an array of `n` elements, each being the index `j + 1` (where `j` ranges from 0 to `n-1`). The function does not return any value; it only prints the results. After processing all input lines, the function finishes, and the final state of the program is the sequence of printed arrays or `-1` values.

