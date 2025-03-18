#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4. For each test case, n is an integer such that 1 <= n <= 10^5, and a is a list of n integers where each integer a_i satisfies 1 <= a_i <= 10^9. The sum of n over all test cases does not exceed 10^5.
def func_1():
    print('-----------------')
    #This is printed: -----------------
    n = int(input())
    arr = list(map(int, input().split()))
    prefix = [0]
    for v in arr:
        prefix.append(v ^ prefix[-1])
        
    #State: - `t` remains unchanged.
    #- `n` remains unchanged.
    #- `arr` remains unchanged.
    #- `prefix` is a list with `n + 1` elements, where the first element is `0` and the subsequent `n` elements are the cumulative XOR results of the elements in `arr`.
    #
    #Output State:
    print(arr, prefix)
    #This is printed: arr, prefix (where arr is the original list and prefix is the list of cumulative XOR results with the first element as 0)
    pre = [[0, 0] for _ in range(32)]
    suf = [[0, 0] for _ in range(32)]
    for i in range(32):
        pre[i][0] += 1
        
    #State: t remains unchanged; n remains unchanged; arr remains unchanged; prefix is a list with n + 1 elements, where the first element is 0 and the subsequent n elements are the cumulative XOR results of the elements in arr; pre is a list of 32 sublists, each containing [1, 0]; suf is a list of 32 sublists, each containing [0, 0].
    for i in range(n, 0, -1):
        cur = prefix[i]
        
        for j in range(32):
            if cur >> j & 1:
                suf[j][1] += 1
            else:
                suf[j][0] += 1
        
    #State: t remains unchanged; n remains unchanged; arr remains unchanged; prefix remains unchanged; pre is a list of 32 sublists, each containing [1, 0]; suf is a list of 32 sublists, each containing [count of 0s, count of 1s] for the corresponding bit position across prefix[1] to prefix[n].
    print(pre)
    #This is printed: [[1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0]]
    print(suf)
    #This is printed: suf (where suf is a list of 32 sublists, each containing [count of 0s, count of 1s] for the corresponding bit position across prefix[1] to prefix[n])
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
        
    #State: t remains unchanged; n remains unchanged; arr remains unchanged; prefix remains unchanged; pre is a list of 32 sublists, each containing [count of 0s, count of 1s] for the corresponding bit position across prefix[1] to prefix[n]; suf is a list of 32 sublists, each containing [count of 0s, count of 1s] for the corresponding bit position across prefix[i+1] to prefix[n]; ans is the computed sum of products of counts of 0s and 1s in pre[k] and suf[k].
    print(ans)
    #This is printed: ans (where ans is the sum of products of counts of 0s and 1s in pre[k] and suf[k] for each bit position k from 0 to 31)
#Overall this is what the function does:The function reads an integer `n` and a list `a` of `n` integers, computes a series of cumulative XOR results, and then calculates a specific sum based on the counts of 0s and 1s in the binary representation of these XOR results. It prints the original list, the list of cumulative XOR results, two lists (`pre` and `suf`) that contain counts of 0s and 1s for each bit position, and finally, the computed sum for each test case.

