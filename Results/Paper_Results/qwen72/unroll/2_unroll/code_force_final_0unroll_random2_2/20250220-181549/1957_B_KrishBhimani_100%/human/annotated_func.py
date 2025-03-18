#State of the program right berfore the function call: The function should take two integers, n and k, as input where 1 ≤ n ≤ 2 · 10^5 and 1 ≤ k ≤ 10^9.
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
        
    #State: The loop will read multiple test cases, each with two integers n and k. For each test case, if n == 1, it will print k. Otherwise, it will print a list of n integers where the first integer is the largest power of 2 less than k, the second integer is the remainder of k after subtracting the first integer, and the remaining n-2 integers are 0. The loop will continue until all test cases have been processed.
#Overall this is what the function does:The function processes multiple test cases, each consisting of two integers `n` and `k` where 1 ≤ n ≤ 2 · 10^5 and 1 ≤ k ≤ 10^9. For each test case, if `n` is 1, it prints `k`. Otherwise, it prints a list of `n` integers where the first integer is the largest power of 2 less than `k`, the second integer is the remainder of `k` after subtracting the first integer, and the remaining `n-2` integers are 0. The function does not return any value; it only prints the results for each test case.

