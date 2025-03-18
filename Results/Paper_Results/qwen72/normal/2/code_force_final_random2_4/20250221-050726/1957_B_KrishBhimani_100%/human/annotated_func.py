#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, representing the number of test cases. For each test case, n and k are integers such that 1 ≤ n ≤ 2 · 10^5 and 1 ≤ k ≤ 10^9, representing the number of non-negative integers to be printed and their sum, respectively.
def func():
    for _ in range(int(input())):
        l1 = input().split()
        
        n, k = list(map(int, l1))
        
        if n == 1:
            print(k)
        else:
            arr = []
            k0 = k
            i = 0
            ans = []
            temp = 1
            while True:
                if temp * 2 < k:
                    temp *= 2
                    i += 1
                else:
                    break
            ans.append((1 << i) - 1)
            ans.append(k - sum(ans))
            ans += [0] * (n - len(ans))
            print(*ans)
        
    #State: After all iterations of the loop, `t` is an integer such that 1 ≤ t ≤ 10^4, and `_` has been incremented by the number of test cases processed. For each test case, `n` and `k` are the integer values of the first and second elements of `l1`, respectively. If `n` is 1, the output for that test case is `k`, and `arr` remains an empty list, `k0` is equal to `k`, and `ans` remains unchanged. If `n` is not 1, the output for that test case is a list of length `n` containing the values \((2^i - 1)\) and \((k - (2^i - 1))\) followed by `n - 2` zeros, where `i` is the largest integer such that \(2^i\) is less than `k`. The variable `temp` is \(2^i\) for each test case where `n` is not 1.
#Overall this is what the function does:The function reads multiple test cases from the standard input. For each test case, it takes two integers `n` and `k` as input, where `n` represents the number of non-negative integers to be printed and `k` represents their sum. If `n` is 1, the function prints `k`. Otherwise, it constructs a list of `n` non-negative integers such that the first element is the largest power of 2 less than `k` minus 1, the second element is the remaining value needed to reach `k`, and the rest of the elements are zeros. The function prints this list for each test case. After processing all test cases, the function completes without returning any value.

