#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n is an integer such that 1 ≤ n ≤ 10^5, and a is a list of n integers where each integer a_i satisfies 1 ≤ a_i ≤ 10^9. The sum of n across all test cases does not exceed 10^5.
def func_1():
    print('-----------------')
    #This is printed: -----------------
    n = int(input())
    arr = list(map(int, input().split()))
    prefix = [0]
    for v in arr:
        prefix.append(v ^ prefix[-1])
        
    #State: `t` is an integer such that 1 ≤ t ≤ 10^4; `n` is the integer input provided by the user such that 1 ≤ n ≤ 10^5; `a` is a list of `n` integers where each integer `a_i` satisfies 1 ≤ `a_i` ≤ 10^9; `arr` is a list of integers provided by the user such that `arr` contains `n` integers where each integer `arr_i` satisfies 1 ≤ `arr_i` ≤ 10^9; `prefix` is a list of `n + 1` integers where the first element is `0` and each subsequent element is the cumulative XOR of the elements in `arr` up to that point.
    print(arr, prefix)
    #This is printed: [arr_0, arr_1, ..., arr_{n-1}], [0, arr_0, arr_0 ^ arr_1, arr_0 ^ arr_1 ^ arr_2, ..., arr_0 ^ arr_1 ^ ... ^ arr_{n-1}] (where arr_i are the elements of the list arr and each subsequent element of prefix is the cumulative XOR of the elements in arr up to that point)
    pre = [[0, 0] for _ in range(32)]
    suf = [[0, 0] for _ in range(32)]
    for i in range(32):
        pre[i][0] += 1
        
    #State: `t` is an integer such that 1 ≤ t ≤ 10^4; `n` is the integer input provided by the user such that 1 ≤ n ≤ 10^5; `a` is a list of `n` integers where each integer `a_i` satisfies 1 ≤ `a_i` ≤ 10^9; `arr` is a list of integers provided by the user such that `arr` contains `n` integers where each integer `arr_i` satisfies 1 ≤ `arr_i` ≤ 10^9; `prefix` is a list of `n + 1` integers where the first element is `0` and each subsequent element is the cumulative XOR of the elements in `arr` up to that point; `pre` is a list of 32 sublists, each containing `[1, 0]`; `suf` is a list of 32 sublists, each containing `[0, 0]`.
    for i in range(n, 0, -1):
        cur = prefix[i]
        
        for j in range(32):
            if cur >> j & 1:
                suf[j][1] += 1
            else:
                suf[j][0] += 1
        
    #State: `t` is an integer such that 1 ≤ t ≤ 10^4; `n` is the integer input provided by the user such that 1 ≤ n ≤ 10^5; `a` is a list of `n` integers where each integer `a_i` satisfies 1 ≤ `a_i` ≤ 10^9; `arr` is a list of `n` integers where each integer `arr_i` satisfies 1 ≤ `arr_i` ≤ 10^9; `prefix` is a list of `n + 1` integers where the first element is `0` and each subsequent element is the cumulative XOR of the elements in `arr` up to that point; `pre` is a list of 32 sublists, each containing `[1, 0]`; `suf` is a list of 32 sublists, where each sublist `[x, y]` contains the count of `0`s and `1`s for the corresponding bit position across the prefix XOR values.
    print(pre)
    #This is printed: [[1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0]]
    print(suf)
    #This is printed: [ [x_0, y_0], [x_1, y_1], ..., [x_31, y_31] ] (where x_i and y_i are the counts of 0s and 1s for the i-th bit position across the prefix XOR values)
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
        
    #State: `t` is an integer such that 1 ≤ t ≤ 10^4; `n` is the integer input provided by the user such that 1 ≤ n ≤ 10^5; `a` is a list of `n` integers where each integer `a_i` satisfies 1 ≤ `a_i` ≤ 10^9; `arr` is a list of `n` integers where each integer `arr_i` satisfies 1 ≤ `arr_i` ≤ 10^9; `prefix` is a list of `n + 1` integers where the first element is `0` and each subsequent element is the cumulative XOR of the elements in `arr` up to that point; `pre` is a list of 32 sublists, each containing `[x, y]`, where `x` and `y` are the final counts of `0`s and `1`s for the corresponding bit position; `suf` is a list of 32 sublists, each containing `[x, y]`, where `x` and `y` are the final counts of `0`s and `1`s for the corresponding bit position across the prefix XOR values; `ans` is the final accumulated value after the loop.
    print(ans)
    #This is printed: ans (where ans is the final accumulated value after the loop completes)
#Overall this is what the function does:The function `func_1` reads an integer `n` and a list of `n` integers from the input. It calculates a cumulative XOR for the list and uses this to compute a final accumulated value `ans` based on the bit positions of the XOR values. The function prints the original list, the cumulative XOR list, intermediate counts of bits, and finally the accumulated value `ans`.

