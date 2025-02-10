#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, representing the number of test cases. For each test case, n is an integer such that 1 ≤ n ≤ 10^5, and a is a list of n integers where each element a_i satisfies 1 ≤ a_i ≤ 10^9. The sum of n over all test cases does not exceed 10^5.
def func_1():
    n = int(input())
    arr = list(map(int, input().split()))
    prefix = [0]
    for v in arr:
        prefix.append(v ^ prefix[-1])
        
    #State: `arr` remains unchanged, `prefix` contains `len(arr) + 1` elements where each element is the cumulative XOR of the elements in `arr` up to that point.
    pre = [[0, 0] for _ in range(32)]
    suf = [[0, 0] for _ in range(32)]
    for i in range(32):
        pre[i][0] += 1
        
    #State: `arr` remains unchanged, `prefix` contains `len(arr) + 1` elements where each element is the cumulative XOR of the elements in `arr` up to that point, `pre` is a list of 32 sublists, where each sublist is `[32, 0]`, `suf` is a list of 32 sublists, each containing `[0, 0]`, `i` is 31, the range is 32.
    for i in range(n, 0, -1):
        cur = prefix[i]
        
        for j in range(32):
            if cur >> j & 1:
                suf[j][1] += 1
            else:
                suf[j][0] += 1
        
    #State: After all iterations of the loop, `arr` remains unchanged, `prefix` contains `len(arr) + 1` elements where each element is the cumulative XOR of the elements in `arr` up to that point, `pre` is a list of 32 sublists, where each sublist is `[32, 0]`, `suf` is a list of 32 sublists, each containing the counts of 0s and 1s for each bit position across all `prefix` values, `i` is 0, and `n` must be 32.
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
        
    #State: After all iterations of the loop, `i` is 32, `n` is 32, `ans` is the sum of the values calculated in each iteration, `pre` is a list of 32 sublists where each sublist contains the counts of 0s and 1s for each bit position across all `prefix` values, and `suf` is a list of 32 sublists, each containing the final counts of 0s and 1s for each bit position across all `prefix` values. The `prefix` list contains `len(arr) + 1` elements where each element is the cumulative XOR of the elements in `arr` up to that point. The `arr` list remains unchanged.
    print(ans)
    #This is printed: ans (where ans is the sum of the values calculated in each iteration)
#Overall this is what the function does:The function `func_1` reads an integer `n` and a list of `n` integers `arr` from the input. It calculates a value `ans` based on the cumulative XOR of the elements in `arr` and the bit counts of these cumulative XOR values. The function then prints the value of `ans`. The function does not return any value; instead, it directly prints the result. The input list `arr` remains unchanged throughout the function execution.

