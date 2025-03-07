#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4; for each test case, n is an integer such that 1 ≤ n ≤ 10^5, and a list of n integers a_1, a_2, ..., a_n where 1 ≤ a_i ≤ 10^9; the sum of all n values across all test cases does not exceed 10^5.
def func_1():
    print('-----------------')
    #This is printed: -----------------
    n = int(input())
    arr = list(map(int, input().split()))
    prefix = [0]
    for v in arr:
        prefix.append(v ^ prefix[-1])
        
    #State: Output State: The `prefix` list will contain the integer 0 followed by the cumulative XOR of all elements in the `arr` list. Specifically, if `arr = [a1, a2, a3, ..., an]`, then `prefix` will be `[0, a1, a1 ^ a2, a1 ^ a2 ^ a3, ..., a1 ^ a2 ^ ... ^ an]`. The variable `t` remains an integer such that \(1 \leq t \leq 10^4\), and `n` remains an input integer such that \(1 \leq n \leq 10^5\). The `arr` list remains unchanged as it was when the loop started.
    #
    #In simpler terms, the `prefix` list will contain 0 followed by the cumulative XOR of all elements in the original `arr` list, with each subsequent element being the XOR of all previous elements including the current one.
    print(arr, prefix)
    #This is printed: [a1, a2, a3, ..., an], [0, a1, a1 ^ a2, a1 ^ a2 ^ a3, ..., a1 ^ a2 ^ ... ^ an]
    pre = [[0, 0] for _ in range(32)]
    suf = [[0, 0] for _ in range(32)]
    for i in range(32):
        pre[i][0] += 1
        
    #State: Output State: `i` is 32; `pre[i][0]` is 32.
    #
    #In natural language: After the loop has executed all its iterations (32 times), the variable `i` will be 32, and each sublist in the `pre` list will have its first element set to 32.
    for i in range(n, 0, -1):
        cur = prefix[i]
        
        for j in range(32):
            if cur >> j & 1:
                suf[j][1] += 1
            else:
                suf[j][0] += 1
        
    #State: `i` is 0, `n` is 32, `cur` is `prefix[0]`, and for each `j` from 0 to 31, `suf[j][1]` contains the total count of 1s in the binary representation of all numbers from 0 to 31 up to and including the `j`-th bit, and `suf[j][0]` contains the total count of 0s in the same range.
    print(pre)
    #This is printed: cur (where cur is the first element of the list `prefix`)
    print(suf)
    #This is printed: [(16, 16), (16, 16), ..., (16, 16)] (32 times)
    ans = 0
    for i in range(1, n + 1):
        y = arr[i - 1]
        
        k = y.bit_length() - 1
        
        ans += pre[k][0] * suf[k][0] + pre[k][1] * suf[k][1]
        
        c = prefix[i]
        
        for j in range(32):
            if c >> j & 1:
                pre[j][1] += 1
                suf[j][1] -= 1
            else:
                pre[j][0] += 1
                suf[j][0] -= 1
        
    #State: `j` is 31, `n` is 32, `y` is `arr[32]`, `k` is 5, `ans` is the sum of `pre[5][0] * suf[5][1] + pre[5][1] * suf[5][0]` for all iterations, `c` is `prefix[34]`, `i` is 34, `suf[j][1]` is 0 for all `j` from 0 to 31, and `pre[j][1]` is 32 for all `j` from 0 to 5 and 0 for all `j` from 6 to 31.
    print(ans)
    #This is printed: 0
#Overall this is what the function does:The function processes multiple test cases, each containing an integer \( t \) (1 ≤ \( t \) ≤ 10^4), an integer \( n \) (1 ≤ \( n \) ≤ 10^5), and a list of \( n \) integers \( a_1, a_2, ..., a_n \) (1 ≤ \( a_i \) ≤ 10^9). For each test case, it calculates and prints the cumulative XOR of the list elements, initializes two lists `pre` and `suf` to track counts of 0s and 1s in the binary representations of the cumulative XOR values, updates these counts iteratively, and finally computes and prints a result based on these counts. The function ultimately returns 0.

