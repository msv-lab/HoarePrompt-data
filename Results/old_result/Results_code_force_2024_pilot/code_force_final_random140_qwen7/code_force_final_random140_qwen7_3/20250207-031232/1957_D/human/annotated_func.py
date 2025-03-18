#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4; for each test case, n is a positive integer such that 1 ≤ n ≤ 10^5, and a list of n integers a_1, a_2, ..., a_n where 1 ≤ a_i ≤ 10^9 for all 1 ≤ i ≤ n; the sum of all n values across all test cases does not exceed 10^5.
def func_1():
    n = int(input())
    arr = list(map(int, input().split()))
    prefix = [0]
    for v in arr:
        prefix.append(v ^ prefix[-1])
        
    #State: Output State: `t` is a positive integer such that \(1 \leq t \leq 10^4\), `n` is an input integer such that \(1 \leq n \leq 10^5\), `arr` is a list of integers obtained from splitting the input string and converting each element to an integer (with at least as many elements as there were iterations of the loop), `prefix` is a list containing `len(arr) + 1` integers where each element (except the first one) is the cumulative bitwise XOR of all previous elements in `arr`, `v` is the current element being processed in `arr`.
    #
    #In simpler terms, after the loop has executed all its iterations, `t` and `n` remain unchanged, `arr` contains the original list of integers, and `prefix` is a list of length equal to the number of elements in `arr` plus one. Each element in `prefix` (starting from the second one) is the result of performing a bitwise XOR operation on all the elements in `arr` up to that point in the sequence.
    pre = [[0, 0] for _ in range(32)]
    suf = [[0, 0] for _ in range(32)]
    for i in range(32):
        pre[i][0] += 1
        
    #State: `i` is 31; `pre[0][0]` is 32; `pre[2][0]` is 32; `pre[30][0]` is 32; `pre[31][0]` is 33.
    for i in range(n, 0, -1):
        cur = prefix[i]
        
        for j in range(32):
            if cur >> j & 1:
                suf[j][1] += 1
            else:
                suf[j][0] += 1
        
    #State: Output State: `i` is 1, `j` is 32, `cur` is `prefix[1]`, and for every `j` from 0 to 31, `suf[j][0]` represents the count of bits set to 0 and `suf[j][1]` represents the count of bits set to 1 from the `j`-th bit to the most significant bit of `cur`.
    #
    #After the loop executes all its iterations, `i` will be reduced to 1 (since it starts at 31 and decreases by 1 in each iteration until it reaches 1). The variable `j` will reach 32 because the loop iterates over the range from 31 down to 1, and `j` is incremented within the inner loop. The variable `cur` will be the value of `prefix[1]` since `i` starts at 31 and decreases to 1. For each bit position `j` from 0 to 31, `suf[j][0]` and `suf[j][1]` will contain the counts of bits set to 0 and 1, respectively, from the `j`-th bit to the most significant bit of `cur`.
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
        
    #State: Output State: After the loop executes all iterations, `j` is 31, `c` is an integer where the highest bit (31st bit) is 1, `pre[31][0]` is 0, `pre[31][1]` is 32, `suf[31][0]` is -32, and `suf[31][1]` is -32.
    #
    #This means that after the loop completes, `c` will have its highest bit set to 1, indicating it is a non-zero integer. The counts in `pre[31]` reflect that there are no zeros (since `pre[31][0]` is 0) and 32 ones across all bits up to the 31st bit. Similarly, `suf[31]` indicates that there are no additional zeros beyond the 31st bit (hence `-32` for `suf[31][0]`) and 32 ones (hence `-32` for `suf[31][1]`).
    print(ans)
    #This is printed: ans (where ans is derived from the provided pre and suf arrays, specifically the counts of zeros and ones up to and beyond the 31st bit)
#Overall this is what the function does:The function processes a series of test cases, each consisting of a positive integer \( n \) and a list of \( n \) integers. It computes and prints a result based on the bitwise XOR operations performed on the list of integers. Specifically, it calculates the sum of certain combinations of bit counts related to the bitwise XOR values of the input list. The function does not return any value but prints the computed result.

