#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4; for each test case, n is a positive integer such that 1 ≤ n ≤ 10^5; and the list a is a list of integers such that 1 ≤ a_i ≤ 10^9 for all 1 ≤ i ≤ n. The sum of all n across all test cases does not exceed 10^5.
def func_1():
    print('-----------------')
    #This is printed: -----------------
    n = int(input())
    arr = list(map(int, input().split()))
    prefix = [0]
    for v in arr:
        prefix.append(v ^ prefix[-1])
        
    #State: Output State: The `prefix` list will contain the cumulative XOR of all elements in `arr` up to each index, starting with 0. Specifically, `prefix[i]` will be the result of `v1 ^ v2 ^ ... ^ vi` for each `i` from 0 to the length of `arr`.
    #
    #For example, if `arr = [a, b, c, d]`, then after the loop completes, `prefix` will be `[0, a ^ 0, (b ^ a) ^ (a ^ 0), ((c ^ b) ^ (b ^ a)) ^ ((a ^ 0)), ((d ^ c) ^ ((c ^ b) ^ (b ^ a))) ^ (((c ^ b) ^ (b ^ a)) ^ ((a ^ 0)))]`, which simplifies to `[0, a, b ^ a, c ^ b ^ a, d ^ c ^ b ^ a]`.
    #
    #This means that `prefix[i]` represents the XOR of all elements in `arr` up to the `i`-th element.
    print(arr, prefix)
    #This is printed: Output:
    pre = [[0, 0] for _ in range(32)]
    suf = [[0, 0] for _ in range(32)]
    for i in range(32):
        pre[i][0] += 1
        
    #State: Output State: `pre` is a list of lists containing 32 elements, each of which is [32, 0]; `suf` is a list of lists containing 32 elements, each of which is [0, 0]; `i` is 32; `n` is 32.
    #
    #Explanation: After the loop has executed all 32 iterations, each sublist in `pre` will have its first element set to 32 (since `pre[i][0] += 1` was executed 32 times for each `i`), while the second element remains 0. The variable `suf` remains unchanged as it is not affected by the loop. The variable `i` will be equal to 32 (one past the last index processed in the loop), and `n` retains its initial value of 32.
    for i in range(n, 0, -1):
        cur = prefix[i]
        
        for j in range(32):
            if cur >> j & 1:
                suf[j][1] += 1
            else:
                suf[j][0] += 1
        
    #State: Output State: `i` is 0, `j` is 0, `cur` is the value of `prefix[0]`, for each `j` from 0 to 31, `suf[j][1]` contains the total count of bits set to 1 in the binary representation of `cur`, and `suf[j][0]` contains the total count of bits set to 0 in the same range.
    #
    #Explanation: After the loop has executed all 32 iterations, `i` will be 0 (one past the last index processed in the loop), and `j` will be 0 (as the loop decrements `j` from 31 to 0). The variable `cur` will hold the value of `prefix[0]` since `cur` is initialized with `prefix[i]` and `i` starts from 32 and decreases to 0. For each bit position `j` from 0 to 31, `suf[j][1]` will contain the total number of 1s in the binary representation of `cur` (since it counts 1s from position `j` to 31, and after 32 iterations, this covers all bits), and `suf[j][0]` will contain the total number of 0s in the same range.
    print(pre)
    #This is printed: prefix[0]
    print(suf)
    #This is printed: [[total_number_of_1s_in_val, total_number_of_0s_in_val]]
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
        
    #State: Output State: `ans` is increased by `pre[4][0] * suf[31][0] + pre[4][1] * suf[31][1]`, where `pre[4][0]` is the count of bits set to 0 in the 4th bit position, `pre[4][1]` is the count of bits set to 1 in the 4th bit position, `suf[31][0]` is the count of bits set to 0 in the last 32 bits, and `suf[31][1]` is the count of bits set to 1 in the last 32 bits. After the loop completes, `pre[31][0]` is 32, indicating there are 32 zeros in the most significant bit position, and `suf[31][0]` is -32, indicating there are 32 more zeros than ones in the last 32 bits. The variable `j` resets to 31, and `k` remains at 4, with `c` and `y` retaining their final values from the last iteration of the loop.
    #
    #In simpler terms, after the loop finishes executing, `ans` is updated based on the final counts of 0s and 1s in specific bit positions, and the counts of 0s and 1s in the last 32 bits are finalized. The variable `j` is reset to 31, and `k` remains at 4, with `c` and `y` holding their values from the last loop iteration.
    print(ans)
    #This is printed: ans (where ans is updated based on the final counts of 0s and 1s in the 4th bit position and the last 32 bits, with pre[31][0] being 32 and suf[31][0] being -32)
#Overall this is what the function does:The function processes a series of test cases, each consisting of a positive integer \( n \) and a list of integers \( a \). It computes the cumulative XOR of elements in the list \( a \) and then calculates a specific value based on the counts of 0s and 1s in certain bit positions. The function ultimately returns the computed value \( ans \).

