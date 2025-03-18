#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4. For each test case, n is an integer such that 1 <= n <= 10^5, and a is a list of n integers where each integer a_i satisfies 1 <= a_i <= 10^9. The sum of n over all test cases does not exceed 10^5.
def func_1():
    print('-----------------')
    #This is printed: -----------------
    n = int(input())
    arr = list(map(int, input().split()))
    prefix = [0]
    for v in arr:
        prefix.append(v ^ prefix[-1])
        
    #State: `t` is an integer such that 1 <= t <= 10^4; `n` is an input integer such that 1 <= n <= 10^5; `arr` is a list of `n` integers where each integer `arr_i` satisfies 1 <= `arr_i` <= 10^9; `prefix` is a list containing `n+1` elements where the first element is `0` and each subsequent element at index `i` (1 <= i <= n) is the cumulative XOR of the first `i` elements of `arr`.
    print(arr, prefix)
    #This is printed: arr (where arr is a list of n integers each satisfying 1 <= arr_i <= 10^9), prefix (where prefix[0] = 0 and prefix[i] = arr[0] ^ arr[1] ^ ... ^ arr[i-1] for 1 <= i <= n)
    pre = [[0, 0] for _ in range(32)]
    suf = [[0, 0] for _ in range(32)]
    for i in range(32):
        pre[i][0] += 1
        
    #State: `t` is an integer such that 1 <= t <= 10^4; `n` is an input integer such that 1 <= n <= 10^5; `arr` is a list of `n` integers where each integer `arr_i` satisfies 1 <= `arr_i` <= 10^9; `prefix` is a list containing `n+1` elements where the first element is `0` and each subsequent element at index `i` (1 <= i <= n) is the cumulative XOR of the first `i` elements of `arr`; `pre` is a list of 32 sublists, each containing two zeros, except each `pre[i][0]` for i in range(32) which is 1; `suf` is a list of 32 sublists, each containing two zeros; `i` is 31.`
    for i in range(n, 0, -1):
        cur = prefix[i]
        
        for j in range(32):
            if cur >> j & 1:
                suf[j][1] += 1
            else:
                suf[j][0] += 1
        
    #State: `t` is an integer such that 1 <= t <= 10^4, `n` is an input integer such that 1 <= n <= 10^5, `arr` is a list of `n` integers where each integer `arr_i` satisfies 1 <= `arr_i` <= 10^9, `prefix` is a list containing `n+1` elements where the first element is `0` and each subsequent element at index `i` (1 <= i <= n) is the cumulative XOR of the first `i` elements of `arr`, `pre` is a list of 32 sublists, each containing two zeros, except each `pre[i][0]` for i in range(32) which is 1, `suf` is a list of 32 sublists, each containing two integers where `suf[j][1]` is the number of times the `j`-th bit was `1` across all `prefix[i]` values from `prefix[n]` to `prefix[1]`, and `suf[j][0]` is the number of times the `j`-th bit was `0` across all those values, `i` is 0, `cur` is `prefix[0]`, and `j` is 32.
    print(pre)
    #This is printed: [[1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0]]
    print(suf)
    #This is printed: suf (where suf is a list of 32 sublists, each containing the count of 0s and 1s for each bit position across the prefix values from prefix[n] to prefix[1])
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
        
    #State: `t` is an integer such that 1 <= t <= 10^4, `n` is an input integer such that 1 <= n <= 10^5, `arr` is a list of `n` integers where each integer `arr_i` satisfies 1 <= `arr_i` <= 10^9, `prefix` is a list containing `n+1` elements where the first element is 0 and each subsequent element at index `i` (1 <= i <= n) is the cumulative XOR of the first `i` elements of `arr`, `pre` is a list of 32 sublists, each containing two integers where `pre[j][0]` and `pre[j][1]` have been updated based on the bits of all `prefix[i]` values, `suf` is a list of 32 sublists, each containing two integers where `suf[j][0]` and `suf[j][1]` have been updated based on the bits of all `prefix[i]` values, `i` is `n + 1`, `cur` is `prefix[0]`, `j` is 32, `ans` is the accumulated sum of products of the counts of 0s and 1s in the `pre` and `suf` lists for each relevant bit position.
    print(ans)
    #This is printed: - The final value of `ans` is printed.
    #
    #Given the problem's context, the exact numerical value of `ans` cannot be determined without the specific values of `arr` and the subsequent computations of `prefix`, `pre`, and `suf`. However, based on the structure of the problem, the print statement will output the calculated value of `ans`.
    #
    #Output:
#Overall this is what the function does:The function `func_1` reads an integer `n` and a list `arr` of `n` integers. It computes a cumulative XOR array `prefix` from the input list `arr`. It then calculates and prints a value `ans` which is derived from the bit counts of the cumulative XOR values in `prefix`. The function performs these operations for a single test case, as it does not explicitly handle multiple test cases within the provided code snippet.

