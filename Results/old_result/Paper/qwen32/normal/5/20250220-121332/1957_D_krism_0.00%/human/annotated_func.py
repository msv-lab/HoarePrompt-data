#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4. For each test case, n is an integer such that 1 <= n <= 10^5, and a is a list of n integers where each integer a_i satisfies 1 <= a_i <= 10^9. The sum of n over all test cases does not exceed 10^5.
def func_1():
    print('-----------------')
    #This is printed: -----------------
    n = int(input())
    arr = list(map(int, input().split()))
    prefix = [0]
    for v in arr:
        prefix.append(v ^ prefix[-1])
        
    #State: `t` is an integer such that 1 <= t <= 10^4, `n` is an input integer such that 1 <= n <= 10^5, `arr` is a list of `n` integers where each integer `a_i` satisfies 1 <= a_i <= 10^9, `prefix` is a list [0, v1, v1 ^ v2, v1 ^ v2 ^ v3, ..., v1 ^ v2 ^ ... ^ vn]
    print(arr, prefix)
    #This is printed: arr (where arr is a list of n integers each satisfying 1 <= a_i <= 10^9), prefix (where prefix is a list [0, v1, v1 ^ v2, v1 ^ v2 ^ v3, ..., v1 ^ v2 ^ ... ^ vn] with v_i being the i-th element of arr)
    pre = [[0, 0] for _ in range(32)]
    suf = [[0, 0] for _ in range(32)]
    for i in range(32):
        pre[i][0] += 1
        
    #State: `t` is an integer such that 1 <= t <= 10^4, `n` is an input integer such that 1 <= n <= 10^5, `arr` is a list of `n` integers where each integer `a_i` satisfies 1 <= a_i <= 10^9, `prefix` is a list [0, v1, v1 ^ v2, v1 ^ v2 ^ v3, ..., v1 ^ v2 ^ ... ^ vn], `pre` is a list of 32 sublists, each containing [1, 0], `suf` is a list of 32 sublists, each containing two zeros, `i` is 31`
    for i in range(n, 0, -1):
        cur = prefix[i]
        
        for j in range(32):
            if cur >> j & 1:
                suf[j][1] += 1
            else:
                suf[j][0] += 1
        
    #State: `t` is an integer such that 1 <= t <= 10^4, `n` is an input integer such that 1 <= n <= 10^5, `arr` is a list of `n` integers where each integer `a_i` satisfies 1 <= a_i <= 10^9, `prefix` is a list [0, v1, v1 ^ v2, v1 ^ v2 ^ v3, ..., v1 ^ v2 ^ ... ^ vn], `pre` is a list of 32 sublists, each containing [1, 0], `suf` is a list of 32 sublists, where each sublist `suf[j]` is [x, y] such that x is the count of times the `j`-th bit of `cur` was 0, and y is the count of times the `j`-th bit of `cur` was 1, after checking all 32 bits for each `cur` in `prefix` from `n` down to 1, `i` is 0, `cur` is `prefix[0]`, `j` is 32.`
    print(pre)
    #This is printed: [[1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0]]
    print(suf)
    #This is printed: suf (where suf is a list of 32 sublists, each containing [x, y], where x is the count of times the j-th bit was 0 and y is the count of times the j-th bit was 1 across all elements in the prefix list)
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
        
    #State: `t` is an integer such that 1 <= t <= 10^4, `n` is an input integer such that 1 <= n <= 10^5, `arr` is a list of `n` integers where each integer `a_i` satisfies 1 <= a_i <= 10^9, `prefix` is a list [0, v1, v1 ^ v2, v1 ^ v2 ^ v3, ..., v1 ^ v2 ^ ... ^ vn], `pre` is a list of 32 sublists with counts of 0s and 1s for each bit across all `prefix[i]` from `i = 1` to `i = n`, `suf` is a list of 32 sublists with counts of 0s and 1s for each bit across all `prefix[i]` from `i = 1` to `i = n` in reverse order, `i` is `n + 1`, `cur` is `prefix[0]`, `j` is 32, `y` is `arr[n - 1]`, `k` is `arr[n - 1].bit_length() - 1`, `c` is `prefix[n]`, and `ans` is the sum of `pre[k][0] * suf[k][0] + pre[k][1] * suf[k][1]` for each `k` corresponding to the bit length of each `arr[i - 1]`.
    print(ans)
    #This is printed: ans (where ans is the sum of pre[k][0] * suf[k][0] + pre[k][1] * suf[k][1] for each k corresponding to the bit length of each arr[i - 1])
#Overall this is what the function does:The function `func_1` processes a single test case where it reads an integer `n` and a list `arr` of `n` integers. It calculates a result based on the bitwise XOR prefix sums of the list and prints intermediate and final results. The final result printed is an integer `ans` which is computed by considering the counts of 0s and 1s in specific bit positions across the prefix sums.

