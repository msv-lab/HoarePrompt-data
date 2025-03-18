#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, representing the number of test cases. For each test case, n and k are integers such that 1 ≤ n ≤ 2 · 10^5 and 1 ≤ k ≤ 10^9, representing the number of non-negative integers to be printed and their sum, respectively. The sum of n over all test cases does not exceed 2 · 10^5.
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
        
    #State: After all iterations, `t` is an integer such that 1 ≤ t ≤ 10^4, `_` is `t - 1`, `n` is the integer value of the first element of `l1` from the last iteration, `k` is the integer value of the second element of `l1` from the last iteration, `k0` is the integer value of the second element of `l1` from the last iteration, `ans` is a list of length `n` containing the values \((1 << i) - 1\) and \(k - ((1 << i) - 1)\), followed by `n - 2` zeros, where `i` is the largest integer such that \(2^i < k\), and `temp` is \(2^i\). `l1` is a list of strings from the input. If `n` is 1, the state remains unchanged. Otherwise, `k0` is now equal to `k`, `ans` is a list containing the values \(2^i - 1\), \(k - 2^i + 1\), and `n - 2` zeros, and `arr` is an empty list.
#Overall this is what the function does:The function processes a series of test cases, each defined by two integers `n` and `k`. For each test case, it generates and prints a list of `n` non-negative integers such that their sum equals `k`. If `n` is 1, the function simply prints `k`. Otherwise, it constructs a list where the first element is the largest power of 2 less than `k` minus 1, the second element is the remainder needed to reach `k`, and the rest are zeros, ensuring the list has exactly `n` elements. The function does not return any value; it only prints the results. After processing all test cases, the state of the program includes the number of test cases `t`, the values of `n` and `k` from the last test case, and the generated list `ans` for the last test case.

