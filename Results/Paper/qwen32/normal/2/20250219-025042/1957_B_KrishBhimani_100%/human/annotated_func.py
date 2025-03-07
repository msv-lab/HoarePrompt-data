#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. Each of the next t lines contains two integers n and k such that 1 ≤ n ≤ 2 · 10^5 and 1 ≤ k ≤ 10^9. The sum of n over all test cases does not exceed 2 · 10^5.
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
        
    #State: All test cases have been processed and their respective outputs have been printed.
#Overall this is what the function does:The function processes multiple test cases, where each test case consists of two integers `n` and `k`. For each test case, it computes a specific list of integers based on the values of `n` and `k`, and prints this list. If `n` is 1, it simply prints `k`. Otherwise, it constructs a list starting with the largest power of 2 minus one that is less than `k`, followed by the remainder when `k` is subtracted by the sum of the list so far, and fills the rest of the list with zeros to ensure its length is `n`.

