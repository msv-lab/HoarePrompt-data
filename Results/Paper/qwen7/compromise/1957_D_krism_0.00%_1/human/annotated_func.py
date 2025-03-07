#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4; for each test case, n is a positive integer such that 1 ≤ n ≤ 10^5, and a list of n integers a_1, a_2, ..., a_n where 1 ≤ a_i ≤ 10^9; the sum of all n values across all test cases does not exceed 10^5.
def func_1():
    print('-----------------')
    #This is printed: -----------------
    n = int(input())
    arr = list(map(int, input().split()))
    prefix = [0]
    for v in arr:
        prefix.append(v ^ prefix[-1])
        
    #State: Output State: The `prefix` list will contain the cumulative XOR values starting from 0 up to the last element of `arr`. Specifically, if `arr` has `k` elements, the `prefix` list will be `[0, v1 ^ 0, v2 ^ (v1 ^ 0), ..., vk ^ (vk-1 ^ ... ^ (v2 ^ (v1 ^ 0))...)]`, where `v1, v2, ..., vk` are the elements of `arr`.
    #
    #This means that each element in the `prefix` list (except the first one) is the result of XORing the current element of `arr` with all previous elements' cumulative XOR results. The loop will execute exactly `len(arr)` times, appending the cumulative XOR value for each element in `arr` to the `prefix` list.
    print(arr, prefix)
    #This is printed: [a1, a2, a3, ..., ak], [0, a1, a1 ^ a2, a1 ^ a2 ^ a3, ..., ak ^ (ak-1 ^ ... ^ a2 ^ a1)]
    pre = [[0, 0] for _ in range(32)]
    suf = [[0, 0] for _ in range(32)]
    for i in range(32):
        pre[i][0] += 1
        
    #State: Output State: `i` is 31; `pre[i][0]` is 32.
    #
    #In natural language: After the loop has executed all 32 iterations, the variable `i` will be 31 (since it starts at 0 and increments by 1 each iteration), and each list in `pre` will have its first element set to 32, as `pre[i][0]` is incremented by 1 in each iteration.
    for i in range(n, 0, -1):
        cur = prefix[i]
        
        for j in range(32):
            if cur >> j & 1:
                suf[j][1] += 1
            else:
                suf[j][0] += 1
        
    #State: `i` is -1, `n` is 31, `cur` is `prefix[-1]` (which is out of index), `j` is 32, `suf` is a 32x2 matrix where for each `j` from 0 to 31, `suf[j][1]` is 32 and `suf[j][0]` is 32.
    print(pre)
    #This is printed: pre (where pre is undefined)
    print(suf)
    #This is printed: [[32, 32], [32, 32], ..., [32, 32]] (a 32x2 matrix with each element being 32)
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
        
    #State: Output State: `i` is 33, `n` is 31, `y` is `arr[32]` (though `arr` does not exist beyond index 31, so `y` is undefined), `k` is 5, `ans` is the sum of `pre[k][0] * suf[k][0] + pre[k][1] * suf[k][1]` for each bit position from 0 to 31, `c` is `prefix[33]` (though `prefix` does not extend beyond index 32, so `c` is undefined), `j` is 32, and for each `j` from 0 to 31, `suf[j][0]` and `suf[j][1]` are both 0, reflecting that all counts have been fully decremented, and `pre[j][0]` and `pre[j][1]` represent the total counts of 0s and 1s across all 32 bits.
    #
    #In simpler terms, after the loop completes all 32 iterations, the variable `i` will be 33 (though it doesn't affect the final state of `suf` and `pre`), `y` and `c` will be undefined because they refer to indices out of bounds, `k` will be 5 (the bit length of `y` minus 1), `ans` will be the accumulated sum calculated during the loop, and for each bit position `j` from 0 to 31, `suf[j][0]` and `suf[j][1]` will be 0, indicating no more counts left to decrement. The `pre[j][0]` and `pre[j][1]` will hold the total counts of 0s and 1s across all 32 bits processed.
    print(ans)
    #This is printed: 0
#Overall this is what the function does:The function processes multiple test cases, each consisting of an integer \( t \) (number of test cases) and for each test case, an integer \( n \) and a list of \( n \) integers \( a_1, a_2, ..., a_n \). For each test case, it calculates and prints the cumulative XOR values of the list elements and then performs bitwise operations to count the occurrences of 0s and 1s for each bit position across all elements. Finally, it computes and prints a result based on these counts, which is always 0 in this specific implementation.

