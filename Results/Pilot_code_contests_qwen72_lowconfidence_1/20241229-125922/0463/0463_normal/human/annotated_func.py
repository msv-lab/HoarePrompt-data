#State of the program right berfore the function call: The function `func` is expected to take an integer n as input where 1 ≤ n ≤ 105.
def func():
    n = input()
    spg = [0] * (n + 1)
    xor = [0] * (n + 1)
    for i in range(3, n + 1):
        k = 2
        
        movs = set()
        
        while k * (k + 1) <= 2 * i:
            s = 2 * i - k * (k - 1)
            if s % (2 * k) == 0:
                a = s / 2 / k
                movs.add(xor[a + k - 1] ^ xor[a - 1])
            k += 1
        
        mex = 0
        
        while mex in movs:
            mex += 1
        
        spg[i] = mex
        
        xor[i] = xor[i - 1] ^ mex
        
    #State of the program after the  for loop has been executed: `n` is a valid integer greater than or equal to 3, `spg` is a list of length `int(n) + 1` where each element from index 3 to `n` is the result of the `mex` calculation for that iteration, `xor` is a list of length `int(n) + 1` where each element from index 3 to `n` is the cumulative XOR of the `mex` values up to that index, `i` is `n`, `k` is the last value of `k` used in the final iteration, `movs` is the set of all possible moves for the final iteration, `mex` is the smallest non-negative integer not present in `movs` for the final iteration.
    if spg[n] :
        k = 2
        while k * (k + 1) <= 2 * i:
            s = 2 * i - k * (k - 1)
            
            if s % (2 * k) == 0:
                a = s / 2 / k
                if xor[a + k - 1] ^ xor[a - 1] == 0:
                    break
            
            k += 1
            
        #State of the program after the loop has been executed: `n` is a valid integer greater than or equal to 3, `spg` is a list of length `int(n) + 1` where each element from index 3 to `n` is the result of the `mex` calculation for that iteration, `xor` is a list of length `int(n) + 1` where each element from index 3 to `n` is the cumulative XOR of the `mex` values up to that index, `i` is `n`, `k` is such that `k * (k + 1) > 2 * i`, `movs` is the set of all possible moves for the final iteration, `mex` is the smallest non-negative integer not present in `movs` for the final iteration, `spg[n]` is true. If the loop did not break early due to the condition `xor[a + k - 1] ^ xor[a - 1] == 0`, `k` will be the smallest integer such that `k * (k + 1) > 2 * i`.
        print(k)
    else :
        print(-1)
    #State of the program after the if-else block has been executed: *`n` is a valid integer greater than or equal to 3, `spg` is a list of length `int(n) + 1` where each element from index 3 to `n` is the result of the `mex` calculation for that iteration, `xor` is a list of length `int(n) + 1` where each element from index 3 to `n` is the cumulative XOR of the `mex` values up to that index, `i` is `n`, `k` is the last value of `k` used in the final iteration, `movs` is the set of all possible moves for the final iteration, `mex` is the smallest non-negative integer not present in `movs` for the final iteration. If `spg[n]` is true, `k` is printed, and `k` is such that `k * (k + 1) > 2 * i`. If `spg[n]` is false, `-1` is printed to the console.
#Overall this is what the function does:The function `func` accepts an integer `n` within the range 1 ≤ n ≤ 105. It computes a sequence of values using a complex algorithm involving the `mex` (minimum excludant) function and cumulative XOR operations. After processing, the function prints either the smallest integer `k` such that `k * (k + 1) > 2 * n` and `xor[a + k - 1] ^ xor[a - 1] == 0` for some valid `a`, or `-1` if no such `k` is found. The final state of the program includes the lists `spg` and `xor` of length `n + 1`, where `spg[i]` holds the result of the `mex` calculation for each `i` from 3 to `n`, and `xor[i]` holds the cumulative XOR of the `mex` values up to that index. The variable `i` is set to `n`, and `k` is the last value used in the final iteration of the loop. If `spg[n]` is false, the function prints `-1`.

