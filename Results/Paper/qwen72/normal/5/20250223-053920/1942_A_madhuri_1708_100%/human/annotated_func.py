#State of the program right berfore the function call: The function should take two parameters, n and k, where n is the length of the array and k is the number of sorted cyclic shifts required, and both are integers such that 1 ≤ k ≤ n ≤ 10^3. The function should return a list of n integers, each between 1 and 10^9, that satisfies the conditions, or -1 if no such array exists.
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
        
    #State: The function will print either a list of n integers, each equal to k, if n == k and k >= 2, or -1 if k >= 2 and n != k, or a list of integers from 1 to n if k < 2. The loop will continue to read and process each line of input until all lines have been processed.
#Overall this is what the function does:The function reads multiple lines of input, each containing two integers `n` and `k`. For each line, it processes `n` and `k` to print either a list of `n` integers where each integer is `k` if `k >= 2` and `n == k`, or `-1` if `k >= 2` and `n != k`, or a list of integers from 1 to `n` if `k < 2`. The function continues to read and process each line until all lines have been processed.

