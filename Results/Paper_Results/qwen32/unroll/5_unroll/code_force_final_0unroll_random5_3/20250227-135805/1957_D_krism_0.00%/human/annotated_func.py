#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n is an integer such that 1 ≤ n ≤ 10^5, and a is a list of n integers where each integer a_i satisfies 1 ≤ a_i ≤ 10^9. The sum of n over all test cases does not exceed 10^5.
def func_1():
    print('-----------------')
    #This is printed: -----------------
    n = int(input())
    arr = list(map(int, input().split()))
    prefix = [0]
    for v in arr:
        prefix.append(v ^ prefix[-1])
        
    #State: `t` is an integer such that 1 ≤ t ≤ 10^4; `n` is an integer read from the input such that 1 ≤ n ≤ 10^5; `a` is a list of `n` integers where each integer `a_i` satisfies 1 ≤ `a_i` ≤ 10^9; `arr` is a list of integers read from the input; `prefix` is a list of length `len(arr) + 1` where the i+1th element is the XOR of the first i elements of `arr`.
    print(arr, prefix)
    #This is printed: [arr[0], arr[1], ..., arr[len(arr) - 1]], [0, arr[0], arr[0] ^ arr[1], arr[0] ^ arr[1] ^ arr[2], ..., arr[0] ^ arr[1] ^ ... ^ arr[len(arr) - 1]] (where arr is the list of integers read from the input and prefix is the list of cumulative XORs of the elements of arr)
    pre = [[0, 0] for _ in range(32)]
    suf = [[0, 0] for _ in range(32)]
    for i in range(32):
        pre[i][0] += 1
        
    #State: `t` is an integer such that 1 ≤ t ≤ 10^4; `n` is an integer read from the input such that 1 ≤ n ≤ 10^5; `a` is a list of `n` integers where each integer `a_i` satisfies 1 ≤ `a_i` ≤ 10^9; `arr` is a list of integers read from the input; `prefix` is a list of length `len(arr) + 1` where the i+1th element is the XOR of the first i elements of `arr`; `pre` is a list of 32 sublists, each containing [1, 0]; `suf` is a list of 32 sublists, each containing [0, 0].
    for i in range(n, 0, -1):
        cur = prefix[i]
        
        for j in range(32):
            if cur >> j & 1:
                suf[j][1] += 1
            else:
                suf[j][0] += 1
        
    #State: `t` is an integer such that 1 ≤ t ≤ 10^4; `n` is an integer read from the input such that 1 ≤ n ≤ 10^5; `a` is a list of `n` integers where each integer `a_i` satisfies 1 ≤ `a_i` ≤ 10^9; `arr` is a list of integers read from the input; `prefix` is a list of length `len(arr) + 1` where the i+1th element is the XOR of the first i elements of `arr`; `pre` is a list of 32 sublists, each containing [1, 0]; `suf` is a list of 32 sublists, where each sublist `[x, y]` indicates that `x` is the count of numbers in `prefix[1]` to `prefix[n]` with the corresponding bit as 0 and `y` is the count of numbers with the corresponding bit as 1.
    print(pre)
    #This is printed: [[1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0]]
    print(suf)
    #This is printed: suf (where suf is a list of 32 sublists, each containing [x, y] where x is the count of numbers in prefix[1] to prefix[n] with the corresponding bit as 0 and y is the count of numbers with the corresponding bit as 1)
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
        
    #State: t is an integer such that 1 ≤ t ≤ 10^4; n is an integer read from the input such that 1 ≤ n ≤ 10^5; a is a list of n integers where each integer a_i satisfies 1 ≤ a_i ≤ 10^9; arr is a list of integers read from the input; prefix is a list of length len(arr) + 1 where the i+1th element is the XOR of the first i elements of arr; pre is a list of 32 sublists, each containing [count of 0s, count of 1s] for each bit position across the prefix array; suf is a list of 32 sublists, each containing [0, 0] for each bit position; ans is the accumulated value based on the counts of 0s and 1s.
    print(ans)
    #This is printed: ans (where ans is the accumulated value based on the counts of 0s and 1s for each bit position across the prefix array)
#Overall this is what the function does:The function `func_1` processes a list of integers for each test case, computes a specific value based on the XOR of prefixes of the list, and prints this value. The function does not accept any parameters directly but reads input values from standard input. For each test case, it reads an integer `n` and a list of `n` integers, then calculates and prints a result based on the counts of 0s and 1s in the bit positions of the cumulative XOR values.

