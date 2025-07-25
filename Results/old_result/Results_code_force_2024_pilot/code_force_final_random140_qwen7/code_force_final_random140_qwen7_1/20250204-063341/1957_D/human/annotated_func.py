#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4; for each test case, n is a positive integer such that 1 ≤ n ≤ 10^5, and a list of n integers a_1, a_2, ..., a_n where 1 ≤ a_i ≤ 10^9; the sum of all n values across all test cases does not exceed 10^5.
def func_1():
    n = int(input())
    arr = list(map(int, input().split()))
    prefix = [0]
    for v in arr:
        prefix.append(v ^ prefix[-1])
        
    #State: Output State: `t` is a positive integer such that \(1 \leq t \leq 10^4\), `n` is an input integer such that \(1 \leq n \leq 10^5\), `arr` is a non-empty list of integers, `v` is the last element of `arr`, and `prefix` is a list where each element is the cumulative XOR of all previous elements in `arr`.
    #
    #In simpler terms, after the loop completes all its iterations, `t` remains unchanged, `n` remains unchanged, `arr` contains the original list of integers, and `prefix` is a list where each element is the result of XORing all the elements in `arr` up to that point in the list. The final element in `prefix` will be the cumulative XOR of all elements in `arr`.
    pre = [[0, 0] for _ in range(32)]
    suf = [[0, 0] for _ in range(32)]
    for i in range(32):
        pre[i][0] += 1
        
    #State: After the loop executes all 32 iterations, `i` is 31; `pre[0][0]` is 32; `pre[2][0]` is 32; `pre[31][0]` is 32.
    for i in range(n, 0, -1):
        cur = prefix[i]
        
        for j in range(32):
            if cur >> j & 1:
                suf[j][1] += 1
            else:
                suf[j][0] += 1
        
    #State: Output State: After the loop executes all 32 iterations, `j` will be 31, `n` will be 1 (since it starts at 32 and decreases by 1 each iteration until it reaches 1), and `suf` will be a list of 32 sublists. Each sublist `suf[i]` will contain two elements. The first element of each sublist will represent the count of times the expression `(cur >> i & 1)` was false, and the second element will represent the count of times it was true across all iterations of the outer loop for `i` from 31 down to 1.
    #
    #This means that for each bit position `i` from 0 to 31, `suf[i][0]` will hold the total number of times the bit at position `i` in `cur` was 0, and `suf[i][1]` will hold the total number of times the bit at position `i` in `cur` was 1, across all iterations of the loop.
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
        
    #State: Output State: After the loop executes all 32 iterations, `j` will be 32, `n` will be 1, and `suf` will be a list of 32 sublists. Each sublist `suf[i]` will contain two elements: the first element will be -1 (indicating that the expression `(cur >> i & 1)` was false for the last iteration), and the second element will be 0 (indicating that the expression was true 0 times). `pre` will also be a list of 32 sublists, where each sublist `pre[i]` will contain two elements: the first element will be 0 (indicating that the expression `(cur >> i & 1)` was false 0 times), and the second element will be 32 (indicating that the expression was true 32 times). `ans` will be the sum of `pre[k][0] * suf[k][0] + pre[k][1] * suf[k][1]` for all `k` from 0 to 31, which simplifies to 0 because `suf[i][0]` is -1 and `suf[i][1]` is 0, and `pre[i][0]` is 0 and `pre[i][1]` is 32, making each term in the sum equal to 0.
    #
    #In natural language: After the loop completes all 32 iterations, `j` will be 32, `n` will be 1, and both `pre` and `suf` will be lists where each sublist contains 0 and 32 for the first and second elements respectively, indicating that the expression `(cur >> i & 1)` was true for all iterations for each bit position. The value of `ans` will be 0 because the contributions from `pre` and `suf` cancel each other out.
    print(ans)
    #This is printed: 0
#Overall this is what the function does:The function processes a series of test cases, where each test case includes a positive integer t (1 ≤ t ≤ 10^4), and for each t, a positive integer n (1 ≤ n ≤ 10^5) and a list of n integers a_1, a_2, ..., a_n (1 ≤ a_i ≤ 10^9). It constructs a prefix XOR array and then uses this array to compute a value based on bit counts. Finally, it prints the computed value, which turns out to be 0 for all test cases.

