#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n and k are integers such that 1 ≤ n ≤ 2 · 10^5 and 1 ≤ k ≤ 10^9. The sum of n over all test cases does not exceed 2 · 10^5.
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
        
    #State: After all iterations, the program will have processed all `t` test cases, and the final output state will be that `t` is 0, and all other variables (`arr`, `k0`, `ans`, `temp`, `i`) will reflect the state after processing the last test case. Specifically, `arr` will be an empty list, `k0` will be the value of `k` from the last test case, `ans` will contain the computed values for the last test case, `temp` will be the highest power of 2 less than `k` from the last test case, and `i` will be the corresponding exponent.
#Overall this is what the function does:The function processes multiple test cases, where each test case consists of two integers `n` and `k`. For each test case, it computes and prints a list of `n` integers. If `n` is 1, it simply prints `k`. Otherwise, it calculates a sequence starting with the largest power of 2 less than `k`, followed by the remainder when `k` is subtracted by the sum of the sequence, and fills the rest of the list with zeros to ensure the list has `n` elements.

