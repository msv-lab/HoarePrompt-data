#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4; for each test case, n is an integer such that 1 ≤ n ≤ 10^5, and a list of n integers a_1, a_2, ..., a_n where 1 ≤ a_i ≤ 10^9; the sum of all n values across all test cases does not exceed 10^5.
def func_1():
    print('-----------------')
    #This is printed: -----------------
    n = int(input())
    arr = list(map(int, input().split()))
    prefix = [0]
    for v in arr:
        prefix.append(v ^ prefix[-1])
        
    #State: Output State: `prefix` is a list containing the cumulative XOR of elements from `arr`. The first element is 0, followed by the XOR of each element in `arr` with the previous cumulative XOR result.
    print(arr, prefix)
    #This is printed: arr, [0, a1, a1 ^ a2, a1 ^ a2 ^ a3, ..., a1 ^ a2 ^ ... ^ an]
    pre = [[0, 0] for _ in range(32)]
    suf = [[0, 0] for _ in range(32)]
    for i in range(32):
        pre[i][0] += 1
        
    #State: Output State: `prefix` is a list containing the cumulative XOR of elements from `arr`. The first element is 0, followed by the XOR of each element in `arr` with the previous cumulative XOR result; `pre` is a list of lists containing [32, 0] repeated 32 times; `suf` is a list containing 32 sublists, each with the values [0, 0].
    for i in range(n, 0, -1):
        cur = prefix[i]
        
        for j in range(32):
            if cur >> j & 1:
                suf[j][1] += 1
            else:
                suf[j][0] += 1
        
    #State: Output State: `prefix` is a list containing the cumulative XOR of elements from `arr`. The first element is 0, followed by the XOR of each element in `arr` with the previous cumulative XOR result; `pre` remains unchanged as a list of lists containing [32, 0] repeated 32 times; `suf` is a list containing 32 sublists, where each sublist has been updated such that the first element (number of zeros) and the second element (number of ones) reflect the count of bits set to 0 and 1, respectively, across all `cur` values for each bit position from 0 to 31 during the loop executions.
    print(pre)
    #This is printed: [[32, 0], [32, 0], [32, 0], ..., [32, 0]] (32 times)
    print(suf)
    #This is printed: [[32, 0]] * 32
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
        
    #State: Output State: `ans` is the sum of the products of the number of zeros and ones for each bit position from 0 to 31, calculated based on the cumulative XOR values of the array elements. `prefix` is a list where each element represents the cumulative XOR up to that index in the array. `pre` remains unchanged as a list of lists containing [32, 0] repeated 32 times. `suf` is a list where each sublist contains the updated counts of zeros and ones for each bit position from 0 to 31 across all `cur` values for each bit position after the loop executions.
    print(ans)
    #This is printed: ans (where ans is the sum of the products of the number of zeros and ones for each bit position from 0 to 31, calculated based on the cumulative XOR values of the array elements)
#Overall this is what the function does:The function processes a series of test cases, where each test case consists of an integer \( n \) and a list of \( n \) integers. It calculates and returns a result based on the cumulative XOR values of the list elements. Specifically, it computes the sum of the products of the number of zeros and ones for each bit position from 0 to 31, derived from the cumulative XOR values of the array elements. The function does not return any value directly but prints the final result.

